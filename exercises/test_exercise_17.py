import unittest
import subprocess
import os


class TestExercise17(unittest.TestCase):

    def run_exercise(self, input_value):
        """Helper method to run the exercise script with the provided input and return its output."""
        exercise_file_path = os.path.join(os.path.dirname(__file__), "exercise_17.py")
        return subprocess.check_output(['python3', exercise_file_path], input=input_value, text=True, universal_newlines=True)

    def test_lucky_ticket_true(self):
        """Ticket is lucky."""
        output = self.run_exercise("123321\n")
        self.assertIn("Happy", output)

    def test_lucky_ticket_false(self):
        """Ticket is not lucky."""
        output = self.run_exercise("123456\n")
        self.assertIn("Ordinary", output)


if __name__ == '__main__':
    unittest.main()
