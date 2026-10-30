# 가속시험·Arrhenius·수명 외삽

ID: `H14` · 단계 4 · 출처 확인: 2026-10-30

가속시험의 시간 환산은 고장 메커니즘과 모형이 사용 조건까지 유지된다는 가정에 의존한다.

## 원리·구조와 메커니즘

온도에 열적으로 활성화되는 동일 메커니즘의 Arrhenius 모형을 적용할 수 있다. 활성화에너지 Ea는 물질 이름만으로 정하지 않고 해당 메커니즘·자료로 확인한다.

## 지표·공식과 적용 조건

AF=t_use/t_stress=exp[(Ea/k)(1/T_use−1/T_stress)]. T는 K=°C+273.15, k=8.617333262×10⁻⁵ eV/K, Ea는 eV다. 이 모형은 전압·습도·열사이클 변형을 자동 반영하지 않는다.

## 직접 만든 적용 예제

가정 Ea=0.7 eV, 사용55°C·시험125°C이면 AF≈77.65. 시험100 h는 이 모형에서 약7765 h에 대응한다. 개인 소자의 보증 수명이나 새로운 측정 결과가 아니다.

## 혼동·적용 한계

고온에서 다른 메커니즘이 지배하면 외삽이 무너질 수 있다. 열사이클 피로는 ΔT·ramp·dwell 등 별도 모형이 필요하다. 여러 스트레스의 AF를 근거 없이 곱하지 않는다.

## 과제에서 확인할 질문

- 동일 메커니즘·활성화에너지·온도 범위를 뒷받침하는 자료가 있는가?
- 환산 시간이 실제 관측과 구분되고 모수 불확실성이 기록됐는가?

## 출처

- [S64: NIST/SEMATECH — Arrhenius](https://www.itl.nist.gov/div898/handbook/apr/section1/apr151.htm)
- [S67: NIST/SEMATECH — How do you choose an appropriate physical acceleration model?](https://www.itl.nist.gov/div898/handbook/apr/section2/apr24.htm)

원리는 공개 출처를 자체 요약했다. 예제·질문은 교육용 작성이며 실제 출제 문제·HBM 제품 사양·공정 레시피·수명 보증값이 아니다.
