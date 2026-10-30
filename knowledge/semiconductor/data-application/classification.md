# 희소 불량 분류·오탐·미탐·임계값

ID: `D09` · 단계 5 · 출처 확인: 2026-10-30

불량을 양성으로 정의하고 혼동행렬·임계값·평가 모집단을 함께 보고한다.

## 원리·적용 절차

precision은 검출한 것 중 진짜 불량 비율, recall은 불량 중 검출 비율이다. 정확도와 순위 지표만으로 실제 운영점의 오탐/미탐을 알 수 없다.

## 지표·공식과 적용 조건

precision=TP/(TP+FP), recall=TP/(TP+FN), F1=2TP/(2TP+FP+FN). 분모0 처리 규칙을 적는다. AP와 사다리꼴 PR 면적은 동일하다고 가정하지 않는다.

## 직접 만든 적용 예제

가상1000개 중 불량10개에서 TP=8, FP=12, FN=2, TN=978이면 precision40%, recall80%, F1≈0.5333, accuracy98.6%. 모두 정상이라는 기준선은 정확도99%지만 recall0%.

## 혼동·적용 한계

임계값은 validation에서 비용·검사 용량·과제 지표로 정한다. test에서 맞추지 않는다. oversampling 뒤의 인공 클래스 비율로 운영 precision을 주장하지 않는다.

## 과제에서 확인할 질문

- 양성 정의·임계값·분모0 규칙이 평가기와 같은가?
- 불량을 놓치는 비용과 추가 검사 용량이 정의됐는가?

## 출처

- [S78: scikit-learn — Metrics and scoring: quantifying the quality of predictions](https://scikit-learn.org/stable/modules/model_evaluation.html)
- [S83: scikit-learn — DummyClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.dummy.DummyClassifier.html)

공개 방법론을 자체 요약하고 반도체 데이터에 적용하는 절차·예제를 작성했다. 예제는 합성 자료이며 실제 출제·채점 기준·제조 데이터·검증 성능을 뜻하지 않는다.
