# 공식 안내 우선 통합 지침

공식 운영 규정, 실제 과제 README, 사용자의 합의문이 이 하네스보다 우선한다.
과제에 설치된 상태라면 `.probe-kit/docs/RULES.md`를, 이 저장소 자체를 검토한다면 `docs/RULES.md`를 먼저 읽는다.
실제 과제의 실행 순서는 설치된 `.probe-kit/docs/RUNBOOK.md`를 따른다. 저장소 검토에서는 `docs/RUNBOOK.md`를 읽는다.
다중 세션 작업은 프로젝트 루트의 `docs/handoff/README.md`와 `docs/handoff/CURRENT.md`를 읽고 자신의 배정 범위를 확인한다. 같은 폴더 안의 파일로 공유하며 대화가 자동 전달된다고 가정하지 않는다.
원본 AGENTS.md, SUB_AGENTS.md, foruser.md, prompts 및 skills는 메인/서브 분업과 작업 흐름의 참고 자료다.
원본 전체를 보존했지만 다음 충돌에서는 반드시 이 지침을 따른다.

- 최초 요구와 계획은 사용자 합의 후 구현한다. 담당자 질문은 초안을 만들고 응시자가 전송하며 답변을 파일에 기록한다.
- 메인은 요구, 설계, 작업 명세와 결과 검토를 담당한다. 중요한 코드와 실행 결과를 직접 확인한다. 서브 사용이 어려우면 메인이 구현할 수 있다.
- 로컬 git add/commit을 전면 금지하지 않는다. 검토한 파일을 단계별로 기록하며 Git Push는 금지다. git reset/clean으로 자료를 지우지 않는다.
- 모델 ID와 xhigh를 강제하지 않는다. /model에서 실제 제공된 허용 모델을 선택하고 Astra는 사용하지 않는다.
- 전역 Codex 설정이나 인증, 승인, 샌드박스, 감독 설정을 변경하지 않는다. upstream의 원본 init.sh 및 subagent.sh를 실행하지 않는다.
- Computer Use 및 브라우저 자동 조작을 사용하지 않는다. 웹 UI는 응시자가 내장 Browser에서 직접 확인한다.
- 제출물 확정 이후에는 AI로 후속 질문이나 답변을 준비하지 않는다. 설명 연습은 확정 전에 마친다.
- 채점 가산점, 토큰 절감률, 출제 확률, 어떤 테스트가 반드시 출제된다는 원본의 주장은 검증된 사실로 쓰지 않는다.
- 실제 시작 시각과 전체 마감으로 plan_time.py를 실행해 기능 동결, 제출 시작과 확정 한계를 CURRENT에 기록한다. 온전한 180분이 있을 때 첫 완주 40분, 기능 동결 140분, 제출 시작 170분을 기본으로 하며 실제 시간이 짧으면 함께 줄인다.
- 숫자와 판정은 코드로, 완료는 실제 증거로 확인한다. DECISIONS와 HANDOFF에 결정 및 다음 작업을 남긴다.
- 공통 요구와 결정은 통합 담당자 한 명이 관리한다. 각 세션은 `docs/handoff/sessions/<session-id>.md`와 자기 보고서에 결과를 남긴다. 여러 세션이 TASK_SPEC, SUB_RESULT, HANDOFF 한 파일을 함께 수정하지 않는다.
- 질문은 업무 맥락에서 구체적인 조건으로 좁힌다. 결정에는 업무 영향, 적용 조건과 재검토 조건을 적는다. 설명이 막히면 코드와 작은 입력으로 이해를 확인한다.

반도체 자료는 `.probe-kit/knowledge/semiconductor/index.jsonl`에서 검색하고 필요한 문서만 읽는다.
서술형 원문은 `references/written-prep.original.md`, 공식 규칙에 맞춘 연습용은 `docs/written-prep.md`에 있다.
