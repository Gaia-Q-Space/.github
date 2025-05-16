import unittest
from emissions import calculate_emissions

class TestCalculateEmissions(unittest.TestCase):
    def test_jet_a(self):
        self.assertEqual(calculate_emissions(1, 500.0), 1575.0)

    def test_lh2(self):
        self.assertEqual(calculate_emissions(2, 500.0), 1425.0)

    def test_electric(self):
        self.assertEqual(calculate_emissions(3, 500.0), 0.0)

    def test_invalid_tech_index_low(self):
        self.assertEqual(calculate_emissions(0, 500.0), -1.0)

    def test_invalid_tech_index_high(self):
        self.assertEqual(calculate_emissions(4, 500.0), -1.0)

if __name__ == '__main__':
    unittest.main()
