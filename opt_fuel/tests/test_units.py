import pytest
from hypothesis import given, strategies as st
from pint import UnitRegistry
from opt_fuel.units import newtons, kilograms_per_newton_hour

unit_registry = UnitRegistry()

def test_newtons():
    value = 10.0
    quantity = newtons(value)
    assert quantity.magnitude == value
    assert quantity.units == unit_registry.newton

def test_kilograms_per_newton_hour():
    value = 0.5
    quantity = kilograms_per_newton_hour(value)
    assert quantity.magnitude == value
    assert quantity.units == unit_registry.kg / (unit_registry.newton * unit_registry.hour)

@given(st.floats(min_value=0.1))
def test_newtons_hypothesis(value):
    quantity = newtons(value)
    assert quantity.magnitude == value
    assert quantity.units == unit_registry.newton

@given(st.floats(min_value=0.1))
def test_kilograms_per_newton_hour_hypothesis(value):
    quantity = kilograms_per_newton_hour(value)
    assert quantity.magnitude == value
    assert quantity.units == unit_registry.kg / (unit_registry.newton * unit_registry.hour)
