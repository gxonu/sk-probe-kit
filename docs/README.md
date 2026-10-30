# 문서 시작점

공식 규칙은 [RULES.md](RULES.md), 현재 작업과 세션 배정은 [handoff/CURRENT.md](handoff/CURRENT.md)에서 확인한다.

| 폴더 | 목적 | 먼저 읽을 문서 |
|---|---|---|
| handoff | 현재 상태, 세션별 작업 범위, 인수인계와 요청 | [공유 절차](handoff/README.md) |
| references | 출처, 시간 위치, 확인 범위와 해석 | [출처 목록](references/README.md) |
| reports | 수행한 작업과 검증 결과 | [보고서 목록](reports/README.md) |

새 세션은 전체 문서를 읽지 않는다. CURRENT → 배정받은 세션 문서 → 관련 보고서와 출처 순으로 필요한 범위만 읽는다.
채팅은 자동 공유되지 않는다. 파일 작성 후 다른 세션에 경로를 알려주고, 수신 세션이 파일을 읽어야 내용이 전달된다.

## 작업 가이드

- [질문](interview.md): 현재 업무와 사례를 이해하고 구체적인 조건을 확인한다.
- [요청 프롬프트](prompts.md): 메인, 작업 세션, 인계와 검증 요청.
- [설명 연습](written-prep.md): 제출물 확정 전에 코드와 실제 결과의 이해를 점검한다.
- [공개 레포 채택 내역](ADOPTED_PRACTICES.md), [도구 조사](TOOL_SURVEY.md).
- [Cofa Probe 제작진 인터뷰 분석](references/cofa-probe-interview-20261031.md).

## 설치한 과제에서의 위치

과제 루트의 `docs/handoff`, `docs/references`, `docs/reports`가 세션 간 공유 위치다.
`.probe-kit/docs`는 설치된 사용 안내와 참고 문서다. 그 안의 CURRENT는 과제 루트의 현재 상태로 연결한다. 하네스 개발 세션과 검증 보고서는 설치하지 않는다.
합의된 요구, 결정, 검증의 공통 원장은 `.probe-kit/runtime`에 유지한다. 경로와 작성자는 과제의 `docs/handoff/CURRENT.md`에 기록한다.
