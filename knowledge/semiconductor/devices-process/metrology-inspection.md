# 계측·검사·CD·오버레이

ID: `P12` · 단계 2 · 출처 확인: 2026-10-30

계측은 치수·두께·정렬 같은 양을 측정하고 검사는 결함 후보를 찾는다. 둘 다 측정 조건이 해석의 일부다.

## 원리·공정 역할

CD는 특정 구조의 중요한 치수이고 overlay는 서로 다른 층 패턴의 정렬 관계다. 광학 계측 타깃·전자빔 검사·설계 비교 등은 서로 다른 정보를 제공한다. 관찰된 결함 후보와 실제 기능 불량을 구분한다.

## 지표·공식과 적용 조건

CD 오차=측정값−목표값. overlay는 x/y 성분·기준층·좌표계를 기록한다. 벡터 크기 sqrt(dx²+dy²)는 성분별 규격과 다른 판정이다. 샘플 위치·측정 불확도·반복성을 확인한다.

## 직접 만든 적용 예제

목표 CD=30 nm, 실측=32 nm이면 오차 +2 nm다. dx=3 nm, dy=4 nm이면 벡터 크기는 5 nm다. 합격 여부에는 실제 규격이 더 필요하다.

## 혼동·적용 한계

측정 타깃이 실제 소자 전 영역을 대표한다고 보장하지 않는다. 검출 한계 미만·미측정·0을 구분한다. 검사 알고리즘/recipe 변경으로 결함 수가 달라질 수 있다.

## 과제에서 확인할 질문

- 동일 장비·recipe·좌표·검출 기준으로 비교했는가?
- wafer/site별 샘플 수와 결측 의미는 무엇인가?

## 출처

- [S27: NIST — Critical Dimension and Overlay Metrology](https://www.nist.gov/publications/critical-dimension-and-overlay-metrology)
- [S28: ASML — Measuring accuracy](https://www.asml.com/en/technology/lithography-principles/measuring-accuracy)

원리는 출처를 자체 요약했다. 예제·확인 질문·분석 절차는 교육용 작성이며 실제 출제 문제·SK하이닉스 내부 레시피·제품 보증값이 아니다.
