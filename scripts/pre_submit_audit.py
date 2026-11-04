#!/usr/bin/env python3
"""Read-only, bounded submission checks. Findings never include matched values."""
import argparse
import json
import os
from pathlib import Path
import re
import stat
import subprocess
import time

CONTENT_EXCLUDES = {".git", ".probe-kit", "node_modules", ".venv", "venv", "__pycache__"}
TEXT_SUFFIXES = {".py", ".js", ".jsx", ".ts", ".tsx", ".json", ".yaml", ".yml",
                 ".toml", ".ini", ".cfg", ".sh", ".md", ".txt", ".log", ".sql", ".env"}
PATTERNS = [
    ("credential-like", re.compile(r"\b(?:sk-[A-Za-z0-9_-]{20,}|AIza[0-9A-Za-z_-]{35}|ghp_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,})")),
    ("assigned-secret-like", re.compile(r"""(?i)\b(?:password|passwd|secret|api[_-]?key|access[_-]?token)['"]?\s*[:=]\s*(?:['"][^'"\r\n]{1,200}['"]|[A-Za-z0-9_./+:-]{8,})""")),
    ("personal-id-like", re.compile(r"\b[0-9]{6}-[1-4][0-9]{6}\b")),
    ("loopback-reference", re.compile(r"\b(?:127\.0\.0\.1|localhost)\b")),
]


def git_summary(root):
    try:
        args = dict(cwd=root, capture_output=True, text=True, timeout=5,
                    env={**os.environ, "GIT_OPTIONAL_LOCKS": "0"})
        top = subprocess.run(["git", "rev-parse", "--show-toplevel"], **args)
        if top.returncode or Path(top.stdout.strip()).resolve() != root:
            return {"status": "NOT_RUN", "reason": "workspace is not the Git repository root"}
        outputs = {}
        for name, command in (
            ("status", ["git", "status", "--short", "--untracked-files=normal"]),
            ("diff_stat", ["git", "diff", "--stat"]),
            ("staged_stat", ["git", "diff", "--cached", "--stat"]),
        ):
            result = subprocess.run(command, **args)
            if result.returncode:
                return {"status": "NOT_RUN", "reason": f"{name} failed"}
            outputs[name] = result.stdout[:8000]
            if len(result.stdout) > 8000:
                outputs[name + "_truncated"] = True
        return {"status": "HUMAN_CHECK", "reason": "S1 must compare paths with assigned scope", **outputs}
    except (OSError, subprocess.TimeoutExpired, UnicodeError):
        return {"status": "NOT_RUN", "reason": "Git unavailable, timed out or output unreadable"}


def resources():
    result = {"memory_status": "HUMAN_CHECK", "reason": "Check actual memory usage in the provided environment"}
    try:
        values = {}
        for line in Path("/proc/meminfo").read_text().splitlines():
            key, value = line.split(":", 1)
            if key in ("MemTotal", "MemAvailable"):
                values[key] = int(value.split()[0]) * 1024
        result.update(values)
        result["memory_status"] = "HUMAN_CHECK"
        result["reason"] = "Host memory snapshot; container limits and process ownership need review"
    except (OSError, ValueError):
        pass
    try:
        result["load_average_1_5_15"] = os.getloadavg()
    except (AttributeError, OSError):
        pass
    return result


def audit(workspace, required=(), max_entries=50000, max_file_bytes=1048576,
          max_scan_bytes=20971520, seconds=15, submission_limit_bytes=10000000000):
    root = Path(workspace).resolve(strict=True)
    if not root.is_dir() or min(max_entries, max_file_bytes, max_scan_bytes, seconds, submission_limit_bytes) <= 0:
        raise ValueError("Use a directory and positive scan limits")
    required_paths = []
    for name in required:
        p = Path(name)
        if p.is_absolute() or ".." in p.parts or not p.parts:
            raise ValueError("Required files must be relative paths inside the workspace")
        required_paths.append(p)
    counts = {"entries": 0, "regular_files": 0, "measured_file_bytes": 0,
              "text_files_read": 0, "scan_bytes": 0, "excluded_content_files": 0,
              "non_text_files": 0, "large_files_skipped": 0, "symlinks_skipped": 0,
              "special_files_skipped": 0, "findings_total": 0}
    errors, findings = [], []
    limited = False
    deadline = time.monotonic() + seconds
    stack = [root]
    while stack:
        if time.monotonic() >= deadline or counts["entries"] >= max_entries:
            limited = True
            break
        directory = stack.pop()
        try:
            with os.scandir(directory) as entries:
                for entry in entries:
                    if time.monotonic() >= deadline or counts["entries"] >= max_entries:
                        limited = True
                        break
                    counts["entries"] += 1
                    p = Path(entry.path)
                    rel = p.relative_to(root)
                    try:
                        info = entry.stat(follow_symlinks=False)
                        if stat.S_ISLNK(info.st_mode):
                            counts["symlinks_skipped"] += 1
                            continue
                        if stat.S_ISDIR(info.st_mode):
                            stack.append(p)
                            continue
                        if not stat.S_ISREG(info.st_mode):
                            counts["special_files_skipped"] += 1
                            continue
                        counts["regular_files"] += 1
                        counts["measured_file_bytes"] += info.st_size
                        if any(part in CONTENT_EXCLUDES for part in rel.parts[:-1]):
                            counts["excluded_content_files"] += 1
                            continue
                        if p.suffix.lower() not in TEXT_SUFFIXES and not p.name.startswith(".env") and p.name not in {"Dockerfile", "Makefile"}:
                            counts["non_text_files"] += 1
                            continue
                        if info.st_size > max_file_bytes or counts["scan_bytes"] + info.st_size > max_scan_bytes:
                            counts["large_files_skipped"] += 1
                            continue
                        # Reject a file replaced with a symlink between traversal and open.
                        fd = os.open(p, os.O_RDONLY | getattr(os, "O_NOFOLLOW", 0) | getattr(os, "O_NONBLOCK", 0))
                        with os.fdopen(fd, "rb") as stream:
                            opened = os.fstat(stream.fileno())
                            if not stat.S_ISREG(opened.st_mode) or (opened.st_dev, opened.st_ino) != (info.st_dev, info.st_ino):
                                errors.append({"path": str(rel), "kind": "changed-during-scan"})
                                continue
                            raw = stream.read(max_file_bytes + 1)
                        counts["scan_bytes"] += len(raw)
                        if len(raw) > max_file_bytes or counts["scan_bytes"] > max_scan_bytes:
                            counts["large_files_skipped"] += 1
                            continue
                        try:
                            text = raw.decode("utf-8")
                            if "\0" in text:
                                raise UnicodeError()
                        except UnicodeError:
                            counts["non_text_files"] += 1
                            errors.append({"path": str(rel), "kind": "unreadable-text"})
                            continue
                        counts["text_files_read"] += 1
                        for line_number, line in enumerate(text.splitlines(), 1):
                            for kind, pattern in PATTERNS:
                                if pattern.search(line):
                                    counts["findings_total"] += 1
                                    if len(findings) < 100:
                                        findings.append({"path": str(rel), "line": line_number, "kind": kind, "status": "HUMAN_CHECK"})
                    except OSError as error:
                        errors.append({"path": str(rel), "kind": type(error).__name__})
        except OSError as error:
            errors.append({"path": str(directory.relative_to(root)), "kind": type(error).__name__})
    incomplete = limited or bool(errors)
    size_incomplete = incomplete or counts["symlinks_skipped"] > 0 or counts["special_files_skipped"] > 0
    size_status = "FAIL" if counts["measured_file_bytes"] > submission_limit_bytes else ("NOT_RUN" if size_incomplete else "PASS")
    scan_status = "NOT_RUN" if incomplete or counts["large_files_skipped"] else ("HUMAN_CHECK" if findings else "PASS")
    required_results = []
    for path in required_paths:
        candidate = root / path
        linked = any(part.is_symlink() for part in [candidate, *candidate.parents] if part != root and root in part.parents)
        try:
            passed = not linked and candidate.is_file() and candidate.stat().st_size > 0
        except OSError:
            passed = False
        required_results.append({"path": str(path), "status": "PASS" if passed else "FAIL"})
    return {
        "workspace": str(root), "read_only": True,
        "size": {"status": size_status, "limit_bytes": submission_limit_bytes,
                 "note": "Logical regular-file bytes, including .git/dependencies. Skipped paths make this a lower bound; platform scope still needs confirmation."},
        "pattern_scan": {"status": scan_status, "findings": findings,
                         "note": "PASS means no listed pattern found in scanned text only. Loopback references can be clients/docs; inspect actual server binding."},
        "coverage": {**counts, "limit_reached": limited, "errors": errors[:100],
                     "errors_total": len(errors), "content_excluded_directories": sorted(CONTENT_EXCLUDES)},
        "required_files": required_results,
        "git": git_summary(root), "resources": resources(),
        "manual_checks": ["Actual README requirements and commands", "Editor files saved",
                          "Required server port/binding and UI flow", "Submission completion indicator"],
        "note": "No grading guarantee, full security assurance, deletion, configuration changes or submission performed.",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workspace", default=".")
    parser.add_argument("--require", action="append", default=[])
    parser.add_argument("--max-entries", type=int, default=50000)
    parser.add_argument("--max-file-bytes", type=int, default=1048576)
    parser.add_argument("--max-scan-bytes", type=int, default=20971520)
    parser.add_argument("--seconds", type=float, default=15)
    parser.add_argument("--submission-limit-bytes", type=int, default=10000000000)
    args = vars(parser.parse_args())
    args["required"] = args.pop("require")
    try:
        report = audit(**args)
        print(json.dumps(report, ensure_ascii=False, indent=2))
        if report["size"]["status"] == "FAIL" or any(x["status"] == "FAIL" for x in report["required_files"]):
            return 1
        if report["pattern_scan"]["status"] != "PASS" or report["size"]["status"] != "PASS":
            return 2
        return 0
    except (OSError, ValueError) as error:
        parser.exit(2, f"Audit NOT_RUN: {type(error).__name__}; verify workspace and options.\n")


if __name__ == "__main__":
    raise SystemExit(main())
