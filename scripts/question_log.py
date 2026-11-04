#!/usr/bin/env python3
"""Append verbatim question/answer events under a file lock (macOS/Linux)."""
import argparse
from datetime import datetime, timezone
import fcntl
import json
from pathlib import Path
import re
import sys

KINDS = {'draft': '질문 초안', 'sent': '전송 질문 확인', 'answer': '답변 수신',
         'correction': '답변 정정', 'user-summary': '사용자 요약 전달 (원문 아님)'}


def field(value, label):
    if not value or '\n' in value or '\r' in value:
        raise ValueError(f'{label}은 비어 있지 않은 한 줄이어야 합니다.')
    return value


def session_id(value):
    if not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9_-]{0,63}', value):
        raise ValueError('세션 ID는 영문/숫자/밑줄/하이픈으로 지정하세요.')
    return value


def raw_block(label, content):
    if content is None:
        return f'### {label}\n\n미제공 또는 미확인.\n\n'.encode()
    content.decode('utf-8')  # Validate without normalizing newlines or whitespace.
    longest = max((len(m.group()) for m in re.finditer(rb'`+', content)), default=0)
    fence = b'`' * max(3, longest + 1)
    separator = b'' if content.endswith(b'\n') else b'\n'
    return (f'### {label}\n\n<!-- raw-bytes: {len(content)} -->\n'.encode()
            + fence + b'text\n' + content + separator + fence + b'\n\n')


def existing_ids(content):
    """Ignore headings inside raw blocks when identifying actual record IDs."""
    result = set()
    fence = None
    for line in content.splitlines():
        if fence is not None:
            if re.fullmatch(re.escape(fence[:1]) + rb'{' + str(len(fence)).encode() + rb',}\s*', line):
                fence = None
            continue
        match = re.match(rb'^(`{3,}|~{3,})', line)
        if match:
            fence = match.group()
            continue
        match = re.fullmatch(rb'## ([A-Za-z0-9][A-Za-z0-9_-]{0,63}-Q[0-9]{3,})', line)
        if match:
            result.add(match.group(1).decode())
    return result


def append(workspace, session, kind, source, question=None, answer=None, summary=None,
           qid=None, origin_session=None, received_at=None):
    session_id(session)
    field(source, '출처')
    if kind not in KINDS:
        raise ValueError('지원하지 않는 기록 종류입니다.')
    if kind in ('draft', 'sent') and not question:
        raise ValueError('질문 초안/전송 확인에는 질문 텍스트가 필요합니다.')
    if kind in ('answer', 'correction', 'user-summary') and not answer:
        raise ValueError('답변 또는 사용자 요약 텍스트가 필요합니다.')
    if received_at is not None:
        field(received_at, '수신 시각')
    if qid is not None and not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9_-]{0,63}-Q[0-9]{3,}', qid):
        raise ValueError('발급된 Q-ID를 지정하세요.')
    origin = session_id(origin_session or (qid.rsplit('-Q', 1)[0] if qid else session))
    if qid and origin != qid.rsplit('-Q', 1)[0]:
        raise ValueError('기존 Q-ID의 진행 세션을 변경할 수 없습니다.')
    # Build raw blocks before touching the shared file.
    blocks = raw_block('질문 초안' if kind == 'draft' else '질문 원문', question)
    blocks += raw_block('사용자 전달 요약 (답변 원문 아님)' if kind == 'user-summary' else '답변 원문', answer)
    blocks += raw_block('AI 정리 (원문과 구분)', summary)
    log = Path(workspace).resolve(strict=True) / '.probe-kit/runtime/QUESTION_LOG.md'
    if log.is_symlink():
        raise ValueError('QUESTION_LOG에 심볼릭 링크를 사용하지 않습니다.')
    with log.open('r+b') as stream:
        fcntl.flock(stream.fileno(), fcntl.LOCK_EX)
        previous = stream.read()
        records = existing_ids(previous)
        if qid:
            if qid not in records:
                raise ValueError('기존 기록에 없는 Q-ID입니다. 새 질문은 --qid 없이 저장하세요.')
            if kind == 'draft':
                raise ValueError('새 초안은 --qid 없이 저장하세요.')
        else:
            ids = [item.rsplit('-Q', 1)[1] for item in records if item.rsplit('-Q', 1)[0] == origin]
            qid = f'{origin}-Q{max(map(int, ids), default=0) + 1:03d}'
        recorded = datetime.now(timezone.utc).isoformat(timespec='seconds')
        header = (f'\n## {qid}\n\n- 진행 세션: {origin}\n- 기록 세션: {session}\n'
                  f'- 상태: {KINDS[kind]}\n- 출처: {source}\n'
                  f'- 수신 시각: {received_at or "미확인"}\n- 기록 시각: {recorded}\n\n').encode()
        payload = header + blocks
        stream.seek(0, 2)
        stream.write(payload)
        stream.flush()
        stream.seek(len(previous))
        if stream.read() != payload:
            raise OSError('저장 후 원문 대조에 실패했습니다.')
    return {'qid': qid, 'origin_session': origin, 'recording_session': session,
            'kind': kind, 'path': str(log), 'raw_verified': True}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--workspace', default='.')
    p.add_argument('--session', required=True)
    p.add_argument('--kind', choices=KINDS, required=True)
    p.add_argument('--source', required=True)
    p.add_argument('--qid')
    p.add_argument('--origin-session')
    p.add_argument('--received-at')
    for name in ('question', 'answer', 'summary'):
        p.add_argument(f'--{name}-file', type=Path)
    args = vars(p.parse_args())
    try:
        for name in ('question', 'answer', 'summary'):
            file = args.pop(name + '_file')
            args[name] = file.read_bytes() if file is not None else None
        print(json.dumps(append(**args), ensure_ascii=False))
    except (ValueError, OSError, UnicodeError) as error:
        p.exit(2, str(error) + '\n')


if __name__ == '__main__':
    main()
