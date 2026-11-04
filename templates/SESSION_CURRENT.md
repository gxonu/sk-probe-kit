# 현재 과제와 세션 배정

상태: 미시작. 아래 항목은 통합 담당자가 실제 과제에서 채운다.
이 파일은 수동 관리하며 실행 중인 세션을 자동 감지하지 않는다.

- 목표:
- 공식 규칙과 과제 위치:
- 시작 시각 / 마감 / 남은 시간 / 시간대:
- 시간표 입력과 plan_time.py 결과:
- 첫 전체 흐름 목표 / 기능 동결:
- 제출 시작 / 예정된 제출 확정 / 과제 확정 한계:
- 후속 서술형과 질문 생성 여유:
- S8 초안(첫 완주 뒤) / 전체 준비 시각 / lead 분 / 최종 변경 확인:
- 통합 담당 세션:
- 갱신 시각:
- 기준 커밋 / 브랜치:
- 공통 요구: `.probe-kit/runtime/REQUIREMENTS.md`
- 질문: `.probe-kit/runtime/QUESTION_LOG.md`
- 결정: `.probe-kit/runtime/DECISIONS.md`
- 검증: `.probe-kit/runtime/EVIDENCE.md`
- 현재 핵심 보고서:

## 배정과 파일 소유권

| 세션 ID | 역할 | 상태 | 쓰기 가능한 경로 | 완료 조건 | 갱신 시각 | 인계 문서 |
|---|---|---|---|---|---|---|
| S1-main | 총괄과 통합 | PLANNED | 미배정 | 실제 과제에서 확정 | - | [인계](sessions/S1-main/HANDOFF.md) |
| S2-worker-a | 개발 A | PLANNED | 미배정 | 실제 과제에서 확정 | - | [인계](sessions/S2-worker-a/HANDOFF.md) |
| S3-worker-b | 개발 B | PLANNED | 미배정 | 실제 과제에서 확정 | - | [인계](sessions/S3-worker-b/HANDOFF.md) |
| S4-data | 데이터와 알고리즘 | PLANNED | 미배정 | 실제 과제에서 확정 | - | [인계](sessions/S4-data/HANDOFF.md) |
| S5-research | 한정된 조사 | PLANNED | 미배정 | 실제 과제에서 확정 | - | [인계](sessions/S5-research/HANDOFF.md) |
| S6-review | 독립 검증과 제약 점검 | PLANNED | 미배정 | 실제 과제에서 확정 | - | [인계](sessions/S6-review/HANDOFF.md) |
| S7-records | 기록과 제출 문서 | PLANNED | 미배정 | 실제 과제에서 확정 | - | [인계](sessions/S7-records/HANDOFF.md) |
| S8-explain | 서술형 대비 | PLANNED | 미배정 | 실제 과제에서 확정 | - | [인계](sessions/S8-explain/HANDOFF.md) |

상태: PLANNED / ACTIVE / WAITING / HANDOFF / CLOSED. 통합 담당자가 등록한 범위에서만 편집한다.
이 파일과 REQUIREMENTS/DECISIONS/EVIDENCE는 S1이 갱신한다. QUESTION_LOG만 각 세션이 question_log.py로 추가한다.
기본 8개 역할만 준비한 상태다. S1이 실제 파일 범위와 자원을 배정한 뒤 ACTIVE로 바꾼다. 필요 없는 역할은 대기하며 세션은 사용자가 직접 연다.
세션별 sessions/<session-id>/TASK_SPEC.md는 메인이, SUB_RESULT.md와 HANDOFF.md는 해당 작업자가 관리한다.
수신한 요청 파일과 관련 인계만 읽고 필요한 근거로 이동한다.

## 실행 자원 소유권

| 서버/포트/DB/출력 경로 또는 무거운 명령 | 관리 세션 | 동시 사용 조건 / 인계 |
|---|---|---|

검토 세션은 실행 중인 공유 서버/DB를 임의로 초기화하지 않는다. 기록 담당의 공통 원장 반영안은 S1이 검토한다.

## 이번 결정과 열린 질문

- 최근 확정한 결정과 근거:
- 해결되지 않은 질문:
- 인계 수신 및 반영 여부:

## 다음 행동

1.
2.
3.

시작 절차: docs/handoff/README.md. 세션 양식: docs/handoff/TEMPLATE.md.
