# 대회용 MCP, 플러그인, 스킬 조사

확인일: 2026-10-31. 주요 공개 저장소 19개, 기존에 비교한 대회 하네스 6개, 현재 앱의 플러그인 카탈로그를 조사했다. 생태계 전체를 빠짐없이 검증한 목록은 아니다. 공식 README, 선택한 SKILL.md 및 MCP 안내를 확인했으며, 실제 Probe 안에서 설치하거나 실행하지는 않았다.

인기도는 [GitHub API 스냅샷](tool-survey-snapshot.json)의 저장소 전체 별 수다. 개별 스킬의 이용자 수나 품질, 대회 허용 여부를 의미하지 않는다. 아래 추천과 부담 평가는 문서 및 대회 규칙을 대조한 판단이며 측정된 설치 시간이나 운영팀 승인 결과가 아니다.

## 먼저 쓸 구성

**기본은 추가 MCP 없이 제공된 Codex와 로컬 도구, 필요한 작업 스킬이다.** 대회에 이미 터미널, 파일 편집, 내장 Browser와 메신저가 있어 기능이 겹치는 서버를 많이 설치할 이유가 작다.

1. 요구 질문, 결정 기록, 디버깅, 완료 검증은 이 통합본의 스킬로 준비했다.
2. 표 데이터는 Python의 csv, 설치돼 있는 pandas 또는 로컬 DuckDB로 먼저 처리한다.
3. PDF가 실제로 나오면 PDF 스킬이나 MarkItDown의 로컬 변환을 선택한다.
4. React/Next.js 과제일 때만 Vercel React Best Practices를 고려한다.
5. 외부 문서 검색이 실제로 필요하고 운영 규칙상 허용됨을 확인했을 때만 Context7 등을 추가한다.

공식 가이드는 공개 MCP/Plugin/Skill 활용을 허용하지만, 문제와 파일의 외부 전송, 외부 AI, 개인 API 키 사용, Computer Use 및 보안 우회를 제한한다. 따라서 공개된 도구라는 이유만으로 모든 기능이 허용되는 것은 아니다. 설정은 플랫폼이 제공한 MCP 화면과 안내를 이용하고 전역 설정을 교체하거나 Codex를 업데이트하지 않는다. [규칙 요약](RULES.md)

## MCP 및 로컬 도구 비교

| 후보와 1차 출처 | 기능 | 외부 전송 및 의존성 | 대회 판단 |
|---|---|---|---|
| [Context7](https://github.com/upstash/context7) | 라이브러리 문서와 예제 검색 | 질의가 외부 서비스로 전달됨. 인증과 제한은 현재 서비스 및 클라이언트에 따라 다름 | **조건부 후보 1위.** 라이브러리 이름, 버전, 일반 API 질문만. 문제, 코드, 데이터는 보내지 않기 |
| [Sequential Thinking](https://github.com/modelcontextprotocol/servers/tree/main/src/sequentialthinking) | 단계별 문제 분해와 판단 수정 기록 | 로컬 stdio 서버, Node 패키지. 도구 호출과 텍스트가 늘어남 | 선택 사항. 이미 계획과 결정 로그가 있으면 중복이 커서 기본 제외. 성능 향상 보장 없음 |
| [Memory](https://github.com/modelcontextprotocol/servers/tree/main/src/memory) | 로컬 지식 그래프 메모리 | 저장 경로 설정 및 관리 필요 | 짧은 시험에서는 HANDOFF.md와 DECISIONS.md로 충분. 기본 제외 |
| [Filesystem](https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem) | 허용 경로의 파일 읽기와 편집 | 로컬 서버, 경로 권한 필요 | Codex 기본 파일 도구와 중복. 기본 도구가 없는 환경일 때만 |
| [Git](https://github.com/modelcontextprotocol/servers/tree/main/src/git) | 로컬 변경과 커밋 조사 | 로컬 저장소 접근 | 터미널 git으로 충분. 원격 push를 허용하는 근거가 아님 |
| [GitHub MCP](https://github.com/github/github-mcp-server) | GitHub 저장소, 이슈, PR 작업 | 원격 서비스 및 인증. 쓰기 작업이 포함됨 | 대회 기본 제외. 공개 코드 반입은 clone이면 충분. private 접근, 이슈/PR로 결과 전송은 하지 않기 |
| [Serena](https://github.com/oraios/serena) | 심볼 기반 코드 검색과 편집 | Python/uv와 언어 서버, 프로젝트 초기화가 필요할 수 있음 | 큰 기존 코드 과제에서 조건부. 작은 신규 과제에서는 준비 비용을 회수하기 어려움 |
| [MarkItDown 및 MCP](https://github.com/microsoft/markitdown) | PDF, Office 등 파일의 텍스트/Markdown 변환 | 로컬 Python 패키지와 형식별 의존성. 선택적 외부 모델/Azure 기능은 끄기 | 문서가 많을 때 유용. MCP 없이 CLI로 먼저 사용. 표 구조와 수식의 보존은 별도 확인 |
| [DuckDB](https://github.com/duckdb/duckdb) | CSV/Parquet의 로컬 SQL 집계와 결합 | 로컬 라이브러리. 기본 조회에 외부 서비스 불필요 | 데이터 과제 추천. MCP는 필수가 아님. 큰 데이터 전체를 프롬프트에 넣지 않고 집계 |
| [Exa MCP](https://github.com/exa-labs/exa-mcp-server) | 웹 검색과 페이지 조회 | 원격 질의. 문서상 익명 제한 사용 및 인증 옵션 있음 | 일반 공개 자료 검색만 조건부. 별도 Exa Agent 기능은 외부 AI 기능이므로 사용 대상에서 제외 |
| [Tavily MCP](https://github.com/tavily-ai/tavily-mcp) | 검색, 추출, 크롤링 | 원격 API, 키 또는 OAuth 흐름 | 인증과 외부 전송 조건 때문에 기본 제외. 제공 환경에서 허용된 접근인지 확인 필요 |
| [Firecrawl MCP](https://github.com/firecrawl/firecrawl-mcp-server) | 검색, 스크래핑, 문서 파싱과 여러 자동화 기능 | 원격 API. 일부 keyless 제한 기능, 다른 기능은 인증 필요 | 단순 공개 자료 조회만 조건부. 문제 파일 파싱 업로드, Agent 및 브라우저 조작 기능은 제외 |
| [Playwright MCP](https://github.com/microsoft/playwright-mcp) | 자동 브라우저 조작과 UI 검증 | 브라우저 설치 및 제어 | **추천 제외.** Computer Use/자동 조작 제한과 충돌. 직접 조작과 터미널 검증으로 대체 |
| [Chrome DevTools MCP](https://github.com/ChromeDevTools/chrome-devtools-mcp) | 브라우저 검사, 디버깅과 조작 | Chrome 연결과 제어 | **추천 제외.** 감독 브라우저/개발자 도구 접근 수단으로 사용하지 않기 |

`MotherDuck-Open-Source/mcp-server-motherduck`는 조사 당시 GitHub API와 웹 모두 404여서 추천 근거로 사용하지 않았다. 유지보수 상태가 확인되지 않은 이름의 SQLite/DuckDB MCP를 추가하기보다 로컬 라이브러리를 권한다.

### Context7에 대한 구체적인 선택

문서 버전이 중요한 웹 개발에서는 유용하다. 다만 [현재 Codex 설치 안내](https://github.com/upstash/context7/blob/master/docs/clients/codex.mdx)의 `ctx7 setup --codex`는 OAuth, API 키 생성, 전역 config와 AGENTS 변경을 포함한다. 이를 시험 중 그대로 실행하지 않는다. 공식적으로 제공된 MCP 설정 경로에서 연결 가능 여부와 인증 조건을 확인해야 한다.

질문 예시는 “pandas merge에서 validate 옵션은 어떻게 쓰는가”처럼 일반화한다. 과제 지문, 원본 코드, 데이터 행을 검색 질의로 보내지 않는다. 인증 없이 되는지, 네트워크가 열리는지, 제공 버전이 해당 연결 방식을 지원하는지는 실제 체험 전에는 확정할 수 없다.

## 스킬 비교

| 출처와 후보 | 활용 | 수정/준비 부담 | 추천 |
|---|---|---|---|
| [Matt Pocock: to-questionnaire](https://github.com/mattpocock/skills/tree/main/skills/productivity/to-questionnaire) | 내가 모르는 사실을 가진 담당자에게 질문 설계 | 일반 비동기 설문 흐름을 짧은 메신저 질문으로 줄이기 | 질문 목적과 정보 격차를 정리하는 원칙 추천. 이 통합본의 probe-interview와 겹치면 추가 설치 불필요 |
| [Matt Pocock: handoff](https://github.com/mattpocock/skills/tree/main/skills/productivity/handoff) | 새 세션용 인계 | 원문은 OS 임시 폴더를 권장함. 과제 기록은 작업 공간에 남기기 | 인계 항목과 중복 방지 원칙 추천 |
| [Matt Pocock: tdd](https://github.com/mattpocock/skills/tree/main/skills/engineering/tdd) | 인터페이스 기준 테스트와 red/green 검증 | 테스트 경계 합의 과정과 참조 파일이 있음 | 핵심 업무 규칙에 선택 적용. 반복 승인으로 구현을 지연하지 않기 |
| [Matt Pocock: diagnosing-bugs](https://github.com/mattpocock/skills/tree/main/skills/engineering/diagnosing-bugs) | 재현 신호를 만든 뒤 원인 확인 | 헤드리스 브라우저나 외부 자료 전송 방식은 제외 | 재현 입력, CLI, 로컬 HTTP 중심으로 추천 |
| [Superpowers: systematic-debugging](https://github.com/obra/superpowers/tree/main/skills/systematic-debugging) | 원인 조사, 패턴 비교, 가설 검증 | 강한 절차 규칙. 단순 문제까지 긴 조사를 강제하지 않기 | 필요한 순간만 선택. 전체 프레임워크 자동 활성화는 비추천 |
| [Superpowers: verification-before-completion](https://github.com/obra/superpowers/tree/main/skills/verification-before-completion) | 실행 결과 없이 완료 선언하지 않기 | 반복되는 전체 재실행을 과제 시간에 맞게 제한 | 강하게 추천하는 원칙. probe-verify에 맞춰 적용 |
| [Superpowers: test-driven-development](https://github.com/obra/superpowers/tree/main/skills/test-driven-development) | 실패를 확인한 테스트부터 구현 | 원문에는 테스트 전에 쓴 코드를 삭제하고 다시 시작하라는 강한 규칙이 있음 | 전체를 강제하기보다 중요한 오류 검출에 적용. 기존 코드와 시간 낭비 방지 |
| [OpenAI: PDF](https://github.com/openai/skills/tree/main/skills/.curated/pdf) | PDF 추출, 생성과 렌더링 확인 | pypdf/pdfplumber/reportlab, 렌더링은 Poppler 등 필요 | PDF 입력 또는 출력이 실제 요구일 때 추천. 관리자 설치 명령은 자동 실행하지 않기 |
| [OpenAI: Jupyter Notebook](https://github.com/openai/skills/tree/main/skills/.curated/jupyter-notebook) | 재실행 가능한 분석 노트북 | 템플릿과 보조 스크립트의 경로 및 실행 환경 확인 | ipynb 제출이 필요하거나 분석 기록에 도움될 때만. 단순 판정은 Python 스크립트로 충분 |
| [OpenAI: Security Best Practices](https://github.com/openai/skills/tree/main/skills/.curated/security-best-practices) | Python, JS/TS, Go의 보안 점검 | 언어별 참조 문서. 요청된 범위의 코드 리뷰 | 실제 인증, 파일 처리, 민감정보가 있는 결과물에 조건부. 플랫폼 공격/우회 용도 아님 |
| [Vercel: React Best Practices](https://github.com/vercel-labs/agent-skills/tree/main/skills/react-best-practices) | React/Next.js 데이터 로딩과 렌더링 개선 | React/Next.js에 한정. 관련 규칙만 로드 | 해당 스택이면 추천. 성능 최적화보다 필수 기능 완주가 먼저 |
| [Vercel: Web Design Guidelines](https://github.com/vercel-labs/agent-skills/tree/main/skills/web-design-guidelines) | 접근성과 UI 코드 점검 | 최신 가이드 다운로드를 요구함. 원격 조회 여부 확인 | 코드 리뷰에 조건부. 자동 브라우저 테스트와 구분 |
| [Anthropic: Frontend Design](https://github.com/anthropics/skills/tree/main/skills/frontend-design) | 화면의 시각적 방향과 디자인 | Claude 런타임과 텍스트 스킬은 별개. 파일별 라이선스 확인 | UI가 핵심인 경우만. 외부 이미지 생성/모델 연결로 확장하지 않기 |
| [Anthropic: XLSX](https://github.com/anthropics/skills/tree/main/skills/xlsx) | 스프레드시트 수식, 서식, 계산 검증 | 현재 frontmatter는 Proprietary, 폴더별 LICENSE 참조. 재계산 도구 의존성 있음 | 엑셀 제출에 조건부. 단순 CSV 분석에는 과함. openpyxl/pandas 직접 사용 우선 |
| [Anthropic 문서 스킬](https://github.com/anthropics/skills) | PDF, DOCX, PPTX 생성 및 편집 | 문서 스킬은 source-available이며 저장소 전체가 Apache라는 가정은 틀림. 형식별 의존성 | 실제 제출 형식이 있을 때만 검토. Claude Code 자체는 사용하지 않음 |
| [Hugging Face: datasets](https://github.com/huggingface/skills/tree/main/skills/huggingface-datasets) | 데이터셋 조회 및 조작 | Hub, 인증 및 업로드 작업이 포함될 수 있음 | 로컬 처리만 분리해 검토. 과제 데이터를 Hub에 올리지 않기 |
| [Hugging Face: 학습, Spaces, Cloud 계열](https://github.com/huggingface/skills) | 외부 실행, 학습과 배포 | 외부 모델, 계정, 컴퓨트, 업로드 | 기본 제외. 이번 대회 제한 및 시간 예산과 맞지 않음 |
| [Trail of Bits: property-based-testing](https://github.com/trailofbits/skills/tree/main/plugins/property-based-testing/skills/property-based-testing) | 불변식과 반례 탐색 | Hypothesis 등 대상 언어 도구가 필요할 수 있음 | 수치/파싱 규칙이 많고 불변식이 분명한 경우 조건부. 예제 테스트만으로 충분하면 생략 |
| [Trail of Bits: dimensional-analysis](https://github.com/trailofbits/skills/tree/main/plugins/dimensional-analysis/skills/dimensional-analysis) | 단위와 스케일 오류 감사 | 여러 역할과 에이전트 디스패치를 요구하는 큰 워크플로 | 전체 설치는 비추천. 단위 표기 및 변환 검증 원칙만 사용 |

일부 스킬은 Claude 전용 도구 이름, 프런트매터, 경로 또는 명령을 포함한다. 텍스트가 공개돼 있다는 사실만으로 제공된 Codex에서 그대로 실행되는 것은 아니다. 호스트 도구와 프로젝트 경로를 확인하고 운영 규칙이 충돌 시 우선한다. [OpenAI 스킬 문서](https://learn.chatgpt.com/docs/build-skills)

## 플러그인 카탈로그에서 확인한 것

현재 로컬 앱의 카탈로그에서 Context7, Firecrawl, Google Drive, SharePoint, Canva, Adobe Acrobat, Data, OpenAI Developers, Vercel 등을 찾았다. **이 앱의 설치 여부와 시험용 Codex의 제공 여부는 별개**다. 이번 조사에서 새 연결이나 설치는 하지 않았다.

| 유형 | 판단 |
|---|---|
| Context7 같은 문서 조회 | 일반 공개 자료 조회 범위에서 조건부. 인증과 전송 내용을 확인 |
| Drive, Notion, SharePoint, Box | 시험 자료를 외부 저장소로 보내거나 비공개 자료에 접근하는 흐름이므로 기본 제외 |
| Canva, Acrobat, 원격 데이터 분석 | 문제 파일을 서비스에 올려 처리하는 방식은 제외. 같은 목적의 로컬 도구 우선 |
| Vercel, Cloudflare, Netlify 배포 | 외부로 결과물을 전송하므로 이번 대회 추천 제외. 내장 Browser 사용 |
| Claude Code 전용 플러그인 | 런타임 그대로 사용하지 않음. 공개 텍스트 스킬을 별도로 읽는 것과 Claude 연결은 구분 |

## 바로 적용한 기능

이 저장소는 외부 도구를 한꺼번에 설치하지 않는다. 기존 하네스와 공개 워크플로의 유용한 부분을 다음 여섯 개의 작은 스킬로 연결했다.

- `probe-workflow`: 공식 규칙, 합의, 작은 완주와 제출 전 검증
- `probe-interview`: 구현을 바꾸는 질문 선택과 답변을 Q-ID → R-ID → 테스트로 연결
- `probe-decisions`: 선택, 대안, 이유, 검증과 한계의 이력
- `probe-debug`: 재현 신호부터 만들고 원인을 좁히는 조사
- `probe-verify`: 실제 실행 증거와 미검증을 구분
- `probe-explain`: 제출 확정 전 본인 구현 설명 연습

유사한 기능의 Matt Pocock와 Superpowers 스킬을 모두 켜지 않는다. 우리 기록과 절차로 충분하면 도구를 추가하지 않는다. 새 도구가 필요한 경우 실패 시 기존 흐름으로 복귀할 수 있어야 한다.

## 인기도 스냅샷

별 수는 2026-10-31 GitHub REST 응답 기준이고 이후 달라진다. 정확한 수치와 저장소 URL은 JSON에 보존했다.

| 저장소 | 별 수 |
|---|---:|
| obra/superpowers | 309,250 |
| mattpocock/skills | 307,231 |
| microsoft/markitdown | 193,036 |
| anthropics/skills | 185,093 |
| anthropics/claude-code | 153,947 |
| modelcontextprotocol/servers | 91,696 |
| upstash/context7 | 63,961 |
| ChromeDevTools/chrome-devtools-mcp | 54,490 |
| duckdb/duckdb | 42,690 |
| microsoft/playwright-mcp | 38,859 |
| github/github-mcp-server | 34,090 |
| vercel-labs/agent-skills | 33,250 |
| oraios/serena | 30,877 |
| openai/skills | 28,415 |
| huggingface/skills | 11,239 |
| trailofbits/skills | 7,893 |
| firecrawl/firecrawl-mcp-server | 7,728 |
| exa-labs/exa-mcp-server | 5,201 |
| tavily-ai/tavily-mcp | 2,464 |

## 아직 검증하지 않은 것

- 제공된 시험 Codex 버전에서 각 외부 스킬 또는 MCP가 실제로 로드되는지
- 네트워크 허용 범위, 서버 인증, 호출 제한과 토큰 비용
- 각 저장소의 모든 파일 및 종속 패키지 보안, 모든 과학적 주장
- 도구가 평가 점수를 높이는지 또는 특정 과제의 정답을 보장하는지

이번 작업에서 실행 검증한 것은 통합본의 설치 및 로컬 보조 도구다. 후보 도구 조사는 문서 검토와 실제 실행 검증을 구분해서 사용한다.
