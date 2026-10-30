# DRAM 셀·전하 공유·센싱·복원

ID: `M01` · 단계 3 · 출처 확인: 2026-10-30

일반적인 1T1C DRAM은 커패시터의 전하 상태를 접근 트랜지스터로 읽고 쓴다.

## 원리·동작

wordline이 접근 소자를 켜면 셀과 bitline 사이 전하가 공유된다. 센스 앰프는 작은 차이를 증폭하고 셀 상태를 복원한다. 쓰기는 원하는 상태로 셀 전하를 바꾼다. 읽기로 교란된 상태의 복원은 정상 읽기 동작에 포함된다.

## 지표·공식과 적용 조건

가상 두 커패시터의 이상적 전하 공유 모델: Vfinal=(Cs×Vs+Cb×Vb)/(Cs+Cb). 스위치 주입·누설·센스 앰프 작동을 제외한 초기 공유 단계만 설명한다.

## 직접 만든 적용 예제

Cs=20 fF, Cb=180 fF, Vs=1 V, Vb=0.5 V이면 Vfinal=0.55 V, bitline 변화는 +0.05 V다. 낮은 셀 상태 Vs=0 V이면 0.45 V다. 실제 제품 마진값이 아니다.

## 혼동·적용 한계

파괴적 읽기는 사용자 데이터가 정상 읽기마다 사라진다는 뜻이 아니다. PRECHARGE는 다음 접근을 위해 bitline을 준비하며 셀 복원 전체를 대신 뜻하지 않는다.

## 과제에서 확인할 질문

- 셀 전압·bitline 초기값·센싱 시점을 구분했는가?
- 누설·정전용량·센스 앰프 오프셋 중 무엇을 측정했는가?

## 출처

- [S36: Carnegie Mellon University / Liu et al. — RAIDR: Retention-Aware Intelligent DRAM Refresh](https://users.ece.cmu.edu/~omutlu/pub/raidr-dram-refresh_isca12.pdf)
- [S37: SK hynix — How Innovative Convergence Technology Is Tackling DRAM Scaling Challenges](https://news.skhynix.com/en/how-innovative-convergence-technology-is-tackling-dram-scaling-challenges/)

원리는 공개 출처를 자체 요약했다. 예제·질문은 교육용 작성이며 실제 출제 문제·제품 보증값·권장 설정이 아니다.
