# 공정 흐름·FEOL·배선·후공정

ID: `P04` · 단계 2 · 출처 확인: 2026-10-30

반도체 제조는 막 형성·패턴 정의·재료 제거·특성 조절·검사를 여러 번 조합하는 흐름이다.

## 원리·공정 역할

웨이퍼 제조 안에서도 소자를 만드는 FEOL과 배선을 만드는 BEOL을 구분한다. 접촉부 연결을 MOL로 나누기도 한다. 산업의 “후공정”은 패키징·테스트를 뜻하기도 하므로 BEOL과 혼동하지 않는다. 공정 순서·반복·재작업은 제품 route에 따른다.

## 지표·공식과 적용 조건

행의 기준을 lot/wafer/die/공정 실행(run)/측정(site)으로 명시한다. step 이름만으로 동일 실행이라고 판단하지 말고 실행 ID·시각·장비·chamber·recipe 버전을 함께 확인한다.

## 직접 만든 적용 예제

동일 웨이퍼의 ETCH 단계가 두 번 나타나도 중복 로그라고 삭제하지 않는다. 서로 다른 layer 또는 재작업일 수 있으므로 route와 실행 ID를 대조한다.

## 혼동·적용 한계

“8대 공정” 같은 교육용 분류가 실제 공정의 고정 8단계 순서는 아니다. 실제 SK 레시피·장비 조건은 이 패키지에서 추정하지 않는다.

## 과제에서 확인할 질문

- 후공정이라는 말이 배선인가 패키징인가?
- 재작업·분기·측정 시점은 어떻게 기록되는가?

## 출처

- [S18: TU Wien / L. Filipovic — Traditional Semiconductor Process Technologies](https://www.iue.tuwien.ac.at/phd/filipovic/node9.html)
- [S29: SK hynix — Semiconductor Back-End Process Episode 1: Understanding Semiconductor Testing](https://news.skhynix.com/en/semiconductor-back-end-process-episode-1-understanding-semiconductor-testing/)

- [S35: imec — Logic technology scaling options for 2nm and beyond](https://www.imec-int.com/en/articles/logic-technology-scaling-options-2nm-and-beyond)

원리는 출처를 자체 요약했다. 예제·확인 질문·분석 절차는 교육용 작성이며 실제 출제 문제·SK하이닉스 내부 레시피·제품 보증값이 아니다.
