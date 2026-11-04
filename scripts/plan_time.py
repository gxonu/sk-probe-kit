#!/usr/bin/env python3
"""Calculate task checkpoints from explicit timezone-aware official times."""
import argparse
from datetime import datetime, timedelta
import json


def plan(start, hard_end, task_minutes=180, generation_minutes=10,
         written_minutes=30, submission_minutes=10, explain_lead_minutes=30,
         submission_at=None):
    begin = datetime.fromisoformat(start)
    end = datetime.fromisoformat(hard_end)
    if begin.utcoffset() is None or end.utcoffset() is None:
        raise ValueError("시작과 종료에 시간대를 넣으세요. 예: +09:00")
    end = end.astimezone(begin.tzinfo)
    if end <= begin or task_minutes <= 0 or written_minutes <= 0:
        raise ValueError("종료는 시작 이후이고 과제 및 서술형 시간은 양수여야 합니다.")
    if generation_minutes < 0 or submission_minutes < 0 or explain_lead_minutes < 0:
        raise ValueError("대기, 제출 여유와 설명 준비 시간은 음수일 수 없습니다.")
    reserve = timedelta(minutes=generation_minutes + written_minutes)
    finish = min(begin + timedelta(minutes=task_minutes), end - reserve)
    planned = datetime.fromisoformat(submission_at) if submission_at else finish
    if planned.utcoffset() is None:
        raise ValueError("제출 예정 시각에도 시간대를 넣으세요.")
    planned = planned.astimezone(begin.tzinfo)
    if planned > finish:
        raise ValueError("제출 예정 시각은 과제 확정 한계를 넘을 수 없습니다.")
    submit = planned - timedelta(minutes=submission_minutes)
    if submit <= begin:
        raise ValueError("작업과 제출 여유 시간을 확보할 수 없습니다. 실제 남은 시간을 확인하세요.")
    budget = (planned - begin).total_seconds() / 60
    explain = min(submit, max(begin, planned - timedelta(minutes=explain_lead_minutes)))
    documents = explain
    freeze = max(begin, documents - timedelta(minutes=min(20, budget * 0.2)))
    first = min(begin + timedelta(minutes=40), freeze)
    return {
        "start": begin.isoformat(timespec="seconds"),
        "requirements_target": min(begin + timedelta(minutes=25), first).isoformat(timespec="seconds"),
        "first_flow_target": first.isoformat(timespec="seconds"),
        "feature_freeze": freeze.isoformat(timespec="seconds"),
        "documents_ready_by": documents.isoformat(timespec="seconds"),
        "submission_start": submit.isoformat(timespec="seconds"),
        "submission_planned": planned.isoformat(timespec="seconds"),
        "task_finish_by": finish.isoformat(timespec="seconds"),
        "explain_draft_after_first_flow": first.isoformat(timespec="seconds"),
        "explain_full_prep": explain.isoformat(timespec="seconds"),
        "explain_lead_minutes": explain_lead_minutes,
        "explain_shortened": explain <= first or (submit - explain).total_seconds() < 15 * 60,
        "explain_note": "첫 완주 뒤 초안, 문서 마감까지 전체 문답 갱신, 마지막 준비 구간은 사용자 설명 연습 중심. 제출 확인 병행, 자동 예약 아님.",
        "written_finish_if_task_ends_at_limit": (finish + reserve).isoformat(timespec="seconds"),
        "hard_end": end.isoformat(timespec="seconds"),
        "task_budget_minutes": budget,
        "generation_reserve_minutes": generation_minutes,
        "written_reserve_minutes": written_minutes,
        "note": "사용자가 입력한 시각의 계획입니다. 실제 화면 타이머와 최신 공식 규칙이 우선합니다.",
        "short_budget": budget < 60,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--start", required=True)
    parser.add_argument("--hard-end", required=True)
    parser.add_argument("--task-minutes", type=int, default=180)
    parser.add_argument("--generation-minutes", type=int, default=10)
    parser.add_argument("--written-minutes", type=int, default=30)
    parser.add_argument("--submission-minutes", type=int, default=10)
    parser.add_argument("--explain-lead-minutes", type=int, default=30)
    parser.add_argument("--submission-at", help="예정된 과제 제출 확정 시각, 시간대 포함")
    args = parser.parse_args()
    try:
        print(json.dumps(plan(**vars(args)), ensure_ascii=False, indent=2))
    except ValueError as error:
        parser.exit(2, str(error) + "\n")
