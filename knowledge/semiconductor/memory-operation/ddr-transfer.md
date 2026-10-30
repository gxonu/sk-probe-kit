# DDR 전송률·버스트·유효 대역폭

ID: `M05` · 단계 3 · 출처 확인: 2026-10-30

MT/s는 데이터 전송률이고 MHz는 클록 주파수이며 둘을 중복 곱하지 않는다.

## 원리·동작

일반 DDR 데이터 버스는 클록 양쪽 에지로 전송한다. 버스트는 연속 전송 횟수다. 내부 prefetch·코어 동작과 외부 버스 클록을 동일시하지 않는다.

## 지표·공식과 적용 조건

피크 payload 대역폭=전송률(T/s)×데이터 폭(bit)/8. MT/s에 DDR의 2를 다시 곱하지 않는다. 버스트 payload=BL×데이터 폭/8이며 ECC 전용 비트는 payload에서 제외한다.

## 직접 만든 적용 예제

가상 3200 MT/s·64 bit 경로는 25.6 GB/s다. BL8의 payload는 64 B이며 연속 데이터 구간은 8/(3.2×10⁹)=2.5 ns다. 실측 16 GB/s면 피크 대비 62.5%다.

## 혼동·적용 한계

버스트 전송 시간은 셀 접근·CAS 지연을 포함한 요청 지연이 아니다. 랭크 수를 독립 채널 수로 곱하거나 DDR5 subchannel과 전체 폭을 중복 계산하지 않는다.

## 과제에서 확인할 질문

- 폭이 칩·subchannel·전체 채널 중 어느 기준인가?
- 측정 대역폭에 읽기/쓰기·대기·ECC 비트가 어떻게 포함됐는가?

## 출처

- [S40: Kingston — Desktop/Notebook Memory — DRAM frequency FAQ](https://www.kingston.com/en/support/technical/products/desktop-notebook-memory)
- [S47: Micron — DDR5 DRAM — Feature differences](https://www.micron.com/products/memory/dram-components/ddr5-sdram)

- [S39: Microchip — DDR Memory — DDR Memory Timing](https://onlinedocs.microchip.com/oxy/GUID-AFCB5DCC-964F-4BE7-AA46-C756FA87ED7B-en-US-21/GUID-A29420D1-4E36-4920-B9BB-DD0B63F5E787.html)

원리는 공개 출처를 자체 요약했다. 예제·질문은 교육용 작성이며 실제 출제 문제·제품 보증값·권장 설정이 아니다.
