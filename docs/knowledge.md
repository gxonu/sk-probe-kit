# 반도체 지식 패키지 사용

원본: [xodbs1021/kty-codex-harness-template](https://github.com/xodbs1021/kty-codex-harness-template/tree/62f0715bbf79e959a8332dc19e828de176a0b5ef/knowledge/semiconductor).
원본 README는 65개 개념과 84개 공개 출처를 설명한다. 이 통합 작업에서 개별 과학적 주장을 모두 재검증한 것은 아니다.

사용자 요청에 따라 원본 폴더를 이 저장소의 `knowledge/semiconductor/`에 보존했다. 본 통합본이 원저작권이나 새 라이선스를 주장하지 않는다. 출처와 고정 버전은 UPSTREAMS.json과 ORIGINS.json에 있다.

--with-knowledge로 선택 설치한 뒤 과제 루트에서 검색한다. 기본 설치에 없는 경우 키트 설치기에 같은 옵션을 붙여 추가한다. 추가 다운로드는 필요 없다.

```bash
python3 .probe-kit/scripts/knowledge.py search .probe-kit/knowledge/semiconductor HBM
python3 .probe-kit/scripts/knowledge.py search .probe-kit/knowledge/semiconductor 수율
```

검색 결과의 `path`는 `.probe-kit/knowledge/semiconductor` 기준이다. 관련 문서만 읽고 근거가 중요한 수치와 조건은 연결된 원출처를 확인한다. KTY의 별도 하네스나 작업 지침보다 우리 공식 규칙과 과제의 요구가 우선한다.

확인 순서:

1. 과제에서 실제로 등장한 용어, 단위, 측정 조건을 찾는다.
2. 색인에서 관련 항목 1~3개를 골라 본문과 적용 조건을 확인한다.
3. 자료의 예제 숫자를 실제 공정 사양이나 합격 기준으로 쓰지 않는다.
4. REQUIREMENTS에 업무 확인이 필요한 조건, DECISIONS에 사용한 문서 ID와 가정을 적는다.
5. 검색 결과가 없거나 자료가 부족하면 추정하지 않고 담당자 질문을 만든다.

외부 원본 저장소의 공개 유지 여부는 이 통합본에서 통제할 수 없다. 결과 통지 전 공개 유지 조건을 충족하는지 사전에 확인한다.
