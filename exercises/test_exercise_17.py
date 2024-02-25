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


class TestExercise17(unittest.TestCase):

    def run_exercise(self, input_value):
        """Helper method to run the exercise script with the provided input and return its output."""
        exercise_file_path = os.path.join(
            os.path.dirname(__file__),
            "exercise_17.py"
        )
        return subprocess.check_output(
            ['python3', exercise_file_path],
            input=input_value,
            text=True,
            universal_newlines=True
        )

    def test_lucky_ticket_true(self):
        """Ticket is lucky."""
        output = self.run_exercise("123321\n")
        self.assertIn("Happy", output)

    def test_lucky_ticket_false(self):
        """Ticket is not lucky."""
        output = self.run_exercise("123456\n")
        self.assertIn("Ordinary", output)


def main():
    # Assume the script is in the same directory as this test runner
    script_path = os.path.join(os.path.dirname(__file__), "exercise_17.py")
    # Check if we should run the tests based on the script's output
    if not should_run_tests(script_path):
        print("You have not attempted to solve the problem yet")
    else:
        # If yes, run the tests
        unittest.main()


if __name__ == '__main__':
    main()
