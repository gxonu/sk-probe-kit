# 참고 자료와 출처

주장별 출처와 확인 범위를 기록한다. 인터뷰의 설계 철학, 공개 레포의 제안, 공식 운영 규칙을 구분한다.

| 출처 ID | 자료 | 확인 범위 |
|---|---|---|
| SRC-COFA-INTERVIEW-20261031 | [Cofa Probe 제작진 인터뷰 분석](cofa-probe-interview-20261031.md) | 사용자 제공 자동 자막 전체, 영상과 원 논문은 별도 미확인 |
| SRC-UPSTREAM-CHECK-20261031 | [chichochoi/sk 최신 확인](upstream-check-20261031.md) | GitHub API main과 기준 커밋 비교, 추가 커밋 0개 |

공식 규칙은 설치한 과제의 `.probe-kit/docs/RULES.md`, 하네스 저장소에서는 `docs/RULES.md`에 있다. 실제 최신 공지가 우선한다.
공개 레포 출처와 고정 커밋은 하네스의 UPSTREAMS.json과 ORIGINS.json, 반도체 자료는 knowledge/semiconductor에서 찾는다.

새 자료에는 출처 ID, 제목, 확인 날짜, 원문 위치나 URL, 페이지 또는 시간, 주장과 한계를 적는다.
확인 상태는 PRIMARY_CHECKED / USER_REPORTED / DOCUMENT_REPORTED / CONFLICT / UNKNOWN을 사용한다.
문서에 적힌 주장은 DOCUMENT_REPORTED이며 실제 실험이나 성과를 독립 검증했다는 뜻이 아니다.
우리의 해석은 '분석', 실행 제안은 '적용 제안'으로 명시한다. 원본을 읽었다는 사실과 주장이 참임을 검증했다는 사실을 구분한다.

공개 준비 자료에는 개인 링크, 인증 정보, 실제 응시 문제와 결과물을 넣지 않는다.
