# 현재 하네스 개발 상태

이 문서는 준비용 sk-probe-kit 저장소의 개발 상태다. 설치한 과제에는 미시작 상태의 별도 CURRENT가 생성된다.

- 목표: chichochoi 원본 흐름을 중심으로 보조 지식과 유연한 다중 세션 공유를 결합.
- 공식 기준: [RULES](../RULES.md). 사용자 요청으로 준비용 저장소를 보완하는 단계다.
- 통합 담당: 20261031-0341-codex-originalflow
- 갱신: 2026-10-31 03:41 KST
- 기준 커밋: 7edb2e3745b3a63a7850b2b1e767067288cdc2eb, main
- 작업 상태: HANDOFF, 구현과 로컬 검증 완료. 변경 커밋은 이 파일의 Git 이력에서 확인한다.
- 작업 폴더: 이 문서가 속한 저장소 루트. 같은 이름의 이전 초안을 사용하지 않는다.
- 관련 출처: [인터뷰 분석](../references/cofa-probe-interview-20261031.md)
- 실전 시작점: [foruser.md](../../foruser.md)
- 현재 보고서: [원본 중심 구성과 다중 세션 확인](../reports/20261031-original-flow.md)

## 세션 배정

| 세션 ID | 역할 | 상태 | 쓰기 범위 | 완료 조건 | 인계 |
|---|---|---|---|---|---|
| 20261031-0230-codex-harness | 통합과 하네스 보완 | HANDOFF | 통합 docs, templates, .agents/skills, scripts/install.py, tests/test_tools.py, README, AGENTS.override, NOTICE | 테스트 14개, 스킬 형식 6개, 원본 125개 해시 확인 완료 | [세션 인계](sessions/20261031-0230-codex-harness.md) |
| 20261031-0303-codex-pipeline | 실전 실행 매뉴얼과 점검 | HANDOFF | RUNBOOK, REHEARSAL, 새 점검 스크립트, 관련 안내와 테스트 | 21개 테스트와 합성 전체 실행 통과, 원본 최신 확인 | [세션 인계](sessions/20261031-0303-codex-pipeline.md) |
| 20261031-0341-codex-originalflow | 원본 중심 안내와 세션 경로 정리 | HANDOFF | foruser, 통합 지침과 안내, 공유 양식, preflight와 subagent 안내 | 원본 125개와 루트 지침 동일, 테스트 21개, 세션 파일 분리 및 재설치 보존 확인 | [세션 인계](sessions/20261031-0341-codex-originalflow/HANDOFF.md) |

다른 세션은 아직 배정하지 않았다. 사용자가 다음 통합 담당 세션을 지정하면 이 인계를 읽고 자신의 ID와 작업 범위를 등록한다.
상태는 수동 기록이며 실제 세션 실행을 자동 감지하지 않는다.

## 결정

- 질문은 열린 업무 질문에서 사례와 구체적 조건으로 좁힌다.
- 결정 기록은 기존 7개 열을 유지하고 이유에 업무 영향과 적용 조건, 한계에 재검토 조건을 포함한다.
- 공유 원장은 통합 담당자 한 명이 관리하고 각 세션은 개별 문서에 제안과 결과를 기록한다.
- 실제 과제의 공유 위치는 루트 docs다. 기존 .probe-kit/runtime 원장은 호환성을 위해 유지한다.
- 원본 AGENTS.md와 SUB_AGENTS.md는 줄이거나 재구성하지 않는다. foruser.md가 주 안내이며 RUNBOOK은 보조 요약이다.
- 메인 + worker-a + worker-b는 예시다. 작업자는 역할과 수를 조정하고 명세, 결과, 인계 파일을 세션별 폴더로 나눈다.

## 다음 행동

1. 새 세션은 이 인계와 관련 보고서를 읽고 맡을 작업과 파일 범위를 등록한다.
2. 실전에서는 foruser.md의 설치와 시작 요청을 사용하고 실제 시각으로 시간표를 확정한다.
3. 실제 과제에서 메인과 필요한 작업 세션의 파일 범위를 배정한다. 로컬 파일 분리와 재설치 보존은 PASS이며 실제 Probe 연결과 AI 세션 운영은 NOT_RUN이다.
