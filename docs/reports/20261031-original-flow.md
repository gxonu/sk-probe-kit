# 원본 중심 구성과 다중 세션 확인

2026-10-31 KST, 기준 커밋 7edb2e3. 준비용 하네스의 변경과 로컬 확인이며 실제 응시 결과가 아니다.

## 변경

- 원본 AGENTS.md 89행과 SUB_AGENTS.md 86행을 그대로 유지했다.
- foruser.md를 원본의 시간순 단계와 요청 문구를 중심으로 복원하고 공식 규칙, 설치 경로와 세션별 공유를 맞췄다. docs/RUNBOOK.md는 보조 요약이다.
- 원본 TASK_SPEC → 구현 → SUB_RESULT → 메인 검토 흐름을 유지한다. 메인 + worker-a + worker-b는 예시이며 역할과 수는 조정 가능하다.
- 각 작업자의 명세, 결과와 인계는 docs/handoff/sessions/<session-id>/ 아래에 둔다. 명세는 메인, 결과와 인계는 해당 작업자가 작성한다. 작업 ID로 명세와 결과를 연결한다.
- 반도체 자료와 서술형 대비는 그대로 보조 자료로 유지한다. docs/handoff, references, reports는 세션 공유 공간이다.
- 15분 체험에는 제공된 작업 공간 내부의 기록 폴더와 명령을 안내한다. 외부 화면 감시나 녹화는 실행하지 않았다.

## 실제 확인

| 확인 | 방법 | 결과 |
|---|---|---|
| 기존 기능 | python3 -m unittest discover -s tests -v | 21 tests, OK |
| 원본 보존 | ORIGINS.json의 각 SHA-256과 파일 대조 | 125개 일치 |
| 루트 지침 보존 | AGENTS.md와 SUB_AGENTS.md를 upstream 원본과 바이트 비교 | 두 파일 동일 |
| 스킬 형식 | quick_validate.py로 probe 스킬 6개 검사 | 모두 유효 |
| 설치 안내 | 새 임시 폴더 설치 후 foruser 바이트 비교와 preflight --files-only | 일치, PASS |
| 3개 세션 기록 분리 | main 인계, worker-a와 worker-b의 명세, 결과, 인계에 서로 다른 합성 표식 기록 | 별도 파일과 내용 확인 |
| 재설치 보존 | 위 7개 파일과 CURRENT 저장 후 재설치 | 8개 파일 바이트 동일, 추가 쓰기 0개 |
| 셸과 변경 형식 | bash -n scripts/subagent.sh, git diff --check | PASS |

세션 기록 검사는 합성 파일을 쓰고 재설치 전후를 비교한 것이다. AI 3개 세션을 실제로 실행하거나 자동 동기화, 파일 잠금을 검증한 결과가 아니다. 실제 Probe 접속, 모델 권한, 감독 연결과 제출은 NOT_RUN이다.

세션마다 같은 프로젝트 루트를 사용하고 메인이 쓰기 범위를 나눠야 한다. 기존 설치본에 수정된 하네스를 덮어쓰는 업그레이드는 지원하지 않으며 충돌 시 중단한다. 새 과제 또는 새 점검 폴더에서 설치한다.
