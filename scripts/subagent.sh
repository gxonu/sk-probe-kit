#!/usr/bin/env bash
set -euo pipefail
cat <<'GUIDE'
과제 루트의 새 터미널에서 codex를 시작하고 /model로 제공된 허용 모델을 선택하세요.
다음 요청을 입력하세요:
[SUB] .probe-kit/AGENTS.override.md를 먼저 읽고 .probe-kit/runtime/TASK_SPEC.md 범위만 구현해.
실행 결과와 미검증을 .probe-kit/runtime/SUB_RESULT.md에 기록해.
기본 승인 및 샌드박스 설정을 유지하고 다른 세션의 파일은 수정하지 마.
GUIDE
