---
name: probe-decisions
description: 담당자 답변, 데이터 처리, 구현 대안, 검증 실패 또는 방향 변경이 생길 때 짧은 결정 기록을 남기고 요구와 증거에 연결한다.
---

`.probe-kit/AGENTS.override.md`를 따른다. 매 명령이 아니라 결과를 바꾸는 선택에만 기록한다.
`.probe-kit/runtime/DECISIONS.md`에 선택, 버린 대안, 이유, Q-ID 또는 R-ID, 실행 근거, 한계를 적는다.
이전 판단을 바꾸면 과거를 지우지 말고 새 행에서 무엇을 정정했는지 밝힌다. 사용자가 하지 않은 판단을 사용자 결정으로 적지 않는다.

안정적으로 행을 추가하려면 다음 스크립트를 사용한다. 각 값은 실제 확인한 사실로 채운다.

```bash
python3 .probe-kit/scripts/decision.py --workspace . --requirement R-01 --choice '선택' --alternative '대안' --reason '이유' --evidence '명령과 결과 또는 NOT_RUN' --limit '남은 한계'
```

검증을 실행하지 않았으면 NOT_RUN으로 남긴다. 제출물 확정 전에 사용자가 선택 이유와 한계를 직접 설명하게 하고, 실제 후속 서술형에서는 이 스킬을 사용하지 않는다.
