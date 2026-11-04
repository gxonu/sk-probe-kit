#!/usr/bin/env python3
"""Fetch a pinned upstream knowledge folder locally, or search its index offline."""
import argparse
import json
from pathlib import Path
import subprocess
import tempfile
import shutil
import sys

KIT = Path(__file__).resolve().parents[1]


def fetch(destination):
    metadata = json.loads((KIT / 'UPSTREAMS.json').read_text())['knowledge']
    dest = Path(destination).expanduser().absolute()
    if dest.exists() or dest.is_symlink():
        raise ValueError('대상이 이미 존재합니다. 기존 자료를 덮어쓰지 않습니다.')
    dest.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='probe-knowledge-') as temporary:
        repo = Path(temporary) / 'source'
        repo.mkdir()
        def git(*args):
            return subprocess.run(['git', '-C', str(repo), *args], check=True,
                                  stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True).stdout.strip()
        git('init', '-q')
        git('remote', 'add', 'origin', metadata['url'])
        git('sparse-checkout', 'init', '--cone')
        git('sparse-checkout', 'set', 'knowledge/semiconductor')
        git('fetch', '--depth', '1', 'origin', metadata['commit'])
        git('checkout', '--detach', 'FETCH_HEAD')
        if git('rev-parse', 'HEAD') != metadata['commit']:
            raise ValueError('요청한 커밋과 실제 커밋이 다릅니다.')
        knowledge = repo / 'knowledge/semiconductor'
        if not (knowledge / 'index.jsonl').is_file():
            raise ValueError('원본 색인을 찾지 못했습니다.')
        for file in knowledge.rglob('*'):
            if file.is_symlink():
                raise ValueError('원본 지식 폴더에 심볼릭 링크가 있습니다.')
        # The fetched reference package is copied without executing its code.
        shutil.copytree(knowledge, dest)
        (dest / 'UPSTREAM_PIN.json').write_text(json.dumps(metadata, indent=2) + '\n')
    print(f'원본 지식 폴더 준비 완료: {dest}')
    print('읽기용 참고 자료입니다. 과제 조건과 개별 출처를 우선 확인하세요.')


def search(folder, query, limit=6):
    if limit < 1:
        raise ValueError('limit must be positive')
    found = []
    with (Path(folder) / 'index.jsonl').open(encoding='utf-8') as stream:
        for line in stream:
            item = json.loads(line)
            fields = [item.get(key, '') for key in ('title', 'aliases', 'keywords', 'problem_signals', 'id')]
            if query.casefold() in json.dumps(fields, ensure_ascii=False).casefold():
                found.append({key: item.get(key) for key in ('id', 'title', 'path', 'source_ids')})
    print(json.dumps({'matches': len(found), 'shown': found[:limit]}, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    sub = p.add_subparsers(dest='action', required=True)
    f = sub.add_parser('fetch')
    f.add_argument('destination', help='과제 폴더 밖의 새 로컬 폴더 권장')
    s = sub.add_parser('search')
    s.add_argument('folder')
    s.add_argument('query')
    s.add_argument('--limit', type=int, default=6)
    args = p.parse_args()
    try:
        if args.action == 'fetch':
            fetch(args.destination)
        else:
            search(args.folder, args.query, args.limit)
    except subprocess.CalledProcessError as error:
        sys.exit('지식 자료 다운로드 실패. 기본 하네스는 그대로 사용할 수 있습니다.\n' + error.stderr[-1000:])
    except (ValueError, OSError) as error:
        sys.exit(str(error))
