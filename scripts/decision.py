#!/usr/bin/env python3
"""Append one decision without rewriting prior rows."""
import argparse
from datetime import datetime, timezone
from pathlib import Path


def cell(value):
    return str(value).replace('\\', '\\\\').replace('|', '\\|').replace('\r', ' ').replace('\n', '<br>')


def append(workspace, requirement, choice, alternative, reason, evidence, limit):
    root = Path(workspace).resolve(strict=True)
    dest = root / '.probe-kit/runtime/DECISIONS.md'
    for path in (root / '.probe-kit', dest.parent, dest):
        if path.is_symlink():
            raise ValueError('심볼릭 링크를 통해 기록하지 않습니다.')
    if not dest.is_file():
        raise ValueError('설치된 DECISIONS.md를 찾을 수 없습니다.')
    previous = dest.read_text(encoding='utf-8').rstrip()
    values = [datetime.now(timezone.utc).isoformat(timespec='seconds'), requirement,
              choice, alternative, reason, evidence, limit]
    with dest.open('a', encoding='utf-8') as stream:
        if previous and not previous.splitlines()[-1].startswith('|'):
            stream.write('\n| 시각 | 요구 ID | 선택 | 버린 대안 | 이유 | 검증 근거 | 남은 한계 |\n|---|---|---|---|---|---|---|\n')
        stream.write('| ' + ' | '.join(cell(value) for value in values) + ' |\n')
    print(dest)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--workspace', default='.')
    for name in ('requirement', 'choice', 'alternative', 'reason', 'evidence', 'limit'):
        parser.add_argument('--' + name, required=True)
    args = parser.parse_args()
    append(**vars(args))
