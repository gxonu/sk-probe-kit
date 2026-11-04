import contextlib
import importlib.util
import io
import json
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch
from datetime import datetime

ROOT = Path(__file__).resolve().parents[1]


def module(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / 'scripts' / f'{name}.py')
    loaded = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(loaded)
    return loaded


class InstallTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.target = self.root / 'task with spaces'
        self.target.mkdir()

    def run_install(self, *extra):
        return subprocess.run(['bash', str(ROOT / 'install.sh'), str(self.target), *extra],
                              text=True, capture_output=True)

    def test_preserve_and_repeat(self):
        instructions = self.target / 'AGENTS.md'
        instructions.write_bytes(b'# Platform\nPreserve these instructions.\n')
        readme = self.target / 'README.md'
        readme.write_text('task specification')
        git_config = self.target / '.git/config'
        git_config.parent.mkdir()
        git_config.write_text('platform sentinel')
        self.assertEqual(self.run_install().returncode, 0)
        self.assertTrue(instructions.read_bytes().startswith(b'# Platform\nPreserve these instructions.\n'))
        runtime = self.target / '.probe-kit/runtime/DECISIONS.md'
        runtime.write_text('my work')
        first = instructions.read_bytes()
        self.assertEqual(self.run_install().returncode, 0)
        self.assertEqual(instructions.read_bytes(), first)
        self.assertEqual(runtime.read_text(), 'my work')
        self.assertEqual(readme.read_text(), 'task specification')
        self.assertEqual(git_config.read_text(), 'platform sentinel')
        self.assertFalse((self.target / '.codex').exists())

    def test_override_is_active(self):
        (self.target / 'AGENTS.md').write_text('ordinary')
        (self.target / 'AGENTS.override.md').write_text('active')
        self.assertEqual(self.run_install().returncode, 0)
        self.assertEqual((self.target / 'AGENTS.md').read_text(), 'ordinary')
        self.assertIn('sk-probe-kit:v1', (self.target / 'AGENTS.override.md').read_text())

    def test_shared_docs_seed_and_existing_records_survive(self):
        readme = self.target / 'docs/README.md'
        readme.parent.mkdir()
        readme.write_text('existing project docs')
        self.assertEqual(self.run_install().returncode, 0)
        self.assertEqual(readme.read_text(), 'existing project docs')
        current = self.target / 'docs/handoff/CURRENT.md'
        self.assertEqual(current.read_bytes(), (ROOT / 'templates/SESSION_CURRENT.md').read_bytes())
        # The harness development session must not become the task's active session.
        self.assertEqual({p.name for p in (self.target / 'docs/handoff/sessions').iterdir()},
                         {sid for sid, _ in module('install').SESSIONS})
        for sid, _ in module('install').SESSIONS:
            for name in ('TASK_SPEC.md', 'SUB_RESULT.md', 'HANDOFF.md'):
                p = self.target / 'docs/handoff/sessions' / sid / name
                self.assertTrue(p.is_file())
                p.write_text(f'existing {sid} {name}')
        self.assertFalse((self.target / '.probe-kit/docs/handoff/sessions').exists())
        pointer = self.target / '.probe-kit/docs/handoff/CURRENT.md'
        self.assertIn('../../../docs/handoff/CURRENT.md', pointer.read_text())
        self.assertFalse((self.target / '.probe-kit/docs/reports/20261031-session-docs.md').exists())
        current.write_text('active task with decisions')
        session = self.target / 'docs/handoff/sessions/my-session.md'
        session.parent.mkdir(exist_ok=True)
        session.write_text('my handoff and uncommitted work')
        report = self.target / 'docs/reports/my-result.md'
        report.write_text('actual evidence')
        self.assertEqual(self.run_install().returncode, 0)
        self.assertEqual(current.read_text(), 'active task with decisions')
        self.assertEqual(session.read_text(), 'my handoff and uncommitted work')
        self.assertEqual(report.read_text(), 'actual evidence')
        for sid, _ in module('install').SESSIONS:
            for name in ('TASK_SPEC.md', 'SUB_RESULT.md', 'HANDOFF.md'):
                self.assertEqual((self.target / 'docs/handoff/sessions' / sid / name).read_text(),
                                 f'existing {sid} {name}')
        self.assertTrue((self.target / 'docs/references/cofa-probe-interview-20261031.md').is_file())

    def test_shared_docs_symlink_fails_before_any_write(self):
        external = self.root / 'external docs'
        external.mkdir()
        (self.target / 'docs').symlink_to(external, target_is_directory=True)
        self.assertNotEqual(self.run_install().returncode, 0)
        self.assertFalse((self.target / '.probe-kit').exists())
        self.assertFalse((self.target / 'AGENTS.md').exists())
        self.assertEqual(list(external.iterdir()), [])

    def test_existing_v1_instruction_gets_shared_docs_once(self):
        legacy = '# Existing platform rules\n' + module('install').BLOCK
        active = self.target / 'AGENTS.md'
        active.write_text(legacy)
        self.assertEqual(self.run_install().returncode, 0)
        first = active.read_text()
        self.assertTrue(first.startswith(legacy))
        self.assertEqual(first.count('<!-- sk-probe-kit:shared-docs:v1 -->'), 1)
        self.assertEqual(self.run_install().returncode, 0)
        self.assertEqual(active.read_text(), first)

    def test_dry_run_does_not_write(self):
        self.assertEqual(self.run_install('--dry-run').returncode, 0)
        self.assertEqual(list(self.target.iterdir()), [])

    def test_conflict_is_detected_before_writes(self):
        conflict = self.target / '.agents/skills/probe-workflow/SKILL.md'
        conflict.parent.mkdir(parents=True)
        conflict.write_text('existing skill')
        self.assertNotEqual(self.run_install().returncode, 0)
        self.assertFalse((self.target / 'AGENTS.md').exists())
        self.assertFalse((self.target / '.probe-kit').exists())
        self.assertEqual(conflict.read_text(), 'existing skill')

    def test_symlink_cannot_redirect_install(self):
        external = self.root / 'elsewhere'
        external.mkdir()
        (self.target / '.probe-kit').symlink_to(external, target_is_directory=True)
        self.assertNotEqual(self.run_install().returncode, 0)
        self.assertEqual(list(external.iterdir()), [])
        self.assertFalse((self.target / 'AGENTS.md').exists())

    def test_original_assets_and_knowledge_are_installed(self):
        self.assertEqual(self.run_install().returncode, 0)
        for relative in ('skills/case1_data_pipeline.md', 'knowledge/semiconductor/index.jsonl',
                         'references/written-prep.original.md', 'AGENTS.override.md'):
            self.assertEqual((self.target / '.probe-kit' / relative).read_bytes(),
                             (ROOT / relative).read_bytes())

    def test_eight_roles_and_practical_materials_only(self):
        self.assertEqual(self.run_install().returncode, 0)
        sessions = self.target / 'docs/handoff/sessions'
        self.assertEqual(len(list(sessions.iterdir())), 8)
        self.assertTrue((sessions / 'S8-explain/SUB_RESULT.md').is_file())
        self.assertTrue((self.target / '.probe-kit/scripts/question_log.py').is_file())
        self.assertTrue((self.target / '.probe-kit/prompts/mock_exam_6.md').is_file())
        for path in ('upstream', 'knowledge/semiconductor/reviews', 'docs/CLEANUP.md',
                     'docs/TOOL_SURVEY.md', 'runtime/HANDOFF.md', 'runtime/SUBMISSION_REPORT.md'):
            self.assertFalse((self.target / '.probe-kit' / path).exists(), path)

    def test_decision_preserves_history_and_escapes_cells(self):
        self.assertEqual(self.run_install().returncode, 0)
        file = self.target / '.probe-kit/runtime/DECISIONS.md'
        previous = file.read_text()
        with contextlib.redirect_stdout(io.StringIO()):
            module('decision').append(self.target, 'R-01', 'A|B\nC', 'D', 'reason', 'NOT_RUN', 'limit')
        self.assertTrue(file.read_text().startswith(previous))
        self.assertIn('A\\|B<br>C', file.read_text())
        self.assertIn('| R-01 |', file.read_text())


class DataTests(unittest.TestCase):
    def test_sample_and_exact_end_are_distinct(self):
        with tempfile.TemporaryDirectory() as directory:
            file = Path(directory) / 'input.csv'
            text = 'id,value\n1,\n1,\n2,ok\n'
            file.write_text(text)
            short = module('data_scan').scan(file, 2)
            full = module('data_scan').scan(file, 3)
            self.assertTrue(short['truncated'])
            self.assertFalse(full['truncated'])
            self.assertEqual(short['duplicate_full_rows_in_scan'], 1)
            self.assertEqual(short['columns'][1]['empty'], 2)
            self.assertEqual(file.read_text(), text)

    def test_duplicate_columns_and_missing_cells(self):
        with tempfile.TemporaryDirectory() as directory:
            file = Path(directory) / 'input.csv'
            file.write_text('id,id,value\n1,2\n3,4,x,extra\n')
            result = module('data_scan').scan(file)
            self.assertEqual(result['duplicate_headers'], ['id'])
            self.assertEqual(result['malformed_rows_in_scan'], 2)
            self.assertEqual(result['columns'][2]['empty'], 1)

    def test_empty_input_is_not_success(self):
        with tempfile.TemporaryDirectory() as directory:
            file = Path(directory) / 'input.csv'
            file.write_text('')
            with self.assertRaises(ValueError):
                module('data_scan').scan(file)

    def test_knowledge_search_has_limit_and_count(self):
        with tempfile.TemporaryDirectory() as directory:
            file = Path(directory) / 'index.jsonl'
            rows = [{'id': str(i), 'title': 'HBM', 'path': f'{i}.md'} for i in range(3)]
            file.write_text('\n'.join(json.dumps(x) for x in rows))
            buffer = io.StringIO()
            with contextlib.redirect_stdout(buffer):
                module('knowledge').search(directory, 'hbm', 1)
            result = json.loads(buffer.getvalue())
            self.assertEqual(result['matches'], 3)
            self.assertEqual(len(result['shown']), 1)


class TimePlanTests(unittest.TestCase):
    def test_full_window_reserves_submission_and_written_time(self):
        p = module('plan_time').plan('2026-10-31T10:00:00+09:00', '2026-10-31T14:00:00+09:00')
        self.assertEqual(p['feature_freeze'], '2026-10-31T12:20:00+09:00')
        self.assertEqual(p['submission_start'], '2026-10-31T12:50:00+09:00')
        self.assertEqual(p['task_finish_by'], '2026-10-31T13:00:00+09:00')

    def test_late_start_shortens_work_before_hard_end(self):
        p = module('plan_time').plan('2026-10-31T11:00:00+09:00', '2026-10-31T14:00:00+09:00')
        self.assertEqual(p['task_budget_minutes'], 140)
        self.assertEqual(p['task_finish_by'], '2026-10-31T13:20:00+09:00')
        self.assertEqual(p['written_finish_if_task_ends_at_limit'], p['hard_end'])

    def test_different_offsets_describe_the_same_deadline(self):
        p = module('plan_time').plan('2026-10-31T11:00:00+09:00', '2026-10-31T05:00:00+00:00')
        self.assertEqual(p['task_budget_minutes'], 140)
        self.assertLessEqual(datetime.fromisoformat(p['written_finish_if_task_ends_at_limit']),
                             datetime.fromisoformat(p['hard_end']))

    def test_short_window_has_ordered_checkpoints(self):
        p = module('plan_time').plan('2026-10-31T13:00:00+09:00', '2026-10-31T14:00:00+09:00')
        times = [datetime.fromisoformat(p[k]) for k in
                 ('start', 'requirements_target', 'first_flow_target', 'feature_freeze', 'submission_start', 'task_finish_by')]
        self.assertEqual(times, sorted(times))
        self.assertTrue(p['short_budget'])

    def test_missing_timezone_and_impossible_window_are_rejected(self):
        for start, end in [('2026-10-31T10:00:00', '2026-10-31T14:00:00+09:00'),
                           ('2026-10-31T13:30:00+09:00', '2026-10-31T14:00:00+09:00'),
                           ('2026-10-31T15:00:00+09:00', '2026-10-31T14:00:00+09:00')]:
            with self.subTest(start=start), self.assertRaises(ValueError):
                module('plan_time').plan(start, end)

    def test_explanation_tracks_planned_submission_and_custom_lead(self):
        result = module('plan_time').plan('2026-11-04T19:00:00+09:00', '2026-11-04T23:00:00+09:00',
                                          submission_at='2026-11-04T21:40:00+09:00', explain_lead_minutes=30)
        self.assertEqual(result['explain_full_prep'], '2026-11-04T21:10:00+09:00')
        self.assertEqual(result['submission_start'], '2026-11-04T21:30:00+09:00')
        self.assertEqual(result['task_finish_by'], '2026-11-04T22:00:00+09:00')

    def test_explanation_does_not_consume_submission_buffer_in_short_window(self):
        result = module('plan_time').plan('2026-11-04T22:00:00+09:00', '2026-11-04T23:00:00+09:00')
        self.assertTrue(result['explain_shortened'])
        self.assertLessEqual(result['start'], result['explain_full_prep'])
        self.assertLessEqual(result['explain_full_prep'], result['submission_start'])

    def test_invalid_preparation_window_is_rejected(self):
        for options in ({'explain_lead_minutes': -1},
                        {'submission_at': '2026-11-04T22:30:00+09:00'},
                        {'submission_at': '2026-11-04T21:00:00'},
                        {'submission_at': '2026-11-04T18:00:00+09:00'}):
            with self.subTest(options=options), self.assertRaises(ValueError):
                module('plan_time').plan('2026-11-04T19:00:00+09:00', '2026-11-04T23:00:00+09:00', **options)


class PreflightTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        with contextlib.redirect_stdout(io.StringIO()):
            module('install').install(self.root)

    def test_missing_required_record_is_reported_without_repair(self):
        preflight = module('preflight')
        self.assertEqual(preflight.inspect(self.root, files_only=True)['local_status'], 'PASS')
        record = self.root / '.probe-kit/runtime/REQUIREMENTS.md'
        record.unlink()
        result = preflight.inspect(self.root, files_only=True)
        self.assertEqual(result['local_status'], 'FAIL')
        self.assertFalse(record.exists())
        self.assertEqual(result['manual_status'], 'NOT_RUN')

    def test_broken_codex_cli_fails_without_installing_or_changing_config(self):
        preflight = module('preflight')
        failure = subprocess.CompletedProcess(['codex', '--version'], 1, '', 'Missing optional dependency')
        with patch.object(preflight.shutil, 'which', return_value='/usr/bin/codex'), \
             patch.object(preflight.subprocess, 'run', return_value=failure) as run:
            result = preflight.inspect(self.root)
        self.assertEqual(result['local_status'], 'FAIL')
        self.assertEqual(run.call_args.args[0], ['/usr/bin/codex', '--version'])
        self.assertFalse((self.root / '.codex').exists())


if __name__ == '__main__':
    unittest.main()
