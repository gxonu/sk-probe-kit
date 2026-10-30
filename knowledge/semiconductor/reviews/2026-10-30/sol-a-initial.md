# 독립 검토 A — 반도체 지식 65개 카드 및 적용 안내

검토 모델: gpt-6.1-sol. 대상 고정 커밋: `731eecb0acf12f2d65f045c87a6a51889ea1dbd5`.
대상: `/Users/kty/Documents/ChatGPT/sk-hynix-hackathon/tmp/semiconductor-sol-sol-review/snapshot`.
검토일: 2026-10-30. 다른 검토자 결과는 보지 않았다. 스냅샷·작업 저장소는 수정하지 않았다.

## 판정

P0/P1 오류는 발견하지 못했다. 적용할 때 계산을 틀리게 만들 수 있는 **P2 한 건(F11의 대역폭 정의 혼용)**을 수정 권고한다. 별도로 조건 명시를 강화할 선택 개선 두 건을 기록한다. 이는 전문가 인증이나 실제 출제 적합성 평가가 아니라 독립 모델 검토다.

## 읽은 범위와 점검 방식

`index.jsonl` 65행과 그 경로의 본문 65개 전체를 읽었다. `sources.json` 83개 항목의 제목·URL·분류·사용 범위·확인일도 전부 읽었다. README.md, metadata.md, VALIDATION.md, application-playbook.md, verify.py, checks/application_checks.py 전체를 읽었다. 큰 출력에서 잘렸던 P02/P03/P04 및 출처 후반은 나누어 다시 읽었다.

| 읽은 ID 전체 목록 | 핵심 검토 |
|---|---|
| F01, F02, F03, F04, F05, F06, F07, F08, F09, F10, F11 | 전류·전위차·옴성 조건·평행판 근사·전력/에너지·운반자·부피 단위·bit/byte·클록·집계 단위·대역폭/지연 |
| P01, P02, P03, P04, P05, P06, P07, P08, P09, P10, P11, P12, P13, P14 | 접합 부호·NMOS 영역·활성도 정의·FEOL/MOL/BEOL·산화/증착·ALD·노광량·선택비·주입량/농도·CMP·배선·계측·검사/재검사·세정 |
| M01, M02, M03, M04, M05, M06, M07, M08, M09, M10, M11, M12, M13 | 전하 공유/복원·계층·타이밍·refresh·DDR 배수·NAND 저장/동작/geometry·상태 수·이력·ECC 범위·WAF·BER 분모 |
| H01, H02, H03, H04, H05, H06, H07, H08, H09, H10, H11, H12, H13, H14, H15 | HBM 용량/대역폭·TSV·2.5D/3D·본딩·MR-MUF/TC-NCF·CTE·열지표·PDN·KGD·열화/시험·FIT/검열·Weibull·AF·FA |
| D01, D02, D03, D04, D05, D06, D07, D08, D09, D10, D11, D12 | join 단위·수율·Wilson·SPC·공정능력·교란·가용 시각·분할/누수·분류·회귀·알람·재현/제출 |

가이드의 입력 프롬프트, 과제 수신 후 7단계, 유형별 읽기 경로, HBM 통합 예제, 검증 실행 설명, 근거 기록 양식까지 검토했다. 과제 계약 우선·불필요한 모델 생략·실제 Probe 미검증의 구분은 적절하다.

재실행: `python3 -I knowledge/semiconductor/verify.py` (스냅샷 루트). 결과: 65 cards, 83 sources, 62 retrieval routes, 91 numeric checks 및 14 synthetic application tests 모두 PASS. 두 코드 파일은 표준 라이브러리만 사용하며 실행에서 원본 과제 파일을 수정하는 동작은 발견하지 못했다. 테스트 함수는 명시된 fixture 범위의 구현으로 읽었고 범용 분석 라이브러리의 입력 검증 수준을 요구하지 않았다.

## 조치가 필요한 발견

### A-01 [P2] 전체 관측 처리량과 전송 구간 속도에 같은 B를 사용한다

- 위치: `knowledge/semiconductor/fundamentals/capacity-bandwidth-latency.md:13` (예제 문장 17행도 함께 정리).
- 문제: 먼저 `B=D/t`를 관측 대역폭으로 정의한 뒤 같은 t/B로 `t≈L+D/B`를 적는다. 측정 시간이 요청 시작부터 완료까지라면 D/B 자체가 전체 시간이므로 L을 두 번 넣는다. 뒤 식의 B는 초기 대기를 제외한 일정 전송 구간의 속도여야 한다. 26행의 측정 구간 확인 질문만으로 두 기호가 서로 다른 양이라는 점이 분명해지지 않는다.
- 독립 반례: D=100 MB, 초기 대기 L=1 s, 이후 속도 B_stream=100 MB/s이면 실제 총 시간은 2 s. 전체 관측 B_obs=100/2=50 MB/s. 원문의 B_obs를 뒤 식에 넣으면 1+100/50=3 s가 되어 50% 과대평가한다. 이 값은 별도 Python 계산으로 확인했다. 단순 산술 검사에는 이 경계 사례가 없다.
- 권장 문구: “전체 구간 관측 처리량은 B_obs=D/t_total이다. 초기 대기 L 뒤 일정 속도 B_stream으로 전송하는 단순 모델은 t_total≈L+D/B_stream이다. B_obs에는 초기 대기가 이미 포함되므로 여기에 L을 다시 더하지 않는다.” 100 MB/2 GB/s 예제도 “초기 대기를 제외한 전송 구간 속도”로 명시한다.
- 근거: 등록 출처 [S13 Intel](https://www.intel.com/content/www/us/en/developer/articles/technical/memory-performance-in-a-nutshell.html)의 Latency, Bandwidth, and Density는 데이터 도착률과 대기를 구분한다. 추가로 직접 읽은 [Argonne MPI tutorial — Interpreting Latency and Bandwidth](https://www.mcs.anl.gov/research/projects/mpi/tutorial/perf/mpiperf/tsld034.htm)는 선형 시간 모델에서 bandwidth를 기울기의 역수로 정의한다. 이 추가 출처는 현재 레지스트리에 없는 자료다.

## 선택 개선 — 오류 건수에 포함하지 않음

### A-O1 [P3] H07의 ΨJT 설명에 방열판 경계조건을 구체화

- 위치: `knowledge/semiconductor/packaging-reliability/thermal-metrics.md:13`, 21행.
- 현재도 적용 조건을 확인하라고 하고 HBM에 일반 IC의 θJA를 그대로 대입하지 말라고 하므로 식 자체를 오류로 판정하지 않았다.
- 다만 원문 [S57 TI SPRA953D](https://www.ti.com/lit/pdf/spra953) §3.2는 방열판을 적용하는 경우 ΨJT를 쓰지 말고 그 상황에 맞는 모델을 쓰도록 구체적으로 제한한다. 이 자료가 HBM 온도 문제의 시작 경로이므로 “방열판/콜드플레이트 등으로 상부 열경로가 바뀌면 데이터시트 ΨJT를 그대로 재사용하지 않는다” 한 문장을 더하면 좋다. 임의 HBM 전용 계수를 추가할 필요는 없다.

### A-O2 [P3] D04의 작은 기대 불량수 예제를 ‘산술 예제’라고 더 명시

- 위치: `knowledge/semiconductor/data-application/spc.md:17`.
- p0=.02, n=100의 UCL=.062 계산과 8/100 초과 판정은 맞다. 다만 np=2여서 이산·비대칭성이 크다. 독립 이항에서 이 한계 초과는 X≥7이며 정확 상측 확률은 약0.004062다. 정규분포의 통상 3σ 상측 확률과 같지 않다.
- 본문에 이미 충분한 표본 근사 점검과 희소 불량 경고가 있으므로 현재 내용을 사실 오류로 세지 않았다. “이 예제는 한계식 산술 설명이며 목표 오경보율을 보장하지 않는다; 희소 불량이면 이항 확률 기반 한계를 검토한다”를 추가하거나 np가 더 큰 예제로 바꾸면 학습자가 주의 문구를 놓칠 가능성이 낮아진다.
- 근거: [S71 NIST p 관리도](https://www.itl.nist.gov/div898/handbook/pmc/section3/pmc332.htm)의 독립 이항 모형·분산·3σ 식. 확률 0.004062는 위 이항모형으로 직접 합산한 값이다.

## 실제로 원문 내용을 대조한 출처

URL 일치 검사와 원문 확인을 구분했다. 아래 **21개 레지스트리 ID**는 웹 도구로 열고 관련 절/문장을 실제 읽었다. PDF는 추출 텍스트의 관련 절을 읽었으며 전 페이지의 그림을 시각 검수한 것은 아니다.

| ID | 실제 읽은 관련 내용과 판단 |
|---|---|
| [S08](https://pml.nist.gov/cuu/Units/binary.html) | 접두어 표, byte=8 bit, MB/MiB와 GB/GiB. F07 환산과 일치. |
| [S13](https://www.intel.com/content/www/us/en/developer/articles/technical/memory-performance-in-a-nutshell.html) | Latency, Bandwidth, and Density. 정의는 일치하며 A-01은 패키지 식의 기호 혼용이다. 과거 제품 수치는 사용하지 않음. |
| [S16](https://www.infineon.com/technology/mosfets) | triode/linear, saturation, pinch-off 및 subthreshold 관련 본문. P02는 원문의 단순 설명에 소스 기준 전압·장채널 조건을 더 명확히 붙임. |
| [S17](https://www.ti.com/lit/pdf/scaa035) | Capacitive-Load Power Consumption과 동적 전력 식. P03은 충전 횟수로 α를 정의해 계수2 혼동을 피함. |
| [S26](https://www.asm.com/our-technology-products/ald) | pulsing/purging, 포화 표면반응. P06는 원문의 ‘원자층’과 무결함 홍보 표현을 보증으로 확대하지 않음. |
| [S36](https://users.ece.cmu.edu/~omutlu/pub/raidr-dram-refresh_isca12.pdf) | §2.1의 채널/랭크/뱅크·셀/센싱/행 접근 및 §2.2의 복원/refresh/tREFI/tRFC. M01/M02/M04 설명과 대조. |
| [S39](https://onlinedocs.microchip.com/oxy/GUID-AFCB5DCC-964F-4BE7-AA46-C756FA87ED7B-en-US-21/GUID-A29420D1-4E36-4920-B9BB-DD0B63F5E787.html) | DDR topology의 rank/bus 설명 및 timing 표의 tRAS/tRCD/tRP/tREFI/tRFC. M03/M04의 핵심 정의와 일치. 표 전체의 정확성을 인증한 것은 아님. |
| [S41](https://www.kioxia.com/en-jp/rd/technology/nand-flash.html) | 저장막·프로그램/소거·전원 차단 보존·문턱전압/읽기전압·직렬 셀 구조. M06의 단순 SLC 구분과 일치. |
| [S52](https://news.skhynix.com/en/creating-new-values-in-dram-using-through-silicon-via-technology-for-continued-scaling-in-memory-system-performance-and-capacity/) | TSV 정의·종횡비 각주·HBM 폭/핀 속도/적층 설명. H01/H02의 구조·계산 축을 대조. 2019년 제품값을 현재값으로 인용하지 않음. |
| [S55](https://news.skhynix.com/en/rulebreaker-revolutions-mr-muf-unlocks-hbm-heat-control/) | MR-MUF/TC-NCF 각주·EMC 역할·적층 열 문제. H05는 당시 개선율을 일반화하지 않음. |
| [S57](https://www.ti.com/lit/pdf/spra953) | θJA 측정/조건, ΨJT 정의·식·방열판 제한. H07 식과 구분은 맞고 A-O1만 추가 권장. |
| [S58](https://www.ti.com/lit/an/swpa222a/swpa222a.pdf) | DC IR drop, capacitor loop inductance, target impedance 절. H08의 IR·루프/기생 관리·정의한 ΔI 기반 목표와 대조. 원문의 특정 전류 스텝 계수를 보편화하지 않음. |
| [S61](https://www.ti.com/quality-reliability/reliability/testing.html) | 시험 표와 HTOL/TC/THB/BHAST/uHAST 설명. H11 스트레스 구분과 일치. 정식 JEDEC 판본은 확인하지 않음. |
| [S63](https://www.itl.nist.gov/div898/handbook/apr/section4/apr451.htm) | total time/failures, Type I censoring, zero fails 단측 MTBF 하한. H12의 역수 λ 상한과 단측95%가 일치. |
| [S64](https://www.itl.nist.gov/div898/handbook/apr/section1/apr151.htm) | 온도-수명 지수식·활성화에너지. H14의 AF 방향·단위와 일치. 원문의 오래된273.16 대신 패키지는273.15를 씀. |
| [S68](https://www.itl.nist.gov/div898/handbook/apr/section1/apr162.htm) | CDF/생존/hazard/평균/중앙수명과 모수. H13은 기호 대응을 명시했고 η를 평균으로 오인하지 않음. |
| [S69](https://pandas.pydata.org/docs/reference/api/pandas.merge.html) | null 키 경고, join 설명. D01의 null 주의와 일치. 제공 환경 pandas 버전은 가정하지 않음. |
| [S70](https://www.itl.nist.gov/div898/handbook/prc/section2/prc241.htm) | Wilson 구간 유도/상하한. D03 식과 숫자 대조. |
| [S71](https://www.itl.nist.gov/div898/handbook/pmc/section3/pmc332.htm) | 불량 개체 비율·독립 Bernoulli/이항·p 관리한계. D02–D04 기본 분모/식과 일치. |
| [S72](https://www.itl.nist.gov/div898/handbook/pmc/section1/pmc16.htm) | 안정 공정·정규성·Cp/Cpk 정의 및 단측 규격 설명. D05 식과 해석 조건 대조. |
| [S76](https://scikit-learn.org/stable/common_pitfalls.html) | Data leakage, train-only fit, split-first, pipeline. D01/D08/D12와 가이드의 분할 후 전처리 원칙에 부합. |

추가 원문 1개: [Argonne MPI tutorial](https://www.mcs.anl.gov/research/projects/mpi/tutorial/perf/mpiperf/tsld034.htm)의 시간-크기 직선 기울기 설명(A-01). 검색 결과의 다른 자료는 이 보고서 근거로 채택하지 않았다.

## 미확인 범위와 수용 가능한 생략

- 83개 출처 전부의 웹 원문을 재검증하지 않았다. 위 21개 이외의 62개는 레지스트리와 본문 연결·논리 검토 범위이며 신규 원문 확인으로 세지 않는다. 따라서 모든 source_type/checked_at의 역사적 진실성을 독립 입증한 것은 아니다.
- S60 Toshiba handbook의 2026 Ver.4 원본 내용, S59 Siemens 백서 본문, 유료 JEDEC 표준, 실제 특정 HBM/DDR/NAND 데이터시트·양산 레시피는 이번 검토에서 읽지 않았다. 메커니즘 정의와 시험 분류에 대해 모든 원문이 일치한다고 단정하지 않는다.
- 실제 Probe·제공 Codex·실제 해커톤 데이터·제품 성능·열 시뮬레이션·ECC 디코더·실제 수명시험은 수행하지 않았다. 구조/합성 검사 PASS를 실제 과제 검증으로 바꾸지 않는다.
- F/P/M/H/D 본문에서 A-01 외의 명백한 식·단위·예제 산술 오류는 발견하지 못했다. 이것은 나머지 모든 기술 주장이 완전 증명됐다는 뜻은 아니다.
- short-channel MOSFET 정량 모델, NAND program algorithm/erase 물리, HBM 세대별 상세 표, RowHammer, JEDEC 타이밍 전체, 열/기계 다중물리 모델, DOE의 무작위화·블로킹 상세는 추가 학습 주제로 가능하다. 이 패키지의 명시된 기초/적용 범위만으로 필수 누락 오류라고 판정하지 않았다.
- VALIDATION.md가 독립 Sol+Sol 미실행이라고 적은 것은 고정 스냅샷 작성 당시 상태다. 이번 검토가 끝난 뒤 기록을 갱신하더라도 전문가 검수·Probe 검증과 구분해야 한다.
