# 메모리 오류 지표·RBER·UBER·분모

ID: `M13` · 단계 3 · 출처 확인: 2026-10-30

ECC 이전의 raw 오류와 정정 후 남는 오류는 측정 위치와 분모를 구분해서 비교한다.

## 원리·동작

RBER는 ECC 이전 오류 bit의 비율, UBER는 지정한 정정 방법 적용 뒤의 복구 불가 데이터 오류를 읽은 bit 수에 대해 표현하는 지표다. 제품 로그의 실패 요청·sector·codeword 수가 오류 bit 수와 같은 것은 아니다.

## 지표·공식과 적용 조건

실제 bit 오류를 센 실험이면 관측 BER=오류 bit 수/읽은 bit 수. UBER 산출에는 해당 시험·규격의 오류 계수 규칙을 확인한다. 0개 관측은 유한한 표본에서 오류를 못 봤다는 뜻이다.

## 직접 만든 적용 예제

알려진 패턴을 ECC 전에 10⁸ bit 읽어 200 bit 불일치라면 관측 RBER=2×10⁻⁶이다. 다른 실행의 “uncorrectable request 1건”을 곧바로 오류 1 bit로 나눠 같은 지표로 비교하지 않는다.

## 혼동·적용 한계

오류가 특정 블록·코드워드에 몰리는지와 읽기 노출량을 함께 본다. 여러 번 읽은 같은 물리 오류의 로그 수를 고유 결함 수로 세지 않는다. 무오류 관측만으로 제품 규격 수준의 UBER를 입증하지 않는다.

## 과제에서 확인할 질문

- 분자가 bit·codeword·sector·요청 중 무엇인가?
- ECC 전후 위치, 읽기 노출량, 중복 오류 처리 규칙은 같은가?

## 출처

- [S50: Kingston — The Difference Between Enterprise & Client SSD](https://www.kingston.com/en/blog/pc-performance/enterprise-versus-client-ssd)

원리는 공개 출처를 자체 요약했다. 예제·질문은 교육용 작성이며 실제 출제 문제·제품 보증값·권장 설정이 아니다.
