# 인터뷰 반영과 세션 공유 보완 검증

- 작성 세션: 20261031-0230-codex-harness
- 날짜: 2026-10-31 KST
- 기준: 557fd59220622051da906c1746282827c6a99df2 이후 준비용 변경
- 인계: [세션 문서](../handoff/sessions/20261031-0230-codex-harness.md)
- 출처: [인터뷰 분석](../references/cofa-probe-interview-20261031.md)

## 변경과 목적

- 제작진 발언을 시간별로 정리하고 관찰 사실, 우리 해석, 공식 규칙의 관계를 구분했다.
- 질문에 열린 업무 탐색, 결정에 업무 영향과 적용 및 재검토 조건을 추가했다.
- 설명이 막히면 코드와 작은 입력을 확인해 이해를 점검하도록 바꿨다.
- docs/handoff, references, reports 및 읽는 순서, 세션별 작성 범위와 요청 방식을 추가했다.
- 설치기는 과제 루트에 공유 구조를 만들고 기존 문서와 작업 기록을 보존한다.
- 기존 전역 설정, 인증, 원격 전송 동작을 추가하지 않았다.

## 검증

작업 폴더는 이 저장소 루트이며 결과는 이번 변경의 코드와 템플릿 기준이다.

| 상태 | 검사 | 실행 및 실제 결과 |
|---|---|---|
| PASS | 기능 회귀와 공유 문서 설치 | `python3 -m unittest discover -s tests -v`: 14 tests, OK, 종료 코드 0 |
| PASS | 여섯 프로젝트 스킬 형식 | skill-creator의 `quick_validate.py .agents/skills/<name>`: 각각 Skill is valid!, 종료 코드 0 |
| PASS | 원본 보존 | ORIGINS.json의 125개 파일을 Python hashlib.sha256으로 비교: 불일치 0 |
| PASS | 문서 링크 | 변경 문서의 상대 링크 46개, 임시 과제 설치 문서의 상대 링크 34개: 누락 0 |
| PASS | 변경 공백 검사 | `git diff --check`: 출력 없음, 종료 코드 0 |

새 기능 검증은 기존 docs/README 보존, 새 CURRENT 초기화, 인계와 보고서 재설치 보존, 개발 이력의 과제 상태 혼입 방지,
docs 심볼릭 링크 발견 시 쓰기 전 중단, 기존 v1 지침에 공유 안내를 한 번만 추가하는 동작을 포함한다.
기존 설치, 충돌, 데이터 요약과 결정 기록 테스트도 함께 통과했다.

원본 비교는 다음 명령으로 재현할 수 있다.

```bash
python3 - <<'PY'
import hashlib, json
from pathlib import Path
files = json.loads(Path('ORIGINS.json').read_text())['files']
bad = [x['path'] for x in files
       if hashlib.sha256(Path(x['path']).read_bytes()).hexdigest() != x['sha256']]
print(len(files), 'checked;', len(bad), 'mismatches')
assert not bad
PY
```

링크 검사는 Python re로 Markdown 상대 링크를 추출하고 파일 존재 여부를 확인했다.
설치용 템플릿의 링크는 소스 templates 폴더가 아닌 실제 설치 위치에서 검증했다.
외부 URL의 접속 가능 여부와 Markdown 화면 렌더링은 이 검사에 포함하지 않았다.

## 범위와 한계

실제 Probe 접속과 채점, 사용자 환경의 여러 세션 실시간 운영은 NOT_RUN이다.
문서 공유는 수동 절차이며 자동 알림, 파일 잠금, 다른 clone 또는 worktree 동기화를 제공하지 않는다.
기존 버전의 하네스 코드 파일과 충돌하는 재설치는 중단한다. 기록을 덮어써서 업그레이드하지 않는다.
