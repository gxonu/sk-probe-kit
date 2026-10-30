# SK AI Probe Kit

Cofa Probe 과제를 위한 공개 자료 통합본. **공식 운영 안내와 실제 과제 지침을 최우선**으로 적용한다.

`chichochoi/sk`를 메인으로, KTY 반도체 지식 패키지와 hamjoon 서술형 대비 원문을 포함한다. 원본 125개 파일은 출처와 고정 커밋을 기록해 보존했다. 실제 응시 문제, 정답, 개인 링크와 인증 정보는 포함하지 않는다.

## 설치

과제 루트에서 실행한다. Python 3.9 이상, Bash와 Git이 필요하다. 대상 임시 경로가 이미 있으면 새 경로를 선택한다.

```bash
git clone https://github.com/gxonu/sk-probe-kit.git /tmp/sk-probe-kit
bash /tmp/sk-probe-kit/init.sh . --dry-run
bash /tmp/sk-probe-kit/init.sh .
codex
```

전역 Codex 설정을 바꾸지 않는다. 기존 과제 지침에는 연결 안내를 추가하고 `.probe-kit/` 및 프로젝트 스킬 여섯 개를 설치한다. 기존 작업 기록은 보존하고 파일 충돌은 덮어쓰지 않고 알린다. 설치 뒤 새 Codex 세션에서 읽은 지침을 확인한다.

첫 요청:

```text
$probe-workflow .probe-kit/AGENTS.override.md와 공식 규칙부터 확인해.
과제 README를 읽고 사실, 가정, 열린 질문, 하지 않을 일, 성공 기준을 정리해.
구현을 바꾸는 담당자 질문 최대 3개와 계획을 보여줘. 내가 승인하면 최소 흐름부터 진행해.
현재 시각과 제출 목표는 내가 알려줄게.
```

스킬이 보이지 않으면 `.agents/skills/probe-workflow/SKILL.md`를 직접 읽도록 요청한다. 실제 응시 환경에서의 자동 발견과 모델 사용 가능 여부는 사전 체험에서 확인한다.

## 구성

| 구성 | 내용 |
|---|---|
| [공식 우선 지침](AGENTS.override.md), [일곱 가지 작업 원칙](docs/RULES.md) | 원본과 충돌할 때 적용할 기준 |
| `AGENTS.md`, `SUB_AGENTS.md`, `skills/`, `prompts/`, `scripts/` | chichochoi 메인/서브 흐름과 과제 유형별 원문 |
| [질문 절차와 질문 은행](docs/interview.md) | 숨은 조건 후보, Q-ID → R-ID → 테스트 연결 |
| [메인/서브 요청](docs/prompts.md) | 사람이 선택해서 두 세션을 운영하거나 한 세션으로 진행 |
| `runtime/`, `templates/` | 작업 명세, 결과, 요구, 질문, 결정, 증거, 인계 기록 |
| `scripts/decision.py` | 과거 결정을 보존하며 선택, 대안, 이유, 검증과 한계를 추가 |
| [반도체 자료](knowledge/semiconductor/README.md) | KTY 원문 94개 파일, 추가 다운로드 없이 로컬 검색 |
| [서술형 원문](references/written-prep.original.md), [연습용 안내](docs/written-prep.md) | 원문 보존, 실제 연습은 제출물 확정 전에 완료 |
| [도구 조사](docs/TOOL_SURVEY.md) | 유명 MCP, 플러그인, 스킬의 용도와 대회 적용 판단 |
| [채택한 공개 레포의 방법](docs/ADOPTED_PRACTICES.md) | 무엇을 가져왔고 무엇을 바꿨는지 |

## 원본 보존과 수정 범위

메인 원본 전체는 `upstream/chichochoi/`에 그대로 있다. 사용 경로의 `init.sh`와 `scripts/subagent.sh`는 공식 규칙에 맞춰 교체했다. 설치는 프로젝트 범위에서만 수행하고 서브 세션은 기본 승인 설정으로 사람이 시작한다. 원본 `config.toml`을 전역에 설치하지 않는다.

원문의 Git 변경 금지, 고정 모델 ID, 채점 가산점 주장, 제출 확정 이후 코칭 안내보다 `AGENTS.override.md`가 우선한다. 원본 보존은 그 주장을 검증하거나 승인했다는 의미가 아니다. 다른 사람이 쓴 문서의 주장과 실제 공식 규정을 구분한다.

반도체 자료 검색 예시:

```bash
python3 .probe-kit/scripts/knowledge.py search .probe-kit/knowledge/semiconductor 수율
python3 .probe-kit/scripts/knowledge.py search .probe-kit/knowledge/semiconductor HBM
```

## 검증과 범위

```bash
python3 -m unittest discover -s tests -v
```

설치, 기존 파일 보존, 재설치, 충돌, 원본 및 지식 설치, CSV 요약, 결정 기록을 로컬에서 검증했다. 실제 Probe 접속, 모델, 감독 연결과 점수는 검증 대상이 아니다. 제공된 Codex 버전을 업데이트하지 않는다.

이 저장소와 사용한 공개 자료는 결과 통지 전까지 공개 유지 조건을 따른다. 시험 중 작업 결과를 원격 저장소로 push하지 않는다.

## 출처

[ORIGINS.json](ORIGINS.json)은 원본 파일 해시, [UPSTREAMS.json](UPSTREAMS.json)은 고정 커밋, [NOTICE](NOTICE)는 출처와 수정 범위를 기록한다. 원본 전체에 새로운 라이선스를 붙이지 않았다. hamjoon의 MIT 고지는 보존했다.
