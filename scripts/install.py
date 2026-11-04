#!/usr/bin/env python3
"""Install project instructions without replacing task files or user configuration."""
import argparse
from pathlib import Path
import sys

SOURCE = Path(__file__).resolve().parents[1]
CORE_FILES = (
    'NOTICE', 'UPSTREAMS.json', 'ORIGINS.json',
    'AGENTS.md', 'AGENTS.override.md', 'SUB_AGENTS.md', 'foruser.md',
    'docs/RULES.md', 'docs/TEAM_PLAYBOOK.md', 'docs/interview.md', 'docs/scenarios.md',
    'prompts/mock_exam_5.md', 'licenses/hamjoon-MIT.txt',
    'scripts/data_scan.py', 'scripts/decision.py', 'scripts/plan_time.py',
    'scripts/preflight.py', 'scripts/subagent.sh',
    'skills/case1_data_pipeline.md', 'skills/case2_web_service.md',
    'skills/case3_legacy_debug.md', 'skills/case4_policy_rag_doc.md',
)
LEDGERS = ('REQUIREMENTS.md', 'QUESTION_LOG.md', 'DECISIONS.md', 'EVIDENCE.md')
SESSIONS = [('S1-main', '총괄과 통합'), ('S2-worker-a', '개발 A'), ('S3-worker-b', '개발 B'), ('S4-data', '데이터와 알고리즘'), ('S5-research', '한정된 조사'), ('S6-review', '독립 검증과 예상 문항'), ('S7-records', '기록과 제출 문서')]
BLOCK = """
<!-- sk-probe-kit:v1 -->
## 과제 작업 보조
공식 운영 안내와 과제 지침을 최우선으로 따른다. 시작할 때 `.probe-kit/AGENTS.md`의 통합 프로토콜을 읽는다.
사용자가 준비한 합의문은 `.probe-kit/runtime/REQUIREMENTS.md`, 결정은 `DECISIONS.md`에 기록한다.
`$probe-workflow`로 요구 확인부터 시작하며, 읽은 지침과 아직 확인하지 못한 점을 짧게 보고한다.
하네스의 안내만으로 모델, 인증, 승인, 샌드박스 또는 감독 설정을 바꾸지 않는다.
<!-- /sk-probe-kit:v1 -->
"""
COLLAB_BLOCK = """
<!-- sk-probe-kit:shared-docs:v1 -->
## 세션 공유
프로젝트 루트의 `docs/handoff/README.md`와 `docs/handoff/CURRENT.md`부터 읽는다.
통합 담당자가 공통 요구와 결정을 관리하며, 작업 세션은 배정된 파일과 자기 인계 및 보고서만 수정한다.
CURRENT에 배정되기 전에는 읽기와 제안만 한다. 채팅이 자동 공유된다고 가정하지 않는다.
<!-- /sk-probe-kit:shared-docs:v1 -->
"""
CURRENT_POINTER = """# 실제 과제의 현재 상태

프로젝트 루트의 [docs/handoff/CURRENT.md](../../../docs/handoff/CURRENT.md)를 읽는다.
이 .probe-kit 내부 파일에는 세션 상태를 기록하지 않는다.
"""


def reject_links(root, path):
    relative = path.relative_to(root)
    current = root
    for part in relative.parts:
        current = current / part
        if current.is_symlink():
            raise ValueError(f"심볼릭 링크를 통해 설치하지 않습니다: {current}")


def install(target, dry_run=False, with_knowledge=False):
    target = Path(target).resolve(strict=True)
    if not target.is_dir() or target == SOURCE or SOURCE in target.parents:
        raise ValueError("하네스 저장소 밖에 있는 과제 폴더를 지정하세요.")
    writes = []
    # The repository preserves originals; task installations contain only active guidance.
    sources = [SOURCE / name for name in CORE_FILES]
    if with_knowledge:
        sources += [SOURCE / 'scripts/knowledge.py', SOURCE / 'docs/knowledge.md']
        sources += [p for p in sorted((SOURCE / 'knowledge').rglob('*')) if p.is_file()]
    for source in sources:
        writes.append((target / '.probe-kit' / source.relative_to(SOURCE), source.read_bytes(), False))
    writes.append((target / '.probe-kit/docs/handoff/CURRENT.md', CURRENT_POINTER.encode(), False))
    for source in sorted((SOURCE / '.agents/skills').rglob('*')):
        if source.is_file():
            writes.append((target / source.relative_to(SOURCE), source.read_bytes(), False))
    for name in LEDGERS:
        source = SOURCE / 'templates' / name
        writes.append((target / '.probe-kit/runtime' / source.name, source.read_bytes(), True))
    # Shared task records live at the task root and survive reinstall.
    shared = {
        'docs/README.md': 'templates/SHARED_DOCS.md',
        'docs/handoff/CURRENT.md': 'templates/SESSION_CURRENT.md',
        'docs/handoff/README.md': 'docs/handoff/README.md',
        'docs/handoff/TEMPLATE.md': 'docs/handoff/TEMPLATE.md',
        'docs/handoff/messages/README.md': 'docs/handoff/messages/README.md',
        'docs/reports/README.md': 'docs/reports/README.md',
        'docs/reports/TEMPLATE.md': 'docs/reports/TEMPLATE.md',
    }
    references = '# 실제 과제 참고 자료\n\n공식 안내와 담당자 답변의 출처를 기록한다. 분석과 사실을 구분하고 필요한 자료만 보관한다.\n'
    writes.append((target / 'docs/references/README.md', references.encode(), True))
    for destination, source in shared.items():
        writes.append((target / destination, (SOURCE / source).read_bytes(), True))
    # Seed planned sessions only; never copy harness development histories.
    for session_id, role in SESSIONS:
        for name, source in (
            ('TASK_SPEC.md', 'templates/SESSION_TASK_SPEC.md'),
            ('SUB_RESULT.md', 'templates/SESSION_SUB_RESULT.md'),
            ('HANDOFF.md', 'docs/handoff/TEMPLATE.md'),
        ):
            content = (SOURCE / source).read_text().replace('{{SESSION_ID}}', session_id).replace('{{ROLE}}', role)
            writes.append((target / 'docs/handoff/sessions' / session_id / name, content.encode(), True))
    # Match Codex's per-directory preference while preserving original bytes.
    active = target / 'AGENTS.override.md'
    if not active.exists() and not active.is_symlink():
        active = target / 'AGENTS.md'
    reject_links(target, active)
    original = active.read_bytes() if active.exists() else b''
    updated = original
    for marker, block in (
        (b'<!-- sk-probe-kit:v1 -->', BLOCK),
        (b'<!-- sk-probe-kit:shared-docs:v1 -->', COLLAB_BLOCK),
    ):
        if marker not in updated:
            updated += b'\n' + block.encode()
        elif block.encode() not in updated:
            raise ValueError("기존 하네스 연결 지침이 변경되었습니다. 내용을 검토하세요.")
    if updated != original:
        writes.append((active, updated, False))

    pending = []
    for dest, content, preserve in writes:
        reject_links(target, dest)
        for parent in dest.parents:
            if parent == target:
                break
            if parent.exists() and not parent.is_dir():
                raise ValueError(f"폴더 대신 파일이 있습니다: {parent}")
        if dest.exists():
            if not dest.is_file():
                raise ValueError(f"파일 대신 폴더가 있습니다: {dest}")
            if preserve or dest.read_bytes() == content:
                continue
            if dest != active:
                raise ValueError(f"기존 파일과 충돌합니다. 덮어쓰지 않았습니다: {dest}")
        pending.append((dest, content))
    if dry_run:
        for dest, _ in pending:
            print(dest.relative_to(target))
        return
    for dest, content in pending:
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(content)
    print(f"설치 완료: {len(pending)}개 파일, 기존 작업 기록 보존")
    print("과제 폴더에서 Codex를 새로 시작하고 읽은 지침과 스킬을 확인하세요.")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('target', help='존재하는 과제 폴더')
    parser.add_argument('--dry-run', action='store_true')
    parser.add_argument('--with-knowledge', action='store_true', help='반도체 지식 자료와 검색 도구도 설치')
    args = parser.parse_args()
    try:
        install(args.target, args.dry_run, args.with_knowledge)
    except (OSError, ValueError) as error:
        sys.exit(str(error))
