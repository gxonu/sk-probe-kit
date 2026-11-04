# 같은 과제 폴더에서 공유하기

공식 과제 지침 -> .probe-kit/AGENTS.md -> [CURRENT](CURRENT.md)와 자기 sessions/<session-id>/TASK_SPEC.md 순으로 읽는다. 배정된 경로와 관련 결과/인계만 추가로 읽는다.

세션은 사용자가 직접 연다. 채팅 자동 공유, 파일 잠금과 자동 알림은 제공하지 않는다.

## 작성자와 기록

- S1만 CURRENT와 .probe-kit/runtime의 REQUIREMENTS, QUESTION_LOG, DECISIONS, EVIDENCE를 최종 갱신한다.
- S1은 세션별 TASK_SPEC에 작업 ID, 목표, 정확한 쓰기 경로, 계약/제약, 검증과 완료 조건을 적는다.
- 작업자는 같은 폴더 SUB_RESULT에 작업 ID, 실제 변경/명령/출력과 한계를, HANDOFF에 다음 행동을 쓴다. [인계 양식](TEMPLATE.md)을 사용한다.
- 기본 ID는 S1-main, S2-worker-a, S3-worker-b, S4-data, S5-research, S6-review, S7-records다. 설치 때 생성되는 PLANNED와 빈 양식은 실행/배정 완료가 아니다.
- 세부 역할은 .probe-kit/docs/TEAM_PLAYBOOK.md를 따른다. 공통 코드/설정뿐 아니라 서버/포트/DB/출력도 소유자를 정한다.
- S7은 근거와 원장 반영안을 제안하고 배정된 제출 문서를 쓴다. S6는 확인된 결함과 의심을 구분해 원 소유자에게 전달한다.
- 진행 중인 명세는 작업자에게 알리지 않고 바꾸지 않는다. 결과의 작업 ID가 현재 명세와 다르면 완료로 수용하지 않는다.

## 전달과 교체

1. 결과를 상태/변경/검증/요청으로 짧게 정리하고 파일 경로를 전달한다. 큰 증거는 자기 docs/reports에 둔다.
2. 수신자는 필요한 원출력과 코드를 확인하고 수신/반영 여부를 기록한다. 별도 요청 파일이 필요하면 [messages](messages/README.md)를 따른다.
3. 종료나 교체 때 자기 HANDOFF에 현재 코드/입력 기준, 실패/미검증, 다음 행동 최대 3개와 남은 시간을 적는다.
4. S1이 CURRENT의 PLANNED/ACTIVE/WAITING/HANDOFF/CLOSED 상태와 갱신 시각을 관리한다. 상태는 자동 감지가 아니다.
5. 소유권을 인수할 때 기존 담당의 종료/인계를 확인한다. 오래된 ACTIVE만 보고 파일을 가져오거나 다른 세션의 변경을 원복하지 않는다.

같은 폴더의 파일만 즉시 공유된다. 다른 clone/worktree에 자동 전달되지 않는다. 시험 중에는 허용된 과제 환경 안에서만 공유하고 외부 전송하지 않는다.
