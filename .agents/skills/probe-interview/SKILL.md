---
name: probe-interview
description: 현재 README, 데이터, 코드와 기존 문답에서 중요한 질문 최대 3개를 추천하고, 순서대로 받은 답변 원문을 QUESTION_LOG에 세션 출처와 함께 저장한다.
---

# 질문 추천과 답변 기록

`.probe-kit/AGENTS.md`, `.probe-kit/docs/interview.md`, CURRENT와 기존 QUESTION_LOG의 관련 부분을 읽는다. 키트 자체에서는 `.probe-kit/` 접두사를 뺀다. 현재 세션 ID는 사용자 선언/CURRENT에서 확인하며 터미널 이름을 자동으로 안다고 가정하지 않는다.

## 질문 준비

- README, 데이터와 코드에서 바로 확인할 수 있는 내용은 먼저 확인한다. 기존 문답에 답이 있으면 다시 묻지 않는다.
- 영향이 큰 미확인 조건을 최대 3개 고른다. 각 질문에 확인 이유와 답이 바꿀 구현/판정을 적는다. 맥락이 부족하면 업무/실패 사례를 묻고 이후 실제 예외 입력으로 좁힌다.
- 각 질문은 question_log.py의 `draft`로 저장해 Q-ID를 받고 사용자에게 번호 순서로 보여준다. 질문 예시가 필요할 때만 dm_question.md의 해당 절을 읽는다. 전송은 사용자가 한다.
- 답변을 기다리는 동안 답에 의존하지 않는 작업만 진행한다. 질문 수를 채우기 위해 조건을 만들어내지 않는다.

## 순서대로 답변 받기

같은 Q-ID의 마지막 기록까지 읽어 답변 수신/정정 상태를 확인한다. 사용자가 답만 붙여넣으면 현재 세션에서 대기 중인 첫 질문에 연결한다. 여러 질문에 답한 내용이거나 대응이 모호하면 확인하고, 잘못된 Q-ID에 저장하지 않는다. 첫 답으로 나머지가 해결되면 남은 질문을 조정한다.
질문 초안과 실제 전송 문구를 구분한다. 사용자가 초안 그대로 전송했다고 확인하면 그 문구를 사용하고, 수정했다면 실제 문구를 받는다. 확인되지 않으면 질문 원문 미확인으로 남긴다.

원문은 문장, 숫자, 오탈자, 줄바꿈을 그대로 UTF-8 임시 입력 파일에 저장하고 아래 도구로 추가한다. shell 문자열 보간으로 원문을 명령에 넣지 않는다. 임시 파일은 입력 전달용이며 기준 기록은 QUESTION_LOG다.

```bash
python3 .probe-kit/scripts/question_log.py --workspace . --session S2-worker-a --kind draft --question-file <질문파일> --source 'AI 질문 초안'
python3 .probe-kit/scripts/question_log.py --workspace . --session S2-worker-a --qid <발급된-ID> --kind answer --question-file <실제질문파일> --answer-file <답변파일> --source '사용자가 전달한 업무 담당자 답변' --summary-file <AI정리파일>
```

진행 세션이 다르면 `--origin-session`으로 지정한다. 질문 원문을 받지 못했으면 `--question-file`을 생략한다. 추가 답변은 같은 Q-ID에 `answer`, 정정은 `correction`으로 추가하며 이전 원문은 보존한다. 원문이 아닌 사용자 요약만 전달됐다면 `--kind user-summary`로 표시한다. 시각은 전달받았을 때만 `--received-at`에 넣는다.

도구는 파일 잠금으로 저장 순서를 보장하고 저장한 Q-ID를 반환한다. 파일을 다시 읽어 원문과 입력을 대조한 뒤 저장 완료를 알린다. AI 해석은 별도 항목이며 원문을 요약으로 대체하지 않는다.
S1은 Q-ID에서 REQUIREMENTS/DECISIONS와 검증으로 연결한다. 다른 세션은 자기 SUB_RESULT에 Q-ID와 구현 영향을 적고 S1에게 전달한다. 원문 저장 자체를 전체 요구 승인으로 처리하지 않는다.

첫 데이터 요약이나 구현 뒤 다시 호출하면 최신 결과에서 새로 드러난 조건만 고른다. 여러 담당자의 요구가 충돌하면 우선순위와 승인권자를 확인한다. 숨은 정답이나 채점 가산점을 가정하지 않는다.
