# SK Probe Kit

데이터 기반 과제의 요구 확인, 구현, 검증, 제출과 서술형 준비를 위한 실전 키트다. 공식 운영 규칙과 실제 README를 최우선으로 따른다.

**시작할 때는 [foruser.md](foruser.md)를 연다.** 시간표, 실제 README의 Case/스킬 식별, S1~S8 시작 요청, 질문과 합의, 구현/검수, S8 문답, 제출까지 단계별 행동과 복사할 프롬프트가 있다. 각 단계에서 입력할 세션과 완료 기준을 확인한다.

## 설치

제공된 과제 루트에서 실행한다. Python 3.9 이상, Bash와 Git이 필요하다.

```bash
probe_kit_dir="$(mktemp -d)"
git clone --depth 1 https://github.com/gxonu/sk-probe-kit.git "$probe_kit_dir"
bash "$probe_kit_dir/init.sh" . --dry-run
bash "$probe_kit_dir/init.sh" .
python3 .probe-kit/scripts/preflight.py --workspace .
```

설치는 과제의 기존 지침에 연결 안내를 덧붙이고 `.probe-kit/`, `.agents/skills/`, 공유 docs를 준비한다. 전역 Codex 설정을 바꾸지 않으며 기존 작업 기록을 보존한다. 다른 버전 파일과 충돌하면 덮어쓰지 않고 중단한다. 실행 중인 과제 폴더를 새 버전으로 자동 교체하지 않는다.
설치 뒤 같은 과제 폴더에서 세션을 시작하고 읽은 지침을 확인한다. S1~S8의 빈 기록은 생성되지만 세션이 자동 실행되지는 않는다.

## 사용하는 자료

| 목적 | 위치 |
|---|---|
| 사람이 따라갈 절차와 복사할 요청 | [foruser.md](foruser.md) |
| 공통 지침과 작업자 지침 | [AGENTS](AGENTS.md), [SUB_AGENTS](SUB_AGENTS.md) |
| 공식 규칙과 8세션 역할 | [RULES](docs/RULES.md), [TEAM_PLAYBOOK](docs/TEAM_PLAYBOOK.md) |
| 질문 추천과 원문 기록 | [interview](docs/interview.md), [질문 예시](dm_question.md) |
| 과제 종류와 스킬 조합 | [scenarios](docs/scenarios.md), `skills/case*.md` |
| 반도체 개념과 검색 | [knowledge](docs/knowledge.md), `knowledge/semiconductor/` |
| S8 주요 6문항, 보조 문항과 답변 | [요청 문구](prompts/mock_exam_6.md), [가상 예시](docs/mock-examples.md) |
| 설치/기록/계산 흐름 검증 | [REHEARSAL](docs/REHEARSAL.md), `tests/` |
| 제출 전 읽기 전용 점검 | `scripts/pre_submit_audit.py`, foruser의 11단계. 비밀값 숨김, 검사 범위와 미확인 표시 |

실제 과제 기록은 `.probe-kit/runtime/`의 공통 원장과 `docs/handoff/sessions/S1-main`~`S8-explain`에 저장한다. 라이선스와 자료 출처는 [NOTICE](NOTICE), [UPSTREAMS.json](UPSTREAMS.json), [ORIGINS.json](ORIGINS.json)에 있다.
실제 문제, 답안, 개인 접속 링크와 인증 정보는 이 공개 레포에 올리지 않는다.
