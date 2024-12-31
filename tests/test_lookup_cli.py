import unittest
from unittest.mock import patch, mock_open

import lookup_cli


class TestLookupCLI(unittest.TestCase):
    @patch("builtins.open", new_callable=mock_open, read_data="""
          - name: Alice
            age: 18
            occupation: student
          - name: Bob
            age: 33
            occupation: unemployed
    """)
    @patch("os.environ.get")
    def test_read_yaml(self, mock_env, mock_file):
        mock_env.return_value = "/fake/path/to/people.yaml"
        data = lookup_cli.read_yaml("/fake/path/to/people.yaml")
        self.assertEqual(len(data), 2)
        self.assertEqual(data[0]["name"], "Alice")
        self.assertEqual(data[1]["name"], "Bob")

    def test_lookup_found(self):
        data = [
            {"name": "Alice", "age": 18, "occupation": "student"},
            {"name": "Bob", "age": 33, "occupation": "unemployed"}
        ]
        self.assertEqual(lookup_cli.lookup("Alice", "age", data), 18)
        self.assertEqual(lookup_cli.lookup("Bob", "occupation", data), "unemployed")

    def test_lookup_name_not_found(self):
        data = [
            {"name": "Alice", "age": 18, "occupation": "student"},
            {"name": "Bob", "age": 33, "occupation": "unemployed"}
        ]
        self.assertEqual(lookup_cli.lookup("Charlie", "age", data), "Name not found")

    def test_lookup_field_not_found(self):
        data = [
            {"name": "Alice", "age": 18, "occupation": "student"},
            {"name": "Bob", "age": 33, "occupation": "unemployed"}
        ]
        self.assertEqual(lookup_cli.lookup("Alice", "salary", data), "Field not found")

    @patch("sys.argv", ["lookup-cli", "Alice", "age"])
    @patch("builtins.open", new_callable=mock_open, read_data="""
            - name: Alice
              age: 18
              occupation: student
            - name: Bob
              age: 33
              occupation: unemployed
    """)
    @patch("os.environ.get")
    def test_main_valid_input(self, mock_env, mock_file):
        mock_env.return_value = "/fake/path/to/people.yaml"
        with patch("builtins.print") as mock_print:
            lookup_cli.main()
            mock_print.assert_called_with(18)

    @patch("sys.argv", ["lookup-cli"])
    def test_main_missing_args(self):
        with patch("builtins.print") as mock_print, self.assertRaises(SystemExit) as cm:
            lookup_cli.main()
            mock_print.assert_called_with("Usage: lookup-cli <name> [<output_field>]")
            self.assertEqual(cm.exception.code, 1)

    @patch("sys.argv", ["lookup-cli", "Charlie", "age"])
    @patch("builtins.open", new_callable=mock_open, read_data="""
          - name: Alice
            age: 18
            occupation: student
          - name: Bob
            age: 33
            occupation: unemployed
    """)
    @patch("os.environ.get")
    def test_main_name_not_found(self, mock_env, mock_file):
        mock_env.return_value = "/fake/path/to/people.yaml"
        with patch("builtins.print") as mock_print:
            lookup_cli.main()
            mock_print.assert_called_with("Name not found")

    @patch("sys.argv", ["lookup-cli", "Alice", "salary"])
    @patch("builtins.open", new_callable=mock_open, read_data="""
        - name: Alice
          age: 18
          occupation: student
        - name: Bob
          age: 33
          occupation: unemployed
    """)
    @patch("os.environ.get")
    def test_main_field_not_found(self, mock_env, mock_file):
        mock_env.return_value = "/fake/path/to/people.yaml"
        with patch("builtins.print") as mock_print:
            lookup_cli.main()
            mock_print.assert_called_with("Field not found")

if __name__ == "__main__":
    unittest.main()
