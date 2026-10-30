# TSV·수직 연결·박막화

ID: `H02` · 단계 4 · 출처 확인: 2026-10-30

TSV는 실리콘을 관통하는 전기 경로이며 다이 사이 접합과는 다른 구조 요소다.

## 원리·구조와 메커니즘

실리콘 내부의 수직 연결, 다이 표면의 접합부, 재배선 경로를 구분한다. 박막화와 TSV 치수는 연결 길이·적층 높이에 관련되지만 공정 손상과 조립 수율도 함께 본다.

## 지표·공식과 적용 조건

원통형 균일 도체 근사 R=ρL/(πr²), 종횡비=L/직경. 접촉 저항·라이너·기생 성분을 생략한 모델이다. 연결 체인의 저항은 TSV만의 저항이 아닐 수 있다.

## 직접 만든 적용 예제

가상 길이 50 μm·직경 5 μm이면 종횡비 10이다. ρ=2×10⁻⁸ Ωm인 꽉 찬 원통 도체 근사에서는 약0.05093 Ω다.

## 혼동·적용 한계

TSV가 정상이어도 접합부가 끊길 수 있고 반대도 가능하다. 하이브리드 본딩이 모든 구조에서 TSV 자체를 없애는 것은 아니다. 체인 fail만으로 고장 위치를 확정하지 않는다.

## 과제에서 확인할 질문

- 측정 경로에 TSV·범프·배선이 각각 몇 개 포함됐는가?
- 박막화 전후 검사·기생 성분·접촉 저항을 분리했는가?

## 출처

- [S52: SK hynix — Creating New Values in DRAM Using Through-Silicon-Via Technology for Continued Scaling in Memory System Performance and Capacity](https://news.skhynix.com/en/creating-new-values-in-dram-using-through-silicon-via-technology-for-continued-scaling-in-memory-system-performance-and-capacity/)
- [S33: OpenStax — Resistivity and Resistance](https://openstax.org/books/university-physics-volume-2/pages/9-3-resistivity-and-resistance)

원리는 공개 출처를 자체 요약했다. 예제·질문은 교육용 작성이며 실제 출제 문제·HBM 제품 사양·공정 레시피·수명 보증값이 아니다.
