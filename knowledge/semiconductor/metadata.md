# 검색 메타데이터 계약 v1

`index.jsonl`은 UTF-8, 빈 줄 없이 한 줄당 JSON 객체 하나다. ID는 단계가 늘어나도 재사용하지 않는다.
본문은 `path`에만 유지하고, 색인에는 짧은 요약·검색어·관계만 둔다.

| 필드 | 형식·의미 |
| --- | --- |
| schema_version | 정수, 현재 1 |
| id | 유일한 개념 ID |
| stage | 정수 1–5, 수집 단계 |
| status | `ready`: 본문 제공. 과제 적용·시험 검증 완료를 뜻하지 않음 |
| title / summary | 한국어 제목·짧은 설명 |
| aliases / keywords | 문자열 배열, 한국어·영어 표현·검색 태그 |
| prerequisites / related | 존재하는 개념 ID 배열. 선수 관계는 순환하지 않음 |
| path | 이 폴더 기준 Markdown 경로 |
| source_ids | `sources.json`에서 찾을 출처 ID 배열 |
| checked_at | YYYY-MM-DD, 실제 출처 확인일 |
| evidence | 현재 `primary-source-synthesis`: 공개 1차 자료를 자체 종합 |
| scope | `general-fundamentals`: 기초 원리, `general-devices-process`: 소자·공정 원리, `general-memory-operation`: DRAM·NAND 동작, `general-packaging-reliability`: HBM·패키징·신뢰성 원리, `general-data-application`: 데이터 적용·검증 방법론 |
| problem_signals | 적용 전에 물어볼 질문 배열. 실제 출제 예측이 아님 |
| metrics | 관련 측정량과 단위의 검색용 이름. 실제 데이터 컬럼명이 아님 |

`sources.json`의 각 객체에는 `id`, `publisher`, `title`, `url`, `checked_at`,
`source_type`, `used_for`가 있다. 원문 제목·URL과 적용한 범위를 보존한다.
`primary_educational`은 원 작성 기관의 기술·교육 자료, `primary_press_release`는 원 발표 기관의 보도자료, `primary_research`는 연구자 원 논문이다. 표준 규격과 동급이라는 뜻은 아니다.
확인일과 자료 발행일은 다르다. 오래된 자료는 안정적인 정의만 사용하며 제품 현황은 가져오지 않는다.

숫자·단위가 중요한 계산은 본문의 적용 조건까지 읽는다. 색인 키워드 일치만으로 공식을 선택하지 않는다.
출처의 주장을 직접 시험한 것으로 표시하지 않으며, 실제 과제 검증은 과제 근거 문서에 별도로 남긴다.
