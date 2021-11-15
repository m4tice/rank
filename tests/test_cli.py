from click.testing import CliRunner
import unittest
import rank.cli as cli

class CLITests(unittest.TestCase):

    def test_input(self):
        file_name = './data/sample-input.txt'
        runner = CliRunner()
        result = runner.invoke(cli.cli, ['-i', file_name])
        self.assertEqual(result.exit_code, 0)
    
    def test_unknown_file(self):
        file_name = 'unknown.txt'
        expected_output = '- Extract phase Started\n- Error: file not found.\n'
        runner = CliRunner()
        result = runner.invoke(cli.cli, ['-i', file_name])
        self.assertEqual(result.exit_code, 0)
        self.assertEqual(result.output, '- Extract phase Started\n- Error: file not found.\n')

    def test_empty_data_(self):
        file_name = './tests/test-input-empty.txt'
        expected_output = '- Extract phase Started\n- Extract phase Ended\n- Transform phase Started\n- Error: wrong data format.\n'
        runner = CliRunner()
        result = runner.invoke(cli.cli, ['-i', file_name])
        self.assertEqual(result.exit_code, 0)
        self.assertEqual(result.output, expected_output)

    def test_wrong_data_format(self):
        file_name = './tests/test-input-wrong-format.txt'
        expected_output = '- Extract phase Started\n- Error: wrong data format.\n'
        runner = CliRunner()
        result = runner.invoke(cli.cli, ['-i', file_name])
        self.assertEqual(result.exit_code, 0)
        self.assertEqual(result.output, expected_output)

if __name__ == '__main__':
    unittest.main()