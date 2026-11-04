# 공개 레포에서 채택한 방법

공식 운영 안내가 우선이다. 아래는 채점 기준이 아니라 실무 진행 방법이다. 고정 커밋은 UPSTREAMS.json에 기록한다.

| 출처 | 채택 | 적용 위치 | 그대로 따르지 않은 부분 |
|---|---|---|---|
| [chichochoi/sk](https://github.com/chichochoi/sk) | 메인/서브 명세와 결과, 데이터 요약, 네 가지 과제 유형, 인계 | upstream 원문 보관, 통합 AGENTS.md와 docs/TEAM_PLAYBOOK.md | 전역 설정 교체, 승인 우회, Git 변경 전면 금지, 메인의 코드 확인 금지 |
| [xodbs1021/kty-codex-harness-template](https://github.com/xodbs1021/kty-codex-harness-template) | 반도체 개념, 적용 조건, 색인과 출처 | knowledge/semiconductor 전체 원문 | 무거운 별도 하네스 설치와 역할 전체 활성화 |
| [hamjoon2003/sk-hynix-2nd-harness](https://github.com/hamjoon2003/sk-hynix-2nd-harness) | 서술형 질문, 결정과 한계 설명, 검증 상태 | 원문 보관 및 prompts/mock_exam_5.md | 실제 출제 및 채점 빈도 단정, 제출 확정 이후 코칭 |
| [hekate-louise/codex-harness](https://github.com/hekate-louise/codex-harness) | 질문 점검과 답 기록, 요구 ID와 테스트 연결, 작은 완주 | docs/interview.md, probe-interview, REQUIREMENTS | 모든 커밋을 사람에게 넘기는 방식은 강제하지 않음 |
| [keepdev0919/hynix](https://github.com/keepdev0919/hynix) | 데이터상 불가능한 목표에서 A/B 선택지, 담당자에게 보낼 5줄 요약 | docs/interview.md, RULES.md | 플랫폼/Helper에 대한 미확인 주장 |
| [ColdTbrew/cofa-skills](https://github.com/ColdTbrew/cofa-skills) | 누수와 결측 의미 확인, 의사결정 이력, 실제 사용 조건에 맞는 검증 | docs/interview.md, probe-decisions, decision.py | 모든 과제를 학습 모델 문제로 가정하지 않음 |

질문 → 받은 답(Q-ID) → 요구(R-ID) → 선택과 이유(DECISIONS) → 구현 → 실제 테스트(EVIDENCE) → 인계(HANDOFF)가 이어지도록 구성했다. 원본이 아닌 통합 문서는 이 작업을 위해 작성했다.

## 제작진 인터뷰 반영

[인터뷰 분석](references/cofa-probe-interview-20261031.md)은 사용자 제공 자동 자막에 근거한다. 평가 철학의 설명과 이번 대회의 공식 규칙을 구분한다.

| 근거 | 보완 | 적용 위치 |
|---|---|---|
| 16:19~19:45 질문으로 업무 맥락 파악 | 열린 업무 질문에서 사례와 구체적 조건으로 좁히기 | interview.md, probe-interview |
| 23:57~26:42 이해와 설계 적합성 | 업무 영향, 적용 조건, 더 단순한 대안과 재검토 조건 | REQUIREMENTS, DECISIONS, probe-decisions |
| 23:57~26:42 인지 평가 | 설명이 막히면 코드와 작은 입력으로 확인 후 다시 설명 | prompts/mock_exam_5.md, probe-explain |
| 08:21~10:22 공유 맥락과 사용자 다중 세션 요청 | CURRENT, 세션별 인계, 출처와 실행 보고서 | docs/handoff, docs/references, docs/reports |

세션 폴더와 파일 소유권 절차는 사용자 요청을 위해 설계한 운영 방식이며 공식 평가 요구사항이 아니다.

2026-11-04 통합: 이 표의 원출처는 실행 의존성 목록이 아니다. 기본 설치에는 정규화한 활성 지침만 포함하고 반도체 지식은 선택 설치한다.
