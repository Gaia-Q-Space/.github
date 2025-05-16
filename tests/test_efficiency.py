import unittest
from efficiency import optimize_fuel_efficiency

class TestOptimizeFuelEfficiency(unittest.TestCase):
    def test_valid_efficiency(self):
        self.assertEqual(optimize_fuel_efficiency(12000.0, 8000.0, 0.6), 2.5)

    def test_zero_drag(self):
        self.assertEqual(optimize_fuel_efficiency(12000.0, 0.0, 0.6), -1.0)

    def test_zero_sfc(self):
        self.assertEqual(optimize_fuel_efficiency(12000.0, 8000.0, 0.0), -1.0)

    def test_negative_drag(self):
        self.assertEqual(optimize_fuel_efficiency(12000.0, -8000.0, 0.6), -1.0)

if __name__ == '__main__':
    unittest.main()
