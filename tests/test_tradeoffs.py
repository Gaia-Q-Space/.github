import unittest
from tradeoffs import analyze_trade_offs

class TestAnalyzeTradeOffs(unittest.TestCase):
    def test_valid_trade_off(self):
        self.assertEqual(analyze_trade_offs(1575.0, 2.5), 0.0015873015873015873)

    def test_zero_emission(self):
        self.assertEqual(analyze_trade_offs(0.0, 2.5), -1.0)

    def test_zero_efficiency(self):
        self.assertEqual(analyze_trade_offs(1575.0, 0.0), -1.0)

    def test_negative_emission(self):
        self.assertEqual(analyze_trade_offs(-1575.0, 2.5), -1.0)

if __name__ == '__main__':
    unittest.main()
