# 현재 하네스 개발 상태

이 문서는 준비용 sk-probe-kit 저장소의 개발 상태다. 설치한 과제에는 미시작 상태의 별도 CURRENT가 생성된다.

- 목표: chichochoi 원본 흐름을 중심으로 보조 지식과 유연한 다중 세션 공유를 결합.
- 공식 기준: [RULES](../RULES.md). 사용자 요청으로 준비용 저장소를 보완하는 단계다.
- 통합 담당: 20261104-codex-team-design
- 갱신: 2026-11-04 KST
- 기준 커밋: 90289633ecb33b2ab32a26906b6e37dfdda7aeb9, prep/seven-session-review
- 작업 상태: HANDOFF, 기본 7개 역할 확정, 활성 파일 정리와 설치 검증 완료. 배포 커밋은 Git 이력에서 확인한다. 아래 이전 기록은 개발 이력이다.
- 작업 폴더: 이 문서가 속한 저장소 루트. 같은 이름의 이전 초안을 사용하지 않는다.
- 관련 출처: [인터뷰 분석](../references/cofa-probe-interview-20261031.md)
- 실전 시작점: [foruser.md](../../foruser.md)
- 현재 보고서: [7개 세션 확정과 정리](../reports/20261104-cleanup.md). 이전 설계: [6~7개 세션과 예상 문항 개선](../reports/20261104-team-design.md). 이전 보고서: [원본 중심 구성](../reports/20261031-original-flow.md).

## 세션 배정

| 세션 ID | 역할 | 상태 | 쓰기 범위 | 완료 조건 | 인계 |
|---|---|---|---|---|---|
| 20261104-codex-team-design | 역할 분담과 예상 문항 프롬프트 | HANDOFF | 통합 docs, prompts/mock_exam_5.md, foruser, README, AGENTS.override, templates/SESSION_CURRENT.md, .agents/skills/probe-explain | 테스트 21개, 스킬 검증, 원본 125개 보존, 설치/7세션 기록 보존 확인 | [인계](sessions/20261104-codex-team-design/HANDOFF.md) |
| 20261031-0230-codex-harness | 통합과 하네스 보완 | HANDOFF | 통합 docs, templates, .agents/skills, scripts/install.py, tests/test_tools.py, README, AGENTS.override, NOTICE | 테스트 14개, 스킬 형식 6개, 원본 125개 해시 확인 완료 | [세션 인계](sessions/20261031-0230-codex-harness.md) |
| 20261031-0303-codex-pipeline | 실전 실행 매뉴얼과 점검 | HANDOFF | RUNBOOK, REHEARSAL, 새 점검 스크립트, 관련 안내와 테스트 | 21개 테스트와 합성 전체 실행 통과, 원본 최신 확인 | [세션 인계](sessions/20261031-0303-codex-pipeline.md) |
| 20261031-0341-codex-originalflow | 원본 중심 안내와 세션 경로 정리 | HANDOFF | foruser, 통합 지침과 안내, 공유 양식, preflight와 subagent 안내 | 원본 125개와 루트 지침 동일, 테스트 21개, 세션 파일 분리 및 재설치 보존 확인 | [세션 인계](sessions/20261031-0341-codex-originalflow/HANDOFF.md) |

다른 세션은 아직 배정하지 않았다. 사용자가 다음 통합 담당 세션을 지정하면 이 인계를 읽고 자신의 ID와 작업 범위를 등록한다.
상태는 수동 기록이며 실제 세션 실행을 자동 감지하지 않는다.

## 결정

- 기본 7개 운영은 TEAM_PLAYBOOK을 따른다. S6 독립 검증과 S7 기록을 분리하고, S5는 구체적인 조사 필요가 있을 때 활성화한다. 공통 원장은 S1이 관리한다.
- 제출 전 약 20분에는 현재 코드와 가상 few-shot으로 예상 5문항을 만든다. 문서/코드 근거로 사용자 답변을 검토하며 실제 출제나 세션 성능을 보장하지 않는다.
- 질문은 열린 업무 질문에서 사례와 구체적 조건으로 좁힌다.
- 결정 기록은 기존 7개 열을 유지하고 이유에 업무 영향과 적용 조건, 한계에 재검토 조건을 포함한다.
- 공유 원장은 통합 담당자 한 명이 관리하고 각 세션은 개별 문서에 제안과 결과를 기록한다.
- 실제 과제의 공유 위치는 루트 docs다. 기존 .probe-kit/runtime 원장은 호환성을 위해 유지한다.
- 원본 AGENTS.md와 SUB_AGENTS.md는 줄이거나 재구성하지 않는다. foruser.md가 실행 순서의 주 안내다. 중복 RUNBOOK과 prompts 안내는 통합했다.
- S1~S7 역할을 기본으로 준비한다. 필요 없는 역할은 대기하며 설치기는 세션별 명세, 결과, 인계와 PLANNED 배정표를 생성한다.
- 04:01 KST 재확인: upstream README의 유형은 9개이며 스킬과 질문 은행은 4개 묶음이다. foruser와 docs/scenarios에 연결을 정정했다. 출제 확률 등급은 작성자 예상이다.
- 사용자 세션명 S1-main, S2-worker-a, S3-worker-b를 foruser의 예시에 적용했다. 앞부분에 본시험 8단계와 보조 스킬 6개의 호출 시점, 입력 예시 및 결과 확인을 추가했다. 스킬을 실제 실행한 결과는 아니다.

## 다음 행동

1. 새 세션은 이 인계와 관련 보고서를 읽고 맡을 작업과 파일 범위를 등록한다.
2. 실전에서는 foruser.md의 설치와 시작 요청을 사용하고 실제 시각으로 시간표를 확정한다.
3. 실제 과제에서 메인과 필요한 작업 세션의 파일 범위를 배정한다. 로컬 파일 분리와 재설치 보존은 PASS이며 실제 Probe 연결과 AI 세션 운영은 NOT_RUN이다.
