# chichochoi/sk 최신 변경 확인

- 확인 시각: 2026-10-31 03:03 KST
- 상태: PRIMARY_CHECKED, GitHub API의 main 및 커밋 비교 결과 확인.
- 저장소: [chichochoi/sk](https://github.com/chichochoi/sk)
- 기준 커밋: a08f364c09ad7074ec6117ffb840290a85419dc8
- 확인된 main: a08f364c09ad7074ec6117ffb840290a85419dc8
- 커밋 시각: 2026-10-30 14:56:24 UTC, 23:56:24 KST.
- 비교: identical, ahead_by 0, behind_by 0, total_commits 0, 변경 파일 0개.
- 결론: 이전에 가져온 원본 이후의 추가 업데이트는 없다. 확인 이후의 변경까지 보장하지 않는다.

근거: [main 브랜치 API](https://api.github.com/repos/chichochoi/sk/branches/main),
[확인된 커밋](https://github.com/chichochoi/sk/commit/a08f364c09ad7074ec6117ffb840290a85419dc8),
[기준 대비 main 비교](https://api.github.com/repos/chichochoi/sk/compare/a08f364c09ad7074ec6117ffb840290a85419dc8...main).

## 최신 커밋에서 설명하는 수정

커밋 메시지는 전역 Codex 경로 설치의 실패 처리, Git 저장소가 아닌 폴더와 .probe-kit 배치 대응,
python3 사용 통일, 붙여넣기 안내, AGENTS 먼저 읽기, Git 없는 환경의 감사 처리 보완을 설명한다.
이 버전의 원본은 이미 upstream/chichochoi에 보존되어 있다.

## 이번 통합본의 적용

원본 foruser.md의 장점인 단계별 실행, 요청 문구, 완료 조건을 docs/RUNBOOK.md에 반영한다.
고정 시각은 실제 시작과 전체 마감에서 계산한다. 여러 작업자는 개별 명세와 결과 파일을 쓴다.
전역 설정 설치, 승인 우회, 메인의 코드 확인 금지, 고정 모델 및 추론 수준, 보장되지 않은 가점과 토큰 절감률은 채택하지 않는다.
원본의 숨은 조건 비율과 모든 환경에서의 작동 보장도 검증된 사실로 사용하지 않는다.
이 판단은 공식 규칙과 사용자의 통합 운영 방식에 따른 것이다.

원본 전체는 해시를 유지한다. 사용자 진입점인 foruser.md는 새 실전 매뉴얼로 연결하고 원본은 upstream/chichochoi/foruser.md에 보존한다.

## 04:01 KST 재확인: 유형 9개, 스킬 4개

main은 여전히 a08f364c09ad7074ec6117ffb840290a85419dc8이다. GitHub API와 이 커밋의 README를 다시 확인했다.
README 493행 이후에 Case 1~9가 있고, 1과 5는 case1, 2는 case2, 3은 case3, 4와 6~8은 case4 스킬을 명시한다.
Case 9는 복합형 설명이며 별도 case9 파일은 없다. 구성 작업의 스킬을 함께 적용한다.

기존에 보존한 원본에도 9개 유형이 있었다. 이번에 새 유형을 내려받은 것이 아니다.
원본 foruser와 질문 은행의 4개 묶음 표기를 통합 안내에 그대로 옮기면서 유형 수와 혼동한 부분을 정정했다.
현재 주 안내는 foruser.md이며 docs/RUNBOOK.md는 보조 요약이다. 위의 이전 적용 설명은 당시 이력이다.
실행 안내와 docs/scenarios.md에서 9개 유형, 4개 스킬, 질문 묶음의 관계를 명시했다.
작성자의 확률 등급은 DOCUMENT_REPORTED이며 공식 확률로 검증한 것이 아니다.
'처음에는 4개였다'는 과거 변경 이력은 이번 확인 범위에 포함하지 않았다.
