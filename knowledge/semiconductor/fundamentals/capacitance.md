# 커패시터·정전용량

ID: `F03` · 단계 1 · 출처 확인: 2026-10-30

커패시터는 분리된 도체 사이에 전하와 에너지를 저장하며 정전용량은 전압당 저장 전하량이다.

## 원리

양쪽 도체에는 반대 부호의 전하가 쌓이고 사이에 유전체를 둘 수 있다. 용량은 형상과 재료에 의존한다. 이상적인 선형 커패시터의 C는 일정하다고 근사한다.

## 공식·단위와 적용 조건

전하 크기 Q = CV, 1 F = 1 C/V. 평행판 근사는 C = εA/d다. ε = κ ε0는 단위 F/m인 절대 유전율이며, κ(=εr)는 무차원 상대 유전율이다. A는 m², d는 m로 넣는다. 균일한 선형·등방성 유전체가 판 사이를 완전히 채우고, 판 간격이 판 크기보다 작아 가장자리 효과가 작을 때 사용한다. 진공에서는 κ=1이다.

## 직접 만든 예제

가상 셀의 C = 20 fF, V = 1 V이면 Q = 20 fC다. 실제 DRAM 사양을 뜻하지 않는다. 별도 가상 평행판에서 예제용 ε0≈8.85×10⁻¹² F/m, κ=4, A=1 μm²=10⁻¹² m², d=10 nm=10⁻⁸ m이면 C≈3.54 fF다. κ=4를 단위 있는 ε 대신 직접 대입하지 않는다.

## 혼동·적용 한계

전하 저장 가능성과 영구 보존은 다르다. 실제 누설·잡음·판독 조건을 알아야 보존 시간을 판단할 수 있다. 실제 3차원 셀을 평행판 공식만으로 설계하지 않는다.

## 과제에서 확인할 질문

- capacitance 단위는 F/pF/fF 중 무엇인가?
- 이상 모델인가, 누설을 포함한 측정인가?

## 출처

- [S03: OpenStax — Capacitors and Capacitance](https://openstax.org/books/university-physics-volume-2/pages/8-1-capacitors-and-capacitance)

- [S84: OpenStax — Capacitor with a Dielectric](https://openstax.org/books/university-physics-volume-2/pages/8-4-capacitor-with-a-dielectric)

출처의 원리를 자체 요약했다. 예제와 과제 질문은 이 패키지의 교육용 작성이며 실제 출제 문제·제품 사양이 아니다.
