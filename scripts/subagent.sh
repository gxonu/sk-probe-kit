#!/usr/bin/env bash
set -euo pipefail
cat <<'GUIDE'
메인이 docs/handoff/CURRENT.md에 세션 ID와 쓰기 경로를 먼저 배정합니다.
같은 과제 루트의 새 터미널에서 codex를 시작하고 실제 제공된 허용 모델을 선택하세요.
다음 요청의 세션 ID만 배정받은 값으로 바꾸세요:
[BUILD] .probe-kit/AGENTS.override.md, docs/handoff/README.md, docs/handoff/CURRENT.md와
docs/handoff/sessions/<session-id>.md를 읽고 승인된 범위만 구현해.
실행 결과와 미검증은 자기 인계와 docs/reports의 자기 보고서에 기록해.
공통 원장 변경은 메인에게 제안하고 다른 세션의 파일은 수정하지 마.
GUIDE
