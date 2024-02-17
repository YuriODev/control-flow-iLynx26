import unittest
import subprocess
import os

class TestBodyMassIndexCategorization(unittest.TestCase):
    def run_exercise(self, input_value):
        exercise_file_path = os.path.join(os.path.dirname(__file__), "example_17.py")
        return subprocess.check_output(['python3', exercise_file_path], input=input_value, text=True, universal_newlines=True)

    def test_underweight(self):
        output = self.run_exercise("1.8\n50\n")
        self.assertIn("underweight", output)

    def test_normal_weight(self):
        output = self.run_exercise("1.8\n70\n")
        self.assertIn("normal weight", output)

    def test_overweight(self):
        output = self.run_exercise("1.8\n90\n")
        self.assertIn("overweight", output)

if __name__ == '__main__':
    unittest.main()
