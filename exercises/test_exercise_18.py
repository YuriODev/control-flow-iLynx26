import unittest
import subprocess
import os


# Helper method to check if we should run tests based on script output
def should_run_tests(script_path):
    try:
        completed_process = subprocess.run(
            ['python3', script_path],
            text=True,
            capture_output=True,
            check=True
        )
        output = completed_process.stdout.strip()
        # print(f"{output = }")
        # print(f"{bool(output) = }")
        # Here you can add more sophisticated checks based on the script's output
        return bool(output)  # Run tests if there's any output
    except subprocess.CalledProcessError as e:
        print(f"Error executing script: {e}")
        return True  # run tests in case of script execution error
    

class TestGreetingDecision(unittest.TestCase):

    def run_exercise(self, input_value):
        """Helper method to run the exercise script with the provided input and return its output."""
        exercise_file_path = os.path.join(
            os.path.dirname(__file__),
            "exercise_18.py"
        )
        return subprocess.check_output(
            ['python3', exercise_file_path],
            input=input_value,
            text=True,
            universal_newlines=True
        )
        

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


def main():
    # Assume the script is in the same directory as this test runner
    script_path = os.path.join(os.path.dirname(__file__), "exercise_18.py")
    # Check if we should run the tests based on the script's output
    if not should_run_tests(script_path):
        print("You have not attempted to solve the problem yet")
    else:
        # If yes, run the tests
        unittest.main()


if __name__ == '__main__':
    main()
