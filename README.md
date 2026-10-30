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
과제 루트의 `docs/handoff`, `docs/references`, `docs/reports`도 준비한다. 기존 docs 파일과 세션 기록은 보존한다.
이전 버전의 .probe-kit 파일과 충돌하면 설치를 중단한다. 실행 중인 과제의 하네스를 자동 교체하지 않으며 새 모의 폴더에서 먼저 확인한다.

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
| [문서 시작점](docs/README.md), [현재 상태](docs/handoff/CURRENT.md) | 여러 세션의 읽는 순서와 파일 작성 범위 |
| [제작진 인터뷰 분석](docs/references/cofa-probe-interview-20261031.md) | 기술, 의도, 인지의 설명과 시간별 근거, 적용 한계 |
| [메인/서브 요청](docs/prompts.md) | 사람이 선택해서 두 세션을 운영하거나 한 세션으로 진행 |
| `runtime/`, `templates/` | 작업 명세, 결과, 요구, 질문, 결정, 증거, 인계 기록 |
| `scripts/decision.py` | 과거 결정을 보존하며 선택, 대안, 이유, 검증과 한계를 추가 |
| [반도체 자료](knowledge/semiconductor/README.md) | KTY 원문 94개 파일, 추가 다운로드 없이 로컬 검색 |
| [서술형 원문](references/written-prep.original.md), [연습용 안내](docs/written-prep.md) | 원문 보존, 실제 연습은 제출물 확정 전에 완료 |
| [도구 조사](docs/TOOL_SURVEY.md) | 유명 MCP, 플러그인, 스킬의 용도와 대회 적용 판단 |
| [채택한 공개 레포의 방법](docs/ADOPTED_PRACTICES.md) | 무엇을 가져왔고 무엇을 바꿨는지 |

## 여러 세션으로 이어가기

사용자가 같은 프로젝트 폴더에서 필요한 세션을 연다. [공유 절차](docs/handoff/README.md)에 따라 통합 담당자가 파일 범위를 배정하고 각 세션이 자기 기록을 남긴다.

```text
docs/
  handoff/
    CURRENT.md            현재 목표, 세션 배정, 공통 원장과 결과 링크
    TEMPLATE.md           세션별 명세와 인계 양식
    sessions/             <session-id>.md, 작업 시작 시 생성
    messages/             필요할 때 요청과 답변을 새 파일로 전달
  references/             출처와 인터뷰 분석
  reports/                세션별 변경 및 실제 검증 결과
```

새 세션의 첫 요청:

```text
프로젝트 공식 지침과 docs/handoff/README.md, docs/handoff/CURRENT.md를 읽어.
나는 이 세션을 [세션 ID와 역할]로 사용할 거야.
배정된 범위와 관련 인계, 보고서를 확인하고 현재 상태와 다음 행동을 요약해.
배정되지 않았거나 다른 세션과 겹치는 파일은 먼저 조정하고, 자기 세션 문서에 결과를 남겨.
```

CURRENT와 공통 요구 및 결정은 통합 담당자 한 명이 관리한다. 세션별 대화는 자동 공유되지 않으므로 파일 경로를 전달하고 상대 세션이 읽어야 한다.
이 저장소의 CURRENT는 하네스 개발 상태다. 설치기는 실제 과제에 별도의 미시작 CURRENT를 만들며 개발 인계를 과제 상태로 복사하지 않는다.

## 원본 보존과 수정 범위

메인 원본 전체는 `upstream/chichochoi/`에 그대로 있다. 사용 경로의 `init.sh`와 `scripts/subagent.sh`는 공식 규칙에 맞춰 교체했다. 설치는 프로젝트 범위에서만 수행하고 서브 세션은 기본 승인 설정으로 사람이 시작한다. 원본 `config.toml`을 전역에 설치하지 않는다.
사용 경로의 `templates/HANDOFF.md`는 새 공유 문서를 가리키는 양식으로 보완했다. 해당 원본도 upstream에 보존한다.

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
