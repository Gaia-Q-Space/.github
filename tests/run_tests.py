import emissions
import efficiency
import tradeoffs

def test_calculate_emissions():
    assert emissions.calculate_emissions(1, 500.0) == 1575.0
    assert emissions.calculate_emissions(2, 500.0) == 1425.0
    assert emissions.calculate_emissions(3, 500.0) == 0.0
    assert emissions.calculate_emissions(0, 500.0) == -1.0
    assert emissions.calculate_emissions(4, 500.0) == -1.0

def test_optimize_fuel_efficiency():
    assert efficiency.optimize_fuel_efficiency(12000.0, 8000.0, 0.6) == 2.5
    assert efficiency.optimize_fuel_efficiency(12000.0, 0.0, 0.6) == -1.0
    assert efficiency.optimize_fuel_efficiency(12000.0, 8000.0, 0.0) == -1.0
    assert efficiency.optimize_fuel_efficiency(12000.0, -8000.0, 0.6) == -1.0

def test_analyze_trade_offs():
    assert tradeoffs.analyze_trade_offs(1575.0, 2.5) == 0.0015873015873015873
    assert tradeoffs.analyze_trade_offs(0.0, 2.5) == -1.0
    assert tradeoffs.analyze_trade_offs(1575.0, 0.0) == -1.0
    assert tradeoffs.analyze_trade_offs(-1575.0, 2.5) == -1.0

if __name__ == "__main__":
    test_calculate_emissions()
    test_optimize_fuel_efficiency()
    test_analyze_trade_offs()
    print("All tests passed.")
