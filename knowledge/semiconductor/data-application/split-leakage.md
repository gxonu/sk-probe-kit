# 학습 분할·그룹·미래 검증·누수

ID: `D08` · 단계 5 · 출처 확인: 2026-10-30

실제 새 데이터의 형태에 맞춰 분할을 먼저 정하고 전처리와 선택을 그 안에서 수행한다.

## 원리·적용 절차

새 lot 일반화는 lot 분리, 미래 생산 예측은 시간 분리를 고려한다. 두 조건이 필요하면 동시에 검증한다. 평균 대치·표준화·특징 선택·재표본추출은 각 학습 fold에만 적합한다.

## 지표·공식과 적용 조건

검사할 조건: 그룹 교집합 공집합(새 그룹 평가일 때), 학습의 정답 가용 시각≤모델 학습 마감, 검증 예측 시각>학습 마감. 겹치는 목표 기간·특징 창은 과제에 맞게 간격/제외를 둔다.

## 직접 만든 적용 예제

가상 train lot A/B, validation lot C, test lot D로 분리하고 시점도 순서대로 둔다. B의 다른 die를 validation에 넣으면 새 lot 성능을 평가하지 못한다. 같은 장비의 미래를 예측하는 과제에서는 장비 재등장이 항상 누수인 것은 아니다.

## 혼동·적용 한계

그룹 분리만으로 시간 순서가 보장되지 않고 시간 분리만으로 그룹 분리가 보장되지 않는다. 최종 test로 임계값·특징·모델을 반복 선택하지 않는다. 양성 없는 fold에서는 정의 불가능한 지표를 명시한다.

## 과제에서 확인할 질문

- 새 lot·새 장비·미래 시점 중 무엇으로 일반화하는가?
- 분할 후에도 전처리·정답 지연·중복 샘플 누수가 없는가?

## 출처

- [S76: scikit-learn — Common pitfalls and recommended practices](https://scikit-learn.org/stable/common_pitfalls.html)
- [S77: scikit-learn — Cross-validation: evaluating estimator performance](https://scikit-learn.org/stable/modules/cross_validation.html)

공개 방법론을 자체 요약하고 반도체 데이터에 적용하는 절차·예제를 작성했다. 예제는 합성 자료이며 실제 출제·채점 기준·제조 데이터·검증 성능을 뜻하지 않는다.
