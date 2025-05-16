"""
Units module for handling physical quantities using pint.

This module sets up pint for unit handling and provides Quantity wrappers
to ensure unit safety in calculations.
"""

import pint

# Set up pint unit registry
unit_registry = pint.UnitRegistry()

# Define Quantity for convenience
Quantity = unit_registry.Quantity

# Example Quantity wrapper functions
def newtons(value):
    return Quantity(value, 'newton')

def kilograms_per_newton_hour(value):
    return Quantity(value, 'kg / (newton * hour)')
