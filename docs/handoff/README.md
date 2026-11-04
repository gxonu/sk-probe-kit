# 세션 간 공유

같은 과제 폴더의 파일을 공유한다. 대화 전달, 세션 실행, 알림과 감시는 자동 제공하지 않는다.
읽는 순서: 공식 지침 → `.probe-kit/AGENTS.md` → [CURRENT.md](CURRENT.md) → 자기 TASK_SPEC과 SUB_RESULT → 필요한 근거다.

| 문서 | 작성자 | 용도 |
|---|---|---|
| CURRENT | S1 | 목표, 실제 시각, S1~S8 배정, 파일과 실행 자원 소유권 |
| REQUIREMENTS/DECISIONS/EVIDENCE | S1 | 합의된 요구, 선택, 실제 검증 |
| QUESTION_LOG | 각 세션이 전용 도구로 추가 | 질문과 답변 원문, 세션/출처, 별도 AI 정리 |
| sessions/<id>/TASK_SPEC | S1 | 목표, 소유 파일, 제약/입출력, 검증, 완료 기준 |
| sessions/<id>/SUB_RESULT | 해당 세션 | 실제 결과, 근거, 실패/미검증, S1 반영 제안과 다음 행동 |
| sessions/<id>/HANDOFF | 해당 세션 | 세션 교체 또는 중단 시 이어갈 맥락 |

QUESTION_LOG는 `.probe-kit/scripts/question_log.py`로만 추가한다. 직접 병렬 편집하지 않는다. 답변을 기록했다고 REQUIREMENTS가 자동 확정되는 것은 아니다.
S1이 진행 중인 명세를 바꿀 때 대상 세션에 변경 사실과 작업 ID를 알려준다. 결과의 작업 ID와 현재 명세가 다르면 완료로 수용하지 않는다.
기준 HEAD가 같아도 미커밋 변경은 다를 수 있다. 관련 파일과 실제 결과를 확인하고 다른 세션의 변경을 되돌리지 않는다.
세션은 PLANNED / ACTIVE / WAITING / HANDOFF / CLOSED 상태와 갱신 시각을 기록한다. 상태 자동 감지가 아니므로 오래된 ACTIVE만 보고 소유권을 가져오지 않는다.
작은 전달은 SUB_RESULT와 Q-ID로 충분하다. 긴 검증만 `docs/reports/<session-id>-<topic>.md`에 분리한다. 별도 메시지가 필요하면 [messages 안내](messages/README.md)를 사용한다.
기록한 뒤 수신자에게 파일 경로를 전달한다. 수신자는 읽은 작업 ID와 처리 결과를 자기 파일에 남긴다. 같은 폴더 밖의 clone/worktree에는 자동 반영되지 않는다.
실제 응시 자료는 제공 환경 안에서만 공유하며 Git push와 외부 전송을 하지 않는다.
