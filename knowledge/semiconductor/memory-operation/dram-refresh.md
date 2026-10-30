# DRAM 리프레시·retention·tREFI·tRFC

ID: `M04` · 단계 3 · 출처 확인: 2026-10-30

셀 전하의 유지 시간과 리프레시 명령 간격·점유 시간은 구분해야 한다.

## 원리·동작

리프레시는 누설로 잃는 저장 상태를 주기적으로 복원한다. tREFI는 평균 명령 간격, tRFC는 리프레시 동작에 필요한 시간이다. 외부 명령 기반 refresh와 장치 내부가 유지하는 self-refresh를 구분한다.

## 지표·공식과 적용 조건

같은 자원을 매번 tRFC 동안 막는 단순 주기 모델의 점유율≈tRFC/tREFI. 전체 행을 갱신하는 기간과 한 명령의 간격은 같지 않다. 실제 세대·모드·온도에 따른 규격을 확인한다.

## 직접 만든 적용 예제

가상 tRFC=300 ns, tREFI=7.5 μs이면 300/7500=4%다. 이 값이 앱 실행시간 4% 증가를 바로 뜻하지는 않는다.

## 혼동·적용 한계

all-bank와 per/same-bank refresh는 겹쳐 처리할 수 있는 범위가 다르다. 오래된 문헌의 갱신 주기를 모든 제품에 고정하지 않는다. 평균 retention만으로 가장 약한 셀을 보호할 수 없다.

## 과제에서 확인할 질문

- 온도·리프레시 모드·대상 자원이 같은가?
- retention 시간과 refresh 명령 간격을 혼동했는가?

## 출처

- [S36: Carnegie Mellon University / Liu et al. — RAIDR: Retention-Aware Intelligent DRAM Refresh](https://users.ece.cmu.edu/~omutlu/pub/raidr-dram-refresh_isca12.pdf)
- [S39: Microchip — DDR Memory — DDR Memory Timing](https://onlinedocs.microchip.com/oxy/GUID-AFCB5DCC-964F-4BE7-AA46-C756FA87ED7B-en-US-21/GUID-A29420D1-4E36-4920-B9BB-DD0B63F5E787.html)

원리는 공개 출처를 자체 요약했다. 예제·질문은 교육용 작성이며 실제 출제 문제·제품 보증값·권장 설정이 아니다.
