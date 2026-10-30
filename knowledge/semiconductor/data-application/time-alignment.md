# 장비 시계열·가용 시점·시간 결합

ID: `D07` · 단계 5 · 출처 확인: 2026-10-30

예측 시점에 실제로 사용할 수 있었던 센서·검사 정보만 연결한다.

## 원리·적용 절차

측정 발생 시각과 수집/판정 완료 시각을 구분하고 시간대·clock offset·chamber·공정 단계 키를 맞춘다. 과거 방향 결합에도 최대 허용 경과시간과 가용 시점 조건이 필요하다. 공정 단계별 구간을 보존한다.

## 지표·공식과 적용 조건

특징에 포함할 관측은 event_time≤prediction_time 및 available_at≤prediction_time을 만족해야 한다. window의 열린/닫힌 경계·단위·샘플링 주기를 정의한다. 불규칙 샘플 평균과 시간 가중 평균은 다르다.

## 직접 만든 적용 예제

가상 예측10:00에서 09:58 측정·10:02 도착값은 제외한다. 09:55 측정·09:56 도착값은 허용 경과시간 안이면 사용할 수 있다. nearest가10:01 미래값을 선택하면 예측 입력으로 부적절하다.

## 혼동·적용 한계

미래값을 이용한 보간·centered rolling·전체 run 완료 후 통계를 실시간 특징으로 사용하지 않는다. 결측과 장비 정지를 구분한다. 긴 빈 구간을 무제한 forward fill하지 않는다.

## 과제에서 확인할 질문

- 예측할 순간에 값과 검사 정답이 실제 공개됐는가?
- 공정 단계·그룹·허용 시간차·window 경계를 명시했는가?

## 출처

- [S75: pandas — pandas.merge_asof](https://pandas.pydata.org/docs/reference/api/pandas.merge_asof.html)
- [S73: NIST/SEMATECH — Assessing Process Stability](https://www.itl.nist.gov/div898/handbook/ppc/section4/ppc45.htm)

공개 방법론을 자체 요약하고 반도체 데이터에 적용하는 절차·예제를 작성했다. 예제는 합성 자료이며 실제 출제·채점 기준·제조 데이터·검증 성능을 뜻하지 않는다.
