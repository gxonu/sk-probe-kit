# 잔여 58개 검토 A — 수정 영향 범위 재검토

기준 commit `9dab381bcccfc70d9c6596e13efff9d1879a2a0a` + fixes.diff SHA256 `7deada885538951378429a65ef51b870af010c8708517a57d758b67e0ed8777f`. 수정 동결본 `revised/`만 읽었고 다른 reviewer 재검토 결과는 읽지 않았다. 이번에는 58개 전수 재대조를 반복하지 않고 F03/S03/S84와 변경된 메타데이터·검사만 확인했다.

## 판정

F03 유전율 설명 수정은 적절하다. 기존 S03의 진공 평행판 근사 자체는 틀리지 않았으며 기존 카드의 ε 일반화도 과학적으로 거짓은 아니었다. 다만 ε를 정의하지 않은 점과 유전체 확장을 S03 단일 절에서 직접 확인하기 어려운 점은 초보 학습자의 κ 오대입과 추적성을 위한 P3 보완으로 타당하다. 새 수정은 이를 해결한다.

S84는 실제 등록 URL인 [OpenStax §8.4 Capacitor with a Dielectric](https://openstax.org/books/university-physics-volume-2/pages/8-4-capacitor-with-a-dielectric)다. **초기 A 검토 중 직접 열어 읽은 동일 공식 원문의 eq8.11 주변(유전체가 간극을 완전히 채움, C=κC0, 진공 κ=1)을 재사용했다. 이번 재검토의 새 원문 fetch로 표현하지 않는다.** S03의 C0=ε0A/d와 결합한 ε=κε0는 맞다. 절대 유전율 F/m·상대 유전율 무차원·A[m²]·d[m] 및 균일/선형/등방성/완전 충전 조건은 근사 범위를 적절히 좁힌다.

예제는 4×8.85×10⁻¹²×10⁻¹²/10⁻⁸ = 3.54×10⁻¹⁵ F = 3.54 fF로 맞다. κ만 ε 대신 수치 대입하면 1/ε0≈1.13×10¹¹배가 되는 잘못된 차원 계산이며, 새 반례 검사는 이 오류를 수치상 구분한다. `wrong_F`라는 테스트 지역명은 잘못된 대입값에 붙인 이름이지 실제 차원적으로 F인 값이라는 교육 주장으로 보지 않았다.

sources.json에서 S03 범위를 진공으로 명시했고 S84 used_for는 §8.4 eq8.11과 결합 유도임을 명시했다. index F03 source_ids=[S03,S84], permittivity aliases/metrics, 카드 링크가 일치한다.

## 새 지적

- **A-R01 / P3 — `knowledge/semiconductor/application-playbook.md:58`**. 수정 후에도 출처 수를 83개로 적었다. 근거는 revised sources.json의 고유 84개와 verify.py 통과 출력(65 cards, 84 sources, 16 tests)이며 README 두 곳은 이미 84다. 반례: 새로 등록한 S84까지 포함하면 83개라는 설명으로 구조 검사의 실제 범위를 재현할 수 없다. **수정: `65개 본문/색인·83개 출처`를 `65개 본문/색인·84개 출처`로 교체한다.** 물리 내용의 결함은 아니며 나머지 변경에서 새 사실 오류를 발견하지 않았다.

## 실제 검증

- fixes.diff SHA256가 전달값과 일치했다.
- revision-manifest.json의 변경 파일 8개에 대해 실제 revised 바이트 SHA256를 계산했고 모두 일치했다: root README, semiconductor README, application-playbook, application_checks, capacitance, index, sources, verify.
- `python3 -B revised/knowledge/semiconductor/verify.py` (실제 명령은 절대 경로): exit0; 65 cards/84 sources, 62 retrieval routes, 91 numeric fixtures, 16 synthetic tests 통과.
- `python3 -B revised/knowledge/semiconductor/checks/application_checks.py`: exit0; 16 tests 통과. AST로 test_ 함수도 16개 확인했다. 새 절대/상대 유전율 검사와 본문 제한 연결 토큰을 직접 읽었다.
- 검사는 본문 전체 의미나 실물 DRAM 사양을 인증하지 않는다. snapshot/코드 수정 없음. 허용된 recheck-a.md만 작성했다.

## 추가 교정 재검토 — A-R01 해결

`copyedit-manifest.json`과 `copyedit-application-playbook.md`를 원래 동결 revised 가이드와 비교했다. 유일한 바이트 차이는 58행의 출처 수 `83→84` 교체이며 기술 내용 변경이 없다. 최종 가이드 SHA256를 직접 계산해 `396c036649730198df2e78229c49cd2b0b0379814dbbbc6bf4d6f9327f464a02`와 일치함을 확인했다. **A-R01은 이 추가 교정본에서 해결됨. 최종 미해결 지적 없음.** 원래 동결 revised는 그대로이며 이 판단은 추가 교정본에 적용한다.
