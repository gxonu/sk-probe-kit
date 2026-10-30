---
name: probe-workflow
description: 제공된 Cofa 과제 환경에서 요구 확인, 메인과 서브 작업 분담, 검증과 제출 전 정리를 진행한다. 실제 후속 서술형 답변에는 사용하지 않는다.
---

# 과제 작업 흐름

과제 루트의 `.probe-kit/docs/RULES.md`를 먼저 읽고 공식 안내를 우선한다.
메인은 원본 `.probe-kit/AGENTS.md`, 작업자는 `.probe-kit/SUB_AGENTS.md`를 읽되 AGENTS.override.md의 충돌 기준이 우선한다. 실전 순서와 요청 문구는 `.probe-kit/foruser.md`를 따른다. 설치 상태는 preflight.py로 확인하되 실제 플랫폼 확인과 구분한다.
이 경로가 없으면 설치되지 않은 상태라고 알리고 임의의 전역 설정을 만들지 않는다.
프로젝트 루트의 docs/handoff/README.md와 CURRENT.md를 읽고 자신의 세션 ID, 담당 경로, 통합 담당자를 확인한다. 기록은 경로를 알려주고 다른 세션이 읽어야 전달된다.

1. README와 제출 규격, 작은 파일 목록을 확인한다. 실제 시작, 전체 마감, 화면의 제한 시간을 묻거나 제공된 값을 사용한다. plan_time.py의 시간표를 CURRENT에 기록하며 날짜를 추정하지 않는다.
2. `.probe-kit/runtime/REQUIREMENTS.md`에 확인된 사실, 가정, 열린 질문, 제외 범위, 수치 또는 검증 가능한 성공 기준을 작성한다. `.probe-kit/docs/interview.md`에서 해당 조건을 골라 질문 초안을 최대 3개씩 제공하고, 받은 답은 QUESTION_LOG의 Q-ID에서 요구 R-ID와 테스트로 연결한다.
3. 최초 계획을 사용자에게 보여 주고 승인 후 최소 동작부터 구현한다. 과제 종류별 점검은 `.probe-kit/docs/scenarios.md`의 해당 절만 읽는다.
4. 사용자가 여러 세션을 쓰면 통합 담당자가 CURRENT에 겹치지 않는 쓰기 경로와 완료 조건을 배정한다. 메인이 docs/handoff/sessions/<session-id>/TASK_SPEC.md에 명세를 쓰고 해당 작업자는 같은 폴더의 SUB_RESULT.md와 HANDOFF.md에 결과를 남긴다. 메인 + 작업자 1~2개는 예시이며 역할과 개수를 고정하지 않는다. 공통 원장 변경은 통합 담당자에게 제안한다. 단일 작업자에게 독점 배정한 경우 기존 TASK_SPEC와 SUB_RESULT를 사용할 수 있다. 별도 세션이 없으면 직접 진행한다.
5. 필요하면 `.probe-kit/scripts/data_scan.py`로 지정한 CSV를 제한된 행 수만 읽는다. 표본의 통계를 전체 데이터의 통계로 보고하지 않는다. 반도체 용어가 막힐 때만 `.probe-kit/docs/knowledge.md`를 읽는다.
6. 담당자 답변, 처리 기준, 대안 포기, 실패 또는 방향 전환 시 DECISIONS.md에 선택, 버린 대안, 이유, 근거, 한계를 남긴다. `scripts/decision.py`로 추가할 수 있으며 과거 판단을 바꾸면 새 행에 정정한다. CURRENT의 실제 시간표를 따라 첫 완주, 기능 동결, 제출을 진행한다.
7. 제출 전에 REQUIREMENTS의 각 항목을 PASS / FAIL / NOT_RUN / HUMAN_CHECK로 갱신한다. 실제 저장과 재실행, 제출 형식을 확인한다. 자동으로 시험 제출 버튼을 누르지 않는다.

세션 교체 시 자신의 인계 문서를 갱신하고 통합 담당자가 CURRENT에 반영한다. 새 세션은 현재 상태, 자신의 인계와 필요한 보고서를 읽고 제약과 다음 행동을 요약한 뒤 이어간다.
출제 예측과 지식 자료는 요구사항이 아니다. 테스트 실행 여부와 가점을 만들어 보고하지 않는다.
