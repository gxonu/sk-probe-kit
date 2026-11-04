# SK AI Probe Kit

데이터로 문제를 해결하는 과제의 질문, 방법 합의, 구현, 검증과 설명을 돕는 키트다. 최신 공식 안내와 실제 README가 우선한다. chichochoi의 명세/결과 흐름, KTY 반도체 참고 자료와 hamjoon 설명 연습을 하나의 프로토콜로 맞췄다.

**사람은 [foruser.md](foruser.md), AI는 [AGENTS.md](AGENTS.md)부터 시작한다.** 현재 상태와 자기 작업은 설치한 과제의 docs/handoff/CURRENT.md와 세션별 TASK_SPEC에 있다. 역할 배정 때만 [7개 세션 운영](docs/TEAM_PLAYBOOK.md)을 참고한다.

## 설치

Python 3.9 이상, Bash와 Git이 있는 실제 과제 루트에서 하나씩 실행한다.

```bash
probe_kit_dir="$(mktemp -d)"
git clone --depth 1 https://github.com/gxonu/sk-probe-kit.git "$probe_kit_dir"
bash "$probe_kit_dir/init.sh" . --dry-run
bash "$probe_kit_dir/init.sh" .
python3 .probe-kit/scripts/preflight.py --workspace .
codex
```

기본 설치에는 활성 지침과 도구, 공통 원장 4개, S1~S7의 PLANNED 배정표와 세션별 양식이 들어간다. 세션을 자동 실행하지 않는다. 반도체 자료 94개와 검색 도구도 필요하면 두 설치 명령에 --with-knowledge를 붙인다. 기본 설치 후 같은 버전에서 추가할 수도 있다.

기존 과제 지침과 기록을 보존하며 내용 충돌은 쓰기 전에 알린다. 전역 설정을 변경하거나 이전 설치본을 강제로 갱신하지 않는다.

## 사용하는 문서

| 용도 | 문서 |
|---|---|
| 시작부터 제출까지의 순서와 복사할 요청 | [foruser](foruser.md) |
| 모든 세션의 공통 규칙 | [AGENTS](AGENTS.md), 실제 공식 안내 |
| 7개 역할과 파일/실행 자원 배정 | [TEAM_PLAYBOOK](docs/TEAM_PLAYBOOK.md) |
| 조건 질문과 필요한 유형 점검 | [interview](docs/interview.md), [scenarios](docs/scenarios.md) |
| 제출 전 코드 기반 5문항, 6개 설명 축과 few-shot | [통합 설명 연습](prompts/mock_exam_5.md) |

실제 공유 기록은 과제 루트 docs 아래에 둔다. S1은 CURRENT와 .probe-kit/runtime의 요구/질문/결정/증거를 관리하고 작업자는 자기 세션 결과/인계를 쓴다. S7은 원장 반영안을 제안하고 배정된 제출 문서를 작성한다.

## 원본과 준비 자료

원본 125개는 [ORIGINS](ORIGINS.json)의 해시와 출처로 보존한다. upstream, 원본 서술형 자료, 제작 이력과 도구 조사는 기본 설치에 포함하지 않는다. 활성 AGENTS/SUB_AGENTS와 Case 안내는 통합 프로토콜로 수정했으며 원문은 upstream에 있다.

[정리 기준](docs/CLEANUP.md), [준비 자료 목록](docs/README.md), [반도체 참고](docs/knowledge.md), [출처와 권리](NOTICE). 시험 문제, 개인 문항 원문과 인증 정보는 공개 키트에 추가하지 않는다.

## 로컬 검증

```bash
python3 -m unittest discover -s tests -v
python3 scripts/rehearse.py
```

두 번째 명령은 새 임시 폴더의 합성 데이터로 설치, 실패 검출, 정상 처리와 기록 보존을 점검한다. 실제 AI 세션/Probe 접속/제출을 수행하는 검증은 아니다. 실제 응시 중에는 합성 점검 대신 과제 필수 흐름을 확인한다.
