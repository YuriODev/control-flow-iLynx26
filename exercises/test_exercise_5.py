import unittest
import subprocess
import os

class TestQuadraticSolver(unittest.TestCase):

    def run_exercise(self, a, b, c):
        """Helper method to run the exercise script with the provided coefficients and return its output."""
        exercise_file_path = os.path.join(os.path.dirname(__file__), "exercise_5.py")
        process = subprocess.Popen(['python3', exercise_file_path], text=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        output, _ = process.communicate(input=f"{a}\n{b}\n{c}\n")
        return output.strip()

    def test_two_distinct_roots(self):
        """Quadratic equation with two distinct real roots."""
        output = self.run_exercise(1, -3, 2)
        self.assertIn("and", output)

    def test_single_root(self):
        """Quadratic equation with a single real root (discriminant is zero)."""
        output = self.run_exercise(1, -2, 1)
        self.assertTrue(any(x in output for x in ["1.0", "-1.0"]))  # Check for the presence of the root

    def test_no_real_roots(self):
        """Quadratic equation with no real roots (negative discriminant)."""
        output = self.run_exercise(1, 2, 5)
        self.assertIn("No roots.", output)

    def test_linear_equation_one_root(self):
        """Linear equation with one root."""
        output = self.run_exercise(0, 2, -4)
        self.assertIn("2.0", output)

    def test_invalid_linear_equation(self):
        """Invalid linear equation (b=0, c!=0)."""
        output = self.run_exercise(0, 0, 3)
        self.assertIn("No roots.", output)

    def test_linear_equation_c_zero(self):
        """Linear equation reduced to c=0 (b!=0)."""
        output = self.run_exercise(0, 2, 0)
        self.assertIn("0", output)

    def test_b_zero_c_nonzero_positive_roots(self):
        """Quadratic equation with b=0 and c!=0 leading to positive roots."""
        output = self.run_exercise(1, 0, -9)
        self.assertIn("and", output)

    def test_b_zero_c_zero_root(self):
        """Quadratic equation with b=0 and c=0."""
        output = self.run_exercise(1, 0, 0)
        self.assertIn("0", output)

    def test_all_zero_infinite_solutions(self):
        """All coefficients zero, theoretically infinite solutions."""
        output = self.run_exercise(0, 0, 0)
        # The expected behavior needs to be defined based on how the script is supposed to handle this case.
        # This test might need adjustment based on the script's actual handling of all-zero input.
        self.assertIn("Infinite roots.", output)  # Placeholder check

if __name__ == '__main__':
    unittest.main()
