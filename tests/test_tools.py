import contextlib
import importlib.util
import io
import json
from pathlib import Path
import subprocess
import tempfile
import unittest

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
        self.assertFalse((self.target / 'docs/handoff/sessions').exists())
        self.assertFalse((self.target / '.probe-kit/docs/handoff/sessions').exists())
        pointer = self.target / '.probe-kit/docs/handoff/CURRENT.md'
        self.assertIn('../../../docs/handoff/CURRENT.md', pointer.read_text())
        self.assertFalse((self.target / '.probe-kit/docs/reports/20261031-session-docs.md').exists())
        current.write_text('active task with decisions')
        session = self.target / 'docs/handoff/sessions/my-session.md'
        session.parent.mkdir()
        session.write_text('my handoff and uncommitted work')
        report = self.target / 'docs/reports/my-result.md'
        report.write_text('actual evidence')
        self.assertEqual(self.run_install().returncode, 0)
        self.assertEqual(current.read_text(), 'active task with decisions')
        self.assertEqual(session.read_text(), 'my handoff and uncommitted work')
        self.assertEqual(report.read_text(), 'actual evidence')
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


if __name__ == '__main__':
    unittest.main()
