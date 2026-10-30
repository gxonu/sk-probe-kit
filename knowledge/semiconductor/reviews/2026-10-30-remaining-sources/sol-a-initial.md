# 잔여 58개 원출처 독립 검토 A

대상 기준: `9dab381bcccfc70d9c6596e13efff9d1879a2a0a` 동결 snapshot. reviewer A는 다른 reviewer 결과·과거 25개 보고서의 결론을 읽지 않았다. 카드와 registry는 수정하지 않았다.

58개 각각의 실제 공식 원문을 열고, linked card 전문(공식, 적용 가정, 자작 예제, 한계 포함)을 대조했다. 원문 확인은 등록 used_for에 대응하는 관련 절 확인이며 전체 교재/백서 전체 정독을 뜻하지 않는다. 등록원문 57개 직접 접근, S45는 Taiwan 도메인의 도구 접근 오류 후 www.kioxia.com 공식 동일 PDF로 대조했다. 최종 상태 58 verified / 0 partial / 0 unavailable은 이 제한된 등록 사용범위에 대한 상태다.

수정이 필요한 사실 오류·중요 누락은 발견하지 않았다. 따라서 actionable finding ID 및 severity/path:line/source/counterexample/correction 목록은 비어 있다. 출처의 지나친 단순화를 카드가 이미 명시적으로 제한한 사항은 새 결함으로 세지 않았다. 원문에 없는 자작 산술/과제 질문은 그 자체로 오인용으로 취급하지 않았고 기초 원리·단위·가정을 점검했다. 이 결과는 실제 제품 사양이나 제조 레시피의 정확성 인증이 아니다.

S03의 등록 §8.1은 진공 평행판 식을 유도한다. 카드의 균일 유전체 확장은 [같은 교재 §8.4](https://openstax.org/books/university-physics-volume-2/pages/8-4-capacitor-with-a-dielectric)의 C=κC0로 보충 대조했다. 최초 보충 URL의 절 번호를 잘못 구성해 접근 오류가 있었고 올바른 §8.4 원문으로 바로잡았다. S27은 공식 초록의 정의 범위, S59는 공개 소개의 KGD/D2D 범위만 검토했으며 미취득 본문을 읽었다고 주장하지 않는다. PDF는 공개 본문 추출의 해당 페이지를 확인했다. 그림 픽셀의 독립 시각 검증이나 도표 숫자의 재현은 하지 않았다.

## 출처별 대조 기록

### S01 — verified

- 카드: F01 `fundamentals/charge-current-voltage.md`
- 원문: [S01](https://openstax.org/books/university-physics-volume-2/pages/9-1-electrical-current)
- 확인 위치: §9.1 Defining Current and the Ampere; Current in a Circuit, eq9.1–9.3
- 대조: 평균/순간 전류, A=C/s, 관습 방향과 전자 방향; 6μC/2ms=3mA
- 판단: 등록 사용범위에서 지지됨; actionable finding 없음.
- 한계: 회로 배선·장비 진단은 자체 적용 질문

### S02 — verified

- 카드: F02 `fundamentals/resistance-ohm.md`
- 원문: [S02](https://openstax.org/books/university-physics-volume-2/pages/9-4-ohms-law)
- 확인 위치: §9.4 Description/Ohm experiment, eq9.11; temperature example
- 대조: 옴성 비례와 원점 직선, V=IR, 온도 조건; 1V/2kΩ=0.5mA
- 판단: 등록 사용범위에서 지지됨; actionable finding 없음.
- 한계: 미분저항 비교와 결측 처리 경고는 원문의 직접 설명보다 넓은 교육용 보완

### S03 — verified

- 카드: F03 `fundamentals/capacitance.md`
- 원문: [S03](https://openstax.org/books/university-physics-volume-2/pages/8-1-capacitors-and-capacitance)
- 확인 위치: §8.1 capacitance definition, parallel-plate derivation eq8.1–8.3; 공식 동권 §8.4 eq8.11 보충
- 대조: Q=CV·F=C/V·평행판의 작은 간격/가장자리 무시 조건; 20fF×1V=20fC
- 판단: 등록 사용범위에서 지지됨; actionable finding 없음.
- 한계: 등록 절은 진공 ε0 유도; 균일 유전체 확장은 같은 출판사 §8.4에서 별도 확인. 전체 교재 미독

### S04 — verified

- 카드: F04 `fundamentals/power-energy.md`
- 원문: [S04](https://openstax.org/books/physics/pages/19-4-electric-power)
- 확인 위치: §19.4 Electric Power, eq19.47–19.50 및 I²R/V²R 유도
- 대조: 전력=에너지/시간, P=VI, 저항 전력; 2W×3s=6J와 1W×8s=8J
- 판단: 등록 사용범위에서 지지됨; actionable finding 없음.
- 한계: 시간 적분과 평균 곱의 한계는 원리에서 도출한 자체 보완

### S05 — verified

- 카드: F05 `fundamentals/semiconductor-bands.md`
- 원문: [S05](https://openstax.org/books/university-physics-volume-3/pages/9-6-semiconductors-and-doping)
- 확인 위치: §9.6 opening; donor/acceptor and impurity bands, fig9.18–9.21 설명
- 대조: 정공·전자·가전자대/전도대·도핑; eV와 V를 구분하는 예제
- 판단: 등록 사용범위에서 지지됨; actionable finding 없음.
- 한계: Hall effect 상세나 모든 밴드갭 값 확인 범위 아님

### S06 — verified

- 카드: F06 `fundamentals/doping-carriers.md`
- 원문: [S06](https://toshiba.semicon-storage.com/us/semiconductor/knowledge/faq/common_common/what-is-an-n-type-semiconductor.html)
- 확인 위치: N-type FAQ 본문
- 대조: Si에 P/As 도핑·자유전자 공급과 n형; 농도 단위 변환 예제 점검
- 판단: 등록 사용범위에서 지지됨; actionable finding 없음.
- 한계: 짧은 FAQ는 보상/불완전 이온화까지 설명하지 않음; 그 한계 문구는 자체 보완

### S07 — verified

- 카드: F06 `fundamentals/doping-carriers.md`
- 원문: [S07](https://toshiba.semicon-storage.com/us/semiconductor/knowledge/faq/common_common/what-is-a-p-type-semiconductor.html)
- 확인 위치: P-type FAQ 본문
- 대조: B/In 도핑, 결합 전자 부족과 정공 이동; F06의 p형 설명
- 판단: 등록 사용범위에서 지지됨; actionable finding 없음.
- 한계: 짧은 FAQ는 모든 농도/온도 조건을 다루지 않음

### S09 — verified

- 카드: F08 `fundamentals/digital-clock-logic.md`
- 원문: [S09](https://faculty.etsu.edu/tarnoff/ntes2150/dig_bin/dig_bin.htm)
- 확인 위치: Digital waveforms/Periodic Pulse Train/Duty cycle; Digital Signals in Real-World; NOT AND OR XOR truth tables
- 대조: f=1/T·duty=high/T·실제 전환·4개 논리; 500MHz=2ns, duty25%
- 판단: 등록 사용범위에서 지지됨; actionable finding 없음.
- 한계: 미갱신 고지 확인; 2003년 특정 하드웨어 수치는 비교 대상 아님

### S10 — verified

- 카드: F09 `fundamentals/wafer-die-ic.md`
- 원문: [S10](https://www.nist.gov/semiconductors/semiconductor-glossary)
- 확인 위치: Semiconductor Glossary: transistor, integrated circuit, wafer, chip, fab 항목
- 대조: 웨이퍼 기반 IC, 구성 소자, fab/집계 단위; 단일다이=단일패키지 가정 금지
- 판단: 등록 사용범위에서 지지됨; actionable finding 없음.
- 한계: 용어집의 chip은 패키지 제품 의미; 문맥별 die 용례는 카드의 범위 보완

### S11 — verified

- 카드: F09 `fundamentals/wafer-die-ic.md`
- 원문: [S11](https://www.asml.com/en/company/stories/2021/semiconductor-manufacturing-process-steps)
- 확인 위치: Six crucial steps: Packaging 절
- 대조: 웨이퍼 절단→개별 die→패키지 개요와 다중 집계 구분
- 판단: 등록 사용범위에서 지지됨; actionable finding 없음.
- 한계: 교육 기사 다른 절의 식각/현상 단순화를 카드 근거로 사용하지 않음; 제품 수치 미검토

### S12 — verified

- 카드: F10 `fundamentals/memory-map.md`
- 원문: [S12](https://news.skhynix.com/en/semiconductor-101-sk-hynix-explains-whats-what-in-the-semiconductor-world/)
- 확인 위치: What are different types; What does semiconductor memory actually do
- 대조: memory/logic·DRAM/SRAM 휘발성·NAND 비휘발성·전원 차단 조건
- 판단: 등록 사용범위에서 지지됨; actionable finding 없음.
- 한계: 기사 permanent를 무한 보존으로 취급하지 않는 카드 제한 확인; 제품 성능 수치 미검토

### S14 — verified

- 카드: F01 `fundamentals/charge-current-voltage.md`
- 원문: [S14](https://openstax.org/books/university-physics-volume-2/pages/7-2-electric-potential-and-potential-difference)
- 확인 위치: §7.2 Electric Potential/Potential Difference eq7.4–7.5
- 대조: 전하당 위치에너지·ΔU=qΔV·V=J/C·기준점; F01 에너지 크기식
- 판단: 등록 사용범위에서 지지됨; actionable finding 없음.
- 한계: 정전기 위치에너지 관계를 일정 전압 예제로 사용한 범위

### S15 — verified

- 카드: P01 `devices-process/pn-junction.md`
- 원문: [S15](https://toshiba.semicon-storage.com/us/semiconductor/knowledge/e-learning/discrete/chap1/chap1-6.html)
- 확인 위치: pn Junction 전체 설명: no/forward/reverse bias
- 대조: PN 경계·공핍층·순/역바이어스·항복; Vp−Vn=-2V 예제
- 판단: 등록 사용범위에서 지지됨; actionable finding 없음.
- 한계: 원문 역전류0/0.7V 이상화를 카드가 실제 누설/연속특성으로 제한함

### S18 — verified

- 카드: P04 `devices-process/process-flow.md`
- 원문: [S18](https://www.iue.tuwien.ac.at/phd/filipovic/node9.html)
- 확인 위치: §1.1 Traditional Semiconductor Process Technologies 전체 짧은 본문
- 대조: 여러 공정 조합으로 형상 생성; 고정 8단계 해석 금지
- 판단: 등록 사용범위에서 지지됨; actionable finding 없음.
- 한계: 실제 route/run 키는 자체 데이터 적용; 개별 양산 레시피 미확인

### S19 — verified

- 카드: P07 `devices-process/lithography.md`
- 원문: [S19](https://www.iue.tuwien.ac.at/phd/filipovic/node10.html)
- 확인 위치: §1.1.1 Lithography 전체 본문
- 대조: 마스크·PR·노광·현상·positive/negative 구분·후속 식각; dose 차원과 20mJ/cm² 산술
- 판단: 등록 사용범위에서 지지됨; actionable finding 없음.
- 한계: bake/정렬/dose 운영 상세는 짧은 절에 없음; 물리적으로 양립하는 자체 보완

### S20 — verified

- 카드: P08 `devices-process/etch.md`
- 원문: [S20](https://www.iue.tuwien.ac.at/phd/filipovic/node11.html)
- 확인 위치: §1.1.2 Etching 전체 본문
- 대조: 선택비·등방성·습식 결정방향/건식 중성종; 10:1/2min/20nm 예제
- 판단: 등록 사용범위에서 지지됨; actionable finding 없음.
- 한계: 정확한 rate 비율 정의·고정률 산술은 카드가 명시한 자체 근사

### S21 — verified

- 카드: P06 `devices-process/deposition.md`
- 원문: [S21](https://www.iue.tuwien.ac.at/phd/filipovic/node12.html)
- 확인 위치: §1.1.3 Deposition 전체 본문
- 대조: PVD 물질 전달·evaporation/sputtering, CVD 반응; 보편 우열 금지
- 판단: 등록 사용범위에서 지지됨; actionable finding 없음.
- 한계: ALD는 이 원문 범위 밖이며 별도 S26 인용 사항; 이번 검토에서 S26 재평가하지 않음

### S22 — verified

- 카드: P10 `devices-process/cmp.md`
- 원문: [S22](https://www.iue.tuwien.ac.at/phd/filipovic/node13.html)
- 확인 위치: §1.1.4 Chemical Mechanical Planarization 전체 본문
- 대조: 화학/물리 제거·평탄화와 리소그래피 초점 관계; 제거율 1nm/s
- 판단: 등록 사용범위에서 지지됨; actionable finding 없음.
- 한계: 원문의 매 증착 뒤 CMP 표현을 카드가 보편 규칙으로 확대하지 않음

### S23 — verified

- 카드: P05 `devices-process/oxidation.md`
- 원문: [S23](https://www.iue.tuwien.ac.at/phd/filipovic/node14.html)
- 확인 위치: §1.1.5 Oxidation 전체 본문
- 대조: O2/H2O 열산화와 외부 증착 구분, 고온 Si 반응; 8→10nm=25%
- 판단: 등록 사용범위에서 지지됨; actionable finding 없음.
- 한계: 실제 성장속도·gate 재료별 신뢰성값 미검토

### S24 — verified

- 카드: P09 `devices-process/implant-anneal.md`
- 원문: [S24](https://www.iue.tuwien.ac.at/phd/filipovic/node15.html)
- 확인 위치: §1.1.6 Ion Implantation 전체 본문
- 대조: 가속 이온 도핑·후속 어닐링/활성화; dose/두께 가정농도=10^18cm^-3
- 판단: 등록 사용범위에서 지지됨; actionable finding 없음.
- 한계: 원문의 원자당 운반자 서술을 카드가 100%활성화 보증으로 쓰지 않음; 각도/손상 상세 자체 보완

### S25 — verified

- 카드: P09 `devices-process/implant-anneal.md`
- 원문: [S25](https://www.iue.tuwien.ac.at/phd/filipovic/node16.html)
- 확인 위치: §1.1.7 Diffusion 전체 본문
- 대조: 도펀트 확산·온도/후속 고온공정으로 분포 변화; dose와 농도 구분
- 판단: 등록 사용범위에서 지지됨; actionable finding 없음.
- 한계: 확산계수·개별 깊이 프로파일 계산은 범위 아님

### S27 — verified

- 카드: P12 `devices-process/metrology-inspection.md`
- 원문: [S27](https://www.nist.gov/publications/critical-dimension-and-overlay-metrology)
- 확인 위치: 공식 출판물 페이지 Abstract (2003)
- 대조: CD의 설계 목표/overlay 층 정렬 역할; 32−30=2nm, 3–4–5 벡터
- 판단: 등록 사용범위에서 지지됨; actionable finding 없음.
- 한계: 공개 초록으로 등록 used_for의 정의만 확인; 유료 장 전체·2003장비 동향 미독

### S28 — verified

- 카드: P12 `devices-process/metrology-inspection.md`
- 원문: [S28](https://www.asml.com/en/technology/lithography-principles/measuring-accuracy)
- 확인 위치: Types of metrology and inspection; Optical metrology/How it works; e-beam 관련 설명
- 대조: 광학/전자빔·타깃·marked locations·feedback; 실제 결함과 후보 구분
- 판단: 등록 사용범위에서 지지됨; actionable finding 없음.
- 한계: 공급사 시스템별 성능 수치나 검사 알고리즘 개별 구현 검증 아님

### S29 — verified

- 카드: P04 `devices-process/process-flow.md`, P13 `devices-process/electrical-test.md`
- 원문: [S29](https://news.skhynix.com/en/semiconductor-back-end-process-episode-1-understanding-semiconductor-testing/)
- 확인 위치: Back-end Process; Testing Temperature/Speed/Movement; Wafer Test/EPM/Repair/Test; Package Test
- 대조: BEOL/후공정 문맥·EPM·wafer/package test·재시험; 최초90%/최종95%
- 판단: 등록 사용범위에서 지지됨; actionable finding 없음.
- 한계: 공개 예시 순서를 모든 제품 고정 route로 해석하지 않음; 실제 test limits 미확인

### S30 — verified

- 카드: P11 `devices-process/interconnect.md`
- 원문: [S30](https://news.skhynix.com/en/people-who-put-a-uniform-drawing-paper-on-a-wafer-thinfilm-technology/)
- 확인 위치: Uniform Thinfilm; PVD/metal line discussion; Damascene 각주
- 대조: 배선 전달·SiO2 패턴→금속 채움→CMP; interconnect 정의와 R 예제
- 판단: 등록 사용범위에서 지지됨; actionable finding 없음.
- 한계: 기사의 RIE=PVD 식 과도한 단순화는 카드에 옮겨지지 않음

### S31 — verified

- 카드: P14 `devices-process/cleaning.md`
- 원문: [S31](https://www.lamresearch.com/product/reliant-strip-clean-products/)
- 확인 위치: Overview/Industry Challenges/Key Applications
- 대조: 공정 사이 unwanted material 제거·다음 표면 준비·fragile structure 손상; 50→10=80%
- 판단: 등록 사용범위에서 지지됨; actionable finding 없음.
- 한계: 약액/레시피·실제 입자 검출 성능은 범위 아님

### S32 — verified

- 카드: P10 `devices-process/cmp.md`
- 원문: [S32](https://www.agc.com/en/products/electoric/detail/cmp.html)
- 확인 위치: CMP Slurry introduction; Chemical Mechanical Polishing
- 대조: slurry/abrasive/chemicals/pad와 높은 영역 우선 제거; 평균만으로 국소품질 판정 금지
- 판단: 등록 사용범위에서 지지됨; actionable finding 없음.
- 한계: 제품 zero defects 광고를 보증으로 사용하지 않음

### S33 — verified

- 카드: P11 `devices-process/interconnect.md`, H02 `packaging-reliability/tsv.md`
- 원문: [S33](https://openstax.org/books/university-physics-volume-2/pages/9-3-resistivity-and-resistance)
- 확인 위치: §9.3 Resistance eq9.8–9.9; uniform cylinder discussion
- 대조: R=ρL/A와 재료/형상 구분; P11=20Ω·H02≈0.05093Ω/AR10
- 판단: 등록 사용범위에서 지지됨; actionable finding 없음.
- 한계: 미세크기/접촉/라이너는 이상모형 밖이라는 한계 확인

### S34 — verified

- 카드: P10 `devices-process/cmp.md`
- 원문: [S34](https://ir.appliedmaterials.com/news-releases/news-release-details/applied-materials-announces-advanced-copper-cmp-processes-new)
- 확인 위치: May17 2000 release: copper CMP solutions and process control paragraphs
- 대조: dishing·erosion·particles/microscratches 관리 근거
- 판단: 등록 사용범위에서 지지됨; actionable finding 없음.
- 한계: 2000장비 성능·시장/양산 현황은 사용·검토 범위 아님

### S35 — verified

- 카드: P04 `devices-process/process-flow.md`
- 원문: [S35](https://www.imec-int.com/en/articles/logic-technology-scaling-options-2nm-and-beyond)
- 확인 위치: BEOL/MOL 질문답변
- 대조: BEOL 배선망, MOL=FEOL-BEOL 연결과 contact S/D/G; P04 구분
- 판단: 등록 사용범위에서 지지됨; actionable finding 없음.
- 한계: 2021 roadmap의 현재성·수치 검증 범위 아님

### S37 — verified

- 카드: M01 `memory-operation/dram-cell.md`
- 원문: [S37](https://news.skhynix.com/en/how-innovative-convergence-technology-is-tackling-dram-scaling-challenges/)
- 확인 위치: DRAM scaling challenges opening; capacitor material rationale
- 대조: 셀 축소시 정전용량 유지·고유전율/저누설 필요; M01의 전하공유 산술0.55V/0.45V
- 판단: 등록 사용범위에서 지지됨; actionable finding 없음.
- 한계: 이 기사 단독으로 M01 센싱 모든 단계를 뒷받침하지 않음; 그 부분은 별도 S36. 연구를 양산 규격으로 취급 안함

### S38 — verified

- 카드: M02 `memory-operation/dram-organization.md`, M08 `memory-operation/nand-operations.md`, M10 `memory-operation/nand-retention-disturb.md`, M11 `memory-operation/ecc-codeword.md`
- 원문: [S38](https://www.micron.com/sales-support/sales/faqs)
- 확인 위치: FAQ: What is a rank; bank versus rank; READ DISTURB; ECC requirement; READ STATUS
- 대조: M02 bank/rank와8×x8=64bit; M08 program/erase status; M10 반복읽기; M11 제품별ECC
- 판단: 등록 사용범위에서 지지됨; actionable finding 없음.
- 한계: 구형 FAQ의 per512B/retire 정책/제품 수명 숫자를 모든 NAND 보편값으로 적용하지 않음

### S40 — verified

- 카드: M05 `memory-operation/ddr-transfer.md`
- 원문: [S40](https://www.kingston.com/en/support/technical/products/desktop-notebook-memory)
- 확인 위치: FAQ KTM-071015-GEN-20 DRAM frequency
- 대조: DDR2 transfers/clock, MHz와MT/s 구분; 3200MT/s×64/8=25.6GB/s
- 판단: 등록 사용범위에서 지지됨; actionable finding 없음.
- 한계: BL8/버스트는 다른 인용 S39 범위; 이번 원문은 주파수 구분만

### S42 — verified

- 카드: M09 `memory-operation/nand-multilevel.md`
- 원문: [S42](https://www.kioxia.com/en-jp/rd/technology/multi-level-cell.html)
- 확인 위치: Threshold voltage/read/write; Mechanism of capacity increases through multi-level cell technology
- 대조: 문턱전압 분포/읽기기준·bit/cell과 상태수; TLC8/QLC16·7/15경계
- 판단: 등록 사용범위에서 지지됨; actionable finding 없음.
- 한계: 상태 경계 수를 실제 페이지 읽기 횟수로 확대하지 않음; 도표 재배포 없음

### S43 — verified

- 카드: M07 `memory-operation/nand-geometry.md`, M09 `memory-operation/nand-multilevel.md`, M12 `memory-operation/ftl-gc-waf.md`
- 원문: [S43](https://www.micron.com/products/storage/nand-flash/choosing-the-right-nand)
- 확인 위치: Raw NAND; SLC/MLC/TLC/QLC; Managed NAND; On-die ECC NAND
- 대조: M07 raw/managed; M09 1/2/3/4bit; M12 controller FTL/ECC/wear management
- 판단: 등록 사용범위에서 지지됨; actionable finding 없음.
- 한계: geometry 숫자 자체는 S44와 자체 가정; bit/cell을 모든 성능·수명 보증으로 쓰지 않음

### S44 — verified

- 카드: M07 `memory-operation/nand-geometry.md`, M08 `memory-operation/nand-operations.md`, M12 `memory-operation/ftl-gc-waf.md`
- 원문: [S44](https://www.kioxia.com/content/dam/kioxia/ja-jp/business/ssd/asset/SNIA-seminar-202502.pdf)
- 확인 위치: 2025교육PDF 인쇄pp8–18: geometry, write/erase, update, GC, LBA/PBA, WL, OP
- 대조: M07 page/block·500MiB; M08 소거/업데이트 제약·70.48μs 산술; M12 주소/GC/WL/예약
- 판단: 등록 사용범위에서 지지됨; actionable finding 없음.
- 한계: 23페이지 전체 정독 아님. 본문 추출 관련절 확인; 제조 도표 복제 없이 원리 대조

### S45 — verified

- 카드: M10 `memory-operation/nand-retention-disturb.md`
- 원문: [S45](https://tw.kioxia.com/content/dam/kioxia/shared/business/memory/automotive/asset/KIOXIA_Automotive_NAND_Data_Retention_White_Paper.pdf) / [실제 취득 공식 미러](https://www.kioxia.com/content/dam/kioxia/shared/business/memory/automotive/asset/KIOXIA_Automotive_NAND_Data_Retention_White_Paper.pdf)
- 확인 위치: 2020PDF 인쇄pp3–5: Data Retention/Temperature/Wear/WAF
- 대조: 시간·P/E 산화막열화·고온 보존 저하; M10 data age와읽기 이력 구분
- 판단: 등록 사용범위에서 지지됨; actionable finding 없음.
- 한계: tw 원본 도구 접근오류; www 공식 동일제목/2020Rev1.0 PDF 확보. 제품 보증·도표 수치 전용 안함

### S46 — verified

- 카드: M11 `memory-operation/ecc-codeword.md`
- 원문: [S46](https://onlinedocs.microchip.com/oxy/GUID-FF8061A7-7A15-470F-A6F5-E733C24D85F0-en-US-11/GUID-B6C8D87D-26CF-4615-8DDA-D79C915B85CE.html)
- 확인 위치: §2.4.1.7 ECC opening and RMW/status description
- 대조: 64data+8ECC·SECDED·쓰기전 초기화; 12.5%/11.11%와 1/2bit배치 예제
- 판단: 등록 사용범위에서 지지됨; actionable finding 없음.
- 한계: 특정 Fabric DDR 구현이며 모든 메모리 동일72bit라는 주장 없음

### S47 — verified

- 카드: M05 `memory-operation/ddr-transfer.md`, M11 `memory-operation/ecc-codeword.md`
- 원문: [S47](https://www.micron.com/products/memory/dram-components/ddr5-sdram)
- 확인 위치: DDR5 versus DDR4 feature differences table: On-die ECC
- 대조: 칩 내부128b+8b SEC/RAS; M05/M11의 내부 보호와 시스템 ECC 구분
- 판단: 등록 사용범위에서 지지됨; actionable finding 없음.
- 한계: 제품 속도/용량 수치 미검토; 시스템 ECC 전체 설계 근거는 다른 출처

### S48 — verified

- 카드: M12 `memory-operation/ftl-gc-waf.md`
- 원문: [S48](https://www.kingston.com/en/support/technical/products/kc2500)
- 확인 위치: KC2500 FAQ KSD-011411-GEN-13 TRIM and garbage collection
- 대조: GC 데이터 통합과 OS TRIM 통지; 즉시 소거/보안삭제 보장 금지
- 판단: 등록 사용범위에서 지지됨; actionable finding 없음.
- 한계: 오래된 RAID 지원 일반화는 카드에 없음

### S49 — verified

- 카드: M06 `memory-operation/nand-cell.md`, M10 `memory-operation/nand-retention-disturb.md`, M12 `memory-operation/ftl-gc-waf.md`
- 원문: [S49](https://americas.kioxia.com/content/dam/kioxia/en-us/business/memory/mlc-nand/asset/KIOXIA_TBW_WAF_NAND_Endurance_Technical_Brief.pdf)
- 확인 위치: 2024Rev1.0 3pp brief: TBW/WAF; NAND Flash Memory Endurance
- 대조: M06 비전도 charge trap; M10 P/E 마모; M12 physical/logical WAF=2.5
- 판단: 등록 사용범위에서 지지됨; actionable finding 없음.
- 한계: TBW근사→수명 보증 확대 없음; 원문의 모든3D가CT라는 일반화 카드가 제한

### S50 — verified

- 카드: M11 `memory-operation/ecc-codeword.md`, M13 `memory-operation/memory-error-metrics.md`
- 원문: [S50](https://www.kingston.com/en/blog/pc-performance/enterprise-versus-client-ssd)
- 확인 위치: Reliability: raw BER paragraph and UBER definition
- 대조: ECC전RBER/ECC후복구불가 UBER; 200/10^8=2×10^-6와 요청/bit 분모 구분
- 판단: 등록 사용범위에서 지지됨; actionable finding 없음.
- 한계: 기사의 JEDEC 표/클래스별 수치를 규격 전체 읽음 또는 제품보증으로 사용하지 않음

### S51 — verified

- 카드: M08 `memory-operation/nand-operations.md`
- 원문: [S51](https://www.kernel.org/doc/html/v4.19/driver-api/mtdnand.html)
- 확인 위치: nand_sdr_timings Definition/Members tBERS_max/tPROG_max/tR_max
- 대조: block erase/page program/page read 시간 명칭과 전송시간을 분리한 예제
- 판단: 등록 사용범위에서 지지됨; actionable finding 없음.
- 한계: v4.19 API 전체나 현재 커널 환경 검증 아님

### S53 — verified

- 카드: H03 `packaging-reliability/package-interposer.md`
- 원문: [S53](https://3dfabric.tsmc.com/english/dedicatedFoundry/technology/cowos.htm)
- 확인 위치: CoWoS introduction and CoWoS-S/R/L descriptions
- 대조: 2.5D logic/HBM 통합·silicon interposer·RDL/polymer/Cu·LSI 역할
- 판단: 등록 사용범위에서 지지됨; actionable finding 없음.
- 한계: 옵션별 치수/생산능력·로드맵·실제HBM BOM 미검토

### S54 — verified

- 카드: H04 `packaging-reliability/hybrid-bonding.md`
- 원문: [S54](https://www.imec-int.com/en/articles/wafer-wafer-hybrid-bonding-pushing-boundaries-400nm-interconnect-pitch)
- 확인 위치: Promise of W2W; process flow; pitfalls; CMP/topography; SiCN
- 대조: Cu/유전체 직접접합·정렬/CMP/clean/recess/anneal; square pitch 반감4배 산술
- 판단: 등록 사용범위에서 지지됨; actionable finding 없음.
- 한계: 원문 hex-grid 연구 치수는 카드 square 가상모형과 충돌 안함; 양산HBM 규격 아님

### S56 — verified

- 카드: H06 `packaging-reliability/thermomechanical.md`
- 원문: [S56](https://www.ti.com/lit/pdf/spraa99)
- 확인 위치: SPRAA99C May2021 §3 Reliability/3.1 calculations/3.2 characteristics (인쇄pp10–12)
- 대조: CTE 불일치·warping·solder fatigue·시간/형상/물성 의존; 12ppm×100K=0.12%
- 판단: 등록 사용범위에서 지지됨; actionable finding 없음.
- 한계: 62페이지 전체 정독 아님; nFBGA 수명모델 계수/시험치를 HBM에 전용하지 않음

### S59 — verified

- 카드: H09 `packaging-reliability/stack-test-yield.md`
- 원문: [S59](https://resources.sw.siemens.com/pl-PL/white-paper-affordable-and-comprehensive-testing-of-3d-stacked-die-devices/)
- 확인 위치: 공개 소개 Design for test 3D stacking considerations
- 대조: D2D interconnect testing·KGD 재검사로 postassembly 결함 확인; q^8a≈90.43%
- 판단: 등록 사용범위에서 지지됨; actionable finding 없음.
- 한계: 공개 소개만 취득/대조. 미취득 whitepaper 본문·IEEE1838 전체를 읽지 않았음; 독립수율식은 명시적 자체예제

### S60 — verified

- 카드: H10 `packaging-reliability/failure-mechanisms.md`, H12 `packaging-reliability/reliability-metrics.md`
- 원문: [S60](https://toshiba.semicon-storage.com/content/dam/toshiba-ss-v3/master/en/semiconductor/knowledge/reliability/reliability-handbook-tdsc-en.pdf)
- 확인 위치: Apr2026Ver4 §1.1 reliability/hazard/product life/FIT; §2.1.1 TDDB/2.1.4 NBTI/2.1.5 EM
- 대조: H10메커니즘·회복/측정지연·J=10^6A/cm²; H12FIT와MTTF/MTBF 구분
- 판단: 등록 사용범위에서 지지됨; actionable finding 없음.
- 한계: 150페이지 전체 정독 아님. 가속계수/제품고장률은 전용하지 않음; CI식은 별도 인용 사항

### S62 — verified

- 카드: H12 `packaging-reliability/reliability-metrics.md`, H13 `packaging-reliability/weibull-life.md`
- 원문: [S62](https://www.itl.nist.gov/div898/handbook/apr/section4/apr412.htm)
- 확인 위치: §8.4.1.2 전체: censored likelihood and exponential MLE
- 대조: 검열 기여·r/총노출시간·작은고장수 모수불확실성; H12 2/10^6=2000FIT
- 판단: 등록 사용범위에서 지지됨; actionable finding 없음.
- 한계: Weibull식은 별도S68; 이 절이 모든 수명분포에 r/T를 허용한다고 읽지 않음

### S65 — verified

- 카드: H15 `packaging-reliability/failure-analysis.md`
- 원문: [S65](https://www.ti.com/quality-reliability/faqs/failure-analysis.html)
- 확인 위치: Failure analysis process; confirmation; non-destructive; internal/global/local isolation; conclusion
- 대조: 재현→비파괴→위치/물리증거·파괴분석 증거보존·재검사; void/open 인과 단정 금지
- 판단: 등록 사용범위에서 지지됨; actionable finding 없음.
- 한계: 특정샘플 판정/장비해상도·HBM 원인 확정 아님

### S67 — verified

- 카드: H14 `packaging-reliability/accelerated-life.md`
- 원문: [S67](https://www.itl.nist.gov/div898/handbook/apr/section2/apr24.htm)
- 확인 위치: §8.2.4 전체
- 대조: 실패모드/스트레스에맞는모형·CoffinManson 피로·가정과적합확인
- 판단: 등록 사용범위에서 지지됨; actionable finding 없음.
- 한계: Arrhenius수치≈77.65는 카드자체가정; 원문이 모든스트레스에 같은AF 허용 안함

### S73 — verified

- 카드: D04 `data-application/spc.md`, D07 `data-application/time-alignment.md`, D11 `data-application/anomaly-drift.md`
- 원문: [S73](https://www.itl.nist.gov/div898/handbook/ppc/section4/ppc45.htm)
- 확인 위치: §3.4.5 전체
- 대조: 시간순서·constant mean/variance/distribution·자기공분산과 안정성; D04/D07/D11 한계
- 판단: 등록 사용범위에서 지지됨; actionable finding 없음.
- 한계: 시점누수 계약/알람병합은 자체 적용, NIST가 해당 구현을 처방했다는 주장 없음

### S74 — verified

- 카드: D06 `data-application/root-cause.md`
- 원문: [S74](https://www.itl.nist.gov/div898/handbook/pri/section3/pri33.htm)
- 확인 위치: §5.3.3 Objectives/Design Selection Guideline 전체
- 대조: 비교·screening·interaction/RSM 목적별선택; D06 교란 역전산술
- 판단: 등록 사용범위에서 지지됨; actionable finding 없음.
- 한계: 실제제조DOE 수행·랜덤배정 보장 아님

### S79 — verified

- 카드: D11 `data-application/anomaly-drift.md`
- 원문: [S79](https://scikit-learn.org/stable/modules/outlier_detection.html)
- 확인 위치: §2.7 introduction; threshold/contamination; LOF novelty warning
- 대조: 오염학습outlier와정상학습novelty 구분·contamination 임계값; D11 이벤트분모
- 판단: 등록 사용범위에서 지지됨; actionable finding 없음.
- 한계: 개별알고리즘성능·확률보정 검증 아님; 점수는 고장확률이 아님

### S80 — verified

- 카드: D01 `data-application/grain-join.md`
- 원문: [S80](https://scikit-learn.org/stable/modules/impute.html)
- 확인 위치: §8.4 intro/univariate; Keeping features constant; MissingIndicator; train/test example
- 대조: 결측추론·전부결측열·indicator·학습통계 적용; D01 라벨결측 정상대치 금지
- 판단: 등록 사용범위에서 지지됨; actionable finding 없음.
- 한계: join semantics는 S69 사항. 현 stable1.9.1로 읽었으나 코드실행 환경 버전 보증 없음

### S81 — verified

- 카드: D05 `data-application/capability-measurement.md`
- 원문: [S81](https://www.itl.nist.gov/div898/handbook/mpc/section4/mpc4.htm)
- 확인 위치: §2.4 Gauge R&R study index and listed dimensions
- 대조: repeatability/reproducibility/stability/bias·operator/artifact/gauge 조건; D05 측정변동 구분
- 판단: 등록 사용범위에서 지지됨; actionable finding 없음.
- 한계: 하위장 전체·개별GRR분산공식 미독; Cp/Cpk는 S72 별도범위

### S82 — verified

- 카드: D06 `data-application/root-cause.md`
- 원문: [S82](https://www.itl.nist.gov/div898/handbook/eda/section3/scatterp.htm)
- 확인 위치: §1.3.3.26 Purpose/Questions/Combining/Causality
- 대조: 관계·비선형·산포·조건부부분집합·association≠causality; Simpson 예제산술
- 판단: 등록 사용범위에서 지지됨; actionable finding 없음.
- 한계: 산점도 자체가공정원인을 증명하지 않는 제한과 일치

### S83 — verified

- 카드: D09 `data-application/classification.md`, D12 `data-application/task-workflow.md`
- 원문: [S83](https://scikit-learn.org/stable/modules/generated/sklearn.dummy.DummyClassifier.html)
- 확인 위치: DummyClassifier class opening, strategy list and example
- 대조: 특징무시기준선·majority/constant 역할; D09정확도99% recall0, D12기준선절차
- 판단: 등록 사용범위에서 지지됨; actionable finding 없음.
- 한계: 전체API정독아님. metrics공식은 S78 별도; 실제성능 주장 없음
