# 독립 Sol 검토 B — 반도체 지식 패키지

검토 기준 커밋: `731eecb0acf12f2d65f045c87a6a51889ea1dbd5`.
검토 사본: `/Users/kty/Documents/ChatGPT/sk-hynix-hackathon/tmp/semiconductor-sol-sol-review/snapshot`.
모델: gpt-6.1-sol. 검토일: 2026-10-30. 검토 A의 결과를 열람하지 않았다. 검토 대상 파일은 수정하지 않았다.

## 판정

65개 본문의 원리·단위·합성 예제·적용 제한을 모두 읽고, 적용 가이드와 구조/합성 검사 코드를 독립 검토했다. 현재 범위에서 P0/P1/P2 수준의 확정된 기술 오류나 사용을 막을 누락은 찾지 못했다. 공개 지식 조회와 분석 절차 안내 용도로 사용할 수 있다. 아래 P3 두 건은 검증 보장의 범위를 더 정확하게 전달하고 희소 비율 예제의 오용을 줄이는 개선이다.

이 결과는 반도체 전문가 인증, 83개 출처 전체의 원문 재검증, 실제 제조 데이터 평가, 실제 Probe 접속·모델 성능·실행 환경 검증이 아니다. 준비용 공개 문서만 사용했고 실제 시험 자료는 다루지 않았다.

## 발견 사항

### B-01 · P3 · 산술 fixture와 본문 숫자의 연결 범위를 명시하거나 연결 검사를 보강

위치: `knowledge/semiconductor/verify.py:45–60`, `knowledge/semiconductor/application-playbook.md:63–71`, `knowledge/semiconductor/VALIDATION.md`의 단계별 계산 검증 설명.

현재 91건 대부분은 코드 안의 숫자로 구성한 `(계산식, 기대값)`끼리 비교한다. F/P/M 본문에 적힌 숫자가 그 결과와 같은지는 검사하지 않는다. H02/H09/H12/H13/H14의 일부 문자열만 본문에서 별도로 찾는다. 따라서 본문 산술 오류를 모두 잡는 회귀 검사로 해석하면 과대평가다. 문서는 이미 기술 내용 전체와 실제 환경은 증명하지 않는다고 명시하므로 사용 차단 사항으로 분류하지 않았다.

구체적 반례를 파일 수정 없이 실행했다. `Path.read_text`를 메모리에서만 대체해 F01 본문의 `= 3 mA다.`를 `= 300 mA다.`로 읽히게 하고 원래 `verify.py`를 실행했다. 변조 본문을 두 번 읽었는데도 65/83 구조, 62개 조회, 91건 계산, 합성 14개가 모두 PASS였다. 실제 저장 파일은 변하지 않았다. F01 원래 예제의 3 mA는 정확하며, 반례는 향후 오류 검출 한계를 확인한 것이다.

제안: 가장 작은 수정은 문구를 “코드에 고정한 교육용 계산 fixture 91건; 본문 숫자 전체의 자동 대조 아님”으로 구체화하는 것이다. 유지보수 검사가 목적이라면 예제의 입력/단위/기대값을 구조화된 자료 한 곳에 두고 본문 생성 또는 대조에 연결한다. 단순 문자열 포함도 문장 의미나 공식의 정확성을 보장하지 않는다는 한계는 남긴다. 이 발견은 저장소 코드에 대한 직접 관찰이며 외부 출처 판정에 의존하지 않는다.

### B-02 · P3 · D04의 희소 비율 예제가 근사 한계에 해당함을 바로 표시

위치: `knowledge/semiconductor/data-application/spc.md:13–21`, `knowledge/semiconductor/checks/application_checks.py:47–52` 및 `test_spc_and_capability_are_separate`.

공식과 `p0=0.02, n=100`에서 UCL=0.062 계산 자체는 맞다. 그러나 이 예제의 기대 불량 수는 2개다. 본문은 “충분한 표본 근사를 점검”하고 희소 불량이 오경보율을 바꾼다고 적지만, 바로 다음 수치 예제가 그 주의 대상임을 연결하지 않는다.

구체적 반례: 독립 이항 `D~Binomial(100,0.02)`에서도 UCL 초과는 `D≥7`이고 정확한 확률은 약 0.004062다. 정규 3σ의 상측 꼬리 약 0.00135와 같지 않다. 즉 실제로 안정한 공정도 명목 정규 해석보다 약 3배 자주 상한을 넘는다. 8/100이 제시한 관리한계 초과라는 진술은 여전히 맞다.

제안: 예제 끝에 “이 경우 np0=2로 희소하므로 3σ라는 이름에서 정규 오경보율을 보장하지 않는다. 실제 알람 설계는 정수 경계의 이항 꼬리확률과 표본 크기를 확인한다”를 추가한다. 고정 수의 만능 표본 기준을 새로 보장할 필요는 없다. 근거: [S71 NIST 비율 관리도](https://www.itl.nist.gov/div898/handbook/pmc/section3/pmc332.htm)의 이항 분포/독립 가정과 관리한계 공식. 위 꼬리확률은 그 이항식으로 직접 계산했다.

## 65개 본문 전수 검토 범위

각 행의 “확인”은 본문을 읽고 내부 논리·단위·예제·적용 조건을 대조했다는 뜻이다. 해당 카드의 모든 외부 출처까지 재열람했다는 뜻은 아니다. 원문 재열람 범위는 아래에 별도로 기록한다.

| ID | 확인한 핵심과 판정 |
| --- | --- |
| F01 | 평균/순간 전류, 관습적 방향, 전위차, 3 mA 환산 타당. |
| F02 | 옴성 조건, V/I와 미분 저항 차이, 전류 0 처리 타당. |
| F03 | Q=CV·평행판 근사, fF/fC 예제, 누설 제한 타당. |
| F04 | 전력과 에너지 구분, 시간 적분, 평균 곱의 한계 타당. |
| F05 | 밴드/정공과 eV/V 구분, 재료·온도 조건 타당. |
| F06 | donor/acceptor, 농도 체적 변환, 중성/보상·활성화 제한 타당. |
| F07 | bit/B·SI/이진 접두어, 용량/전송률 예제 타당. |
| F08 | 논리, 주파수/주기/듀티, 클록과 전송률 구분 타당. |
| F09 | wafer/die/IC/package, 좌표 복합 키와 집계 단위 타당. |
| F10 | 휘발성/비휘발성·RAM 분류 축, 영구 보증 제한 타당. |
| F11 | 용량/처리량/지연, L+D/B 근사의 경합·큐잉 한계 타당. |
| P01 | PN 부호와 바이어스, 공핍층의 고정 전하, 0.7 V 근사 제한 타당. |
| P02 | VGS/VDS 기준, 장채널 NMOS 영역 경계와 예제 타당. S16 해당 설명 대조. |
| P03 | 활동도 정의에 맞는 αCV²f, 내부/누설 성분과 계수 2 주의 타당. |
| P04 | FEOL/MOL/BEOL와 패키징 후공정 구분, 재작업/run 구분 타당. |
| P05 | 열산화/증착 구분, 비선형 성장률, 두께와 품질 분리 타당. |
| P06 | PVD/CVD/ALD, GPC 정상구간·핵생성 지연, 피복성 분모 타당. |
| P07 | positive/negative PR, dose 단위, 현상과 식각 구분 타당. |
| P08 | 선택비 분자/분모, 방향성 예외, 일정 식각률 예제 타당. |
| P09 | dose/농도·에너지 구분, 활성 농도 및 분포 제한 타당. |
| P10 | 대응 위치의 제거율, 평균과 국소 dishing/erosion 분리 타당. |
| P11 | 균일 도선 저항식·단위, 접촉/비아 저항과 open/short 구분 타당. |
| P12 | CD/overlay 성분과 벡터, 검출 한계/불확실도/recipe 조건 타당. |
| P13 | EPM·다이/패키지 검사, bin 의미·최초/최종 분모 타당. |
| P14 | 동일 검출 조건의 겉보기 감소율, 신규 손상/0 검출 제한 타당. |
| M01 | 전하 공유 초기 모형과 센싱 복원, precharge 구분 타당. S36 배경 대조. |
| M02 | 채널/랭크/뱅크와 공유 버스·랭크 중복 배수 제한 타당. |
| M03 | 명령 간 시간·nCK 올림, 행 상태별 첫 데이터 근사·대기 제약 타당. |
| M04 | retention/tREFI/tRFC 분리, 자원별 refresh 점유율과 앱 시간 제한 타당. |
| M05 | MT/s·폭·버스트, DDR 2 중복 배수 및 ECC payload 제한 타당. |
| M06 | FG/charge-trap·Vth/Vref, SLC 판별 예제와 인코딩 제한 타당. |
| M07 | page/block/main/OOB, TLC 중복 배수와 예약 영역 제한 타당. |
| M08 | 내부 시간/전송 시간/호스트 완료, ready와 성공 구분 타당. |
| M09 | 상태 2^b·경계 수, 실제 페이지 읽기 횟수 구분 타당. |
| M10 | retention/read-disturb/P/E·열 이력과 retry/refresh 분리 타당. |
| M11 | 코드워드별 SECDED, 3-bit 이상 보장 제한·on-die 보호 범위 타당. |
| M12 | 구간 카운터 WAF·reset/압축/캐시, TRIM과 소거 구분 타당. |
| M13 | RBER/UBER 측정 경계·분모, request를 bit로 세지 않는 주의 타당. |
| H01 | 코어 용량/스택 폭과 pin rate, base die·적층 수 중복 배수 제한 타당. |
| H02 | TSV/접합/체인 구분, 원통 저항·종횡비 예제 타당. |
| H03 | 2.5D와 수직 적층, interposer/RDL·스택과 DRAM 다이 집계 구분 타당. |
| H04 | 금속/유전체 본딩, 표면·CMP·정렬·피치 밀도 근사 제한 타당. |
| H05 | MR-MUF/TC-NCF 재료 역할, void 면적/부피·불량률 구분 타당. |
| H06 | 자유 열팽창과 구속 응력 구분, CTE 단위·프로파일 제한 타당. |
| H07 | θJA/θJC/ΨJT 경계조건과 정상상태 예제 타당. S57 §3 대조. |
| H08 | IR/Ldi/dt/목표 임피던스, 별도 예제의 무조건 합산 금지 타당. |
| H09 | 선별 후 잔여 확률 q의 독립 조립 모형, raw wafer 수율 대입 금지 타당. |
| H10 | EM/TDDB/BTI와 관측 신호 구분, 전류밀도·회복 시간 주의 타당. |
| H11 | HTOL/HTSL/TC/습도/ESD 스트레스·판본 조건 구분 타당. |
| H12 | 노출시간/검열, 일정 hazard·FIT/MTTF·0고장 단측 상한 타당. S63/S66 대조. |
| H13 | Weibull 모수 대응·hazard·특성/중앙수명과 검열 주의 타당. S68 대조. |
| H14 | Kelvin·AF 방향/단위, 동일 메커니즘·모수 불확실성 제한 타당. S64 대조. |
| H15 | 재현·비파괴/파괴 분석·정상 비교, 위치와 원인 증거 구분 타당. |
| D01 | m:1/1:1·null 매칭·팽창률·미매칭·결측 처리 타당. S69 대조. |
| D02 | 최초/최종 판정·고유 개체와 이벤트 분모·가중 합 타당. |
| D03 | 불량 개체/결함 수·Wilson·표본0·군집 상관 제한 타당. S70/S71 대조. |
| D04 | 관리/규격한계 분리 및 수식 타당. 희소 예제의 오경보율 설명 보강 권고 B-02. |
| D05 | 안정성·정규·σ 추정/부분군·측정 변동 제한 타당. S72 대조. |
| D06 | 제품 구성의 집계 역전 예제·교란/반증·원인 확정 제한 타당. |
| D07 | event/available 시점·최대 나이·미래 보간 제한 타당. S75와 자체 toy 대조. |
| D08 | 일반화 목적에 따른 그룹/시간 분리·라벨 지연·fold 안 전처리 타당. S76/S77 대조. |
| D09 | 불량 양성·혼동행렬·분모0·기준선·임계값/test 분리 타당. S78 대조. |
| D10 | MAE/RMSE 단위·목표 역변환·조건별 잔차·상수 정답 한계 타당. S78 대조. |
| D11 | novelty/outlier·샘플/이벤트·정답 없는 오알람률 금지 타당. |
| D12 | 과제 계약→분할→기준선→동일 검증→제출·재현 기록 타당. |

## 가이드·색인·검증 문서 검토

- `index.jsonl`: 65개 항목의 ID/경로/선수/관련/출처 연결을 전수 확인했다. 모든 본문을 실제로 읽었다. 검색 검사는 정답 ID가 문자열 검색 결과에 포함되는지 확인하며 순위·유일 검색·모델의 검색 성공률을 평가하지 않는다.
- `sources.json`: 83개 레코드의 출판 주체·원제·URL·사용 범위·날짜 기록을 읽었다. source ID/URL 매칭은 출처 내용의 사실 검증이 아니다. 오래된 자료에서 현재 제품 수치를 가져오지 않도록 사용 범위가 제한돼 있다. S59가 미취득 백서 본문 대신 공개 소개만 사용했다고 기록한 점도 구분했다.
- `README.md`: 사용 순서, 65개 빠른 조회 경로, 반입 경로 보존, 예제/제품 사양 구분을 확인했다.
- `metadata.md`: ready의 범위, checked_at과 발행일 차이, evidence·source_type의 의미가 전문가/실물 검증을 뜻하지 않도록 적혀 있다.
- `application-playbook.md`: 제공 Codex 프롬프트, 7단계 절차, 6개 문제 시작 경로, HBM 통합 예제, 검증 명령, 합성 검사 제한, 근거 기록 양식을 모두 읽었다. 설명/집계 문제에 무조건 모델을 만들지 않고, 진단과 사전 예측 입력을 구분한다. ID·열·순서 등 제출 계약을 실제 과제에 맞추도록 안내한다.
- `VALIDATION.md`: 단계별 완료 시점의 개수와 현재 전체 개수가 구분된다. 저자 검증과 미수행 독립 검수/실제 환경 검증도 구분돼 있다. 이번 검토가 반영되기 전의 “Sol+Sol 미수행” 기록은 동결 시점의 설명이므로 오류로 잡지 않았다.
- `verify.py`: 전체 소스를 읽고 실행했다. ID·경로·내부 링크·비순환 관계·카드 헤더와 출처 URL·합성 산술 검사가 범위다. JSON schema의 필드 전체 타입·source_type 열거형·모든 메타데이터 의미·외부 페이지·모든 주장 정확성을 완전히 검증하는 코드는 아니다.
- `checks/application_checks.py`: 전체 소스와 14개 테스트를 읽었다. 이 함수들은 실제 파일/모델용 라이브러리가 아니라 fixture 계약을 가진 교육 예제다. 최소 입력 검증을 생산 수준으로 확장하지 않았다는 이유만으로 결함을 만들지 않았다.

## 실제 실행한 검사와 반례

동결 사본에서 `git rev-parse HEAD`가 기준 SHA와 같음을 확인했다.

`python3 -I knowledge/semiconductor/verify.py` 실행 결과:

```text
PASS: 65 cards, 83 sources, IDs/links/references/acyclic prerequisites, 62 retrieval routes, 91 numeric checks, rounded examples, zero-failure bound, AF direction and Weibull exponential boundary
PASS: 14 synthetic application tests; no actual Probe/model validation
Ran 14 tests ... OK
```

14개 검사는 재검사/결합, last-pass와 any-pass 차이, 잘못된 결합키, Wilson 경계, SPC/Cpk, 제품 구성 교란, point-in-time 결합, 그룹/시간 조건, train-only 대치, 희소 분류/기준선, 회귀 단위, 샘플/이벤트 알람, HBM 단위, 제출 확률/ID 계약을 각각 다룬다.

특히 `past_value`는 후보를 event/available 두 조건으로 먼저 제한하므로 최신 이벤트가 아직 도착하지 않았을 때 이전의 가용 값을 선택한다. 실제 pandas backward 결합 후 최신 미도착 행만 버리는 잘못된 순서와는 다르다. `validate_split`은 이 fixture의 “미래 새 그룹” 계약을 강제하므로, 같은 장비 미래 예측에서 장비를 무조건 새 그룹으로 분리하라는 보편 규칙으로 읽으면 안 된다. 본문 D08은 이미 이를 구분한다.

검사는 모든 함수의 모든 입력 경계·시간대·동일 timestamp의 여러 버전·실제 CSV 스키마·모델 학습/일반화·자원 제한을 증명하지 않는다. 원래 문서가 이 한계를 명시하므로 실제 사용 코드가 아니라는 이유를 무시하고 생산 라이브러리 수준의 결함으로 분류하지 않았다.

추가 실행은 B-01 메모리 내 본문 치환과 B-02 정확 이항 꼬리 합이다. 실제 파일, 스냅샷, 작업 저장소는 변경하지 않았다.

## 이번 검토에서 원문을 실제로 연 출처

83개 출처 레코드를 읽은 것과 별도로 아래 15개 원문 URL을 열었다. 웹 도구가 반환한 본문/관련 단락을 대조했으며 전체 장문 사이트·논문·PDF를 끝까지 읽었다고 주장하지 않는다. PDF 페이지는 1부터 센다. 나머지 68개 원문은 이번 B 검토에서 재열람하지 않았다.

| ID | 실제 열람 단락/페이지와 대조 내용 |
| --- | --- |
| S16 | [Infineon MOSFET](https://www.infineon.com/technology/mosfets): enhancement planar 및 inversion의 linear/saturation 설명. VGS−Vth 경계와 소스 기준의 본문 모델을 대조. |
| S36 | [RAIDR 원 논문](https://users.ece.cmu.edu/~omutlu/pub/raidr-dram-refresh_isca12.pdf): p.1 초록/도입, p.2 §2.1 조직·전하 공유·센싱·precharge와 p.3 §2.2 refresh 배경 단락을 열람. 현행 제품 수치로 외삽하지 않음. |
| S57 | [TI SPRA953D](https://www.ti.com/lit/pdf/spra953): p.1 범위, p.3 θJA 조건, p.8 §3 ΨJT 정의/식/열경로, p.9 온도 측정 단락 일부. H07 경계조건과 식 대조. |
| S63 | [NIST HPP/exponential](https://www.itl.nist.gov/div898/handbook/apr/section4/apr451.htm): 추정식/검열, 신뢰한계 사용법 및 zero-fails 식/해석 단락 확인. 모형 조건과 단측 수준을 구분. |
| S64 | [NIST Arrhenius](https://www.itl.nist.gov/div898/handbook/apr/section1/apr151.htm): 시간-온도 식, 활성화에너지·AF 방향. 원문 옛 섭씨 변환 상수 대신 카드의 273.15 사용은 타당. |
| S66 | [NIST Exponential](https://www.itl.nist.gov/div898/handbook/apr/section1/apr161.htm): R·hazard·MTTF, 일정 hazard의 사용 범위. |
| S68 | [NIST Weibull](https://www.itl.nist.gov/div898/handbook/apr/section1/apr162.htm): R·hazard·median, 기호의 다양성과 지수분포 경계. |
| S69 | [pandas.merge](https://pandas.pydata.org/docs/reference/api/pandas.merge.html): API 개요·null 매칭 경고. D01 경고와 부합. |
| S70 | [NIST confidence intervals](https://www.itl.nist.gov/div898/handbook/prc/section2/prc241.htm): Wilson 공식·단측/양측 구분. D03 식과 예제 대조. |
| S71 | [NIST proportions charts](https://www.itl.nist.gov/div898/handbook/pmc/section3/pmc332.htm): 개체 불량/이항·독립 가정·p-chart 공식과 기준 추정. |
| S72 | [NIST capability](https://www.itl.nist.gov/div898/handbook/pmc/section1/pmc16.htm): 안정/정규·Cp/Cpk 식, 단측 규격 단락 시작. |
| S75 | [pandas.merge_asof](https://pandas.pydata.org/docs/reference/api/pandas.merge_asof.html): backward/forward/nearest·정렬·by 의미. available_at 추가 조건은 pandas가 자동 제공하는 기능으로 오기하지 않음. |
| S76 | [scikit-learn pitfalls](https://scikit-learn.org/stable/common_pitfalls.html): 전처리 일관성, §12.2 누수·분할 후 fit·pipeline 설명. |
| S77 | [scikit-learn cross-validation](https://scikit-learn.org/stable/modules/cross_validation.html): GroupKFold와 시계열 분할 관련 단락, 목적별 분리 대조. |
| S78 | [scikit-learn metrics](https://scikit-learn.org/stable/modules/model_evaluation.html): precision/recall/F1·분모0·AP와 사다리꼴 면적 차이, MSE/RMSE 및 목표 단위·MAPE 설명. |

## 누락 판단과 한계

다음은 별도 결함으로 올리지 않았다. 단측 규격의 Cpu/Cpl, 공정능력의 장단기 추정 실무, 정확 이항 관리 경계, 확률 보정·비용곡선, 다중검정, 정교한 생존모형, 모델 tuning의 nested 평가 등은 추가 교재가 될 수 있다. 현재 카드가 해당 범위의 구현을 보장하지 않고 실제 계약·모형 조건을 우선하도록 안내하므로, 모두 필수 누락이라고 주장할 근거가 없다. B-02는 기존 희소 예제에 직접 붙는 한 문장의 안전장치라 구분했다.

일부 장문 출력이 도구에서 잘려 보인 부분은 해당 본문을 다시 개별 열람했다. 카드 65개는 누락 없이 읽었다. 리뷰의 신뢰도는 공개 기초 원리와 명시한 합성 예제의 검토에 한정된다. 실제 과제에서 올바른 카드를 선택하고 데이터를 정확하게 매핑하는 능력은 별도 검증이 필요하다.
