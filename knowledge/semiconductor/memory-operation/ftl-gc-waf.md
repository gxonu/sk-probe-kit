# FTL·GC·TRIM·쓰기 증폭

ID: `M12` · 단계 3 · 출처 확인: 2026-10-30

관리기는 논리 주소를 물리 위치에 연결하며 내부 이동 때문에 호스트 쓰기와 NAND 쓰기가 달라진다.

## 원리·동작

FTL은 논리/물리 주소를 관리한다. GC는 필요한 데이터를 옮기고 블록을 재사용할 수 있게 정리한다. wear leveling은 마모 편중을 완화하고 예약 공간은 관리 여유를 제공한다. TRIM은 불필요해진 논리 범위를 알리는 기능이다.

## 지표·공식과 적용 조건

WAF=같은 측정 구간의 NAND 물리 쓰기 bytes/호스트 논리 쓰기 bytes. 시작·끝 누적 카운터 차이를 쓰며 단위·reset·압축·캐시 지연을 확인한다. 분모가 0이면 그 구간 비율은 정의하지 않는다.

## 직접 만든 적용 예제

같은 구간 호스트 쓰기 증가 10 GB, NAND 쓰기 증가 25 GB면 WAF=2.5다. 누적 카운터 자체를 나누면 구간별 변화가 감춰질 수 있다.

## 혼동·적용 한계

TRIM은 즉시 물리 소거·보안 삭제 보장이 아니다. GC와 wear leveling은 목적이 다르며 둘 다 이동을 유발할 수 있다. WAF만으로 실제 잔여 수명이나 성능을 확정하지 않는다.

## 과제에서 확인할 질문

- 물리/논리 쓰기 카운터의 단위와 측정 구간이 같은가?
- 캐시·background GC·예약 공간·작업 부하가 같은가?

## 출처

- [S43: Micron — Choosing the right NAND](https://www.micron.com/products/storage/nand-flash/choosing-the-right-nand)
- [S44: KIOXIA — ゼロから学ぶSSD：構造、動作、耐久性のポイント](https://www.kioxia.com/content/dam/kioxia/ja-jp/business/ssd/asset/SNIA-seminar-202502.pdf)
- [S48: Kingston — KC2500 Support — What is TRIM and Garbage Collection?](https://www.kingston.com/en/support/technical/products/kc2500)
- [S49: KIOXIA — Analyzing Managed Flash Device Lifetime Reliability Part 1: The Fundamentals of TBW, WAF and NAND Flash Memory Endurance](https://americas.kioxia.com/content/dam/kioxia/en-us/business/memory/mlc-nand/asset/KIOXIA_TBW_WAF_NAND_Endurance_Technical_Brief.pdf)

원리는 공개 출처를 자체 요약했다. 예제·질문은 교육용 작성이며 실제 출제 문제·제품 보증값·권장 설정이 아니다.
