#!/usr/bin/env bash
set -euo pipefail
cat <<'GUIDE'
메인이 docs/handoff/CURRENT.md에 세션 ID와 쓰기 경로를 먼저 배정합니다.
같은 과제 루트의 새 터미널에서 codex를 시작하고 실제 제공된 허용 모델을 선택하세요.
다음 요청의 세션 ID만 배정받은 값으로 바꾸세요:
[SUB] .probe-kit/SUB_AGENTS.md와 .probe-kit/AGENTS.override.md,
docs/handoff/README.md, docs/handoff/CURRENT.md,
docs/handoff/sessions/<session-id>/TASK_SPEC.md를 읽고 배정된 역할과 범위만 수행해.
작업 ID와 실제 결과는 같은 세션 폴더의 SUB_RESULT.md, 인계는 HANDOFF.md에 남겨.
실행 결과가 길면 docs/reports의 자기 보고서에 기록해.
질문 원문은 question_log.py로 추가하고 다른 공통 원장 변경은 S1에게 제안해.
GUIDE
