# 독립 검토 A — 수정 영향 범위 재검토

모델: gpt-6.1-sol. 검토일: 2026-10-30.
검토 대상: `/Users/kty/Documents/ChatGPT/sk-hynix-hackathon/tmp/semiconductor-sol-sol-review/revised`의 고정 사본.
기준 커밋: `731eecb0acf12f2d65f045c87a6a51889ea1dbd5`.
패치 SHA256: `1bfcadd87156adedab8dbed3482c1a11c90160efbae6fa34e5bd40bcfc0e57ad`.

## 판정

**A-01, A-O1, A-O2는 해소됐다.** 부모가 전달한 B-02의 희소 SPC 지적, B-01의 검사 범위 설명도 수정 문구와 실제 코드 기준으로 해소된 것으로 판단한다. B의 초기 보고서나 재검토 보고서는 읽지 않았다. 이번 영향 범위에서 신규 기술 오류·미해결 항목은 발견하지 못했다.

## 실제 확인

- fixes.diff 전체를 읽고 revision-manifest.json의 패치 SHA256 및 변경 파일 7개의 SHA256을 직접 계산해 전부 일치함을 확인했다.
- 수정 F11/H07/D04 본문과 F11 색인, application_checks.py, application-playbook.md를 읽었다. 루트 README의 수정 검증 설명과 주변 문맥도 확인했다.
- `python3 -I knowledge/semiconductor/verify.py`를 revised 루트에서 실행했다. 65 cards, 83 sources, 62 retrieval routes, 91 numeric checks와 **15 synthetic application tests** 모두 PASS(종료 코드0).
- 검증 코드와 별개의 Python 산술로 F11 및 SPC 수치를 재계산했다. 원래 A-01 반례 D=100MB, L=1s, B_stream=100MB/s도 다시 확인했다: 총2s, B_obs=50MB/s, 잘못된 초기 지연 재가산은3s다.

## 항목별 결과

| 항목 | 상태 | 확인한 수정과 근거 |
|---|---|---|
| A-01 / F11 P2 | 해소 | 13행에서 B_obs=D/t_total과 B_stream을 구별하고 `t_total≈L+D/B_stream`, 초기 지연 재가산 금지를 명시했다. 17행은 100MB/2GB/s=0.05s, L=.01s를 더한 총.06s, B_obs≈1.667GB/s, 잘못된.07s를 구분한다. 새 회귀 검사는 이 관계를 수치로 검사하고 해당 본문 기호/예제에 제한적으로 연결한다. |
| A-O1 / H07 P3 | 해소 | 21행에 TI §3.2의 방열판 적용 시 ΨJT 사용 제한을 직접 적고, 콜드플레이트 등 상부 열경로가 바뀔 때 해당 구성의 모델·측정값을 확인하도록 했다. 이전 원문 대조의 조건과 일치한다. |
| A-O2 및 전달된 B-02 / D04 P3 | 해소 | 17행에서 np0=2인 희소 예제임을 밝혔으며 상한 초과 정수 경계 D≥7, 정확 이항 확률.004062, 정규 상측3σ 확률.00135가 다름을 적었다. 목표 오경보율을 보장하지 않는다는 주의도 추가했다. 별도 계산 결과 UCL=.062, 최소 초과7개, 이항 꼬리=.0040620540801008355, 정규 꼬리=.0013498980316300957로 일치했다. |
| 전달된 B-01 / 검사 범위 P3 | 해소 | 가이드와 루트 README가 91개를 코드에 고정한 교육용 fixture로 명시하고, 본문 숫자 전체의 자동 대조가 아님을 밝혔다. 일부 예제 문자열만 연결한다는 설명도 실제 구현과 맞다. 합성 검사15개 표기와 실행 개수가 일치한다. |

## 출처 조건 및 한계

이번에는 신규 웹 원문 조회를 하지 않았다. 초기 A 검토에서 실제 읽은 다음 근거를 **재사용**했다: [S13 Intel의 대역폭/지연 정의](https://www.intel.com/content/www/us/en/developer/articles/technical/memory-performance-in-a-nutshell.html), [Argonne의 지연+크기/속도 모델](https://www.mcs.anl.gov/research/projects/mpi/tutorial/perf/mpiperf/tsld034.htm), [S57 TI SPRA953D §3.2](https://www.ti.com/lit/pdf/spra953), [S71 NIST의 독립 이항 p 관리도](https://www.itl.nist.gov/div898/handbook/pmc/section3/pmc332.htm). 초기 보고서의 원문 대조 범위21개를 이번에 새로 조회한 것으로 세지 않는다.

수정된 7개 파일과 해당 계산·검증 설명에 대한 집중 재검토다. 65개 본문 전체를 이번 단계에서 다시 읽거나 83개 원문을 재검증한 것은 아니다. 초기 전수 읽기 결과와 미확인 범위는 review-a.md가 정본이다. 본문 토큰 검사는 의미 전체의 자동 증명이 아니며 가이드도 그 한계를 정확히 밝힌다. 실제 Probe·실제 데이터·제품 시험은 수행하지 않았다.

루트 README의 재검토 진행 중 문구와 부모가 생성할 최종 리뷰 링크는 출판 마무리 범위로 남겨 두었다. 이 집중 기술 검토의 차단 항목으로 세지 않았다. revised·라이브 저장소는 수정하지 않았으며 이 보고서만 작성했다.

## 확인한 변경 파일 해시

| 파일 | SHA256 |
|---|---|
| `README.md` | `7397bfb36083872a78cffd9ace30a491bae0f1a3cf5998976db6d555529d5a7e` |
| `knowledge/semiconductor/application-playbook.md` | `f607038091c09a7b9d0c6e8e0159d79d112ec8d4efbf2a615dbbb1c18cbd45ce` |
| `knowledge/semiconductor/checks/application_checks.py` | `9e4bd95564ac6cffcef530b2949e6f6bc79f70c9fd5a6b564274d602255feb61` |
| `knowledge/semiconductor/data-application/spc.md` | `9548900af4ce2860fc8ec0a6371dc491285b25d1cee892a4e6c073474c1dad1a` |
| `knowledge/semiconductor/fundamentals/capacity-bandwidth-latency.md` | `ef3c65e5c37910e2beb0e2b0d85b569cb829d4e731e497bca8d9e3d5b403db53` |
| `knowledge/semiconductor/index.jsonl` | `26cb7aa27b59fd4c2b860f0b01dc941dce66ead243184e8f7498aa3a35dde4cb` |
| `knowledge/semiconductor/packaging-reliability/thermal-metrics.md` | `e894657faec178a738b4fd53df1fe473cef81082a8fd65673ea73c588585154f` |
