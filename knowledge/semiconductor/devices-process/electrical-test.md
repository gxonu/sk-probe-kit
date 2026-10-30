# 전기적 검사·EPM·웨이퍼 테스트

ID: `P13` · 단계 2 · 출처 확인: 2026-10-30

전기적 검사는 전압·전류·신호를 주고 소자 특성이나 기능이 정한 조건을 만족하는지 확인한다.

## 원리·공정 역할

EPM은 트랜지스터·접촉 저항 같은 기본 특성으로 공정에 피드백을 준다. 웨이퍼 테스트는 개별 다이, 패키지 테스트는 조립된 제품을 대상으로 한다. test·repair·retest의 세부 구성은 제품별로 다르다.

## 지표·공식과 적용 조건

판정에는 test item·limits·온도·전압·프로그램 버전이 필요하다. bin 번호는 보편 불량 코드가 아니므로 mapping을 확인한다. 합격률은 대상 다이 수와 재시험 처리 규칙을 명시한다.

## 직접 만든 적용 예제

첫 시험 100개 중 90개 pass, 재시험 후 같은 100개 중 최종 95개 pass라면 최초 합격률 90%, 최종 95%다. 시험 로그 행 수를 분모로 쓰지 않는다.

## 혼동·적용 한계

외관 결함과 전기적 fail은 같은 라벨이 아니다. pass는 실시한 검사 조건의 통과이며 모든 수명·환경에서 무결함을 뜻하지 않는다. 과제의 Probe 플랫폼과 probe card는 다른 용어다.

## 과제에서 확인할 질문

- first-pass/final-pass 중 어떤 기준인가?
- bin 정의·retest·repair 이력과 유일한 die 키가 있는가?

## 출처

- [S29: SK hynix — Semiconductor Back-End Process Episode 1: Understanding Semiconductor Testing](https://news.skhynix.com/en/semiconductor-back-end-process-episode-1-understanding-semiconductor-testing/)

원리는 출처를 자체 요약했다. 예제·확인 질문·분석 절차는 교육용 작성이며 실제 출제 문제·SK하이닉스 내부 레시피·제품 보증값이 아니다.
