import unittest
import subprocess
import os

# This is a general approach; you'll need to define exercise_file_path for each specific script you're testing
exercise_file_path = os.path.join(os.path.dirname(__file__), "example_4.py")  # Adjust "exercise_1.py" accordingly


class TestSpacecraftTrajectory(unittest.TestCase):
    def run_exercise(self, input_value):
        """Helper method to run the exercise script with the provided input and return its output."""
        return subprocess.check_output(['python3', exercise_file_path], input=input_value, text=True, universal_newlines=True)

    def test_fall_to_earth(self):
        output = self.run_exercise("5\n")
        self.assertIn("The device will fall to the Earth's surface.", output)

    def test_earth_satellite(self):
        output = self.run_exercise("8\n")
        self.assertIn("The device will become a satellite of the Earth.", output)

    def test_sun_satellite(self):
        output = self.run_exercise("12\n")
        self.assertIn("The device will become a satellite of the Sun.", output)

    def test_leave_solar_system(self):
        output = self.run_exercise("17\n")
        self.assertIn("The device will leave the Solar System.", output)


if __name__ == '__main__':
    unittest.main()
