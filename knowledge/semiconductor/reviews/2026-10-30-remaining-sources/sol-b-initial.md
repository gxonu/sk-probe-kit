# 잔여 58개 출처 독립 원문 대조 B

대상: frozen commit `9dab381bcccfc70d9c6596e13efff9d1879a2a0a`의 snapshot과 targets.json. A 보고서·라이브 저장소·기존 source 보고서를 결론에 사용하지 않았다. 모든 58개 canonical 원문에 실제 GET/web open을 수행해 본문/공개 초록/PDF 지정 페이지를 읽고, 각 연결 카드 전체 문장·가정·자체 예제를 대조했다. 원문 내용을 대량 복제하지 않고 판단만 기록했다.

57 verified, 1 partial(S03: 원문 접근 성공, 유전체 확장 부분의 인용·기호 설명 보강 필요). unavailable 0. verified는 등록 used_for와 해당 원문 구간 확인을 뜻하며 출판물 전체·현행 제품 검증이나 모든 교육용 체크리스트의 직접 출처 보증을 뜻하지 않는다. PDF는 메모리에서 추출해 관련 전체 페이지를 확인했고 원문 도표를 재배포하지 않았다. 원문에 동일한 자체 숫자 예제가 없어도 원리와 가정에서 타당하게 도출되면 오류로 판정하지 않았다.

## 수정 후보

### [P3] 절대 유전율과 상대 유전율을 구분하도록 기호를 정의

- 위치: `knowledge/semiconductor/fundamentals/capacitance.md:13` (F03), 출처 S03.
- 원문: OpenStax §8.1 Parallel-Plate Capacitor는 진공의 ε0(F/m)로 C=ε0A/d를 유도한다. 카드의 C=εA/d는 균일 선형 유전체의 올바른 확장이지만 ε의 정의·단위를 주지 않고 등록 출처도 §8.1뿐이다.
- 결과: 초기 학습자가 자료의 무차원 dielectric constant를 ε에 직접 넣으면 계산이 잘못된다. 이는 공식 자체의 사실 오류가 아니라 기호·인용 범위의 작은 누락이다. 카드의20fF×1V=20fC 예제는 올바르다.
- 권고: ε=κ ε0인 절대 유전율(F/m), κ는 무차원 상대 유전율임을 한 문장으로 명시하고 A[m²],d[m]를 표시한다. 같은 출판사 [§8.4 Capacitor with a Dielectric](https://openstax.org/books/university-physics-volume-2/pages/8-4-capacitor-with-a-dielectric)의 C=κC0 원문도 실제 확인했으므로 보강 인용할 수 있다. §8.5의 dielectric constant 정의도 확인했다.

그 외 필수 수정급 기술 오류나 현재 학습 범위의 중요한 누락은 발견하지 못했다. 원문의 과도한 단순화(역전류0,0.7V switch,매증착CMP,100%활성화,영구보존)를 카드가 적절히 제한한다. 고급실라버스 추가를 요구하지 않는다.

## 접근·범위 제한

- S34, S40, S48, S50은 requests403 후 web로 동일 publisher canonical 본문을 회복했다. 단순200 응답을 확인 완료 근거로 쓰지 않았다.
- S27은 공개 NIST abstract에 CD/overlay 정의가 직접 있어 그 용도로만 확인. 발표 전문 미열람. S59는 공개 Siemens 소개의 KGD 재검사·D2D검사만 읽었으며 whitepaper 전문·IEEE1838 내용을 읽었다고 하지 않는다.
- S06/S07의 짧은 FAQ는 donor/acceptor 예시를 직접 지원하지만 보상도핑·불완전이온화는 상세 설명하지 않는다. 카드의 타당한 추가 주의를 곧바로 과학 오류로 판정하지 않았다. 같은 원칙으로 time alignment/event alarm/식별키 등 자체 적용 절차를 원문 문장과 구분했다.
- PDF: S44 pp8–18, S45 pp3–5, S49 pp1–3, S56 pp10–12 §3, S60 §1.1 FIT/life 및 §2.1 TDDB/NBTI/EM의 관련 페이지. 문서 전체를 읽었다는 주장은 하지 않는다.

## 58개 전수 범위

정확한 canonical/retrieved URL, 읽은 위치, 연결 카드, 대조한 주장, 개별 한계는 `coverage-b.json`의58개 행을 기준으로 한다. 아래는 누락 방지를 위한 ID 목록이다.

- 기초: S01, S02, S03, S04, S05, S06, S07, S09, S10, S11, S12, S14, S15
- 공정: S18, S19, S20, S21, S22, S23, S24, S25, S27, S28, S29, S30, S31, S32, S33, S34, S35
- 메모리 및 인터포저: S37, S38, S40, S42, S43, S44, S45, S46, S47, S48, S49, S50, S51, S53
- 패키징·신뢰성·데이터: S54, S56, S59, S60, S62, S65, S67, S73, S74, S79, S80, S81, S82, S83
