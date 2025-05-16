import pytest
from hypothesis import given, strategies as st
from opt_fuel.core import optimize_fuel_efficiency

def test_optimize_fuel_efficiency_valid():
    assert optimize_fuel_efficiency(12000.0, 8000.0, 0.6) == 2.5

def test_optimize_fuel_efficiency_zero_drag():
    assert optimize_fuel_efficiency(12000.0, 0.0, 0.6) == -1.0

def test_optimize_fuel_efficiency_zero_sfc():
    assert optimize_fuel_efficiency(12000.0, 8000.0, 0.0) == -1.0

def test_optimize_fuel_efficiency_negative_drag():
    assert optimize_fuel_efficiency(12000.0, -8000.0, 0.6) == -1.0

@given(st.floats(min_value=0.1), st.floats(min_value=0.1), st.floats(min_value=0.1))
def test_optimize_fuel_efficiency_hypothesis(thrust, drag, sfc):
    result = optimize_fuel_efficiency(thrust, drag, sfc)
    assert result == thrust / (drag * sfc)
