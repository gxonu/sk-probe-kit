# SLC·MLC·TLC·QLC·상태 분포

ID: `M09` · 단계 3 · 출처 확인: 2026-10-30

셀당 bit 수가 증가하면 구분해야 하는 저장 상태 수는 지수적으로 늘어난다.

## 원리·동작

SLC/2-bit MLC/TLC/QLC는 각각 1/2/3/4 bit per cell이며 2/4/8/16개 상태를 구분한다. MLC는 문맥에 따라 다중 레벨의 총칭 또는 2-bit 제품을 뜻한다. 분포의 겹침과 읽기 기준이 오류에 영향을 준다.

## 지표·공식과 적용 조건

b bit를 표현하는 상태 수=2^b. 완전히 정렬된 L개 상태를 모두 구분하는 경계는 L−1개다. 이것은 한 논리 페이지 읽기의 실제 비교·재시도 횟수와 같다는 뜻이 아니다.

## 직접 만든 적용 예제

TLC는 8상태·7경계, QLC는 16상태·15경계다. 가상 동일 셀 수 100만 개의 raw bit 합은 각각 300만·400만 bit로 비율은 4/3이다. 예약·ECC와 실제 die 크기는 제외한 비교다.

## 혼동·적용 한계

동일 전압 창에서 상태 수가 늘면 분리 여유 관리가 어려워지지만 간격이 항상 균등하지는 않다. bit/cell만으로 특정 제품의 속도·보증 수명을 확정하지 않는다.

## 과제에서 확인할 질문

- MLC가 총칭인가 2-bit 셀인가?
- raw 셀 용량과 호스트 용량·실제 읽기 횟수를 구분했는가?

## 출처

- [S42: KIOXIA — What is Multi-level Cell Technology Realizing Larger Capacity Flash Memory?](https://www.kioxia.com/en-jp/rd/technology/multi-level-cell.html)
- [S43: Micron — Choosing the right NAND](https://www.micron.com/products/storage/nand-flash/choosing-the-right-nand)

원리는 공개 출처를 자체 요약했다. 예제·질문은 교육용 작성이며 실제 출제 문제·제품 보증값·권장 설정이 아니다.
