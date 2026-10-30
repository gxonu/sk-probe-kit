# NAND 읽기·프로그램·소거·상태 확인

ID: `M08` · 단계 3 · 출처 확인: 2026-10-30

호스트 쓰기 완료와 NAND 내부 프로그램 완료는 측정 경계가 다를 수 있다.

## 원리·동작

읽기는 셀 상태를 판별해 출력하고, 프로그램은 저장 상태를 바꾸며, 소거는 블록을 다시 사용할 상태로 만든다. 제자리 임의 덮어쓰기를 RAM처럼 취급하지 않는다. 프로그램·소거 후에는 장치 규약에 따라 성공 상태를 확인한다.

## 지표·공식과 적용 조건

tR/tPROG/tBERS는 각각 내부 읽기·프로그램·소거 시간의 흔한 이름이며 기준은 데이터시트로 확인한다. 직렬 단일 페이지 읽기를 단순화하면 총 시간=내부 읽기+데이터 전송+명령 등 나머지 지연이다.

## 직접 만든 적용 예제

가상 4 KiB를 200 MB/s로 전송하면 20.48 μs다. 내부 읽기 50 μs에 명령 지연을 생략하면 70.48 μs이며 약58.12 MB/s다. cache read·병렬화가 없다는 가정이다.

## 혼동·적용 한계

Ready는 다음 상태 확인이 가능하다는 뜻일 수 있으며 성공 판정과 동일하지 않다. partial program·쓰기 순서·재프로그램 허용 횟수는 제품별이다. 소거로 같은 블록의 다른 유효 데이터를 잃지 않게 관리해야 한다.

## 과제에서 확인할 질문

- 지연 측정이 명령 제출·장치 완료·호스트 완료 중 어디까지인가?
- status fail·재시도·bad block 처리가 기록됐는가?

## 출처

- [S41: KIOXIA — What is NAND Flash Memory?](https://www.kioxia.com/en-jp/rd/technology/nand-flash.html)
- [S44: KIOXIA — ゼロから学ぶSSD：構造、動作、耐久性のポイント](https://www.kioxia.com/content/dam/kioxia/ja-jp/business/ssd/asset/SNIA-seminar-202502.pdf)
- [S38: Micron — FAQs](https://www.micron.com/sales-support/sales/faqs)

- [S51: Linux kernel documentation — NAND timing fields](https://www.kernel.org/doc/html/v4.19/driver-api/mtdnand.html)

원리는 공개 출처를 자체 요약했다. 예제·질문은 교육용 작성이며 실제 출제 문제·제품 보증값·권장 설정이 아니다.
