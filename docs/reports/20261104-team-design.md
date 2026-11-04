# 6~7개 세션과 코드 기반 예상 문항 개선

2026-11-04 / 준비용 키트의 로컬 개선안.

## 변경 결과

- 역할을 S1 총괄, S2/S3 개발, S4 데이터/알고리즘, S5 조사, S6 독립 검증, S7 기록/제출 문서로 구체화했다.
- 6개로 줄일 때 S5의 한정된 조사를 S1 또는 S4에 배정하는 안을 제시했다. 파일과 실행 자원의 소유권은 실제 과제에서 확정한다.
- S6는 반례, 재현, 영향, 최소 수정 방향을 보고하고 제품 수정은 소유자에게 맡긴다.
- S7은 자기 근거 기록과 공통 원장 반영안을 만들고, 독점 배정된 제출 문서를 작성한다. CURRENT와 공통 원장은 S1이 유지한다.
- 코드 기반 예상 문항 P1~P5와 먼저 답한 뒤 피드백하는 절차를 추가했다.
- 최적화 배정과 CSV 집계의 가상 few-shot 두 개를 넣어 특정 과제에 고정되지 않도록 했다. 예시 경로와 구현을 현재 사실로 사용하지 않도록 명시했다.
- foruser, README, 공유 안내, CURRENT 양식, 기존 probe-explain 스킬에 연결했다. 설치 프로그램 변경과 새 자동 세션 실행기는 없다.
- 원본 AGENTS, SUB_AGENTS와 upstream 원본은 보존했다.

## 주요 경로

- [역할과 시작 프롬프트](../TEAM_PLAYBOOK.md)
- [제출 전 20분 절차](../../prompts/mock_exam_5.md)
- [가상 few-shot](../../prompts/mock_exam_5.md)
- [출제 프롬프트](../../prompts/mock_exam_5.md)
- [주 안내](../../foruser.md)

## 검증

| 확인 | 결과 |
|---|---|
| python3 -m unittest discover -s tests -v | 21개 PASS |
| skill-creator quick_validate.py / probe-explain | PASS. 기본 Python에는 YAML이 없어 기존 패키지 캐시를 읽어 검증기를 실행했다. 전역 패키지를 설치하지 않았다 |
| ORIGINS 원본 해시 | 125개 일치 |
| 루트 AGENTS/SUB_AGENTS와 upstream 원본 | 바이트 일치 |
| 새 임시 과제 설치 | 새 가이드 3개, 출제 프롬프트와 수정 스킬 포함 |
| 설치된 새 안내의 상대 링크 | PASS |
| 7개 세션 인계와 기존 CURRENT를 만든 뒤 재설치 | 기록 보존 PASS |
| git diff --check | PASS |
| 공개용 변경 검토 | 실제 문제/전사/개인 경로를 넣지 않고 가상 예시 사용 |
| 실제 7개 AI 세션/현재 과제 기반 문답 | NOT_RUN |

파일 설치와 보존 검증은 실제 동시 세션 운영의 성능 검증이 아니다. few-shot 및 역할 설계가 점수나 시간 절감을 보장한다고 주장하지 않는다.

## 작업 기준

시작 시 GitHub 기본 브랜치와 로컬 HEAD는 90289633ecb33b2ab32a26906b6e37dfdda7aeb9로 같았다. 로컬 작업 브랜치는 prep/seven-session-review다. 이 보고서는 게시 완료 기록이 아니다.
