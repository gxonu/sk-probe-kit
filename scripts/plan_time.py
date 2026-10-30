#!/usr/bin/env python3
"""Calculate task checkpoints from explicit timezone-aware official times."""
import argparse
from datetime import datetime, timedelta
import json


def plan(start, hard_end, task_minutes=180, generation_minutes=10,
         written_minutes=30, submission_minutes=10):
    begin = datetime.fromisoformat(start)
    end = datetime.fromisoformat(hard_end)
    if begin.utcoffset() is None or end.utcoffset() is None:
        raise ValueError("시작과 종료에 시간대를 넣으세요. 예: +09:00")
    end = end.astimezone(begin.tzinfo)
    if end <= begin or task_minutes <= 0 or written_minutes <= 0:
        raise ValueError("종료는 시작 이후이고 과제 및 서술형 시간은 양수여야 합니다.")
    if generation_minutes < 0 or submission_minutes < 0:
        raise ValueError("대기와 제출 여유 시간은 음수일 수 없습니다.")
    reserve = timedelta(minutes=generation_minutes + written_minutes)
    finish = min(begin + timedelta(minutes=task_minutes), end - reserve)
    submit = finish - timedelta(minutes=submission_minutes)
    if submit <= begin:
        raise ValueError("작업과 제출 여유 시간을 확보할 수 없습니다. 실제 남은 시간을 확인하세요.")
    budget = (finish - begin).total_seconds() / 60
    freeze = max(begin, submit - timedelta(minutes=min(30, budget * 0.2)))
    first = min(begin + timedelta(minutes=40), freeze)
    return {
        "start": begin.isoformat(timespec="seconds"),
        "requirements_target": min(begin + timedelta(minutes=25), first).isoformat(timespec="seconds"),
        "first_flow_target": first.isoformat(timespec="seconds"),
        "feature_freeze": freeze.isoformat(timespec="seconds"),
        "submission_start": submit.isoformat(timespec="seconds"),
        "task_finish_by": finish.isoformat(timespec="seconds"),
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
    args = parser.parse_args()
    try:
        print(json.dumps(plan(**vars(args)), ensure_ascii=False, indent=2))
    except ValueError as error:
        parser.exit(2, str(error) + "\n")
