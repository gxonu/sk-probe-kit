# DRAM 채널·랭크·뱅크·행 버퍼

ID: `M02` · 단계 3 · 출처 확인: 2026-10-30

DRAM의 용량 계층과 동시에 처리할 수 있는 범위는 서로 다른 개념이다.

## 원리·동작

채널은 전송 경로, 랭크는 함께 선택되는 DRAM 소자 묶음, 뱅크는 소자 내부의 배열 단위로 이해한다. 열린 행에 접근하면 row hit, 같은 뱅크의 다른 행이면 기존 행을 닫고 새 행을 열어야 한다. bank group·subchannel 구성은 세대별이다.

## 지표·공식과 적용 조건

서로 다른 뱅크·랭크의 일부 작업을 겹칠 수 있지만 공유 버스·전력·명령 제약은 남는다. 랭크 수를 채널 수로 대입해 대역폭을 곱하지 않는다.

## 직접 만든 적용 예제

가상 ECC 없는 구성에서 x8 칩 8개가 함께 데이터 버스를 만들면 폭은 64 bit다. 같은 채널에 두 번째 랭크를 더해도 버스 폭이 128 bit로 바뀌지는 않는다.

## 혼동·적용 한계

뱅크 번호·행 주소를 데이터셋 ID만 보고 추측하지 않는다. 컨트롤러 주소 매핑과 DDR 세대를 확인한다. DIMM 한 개가 항상 채널 한 개라는 규칙도 없다.

## 과제에서 확인할 질문

- 주소 매핑과 row hit/miss 정의가 있는가?
- 채널·랭크·뱅크·칩 개수를 중복 집계했는가?

## 출처

- [S36: Carnegie Mellon University / Liu et al. — RAIDR: Retention-Aware Intelligent DRAM Refresh](https://users.ece.cmu.edu/~omutlu/pub/raidr-dram-refresh_isca12.pdf)
- [S38: Micron — FAQs](https://www.micron.com/sales-support/sales/faqs)

원리는 공개 출처를 자체 요약했다. 예제·질문은 교육용 작성이며 실제 출제 문제·제품 보증값·권장 설정이 아니다.
