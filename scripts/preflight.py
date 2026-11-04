#!/usr/bin/env python3
"""Check local installation and CLI startup; never install or change settings."""
import argparse
import json
from pathlib import Path
import shutil
import subprocess
import sys

REQUIRED = [
    ".probe-kit/AGENTS.md", ".probe-kit/SUB_AGENTS.md", ".probe-kit/foruser.md",
    ".probe-kit/AGENTS.override.md", ".probe-kit/docs/RULES.md",
    ".probe-kit/docs/TEAM_PLAYBOOK.md", ".probe-kit/runtime/REQUIREMENTS.md",
    ".probe-kit/runtime/QUESTION_LOG.md", ".probe-kit/runtime/DECISIONS.md",
    ".probe-kit/runtime/EVIDENCE.md", "docs/handoff/README.md",
    "docs/handoff/CURRENT.md", "docs/handoff/TEMPLATE.md",
    "docs/reports/TEMPLATE.md", "docs/references/README.md",
    ".probe-kit/knowledge/semiconductor/index.jsonl",
    ".probe-kit/scripts/question_log.py",
    "docs/handoff/sessions/S8-explain/TASK_SPEC.md",
    "docs/handoff/sessions/S8-explain/SUB_RESULT.md",
]
SKILLS = ("workflow", "interview", "decisions", "debug", "verify", "explain")


def inspect(workspace, files_only=False):
    root = Path(workspace).resolve(strict=True)
    if not root.is_dir():
        raise ValueError("과제 폴더를 지정하세요.")
    checks = []
    def record(name, passed, detail):
        checks.append({"check": name, "status": "PASS" if passed else "FAIL", "detail": detail})
    record("python", sys.version_info >= (3, 9), sys.version.split()[0])
    for name in REQUIRED + [f".agents/skills/probe-{x}/SKILL.md" for x in SKILLS]:
        p = root / name
        record(name, p.is_file() and p.stat().st_size > 0, "존재하고 비어 있지 않아야 함")
    for name in ("bash", "git"):
        record(name, bool(shutil.which(name)), "실행 파일 존재 확인")
    if files_only:
        checks.append({"check": "codex --version", "status": "NOT_RUN", "detail": "--files-only"})
    else:
        cli = shutil.which("codex")
        if not cli:
            record("codex --version", False, "codex 명령을 찾을 수 없음")
        else:
            try:
                result = subprocess.run([cli, "--version"], cwd=root, text=True,
                                        capture_output=True, timeout=10)
                record("codex --version", result.returncode == 0,
                       (result.stdout or result.stderr).strip()[:500])
            except (OSError, subprocess.TimeoutExpired) as error:
                record("codex --version", False, str(error))
    return {
        "workspace": str(root),
        "local_status": "FAIL" if any(x["status"] == "FAIL" for x in checks) else "PASS",
        "checks": checks,
        "manual_status": "NOT_RUN",
        "manual_checks": [
            "당일 규칙과 시작, 종료, 남은 시간",
            "Codex 로그인 및 응시 환경의 허용 모델 목록",
            "담당자와 Helper 접근, 카메라 및 감독 연결",
            "실제 과제 실행 명령, 내장 Browser 화면, 제출 형식",
        ],
        "note": "PASS는 로컬 구성 점검 결과이며 실제 과제 완료나 플랫폼 연결 성공이 아닙니다.",
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workspace", default=".")
    parser.add_argument("--files-only", action="store_true")
    args = parser.parse_args()
    try:
        result = inspect(**vars(args))
        print(json.dumps(result, ensure_ascii=False, indent=2))
        sys.exit(0 if result["local_status"] == "PASS" else 1)
    except (ValueError, OSError) as error:
        parser.exit(2, str(error) + "\n")
