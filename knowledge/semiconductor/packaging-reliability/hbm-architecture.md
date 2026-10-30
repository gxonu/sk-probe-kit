# HBM 적층·용량·대역폭

ID: `H01` · 단계 4 · 출처 확인: 2026-10-30

HBM은 DRAM 적층과 넓은 병렬 인터페이스로 용량과 데이터 전송 경로를 구성한다.

## 원리·구조와 메커니즘

코어 DRAM 다이의 수와 다이당 용량, 스택의 데이터 I/O 폭·핀당 전송률을 따로 본다. base die를 저장 DRAM 다이와 동일하게 세지 않는다. 내부 DRAM의 행 접근·리프레시 제약도 남는다.

## 지표·공식과 적용 조건

저장 용량=코어 다이당 bit×코어 다이 수/8. 스택 피크 대역폭=핀당 bit/s×payload I/O 수/8. 여러 스택의 합은 독립 경로가 모두 사용될 때의 이론 합이다.

## 직접 만든 적용 예제

가상 16 Gibit 코어 8개는 16 GiB다. 1024 bit 폭·핀당 4 Gbit/s이면 512 GB/s, 독립 스택 4개의 합은 2.048 TB/s다. 8개 적층 수를 대역폭에 다시 곱하지 않는다.

## 혼동·적용 한계

세대별 I/O 폭·채널 구성을 고정하지 않는다. 이 수치는 특정 HBM의 사양이 아니다. 스택 추가·높이 증가만으로 지연·앱 속도가 비례 개선되는 것은 아니다.

## 과제에서 확인할 질문

- 용량 표기의 Gb/Gibit·GB/GiB 기준은 무엇인가?
- 대역폭이 핀·채널·스택·전체 시스템 중 어느 기준인가?

## 출처

- [S52: SK hynix — Creating New Values in DRAM Using Through-Silicon-Via Technology for Continued Scaling in Memory System Performance and Capacity](https://news.skhynix.com/en/creating-new-values-in-dram-using-through-silicon-via-technology-for-continued-scaling-in-memory-system-performance-and-capacity/)

원리는 공개 출처를 자체 요약했다. 예제·질문은 교육용 작성이며 실제 출제 문제·HBM 제품 사양·공정 레시피·수명 보증값이 아니다.
