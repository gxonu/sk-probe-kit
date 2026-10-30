# 5단계 범위와 진행 상태

확인일: 2026-10-30. 단계는 학습/수집 범위이며 출제 확률 순위가 아니다.

| 단계 | 범위 | 상태 |
| --- | --- | --- |
| 1 | 전기·반도체·단위·디지털·제품 분류 기초 | 본문·색인 제공 |
| 2 | PN 접합·MOSFET·CMOS·제조 공정·계측·검사 | 본문·색인 제공 |
| 3 | DRAM·NAND 동작·리프레시·타이밍·오류·ECC 기초 | 본문·색인 제공 |
| 4 | HBM·TSV·적층·본딩·패키징·열/전력·신뢰성 | 본문·색인 제공 |
| 5 | 수율·불량·장비 시계열 등 데이터 문제 적용·통합 검증 | 본문·색인·합성 검사 제공 |

## 1단계 읽기 지도

- [F01 전하·전류·전압](fundamentals/charge-current-voltage.md) — 선수: 없음
- [F02 저항과 옴의 법칙](fundamentals/resistance-ohm.md) — 선수: F01
- [F03 커패시터·정전용량](fundamentals/capacitance.md) — 선수: F01
- [F04 전력·에너지](fundamentals/power-energy.md) — 선수: F01, F02
- [F05 반도체·밴드·전자와 정공](fundamentals/semiconductor-bands.md) — 선수: F01
- [F06 도핑·n형·p형](fundamentals/doping-carriers.md) — 선수: F05
- [F07 비트·바이트·단위 접두어](fundamentals/bits-bytes-prefixes.md) — 선수: 없음
- [F08 디지털 논리·클록·주파수](fundamentals/digital-clock-logic.md) — 선수: F07
- [F09 웨이퍼·다이·IC·패키지](fundamentals/wafer-die-ic.md) — 선수: F05
- [F10 메모리·로직·휘발성 구분](fundamentals/memory-map.md) — 선수: F07, F09
- [F11 용량·대역폭·지연시간](fundamentals/capacity-bandwidth-latency.md) — 선수: F07, F08, F10

문제를 받은 뒤에는 전부 순서대로 읽지 말고 index.jsonl의 problem_signals와 aliases로 필요한 항목을 고른다. 검색된 정의만으로 실제 과제의 원인이나 성능을 확정하지 말고 해당 단계 본문의 적용 조건을 읽는다.

## 2단계 읽기 지도

- [P01 PN 접합·공핍층·바이어스](devices-process/pn-junction.md) — 선수: F01, F05, F06
- [P02 MOSFET·문턱전압·동작 영역](devices-process/mosfet.md) — 선수: P01, F03
- [P03 CMOS 인버터·동적 전력·누설](devices-process/cmos-power.md) — 선수: P02, F04, F08
- [P04 공정 흐름·FEOL·배선·후공정](devices-process/process-flow.md) — 선수: F09, P02
- [P05 열산화·산화막·절연](devices-process/oxidation.md) — 선수: F03, F05, P04
- [P06 증착·PVD·CVD·ALD](devices-process/deposition.md) — 선수: P04, F03
- [P07 포토리소그래피·노광·현상](devices-process/lithography.md) — 선수: P04
- [P08 식각·선택비·이방성](devices-process/etch.md) — 선수: P06, P07
- [P09 이온 주입·확산·어닐링](devices-process/implant-anneal.md) — 선수: F06, P04
- [P10 CMP·평탄화·표면 손상](devices-process/cmp.md) — 선수: P06, P08
- [P11 금속 배선·컨택·비아·다마신](devices-process/interconnect.md) — 선수: F02, P06, P08, P10
- [P12 계측·검사·CD·오버레이](devices-process/metrology-inspection.md) — 선수: P07, P08, F09
- [P13 전기적 검사·EPM·웨이퍼 테스트](devices-process/electrical-test.md) — 선수: P02, P11, P12
- [P14 세정·오염·잔사](devices-process/cleaning.md) — 선수: P04, P07

## 3단계 읽기 지도

- [M01 DRAM 셀·전하 공유·센싱·복원](memory-operation/dram-cell.md) — 선수: F03, P02
- [M02 DRAM 채널·랭크·뱅크·행 버퍼](memory-operation/dram-organization.md) — 선수: M01, F09
- [M03 DRAM 명령·tRCD·tRP·tRAS·CL](memory-operation/dram-timing.md) — 선수: M02, F08
- [M04 DRAM 리프레시·retention·tREFI·tRFC](memory-operation/dram-refresh.md) — 선수: M01, M03
- [M05 DDR 전송률·버스트·유효 대역폭](memory-operation/ddr-transfer.md) — 선수: M02, F07, F11
- [M06 NAND 셀·전하 저장·문턱전압](memory-operation/nand-cell.md) — 선수: P02, F10
- [M07 NAND 페이지·블록·물리 용량](memory-operation/nand-geometry.md) — 선수: M06, F07, F09
- [M08 NAND 읽기·프로그램·소거·상태 확인](memory-operation/nand-operations.md) — 선수: M06, M07
- [M09 SLC·MLC·TLC·QLC·상태 분포](memory-operation/nand-multilevel.md) — 선수: M06, F07
- [M10 NAND retention·read disturb·P/E 이력](memory-operation/nand-retention-disturb.md) — 선수: M08, M09
- [M11 ECC·코드워드·SECDED·보호 범위](memory-operation/ecc-codeword.md) — 선수: F08, M01, M06
- [M12 FTL·GC·TRIM·쓰기 증폭](memory-operation/ftl-gc-waf.md) — 선수: M07, M08
- [M13 메모리 오류 지표·RBER·UBER·분모](memory-operation/memory-error-metrics.md) — 선수: M11, F07

DRAM은 M01 → M02 → M03/M04/M05, NAND는 M06 → M07/M09 → M08/M10/M12 순으로 읽는다.
오류 지표를 해석할 때는 M11 → M13을 함께 읽는다. 실측 원인 분석·통계 검증은 5단계 범위다.

## 4단계 읽기 지도

- [H01 HBM 적층·용량·대역폭](packaging-reliability/hbm-architecture.md) — 선수: M02, M05, F09
- [H02 TSV·수직 연결·박막화](packaging-reliability/tsv.md) — 선수: P08, P11, H01
- [H03 2.5D·3D 패키징·인터포저·RDL](packaging-reliability/package-interposer.md) — 선수: F09, P11, H01
- [H04 마이크로범프·하이브리드 본딩·정렬](packaging-reliability/hybrid-bonding.md) — 선수: P10, P12, P14, H02
- [H05 MR-MUF·TC-NCF·언더필·몰딩](packaging-reliability/muf-ncf.md) — 선수: H04, P14
- [H06 열팽창·휨·박리·접합 피로](packaging-reliability/thermomechanical.md) — 선수: H03, H05
- [H07 접합온도·열저항·열경로](packaging-reliability/thermal-metrics.md) — 선수: F04, H05, H06
- [H08 전원망·IR drop·인덕턴스·디커플링](packaging-reliability/power-delivery.md) — 선수: F02, F03, H02
- [H09 KGD·적층 검사·조립 수율](packaging-reliability/stack-test-yield.md) — 선수: P13, H04
- [H10 EM·TDDB·BTI·열화 메커니즘](packaging-reliability/failure-mechanisms.md) — 선수: P02, P11, H06
- [H11 HTOL·HTSL·TC·습도·ESD 시험](packaging-reliability/reliability-tests.md) — 선수: H10, P13
- [H12 고장률·FIT·MTTF·무고장 신뢰한계](packaging-reliability/reliability-metrics.md) — 선수: H11, F07
- [H13 Weibull·형상모수·특성수명](packaging-reliability/weibull-life.md) — 선수: H12
- [H14 가속시험·Arrhenius·수명 외삽](packaging-reliability/accelerated-life.md) — 선수: H10, H12
- [H15 불량 분석·비파괴 검사·원인 증거](packaging-reliability/failure-analysis.md) — 선수: H02, H05, H10, P12

구조는 H01 → H02/H03 → H04/H05, 열·전력은 H06 → H07/H08 순으로 연결한다.
검사·신뢰성은 H09/H10 → H11 → H12 → H13/H14를 읽고, 원인 증거는 H15로 점검한다.
현재 세대 제품 사양·제조 레시피·수명 보증값을 제공하는 자료가 아니다.
5단계에서 실제 데이터의 집계·분할·검증 절차로 연결한다.

## 5단계 읽기 지도

- [D01 데이터 단위·식별키·결합·결측](data-application/grain-join.md) — 선수: F07, F09, P04
- [D02 수율·재검사·분모·가중 집계](data-application/yield-retest.md) — 선수: P13, D01, H09
- [D03 불량 개체·결함 수·비율 불확실성](data-application/defects-uncertainty.md) — 선수: D02, H12, M13
- [D04 SPC·관리한계·규격한계·시간 순서](data-application/spc.md) — 선수: D02, D03, P12
- [D05 공정능력·Cp/Cpk·측정 신뢰성](data-application/capability-measurement.md) — 선수: P12, D04
- [D06 원인 가설·층별 비교·교란·실험 설계](data-application/root-cause.md) — 선수: P04, H15, D01, D02
- [D07 장비 시계열·가용 시점·시간 결합](data-application/time-alignment.md) — 선수: P04, D01
- [D08 학습 분할·그룹·미래 검증·누수](data-application/split-leakage.md) — 선수: D01, D07
- [D09 희소 불량 분류·오탐·미탐·임계값](data-application/classification.md) — 선수: D03, D08
- [D10 연속값 예측·잔차·MAE/RMSE](data-application/regression.md) — 선수: F07, P12, D08
- [D11 이상 탐지·분포 변화·알람 운영](data-application/anomaly-drift.md) — 선수: D04, D07, D08
- [D12 문제 적용·기준선·근거·재현·제출](data-application/task-workflow.md) — 선수: D02, D06, D08, D09, D10, D11

[실제 과제 적용 순서](application-playbook.md)에서 필요한 경로만 고른다.
1–5단계 수집과 합성 예제 검증을 완료했으며, 실제 과제·Probe 환경 검증은 별도다.
