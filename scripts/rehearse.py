#!/usr/bin/env python3
"""Exercise the kit in a new synthetic temporary task; no AI or network calls."""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile

SOURCE = Path(__file__).resolve().parents[1]
DATA = "id,status,value\nA,measured,10\nB,measured,20\nC,cancelled,90\nD,measured,\n"
PIPELINE = """import csv,json,sys
rows=list(csv.DictReader(open('data.csv',newline='',encoding='utf-8')))
total=count=excluded=review=0
for row in rows:
    if row['status']=='cancelled' and '--include-cancelled' not in sys.argv:
        excluded+=1
    elif not row['value']:
        review+=1
    else:
        total+=int(row['value']); count+=1
print(json.dumps(dict(total=total,count=count,excluded=excluded,review=review)))
"""
VALIDATOR = """import json,sys
# Fixed oracle calculated from the four synthetic rows, independent of pipeline.
actual=json.load(open(sys.argv[1],encoding='utf-8'))
expected={'total':30,'count':2,'excluded':1,'review':1}
if actual != expected:
    print('FAIL: output differs from the fixed oracle')
    sys.exit(1)
print('PASS: total=30 count=2 excluded=1 review=1')
"""


def rehearse():
    if not (SOURCE / '.agents/skills').is_dir() or not (SOURCE / 'install.sh').is_file():
        raise ValueError("준비용 sk-probe-kit 원본 저장소의 scripts/rehearse.py를 실행하세요.")
    task = Path(tempfile.mkdtemp(prefix="probe-kit-rehearsal-"))
    report = {"kind": "SYNTHETIC_LOCAL_REHEARSAL", "workspace": str(task),
              "timestamp": datetime.now(timezone.utc).isoformat(),
              "status": "RUNNING", "steps": [], "ai_sessions": "NOT_RUN",
              "probe_platform": "NOT_RUN"}
    def run(label, command, expected_exit=0):
        r = subprocess.run(command, cwd=task, text=True, capture_output=True, timeout=60)
        report["steps"].append({"step": label, "command": command, "exit_code": r.returncode,
                                "expected_exit": expected_exit, "stdout": r.stdout, "stderr": r.stderr})
        if r.returncode != expected_exit:
            raise RuntimeError(f"{label}: expected exit {expected_exit}, got {r.returncode}: {r.stderr}")
        return r.stdout

    def save():
        (task / "docs/reports").mkdir(parents=True, exist_ok=True)
        (task / "docs/reports/rehearsal.json").write_text(
            json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    try:
        (task / "README.md").write_text(
            "# SYNTHETIC FIXTURE\nSum measured values, exclude cancelled rows, review missing values.\n",
            encoding="utf-8")
        (task / "data.csv").write_text(DATA, encoding="utf-8")
        baseline = {p: (task / p).read_bytes() for p in ("README.md", "data.csv")}
        installer = [sys.executable, str(SOURCE / "scripts/install.py"), str(task)]
        run("installation preview", installer + ["--dry-run"])
        if (task / ".probe-kit").exists():
            raise RuntimeError("dry run created installation files")
        run("installation", installer)
        scripts = task / ".probe-kit/scripts"
        run("preflight", [sys.executable, str(scripts / "preflight.py"), "--workspace", str(task)])
        schedule = json.loads(run("schedule", [
            sys.executable, str(scripts / "plan_time.py"),
            "--start", "2026-10-31T10:00:00+09:00", "--hard-end", "2026-10-31T14:00:00+09:00"]))
        if not (schedule["feature_freeze"].endswith("12:20:00+09:00")
                and schedule["submission_start"].endswith("12:50:00+09:00")
                and schedule["task_finish_by"].endswith("13:00:00+09:00")):
            raise RuntimeError("schedule differs from the synthetic expected checkpoints")
        sessions = task / "docs/handoff/sessions"
        sessions.mkdir()
        (task / "docs/handoff/CURRENT.md").write_text(
            "# SYNTHETIC ONLY\nIntegrator: main. Worker: build.\n"
            "main owns runtime ledgers; build owns pipeline.py and its report.\n"
            "No AI session was started; a deterministic local driver executes this fixture.\n",
            encoding="utf-8")
        (sessions / "main.md").write_text(
            "# main — synthetic fixture driver\nR-01: total=30, count=2, excluded=1, review=1.\n"
            "Q-01: cancellation and missing-value behavior is specified by fixture README.\n",
            encoding="utf-8")
        (sessions / "build.md").write_text(
            "# build — synthetic fixture driver\nScope: pipeline.py, validate_fixture.py, result.json.\n"
            "Acceptance: python validate_fixture.py result.json\nState: ACTIVE\n",
            encoding="utf-8")
        runtime = task / ".probe-kit/runtime"
        with (runtime / "QUESTION_LOG.md").open("a", encoding="utf-8") as f:
            f.write("| Q-01 | cancellation and missing values | fixture contract | "
                    "SYNTHETIC README: exclude cancelled, review missing | DOCUMENT_REPORTED | R-01 | fixed oracle |\n")
        with (runtime / "REQUIREMENTS.md").open("a", encoding="utf-8") as f:
            f.write("\nR-01: SYNTHETIC contract, exclude cancelled and review missing. Verification pending.\n")
        scan = json.loads(run("data scan", [sys.executable, str(scripts / "data_scan.py"), "data.csv"]))
        if scan["rows_scanned"] != 4 or scan["truncated"]:
            raise RuntimeError("data scan did not cover the four-row fixture")
        (task / "pipeline.py").write_text(PIPELINE, encoding="utf-8")
        (task / "validate_fixture.py").write_text(VALIDATOR, encoding="utf-8")
        (task / "wrong.json").write_text(run("deliberately wrong output", [
            sys.executable, "pipeline.py", "--include-cancelled"]), encoding="utf-8")
        run("oracle rejects wrong output", [sys.executable, "validate_fixture.py", "wrong.json"], expected_exit=1)
        (task / "result.json").write_text(run("correct output", [sys.executable, "pipeline.py"]), encoding="utf-8")
        run("oracle accepts correct output", [sys.executable, "validate_fixture.py", "result.json"])
        run("decision record", [
            sys.executable, str(scripts / "decision.py"), "--workspace", str(task),
            "--requirement", "R-01", "--choice", "exclude cancelled; review missing",
            "--alternative", "include cancelled in sum", "--reason", "synthetic README contract",
            "--evidence", "oracle rejects wrong.json and accepts result.json",
            "--limit", "synthetic rule only; revisit if the actual task contract differs"])
        with (runtime / "EVIDENCE.md").open("a", encoding="utf-8") as f:
            f.write("| R-01 | python validate_fixture.py result.json | total=30, count=2, excluded=1, review=1 | PASS | result.json | pipeline.py | wrong.json rejected with exit 1 |\n")
        with (runtime / "REQUIREMENTS.md").open("a", encoding="utf-8") as f:
            f.write("R-01: PASS, see EVIDENCE.md and docs/reports/build-01.md.\n")
        (task / "docs/reports/build-01.md").write_text(
            "# Synthetic execution evidence\nExecutor: deterministic fixture driver, no AI worker.\n"
            "Wrong output rejected with exit 1. Correct output accepted with exit 0.\n"
            "Result: total=30, count=2, excluded=1, review=1.\n",
            encoding="utf-8")
        with (sessions / "build.md").open("a", encoding="utf-8") as f:
            f.write("State: HANDOFF. Read docs/reports/build-01.md; R-01 verified.\n")
        with (sessions / "main.md").open("a", encoding="utf-8") as f:
            f.write("Received build report. Actual oracle output inspected; ledgers updated. State: HANDOFF.\n")
        protected = list(baseline) + [
            "docs/handoff/CURRENT.md", "docs/handoff/sessions/main.md",
            "docs/handoff/sessions/build.md", "docs/reports/build-01.md",
            ".probe-kit/runtime/DECISIONS.md", ".probe-kit/runtime/EVIDENCE.md",
            ".probe-kit/runtime/REQUIREMENTS.md", ".probe-kit/runtime/QUESTION_LOG.md",
        ]
        before = {p: (task / p).read_bytes() for p in protected}
        run("reinstall after handoff", installer)
        if any((task / p).read_bytes() != value for p, value in before.items()):
            raise RuntimeError("reinstallation changed existing task records")
        if any((task / p).read_bytes() != value for p, value in baseline.items()):
            raise RuntimeError("original README or data changed")
        report["status"] = "PASS"
        report["result"] = json.loads((task / "result.json").read_text())
        report["protected_files"] = len(protected)
        report["fixture_sha256"] = hashlib.sha256(DATA.encode()).hexdigest()
        save()
        return report
    except Exception as error:
        report["status"] = "FAIL"
        report["error"] = str(error)
        save()
        raise RuntimeError(f"{error}\nEvidence: {task / 'docs/reports/rehearsal.json'}") from error


if __name__ == "__main__":
    try:
        result = rehearse()
        print(json.dumps({k: v for k, v in result.items() if k != "steps"}, ensure_ascii=False, indent=2))
    except Exception as error:
        sys.exit(str(error))
