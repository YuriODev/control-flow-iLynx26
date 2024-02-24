import unittest
import subprocess
import os


class TestExercise17(unittest.TestCase):

    def run_exercise(self, input_value):
        """Helper method to run the exercise script with the provided input and return its output."""
        exercise_file_path = os.path.join(os.path.dirname(__file__), "exercise_17.py")
        return subprocess.check_output(['python3', exercise_file_path], input=input_value, text=True, universal_newlines=True)

    @unittest.skipIf(os.environ.get('RUN_TESTS') != '1', "Skipping test because RUN_TESTS environment variable is not set to 1")
    def test_lucky_ticket_true(self):
        """Ticket is lucky."""
        output = self.run_exercise("123321\n")
        self.assertIn("Happy", output)

    @unittest.skipIf(os.environ.get('RUN_TESTS') != '1', "Skipping test because RUN_TESTS environment variable is not set to 1")
    def test_lucky_ticket_false(self):
        """Ticket is not lucky."""
        output = self.run_exercise("123456\n")
        self.assertIn("Ordinary", output)

def run_tests_manually():
    suite = unittest.TestSuite()
    suite.addTest(TestExercise17('test_lucky_ticket_true'))
    suite.addTest(TestExercise17('test_lucky_ticket_false'))
    
    result = unittest.TestResult()
    suite.run(result)
    
    print(result.wasSuccessful())
    print(result.skipped)
    if not result.wasSuccessful() and result.skipped:
        if len(result.skipped) == 2:
            print("You have not attempted to solve the problem yet")
        else:
            for test, reason in result.skipped:
                print(f"Skipped {test}: {reason}")
            for test, err in result.errors:
                print(f"Error {test}: {err}")
            for test, err in result.failures:
                print(f"Failure {test}: {err}")
    else:
        print("All tests passed successfully!")

if __name__ == '__main__':
    if os.environ.get('RUN_TESTS') != '0':
        run_tests_manually()
    else:
        print("You have not attempted to solve the problem yet")
