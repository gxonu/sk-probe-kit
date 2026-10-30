# ECC·코드워드·SECDED·보호 범위

ID: `M11` · 단계 3 · 출처 확인: 2026-10-30

ECC의 정정 능력은 코드워드와 보호 경로별로 정의되며 모든 오류를 고치지는 못한다.

## 원리·동작

쓰기 시 검사 비트를 만들고 읽기 시 불일치를 검사한다. SECDED는 한 코드워드의 1-bit 오류 정정·2-bit 오류 검출을 보장하는 유형이다. DDR5 on-die ECC는 칩 내부의 보호이며 외부 버스를 포함하는 시스템 ECC와 범위가 다르다. NAND의 요구 정정 강도·코드 종류는 장치별이다.

## 지표·공식과 적용 조건

가상 64 data+8 check 구성의 부가 비트/data 비율=8/64=12.5%, 전체 코드워드 중 비중=8/72≈11.11%. 정정 가능 오류 수를 페이지 전체 합계로만 비교하지 않는다.

## 직접 만든 적용 예제

서로 다른 코드워드에 1-bit 오류가 하나씩 있으면 각 SECDED가 정정할 수 있다. 같은 코드워드 안의 2-bit 오류는 검출 대상이며 정정 보장은 없다. 같은 총 오류 2개라도 배치가 중요하다.

## 혼동·적용 한계

SECDED를 3개 이상 오류의 완전 검출 보장으로 확대하지 않는다. corrected 로그는 물리 결함 수와 같지 않다. 초기화되지 않은 검사 비트·누락 로그·내부 ECC 비가시성도 확인한다. BCH/LDPC의 실제 능력은 파라미터·디코더 조건이 필요하다.

## 과제에서 확인할 질문

- 코드워드 크기·보호 경로·정정 강도는 무엇인가?
- 로그가 내부 정정 전인가 후인가, 누적·중복 집계인가?

## 출처

- [S46: Microchip — Fabric DDR Subsystem — ECC](https://onlinedocs.microchip.com/oxy/GUID-FF8061A7-7A15-470F-A6F5-E733C24D85F0-en-US-11/GUID-B6C8D87D-26CF-4615-8DDA-D79C915B85CE.html)
- [S47: Micron — DDR5 DRAM — Feature differences](https://www.micron.com/products/memory/dram-components/ddr5-sdram)
- [S38: Micron — FAQs](https://www.micron.com/sales-support/sales/faqs)

- [S50: Kingston — The Difference Between Enterprise & Client SSD](https://www.kingston.com/en/blog/pc-performance/enterprise-versus-client-ssd)

원리는 공개 출처를 자체 요약했다. 예제·질문은 교육용 작성이며 실제 출제 문제·제품 보증값·권장 설정이 아니다.
