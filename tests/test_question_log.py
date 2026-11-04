import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('question_log', ROOT / 'scripts/question_log.py')
logtool = importlib.util.module_from_spec(spec)
spec.loader.exec_module(logtool)


class QuestionLogTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.log = self.root / '.probe-kit/runtime/QUESTION_LOG.md'
        self.log.parent.mkdir(parents=True)
        self.initial = b'# Existing log\r\nDo not rewrite me.\r\n'
        self.log.write_bytes(self.initial)

    def test_verbatim_payloads_and_followup_preserve_existing_bytes(self):
        question = '  질문 | A?\r\n```text\r\n## S2-worker-a-Q999\r\n```\r\n'.encode()
        answer = '오탈자 그대루.\r\n수치: 001.00\n\n끝  '.encode()
        first = logtool.append(self.root, 'S2-worker-a', 'draft', 'AI 초안', question=question)
        self.assertEqual(first['qid'], 'S2-worker-a-Q001')
        old = self.log.read_bytes()
        result = logtool.append(self.root, 'S1-main', 'answer', '사용자 전달',
                                question=question, answer=answer, qid=first['qid'])
        current = self.log.read_bytes()
        self.assertTrue(current.startswith(old))
        self.assertIn(question, current[len(old):])
        self.assertIn(answer, current[len(old):])
        self.assertEqual(result['origin_session'], 'S2-worker-a')
        second = logtool.append(self.root, 'S2-worker-a', 'draft', 'AI 초안', question=b'next')
        self.assertEqual(second['qid'], 'S2-worker-a-Q002')
        self.assertEqual(logtool.existing_ids(self.log.read_bytes()), {first['qid'], second['qid']})

    def test_invalid_reference_and_incomplete_answer_do_not_mutate(self):
        for kwargs in ({'kind': 'answer', 'answer': b'answer', 'qid': 'S2-worker-a-Q999'},
                       {'kind': 'answer'}, {'kind': 'draft', 'question': b'\xff'}):
            with self.subTest(kwargs=kwargs), self.assertRaises((ValueError, UnicodeError)):
                logtool.append(self.root, 'S2-worker-a', source='fixture', **kwargs)
            self.assertEqual(self.log.read_bytes(), self.initial)

    def test_user_summary_and_correction_are_explicit_append_events(self):
        record = logtool.append(self.root, 'S4-data', 'user-summary', '사용자 요약', answer=b'summary')
        before = self.log.read_bytes()
        logtool.append(self.root, 'S4-data', 'correction', '담당자 정정', answer=b'correction', qid=record['qid'])
        self.assertTrue(self.log.read_bytes().startswith(before))
        self.assertIn('답변 원문 아님'.encode(), before)
        self.assertIn('답변 정정'.encode(), self.log.read_bytes())

    def test_parallel_cli_writes_lose_no_answers_or_ids(self):
        jobs = []
        for n in range(12):
            qfile, afile = self.root / f'q{n}', self.root / f'a{n}'
            qfile.write_bytes(f'question {n}\r\n'.encode())
            afile.write_bytes(f'answer {n}\r\n원문 유지  '.encode())
            command = [sys.executable, str(ROOT / 'scripts/question_log.py'),
                       '--workspace', str(self.root), '--session', 'S2-worker-a',
                       '--kind', 'answer', '--source', 'SYNTHETIC',
                       '--question-file', str(qfile), '--answer-file', str(afile)]
            jobs.append((subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE), qfile, afile))
        ids = []
        for process, qfile, afile in jobs:
            stdout, stderr = process.communicate(timeout=20)
            self.assertEqual(process.returncode, 0, stderr.decode())
            ids.append(json.loads(stdout)['qid'])
            self.assertIn(qfile.read_bytes(), self.log.read_bytes())
            self.assertIn(afile.read_bytes(), self.log.read_bytes())
        self.assertEqual(len(set(ids)), 12)
        self.assertEqual(len(logtool.existing_ids(self.log.read_bytes())), 12)
        self.assertTrue(self.log.read_bytes().startswith(self.initial))


if __name__ == '__main__':
    unittest.main()
