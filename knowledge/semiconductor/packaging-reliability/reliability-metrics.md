# 고장률·FIT·MTTF·무고장 신뢰한계

ID: `H12` · 단계 4 · 출처 확인: 2026-10-30

신뢰도는 시간에 따른 생존 확률이며 FIT와 무고장 관측은 조건·모형·노출량을 포함해 해석한다.

## 원리·구조와 메커니즘

일정 hazard λ의 지수모형에서 R(t)=exp(−λt), MTTF=1/λ. FIT는 λ[h⁻¹]×10⁹이다. MTBF는 수리 가능한 시스템 맥락의 지표이므로 단품 수명을 자동 대체하지 않는다.

## 지표·공식과 적용 조건

같은 조건의 독립 관측에서 λ 추정값=r/총 노출시간 T. 고장 전 시간·중도 종료된 생존 관측을 포함하고 고장 뒤 시간을 더하지 않는다. 고정시간 무고장 시험의 단측 (1−α) 신뢰상한은 λ_U=−ln(α)/T다.

## 직접 만든 적용 예제

가상 총 10⁶ device·h에서 2고장이면 2000 FIT. 이 일정 hazard 모형의 R(1000 h)≈0.998002다. 별개 시험에서 같은 노출량에 0고장이라면 단측95% 상한은 약2995.73 FIT다.

## 혼동·적용 한계

0고장을 고장률0 또는 무한 수명 보증으로 쓰지 않는다. 시험 중단 규칙·독립성·일정 hazard 가정을 확인한다. 가속시험의 노출시간을 사용 조건 노출시간에 검증 없이 합치지 않는다.

## 과제에서 확인할 질문

- 고장 수와 샘플별 고장/검열 시간이 있는가?
- 추정값인가 신뢰상한인가, 신뢰수준·사용 조건이 같은가?

## 출처

- [S60: Toshiba — Reliability Handbook (Apr 2026 Ver.4)](https://toshiba.semicon-storage.com/content/dam/toshiba-ss-v3/master/en/semiconductor/knowledge/reliability/reliability-handbook-tdsc-en.pdf)
- [S62: NIST/SEMATECH — Maximum likelihood estimation](https://www.itl.nist.gov/div898/handbook/apr/section4/apr412.htm)
- [S63: NIST/SEMATECH — Constant repair rate (HPP/exponential) model](https://www.itl.nist.gov/div898/handbook/apr/section4/apr451.htm)
- [S66: NIST/SEMATECH — Exponential](https://www.itl.nist.gov/div898/handbook/apr/section1/apr161.htm)

원리는 공개 출처를 자체 요약했다. 예제·질문은 교육용 작성이며 실제 출제 문제·HBM 제품 사양·공정 레시피·수명 보증값이 아니다.
