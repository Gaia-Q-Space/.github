"""
Calculate the classical baseline cost for fuel efficiency optimization.

This function calculates the classical baseline cost for fuel efficiency optimization
by summing the fuel efficiency values for given thrust, drag, and specific fuel consumption (sfc) values.

Parameters:
thrusts (list of float): List of thrust values in Newtons (N)
drags (list of float): List of drag values in Newtons (N)
sfcs (list of float): List of specific fuel consumption values in kg/Nh

Returns:
float: The classical baseline cost for fuel efficiency optimization
"""

from opt_fuel.core import optimize_fuel_efficiency

def classical_baseline_cost(thrusts, drags, sfcs):
    return sum(optimize_fuel_efficiency(t, d, s) for t, d, s in zip(thrusts, drags, sfcs))
