# 실전 시작 안내

당일에는 [docs/RUNBOOK.md](docs/RUNBOOK.md)를 열고 단계별로 진행한다. 설치 후 경로는 .probe-kit/docs/RUNBOOK.md다.
공식 규칙과 응시 화면이 이 문서보다 우선한다.

1. 실제 시작 시각, 과제 제한, 전체 마감과 후속 서술형 시간을 확인한다.
2. README 설치 명령을 과제 루트에서 실행하고 preflight.py로 구성과 Codex 시작을 점검한다.
3. 메인 세션에 RUNBOOK의 시작 요청을 전달하고 plan_time.py 결과를 CURRENT에 기록한다.
4. 담당자 답으로 요구와 최초 계획을 확정한다.
5. 메인이 BUILD의 파일 범위를 배정하고 응시자가 같은 폴더에서 작업 세션을 연다.
6. 명세, 구현, 실행, 메인 확인, 원장 반영을 반복하며 첫 전체 흐름을 완성한다.
7. 계산한 기능 동결 시각에 필수 요구와 실제 실행 증거, 저장과 제출 형식을 확인한다.
8. 제출 확정 전 자기 구현의 선택과 한계를 확인하고, 확정 이후 AI 작업을 멈춘다.

- 현재 상태: 프로젝트 루트의 docs/handoff/CURRENT.md
- 세션별 명세와 결과: docs/handoff/sessions/<session-id>.md
- 실행 증거: docs/reports/<session-id>-<topic>.md
- 합의된 요구와 결정: .probe-kit/runtime

[설치 전 전체 흐름 점검](docs/REHEARSAL.md)은 새 임시 폴더에서만 합성 자료로 진행한다.
원본 foruser.md는 upstream/chichochoi/foruser.md에 보존한다.
