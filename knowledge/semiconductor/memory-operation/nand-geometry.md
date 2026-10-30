# NAND 페이지·블록·물리 용량

ID: `M07` · 단계 3 · 출처 확인: 2026-10-30

페이지와 블록은 동작 단위이며 호스트의 논리 블록과 같은 단어라도 크기·의미가 다르다.

## 원리·동작

기본적으로 읽기·프로그램은 페이지, 소거는 여러 페이지로 구성된 블록 단위다. 부분 접근 지원·페이지 크기·블록당 페이지 수·plane 병렬 조건은 부품별이다. raw NAND와 관리형 장치의 호스트 주소 공간을 구분한다.

## 지표·공식과 적용 조건

주 데이터 용량=페이지당 main bytes×블록당 페이지 수×사용 대상 블록 수. spare/OOB·불량 블록·예약 영역·호스트 노출 용량은 별도로 확인한다. TLC page 개수가 이미 반영된 geometry에 3을 다시 곱하지 않는다.

## 직접 만든 적용 예제

가상 4 KiB/page×128 page/block=512 KiB/block. 전체 1024개 중 계산 대상이 1000블록이면 주 데이터 합계는 500 MiB다. 이것만으로 SSD 표시 용량을 정하지 않는다.

## 혼동·적용 한계

page와 OS page, NAND block과 LBA를 혼동하지 않는다. die·LUN·plane이 제품마다 1:1 대응한다고 단정하지 않는다. 채널 수는 용량에 이미 포함된 die를 다시 곱하는 인수가 아니다.

## 과제에서 확인할 질문

- geometry의 page bytes가 main만인가 spare 포함인가?
- 블록 수가 전체·정상·예약 제외 중 무엇인가?

## 출처

- [S44: KIOXIA — ゼロから学ぶSSD：構造、動作、耐久性のポイント](https://www.kioxia.com/content/dam/kioxia/ja-jp/business/ssd/asset/SNIA-seminar-202502.pdf)
- [S43: Micron — Choosing the right NAND](https://www.micron.com/products/storage/nand-flash/choosing-the-right-nand)

원리는 공개 출처를 자체 요약했다. 예제·질문은 교육용 작성이며 실제 출제 문제·제품 보증값·권장 설정이 아니다.
