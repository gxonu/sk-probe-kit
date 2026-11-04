# 활성 파일 정리

2026-11-04. 기본 운영은 사용자가 직접 여는 7개 세션이다.

## 읽는 문서의 기준

- 실행 순서와 스킬 호출 시점: [foruser](../foruser.md).
- 7개 역할, 파일 소유권, 시작 요청: [TEAM_PLAYBOOK](TEAM_PLAYBOOK.md).
- 현재 과제의 배정과 진행: 설치 대상의 docs/handoff/CURRENT.md.
- 명세, 결과, 인계: docs/handoff/sessions/<session-id>/ 아래 세 파일.
- 공통 요구, 질문, 결정, 증거: .probe-kit/runtime. S1만 최종 반영한다.

## 제거와 통합

활성 경로 15개를 정리했다. 내용이 필요한 원본 12개는 upstream/chichochoi에 동일한 바이트로 남겨 두었다. 원본 보관본은 실행 지침이 아니며 AGENTS.override가 우선한다.

| 제거한 활성 파일 | 처리와 현재 대안 |
|---|---|
| START_HERE.md, docs/RUNBOOK.md, docs/prompts.md | 설치와 단계는 foruser, 역할별 요청은 TEAM_PLAYBOOK으로 통합. 기존 버전은 Git 이력에 보존 |
| config.toml | upstream 원본만 보관. 전역 설정에 설치하지 않음 |
| prompts/02_codex_prompts.md, prompts/03_post_qna_formula.md | 원본만 보관. 현재 요청은 foruser/TEAM_PLAYBOOK, 설명 연습은 mock-exam |
| templates/NOTES.md, skills/handoff.md | 원본만 보관. 공통 원장과 세션별 HANDOFF 사용 |
| scripts/init.sh | 중복 래퍼 제거. 루트 init.sh가 설치 진입점 |
| scripts/handoff.py, scripts/handoff.sh | 원본만 보관. 여러 세션이 같은 로그에 쓰는 구형 흐름 제거 |
| scripts/pre_submit_audit.py, scripts/pre_submit_audit.sh | 원본만 보관. 변경 확인은 git status/diff, 기능 확인은 실제 실행과 probe-verify |
| runtime/TASK_SPEC.md, runtime/SUB_RESULT.md | 공용 작업 지시서/결과 사본 제거. 설치기가 세션마다 독립된 양식 생성 |

## 보존한 파일

- 원본 AGENTS.md와 SUB_AGENTS.md, ORIGINS에 기록된 원본 125개.
- 네 가지 Case 안내. 세션 경로와 제거한 감사 스크립트 호출만 현재 방식으로 연결.
- 반도체 지식 94개 파일, 서술형 참고 자료, 출처와 라이선스.
- data_scan과 eda_scan: 제한된 CSV 요약과 상세 분석이라는 용도가 다르므로 유지.
- sample_check_template과 SUBMISSION_REPORT: 참고 양식으로 유지. 실제 검증과 제출 규격은 해당 과제를 기준으로 삼는다.
- 날짜가 붙은 제작 이력은 실제 과제에 설치하지 않는다. 당시의 RUNBOOK 등 언급은 과거 이력이다.

## 새 설치와 재설치

S1~S7은 PLANNED로 생성된다. 각 폴더의 TASK_SPEC, SUB_RESULT, HANDOFF는 미작성 양식이며 자동 실행 또는 배정 완료가 아니다. 실제 파일과 실행 자원은 S1이 배정한다.

기존 CURRENT, 세션 기록과 과제 파일은 보존한다. 이전 버전의 설치 파일과 충돌하면 쓰기 전에 중단한다. 진행 중인 과제를 강제로 갱신하거나 오래된 기록을 자동 삭제하지 않는다.
