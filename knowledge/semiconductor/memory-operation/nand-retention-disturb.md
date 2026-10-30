# NAND retention·read disturb·P/E 이력

ID: `M10` · 단계 3 · 출처 확인: 2026-10-30

보존 시간, 반복 읽기에 의한 교란, 프로그램·소거 마모는 서로 다른 이력이다.

## 원리·동작

retention은 마지막 기록 뒤 시간에 따른 상태 보존, read disturb는 반복 읽기의 영향, P/E 이력은 프로그램·소거 반복에 따른 마모를 뜻한다. 온도·셀 상태·관리 동작에 따라 관측 오류가 달라진다.

## 지표·공식과 적용 조건

같은 P/E 수준에서도 마지막 프로그램 시각, 보관 온도, 읽기 횟수, 재기록/refresh 유무를 함께 기록한다. lifetime model 없이 P/E 한도나 시간만으로 잔여 수명을 계산하지 않는다.

## 직접 만든 적용 예제

같은 1000 P/E 블록 A/B라도 마지막 기록 후 A=1시간, B=100시간이라면 동일 retention 조건이 아니다. B의 오류가 많다는 관측만으로 read disturb가 원인이라고 결론 내릴 수 없다.

## 혼동·적용 한계

NAND 관리기의 데이터 재배치·재기록은 DRAM 주기적 리프레시와 구현이 다르다. read-retry로 읽기 기준을 바꾸는 것과 실제 저장 상태를 다시 쓰는 것도 구분한다. 신뢰성 시험·가속 모델은 4단계에서 다룬다.

## 과제에서 확인할 질문

- data age·읽기 횟수·P/E·온도가 분리 기록됐는가?
- 관측 전에 refresh·이동·read-retry가 있었는가?

## 출처

- [S45: KIOXIA — Why Data Retention is Becoming More Critical in Automotive Applications](https://tw.kioxia.com/content/dam/kioxia/shared/business/memory/automotive/asset/KIOXIA_Automotive_NAND_Data_Retention_White_Paper.pdf)
- [S38: Micron — FAQs](https://www.micron.com/sales-support/sales/faqs)
- [S49: KIOXIA — Analyzing Managed Flash Device Lifetime Reliability Part 1: The Fundamentals of TBW, WAF and NAND Flash Memory Endurance](https://americas.kioxia.com/content/dam/kioxia/en-us/business/memory/mlc-nand/asset/KIOXIA_TBW_WAF_NAND_Endurance_Technical_Brief.pdf)

원리는 공개 출처를 자체 요약했다. 예제·질문은 교육용 작성이며 실제 출제 문제·제품 보증값·권장 설정이 아니다.
