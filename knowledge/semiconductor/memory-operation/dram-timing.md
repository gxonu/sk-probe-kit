# DRAM 명령·tRCD·tRP·tRAS·CL

ID: `M03` · 단계 3 · 출처 확인: 2026-10-30

DRAM 지연은 명령 사이 최소 간격과 현재 열린 행 상태를 함께 봐야 한다.

## 원리·동작

ACTIVATE는 행을 열고 READ/WRITE는 열려 있는 행에 접근한다. tRCD는 ACT에서 읽기/쓰기 명령까지, tRP는 PRE에서 다음 ACT까지, tRAS는 ACT 후 행을 유지해야 하는 최소 시간이다. CL은 해당 설정에서 READ부터 첫 데이터까지의 클록 수다.

## 지표·공식과 적용 조건

시간=nCK×tCK. ns 조건을 클록으로 바꿀 때 ceil(tmin/tCK)와 별도의 최소 nCK 조건을 모두 만족시킨다. AL 등 추가 지연이 없는 단순 읽기에서 row hit는 CL, 닫힌 행은 tRCD+CL, 충돌은 남은 대기+tRP+tRCD+CL로 생각한다.

## 직접 만든 적용 예제

tCK=0.625 ns, CL=24이면 CAS 부분은 15 ns다. tRCD=tRP=15 ns이고 기존 행을 바로 닫을 수 있다면 닫힌 행 30 ns, 충돌 45 ns다. 최소 14 ns 조건은 ceil(14/0.625)=23클록으로 14.375 ns가 된다.

## 혼동·적용 한계

이 예제는 버스트 완료·큐잉·버스 경합·refresh를 제외한 첫 데이터 근사다. PRE 허용 시점에는 tRAS, 읽기/쓰기 관련 제약도 적용된다. 실제 설정은 부품 규격을 따른다.

## 과제에서 확인할 질문

- 지연이 첫 데이터인가 전체 요청 완료인가?
- ns와 nCK 조건, 현재 행 상태·명령 이력이 있는가?

## 출처

- [S39: Microchip — DDR Memory — DDR Memory Timing](https://onlinedocs.microchip.com/oxy/GUID-AFCB5DCC-964F-4BE7-AA46-C756FA87ED7B-en-US-21/GUID-A29420D1-4E36-4920-B9BB-DD0B63F5E787.html)

원리는 공개 출처를 자체 요약했다. 예제·질문은 교육용 작성이며 실제 출제 문제·제품 보증값·권장 설정이 아니다.
