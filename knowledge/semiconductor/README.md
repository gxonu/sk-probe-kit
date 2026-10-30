# 반도체 지식 패키지 — 해커톤 환경용

현재 **1–5단계 전체**를 제공한다. 확인일: 2026-10-30.
기초 11개·소자/공정 14개·메모리 동작 13개·HBM/패키징/신뢰성 15개·데이터 적용 12개,
총 65개 개념에 공개 1차 자료 84개의 출처를 연결했다.
이는 공개 기초 지식이며 SK하이닉스의 출제 내용·채점 기준·내부 공정 자료가 아니다.

문제를 받으면 [실제 과제 적용 순서·입력 프롬프트·통합 검증](application-playbook.md)에서 시작한다.

## 제공 Codex가 사용하는 순서

1. 실제 과제 README·데이터 설명·업무 답변에서 모르는 용어, 단위, 측정 조건을 추출한다.
2. 이 폴더의 `index.jsonl`에서 `title`, `aliases`, `keywords`, `problem_signals`를 찾아 관련 ID를 고른다.
3. `path`가 가리키는 본문을 읽는다. 모든 경로는 **이 README가 있는 폴더 기준**이다.
   필요한 경우 `prerequisites`의 ID를 다시 색인에서 찾아 읽는다.
4. 본문의 원리·공식 적용 조건·혼동 항목을 확인한다. 예제 숫자를 실제 제품 사양으로 사용하지 않는다.
5. 과제에서 받은 사실을 우선한다. 일반 지식과 충돌하면 의미·측정 조건부터 확인한다.
   데이터만으로 원인을 확정할 수 없으면 가설로 남기고 판별할 관찰을 제안한다.
6. 사용한 ID·가정·단위·실제 검증 결과를 과제의 근거 문서에 기록한다.
   하네스가 설치됐다면 `.harness/task-evidence.md`에 연결한다.

반입한 저장소의 본문·색인만으로 조회할 수 있다. 별도 설치·API·임베딩·네트워크 검색은 필요 없다.
터미널에 `rg`가 있으면 아래처럼 검색할 수 있고, 없어도 제공 Codex의 파일 읽기로 색인을 조회한다.

```bash
# 반입한 하네스 저장소 루트에서 실행하는 조회 예시
rg -n -i '정전용량|capacitance|fF' knowledge/semiconductor/index.jsonl
```

하네스 설치기는 이 지식 폴더를 과제 루트로 복사하지 않는다. **반입 저장소를 유지**하고,
현재 세션에서 확인한 지식 폴더 경로를 과제 진행 문서에 적어 새 세션에서도 찾게 한다.
단순 지식 갱신은 반입 저장소에서 pull한 파일을 다시 읽으면 된다. 하네스 설정 갱신은 루트 README의 재설치 절차를 따른다.

## 질문으로 빠르게 찾기

| 문제에서 보인 표현 | 먼저 읽을 ID |
| --- | --- |
| 전류·전압·센서 단위 | F01, F02 |
| 전하 저장·커패시턴스·fF | F03 |
| W와 J·소비전력·에너지 효율 | F04 |
| 밴드갭·전자·정공 | F05 |
| donor·acceptor·n형·p형·농도 | F06 |
| Gb/GB/GiB·용량 환산 | F07 |
| 클록·MHz·주기·논리 | F08 |
| wafer/die/chip·집계 단위 | F09 |
| DRAM/SRAM/NAND·전원 차단 | F10 |
| 대역폭·지연·처리량 | F11 |
| PN·공핍층·역바이어스 | P01 |
| VGS·Vth·문턱전압·포화 | P02 |
| CMOS·동적 전력·활성도 | P03 |
| FEOL/MOL/BEOL·공정 이력·재작업 | P04 |
| 산화막·열산화·성장률 | P05 |
| PVD/CVD/ALD·GPC·단차피복성 | P06 |
| PR·노광·현상·노광 dose | P07 |
| 식각·선택비·undercut | P08 |
| 주입 dose·농도·활성화·어닐링 | P09 |
| CMP·평탄도·제거율 | P10 |
| via/contact·배선 저항·open/short | P11 |
| CD·overlay·결함 검출 | P12 |
| EPM·wafer test·bin·retest | P13 |
| 세정·particle·잔사 | P14 |
| 1T1C·sense amplifier·셀 복원 | M01 |
| channel/rank/bank·row hit | M02 |
| tRCD/tRP/tRAS·CL·첫 데이터 지연 | M03 |
| refresh·tREFI/tRFC·retention | M04 |
| MT/s·버스트·버스 폭·대역폭 | M05 |
| NAND·floating gate/charge trap·문턱전압 | M06 |
| page/block·geometry·물리 용량 | M07 |
| program/erase·상태 확인·NAND 지연 | M08 |
| SLC/MLC/TLC/QLC·상태 수 | M09 |
| NAND retention·read disturb·P/E 이력 | M10 |
| ECC·SECDED·codeword·on-die | M11 |
| FTL·GC·TRIM·WAF | M12 |
| RBER/UBER·오류 수·노출량 | M13 |
| HBM·스택·다이 수·대역폭 | H01 |
| TSV·박막화·체인 저항 | H02 |
| 2.5D/3D·interposer·RDL | H03 |
| microbump·hybrid bonding·Cu-Cu | H04 |
| MR-MUF·TC-NCF·underfill·void | H05 |
| CTE·warpage·delamination·피로 | H06 |
| θJA/θJC/ΨJT·접합온도·hotspot | H07 |
| PDN·IR drop·ESR/ESL·전압 변동 | H08 |
| KGD·D2D·적층 수율·검사 범위 | H09 |
| EM·TDDB·NBTI·열화 | H10 |
| HTOL·HTSL·TC·BHAST·ESD HBM | H11 |
| FIT·MTTF·검열·무고장 신뢰상한 | H12 |
| Weibull·β/η·특성수명 | H13 |
| Arrhenius·AF·활성화에너지·수명 환산 | H14 |
| FA·X-ray·SAM·불량 원인 증거 | H15 |
| 행 단위·키·join·중복·결측 | D01 |
| 수율·FPY·retest·가중 집계 | D02 |
| 불량 개체/결함 수·Wilson·신뢰구간 | D03 |
| SPC·p 관리도·UCL/LCL | D04 |
| Cp/Cpk·규격·gauge R&R | D05 |
| 원인 분석·교란·DOE·wafer map | D06 |
| event_time/available_at·시간 결합·센서 | D07 |
| GroupKFold·시간 분할·data leakage | D08 |
| 희소 불량·precision/recall/F1·임계값 | D09 |
| MAE/RMSE·잔차·연속값 예측 | D10 |
| novelty/outlier·drift·알람 이벤트 | D11 |
| 기준선·실행 근거·제출·재현 | D12 |

## 파일 안내

- [과제 적용 순서·검증 실행](application-playbook.md)
- [단계별 범위·읽기 지도](curriculum.md)
- [검색 메타데이터](index.jsonl): 한 줄에 한 개념, UTF-8 JSON
- [메타데이터 계약](metadata.md)
- [출처 목록](sources.json): 확인 날짜·자료 사용 범위
- [검증 기록](VALIDATION.md)
- [Sol + Sol 독립 검토·수정 기록](reviews/2026-10-30/README.md)
- [추가58개 원문 대조·유전율 보강·현재84개 출처 범위](reviews/2026-10-30-remaining-sources/README.md)

출처 원문·그림·강의 파일을 재배포하지 않고 짧은 자체 요약과 링크를 제공한다.
예제·질문은 자체 작성이다. 제품별 최신 수치·실제 공정 레시피는 포함하지 않는다.
원문이 초급 설명을 위해 단순화한 표현도 실제 보증 조건으로 확대하지 않는다.
