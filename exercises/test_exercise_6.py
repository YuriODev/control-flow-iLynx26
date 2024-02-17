import unittest
import subprocess
import os


class TestExercise6(unittest.TestCase):

    def run_exercise(self, input_value):
        """Helper method to run the exercise script with the provided input and return its output."""
        exercise_file_path = os.path.join(os.path.dirname(__file__), "exercise_6.py")
        return subprocess.check_output(['python3', exercise_file_path], input=input_value, text=True, universal_newlines=True)

    def test_point_a_further(self):
        """Point A is further from the origin than B."""
        output = self.run_exercise("3\n4\n1\n2\n")
        self.assertIn("A is further from the origin.", output)

    def test_point_b_further(self):
        """Point B is further from the origin than A."""
        output = self.run_exercise("1\n1\n4\n5\n")
        self.assertIn("B is further from the origin.", output)

    def test_same_distance(self):
        """Points A and B are at the same distance from the origin."""
        output = self.run_exercise("3\n4\n-3\n-4\n")
        self.assertIn("A and B are at the same distance from the origin.", output)


if __name__ == '__main__':
    unittest.main()