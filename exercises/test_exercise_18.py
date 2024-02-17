import unittest
from unittest.mock import patch
import subprocess
import os


class TestGreetingDecision(unittest.TestCase):

    def run_exercise(self, inputs):
        """Helper method to run the exercise script with the provided inputs and return its output."""
        # The inputs list is joined into a single string, each separated by '\n'
        input_value = '\n'.join(inputs) + '\n'
        return subprocess.check_output(['python3', 'exercise_18.py'], input=input_value, text=True, universal_newlines=True)

    def test_remember_name_yes_ex_yes_drunk_yes_rekindle(self):
        inputs = ['yes', 'yes', 'yes', 'yes']
        output = self.run_exercise(inputs)
        self.assertIn("Say hi.", output)

    def test_remember_name_yes_ex_yes_drunk_no(self):
        inputs = ['yes', 'yes', 'yes', 'no']
        output = self.run_exercise(inputs)
        self.assertIn("Don't say hi.", output)

    def test_remember_name_yes_ex_no_friend_ex_yes(self):
        inputs = ['yes', 'no', 'yes']
        output = self.run_exercise(inputs)
        self.assertIn("Don't say hi.", output)

    def test_remember_name_yes_ex_no_friend_ex_no_enemy_no_convertible_yes(self):
        inputs = ['yes', 'no', 'no', 'no', 'yes']
        output = self.run_exercise(inputs)
        self.assertIn("Don't say hi.", output)

    def test_remember_name_no_time_to_flee_yes(self):
        inputs = ['no', 'yes']
        output = self.run_exercise(inputs)
        self.assertIn("Run for it.", output)

    def test_remember_name_no_time_to_flee_no_pretend_call_yes(self):
        inputs = ['no', 'no', 'yes']
        output = self.run_exercise(inputs)
        self.assertIn("Hello, doctor. What are my test results?", output)

    # ... more tests covering all branches of the decision tree


if __name__ == '__main__':
    # Path to the script that contains the decision logic
    # exercise_file_path = os.path.join(os.path.dirname(__file__), "greeting_decision.py")
    unittest.main()
