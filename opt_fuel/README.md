# opt_fuel

## Overview

The `opt_fuel` package provides tools for optimizing fuel efficiency in aerospace applications. It includes functions for calculating fuel efficiency based on thrust, drag, and specific fuel consumption (sfc), as well as handling physical quantities with units.

## Installation

To install the `opt_fuel` package, use the following command:

```bash
pip install opt_fuel
```

## Usage

### Optimizing Fuel Efficiency

The core function of the package is `optimize_fuel_efficiency`, which calculates fuel efficiency based on thrust, drag, and specific fuel consumption (sfc).

```python
from opt_fuel.core import optimize_fuel_efficiency

thrust = 12000.0  # in Newtons (N)
drag = 8000.0     # in Newtons (N)
sfc = 0.6         # in kg/Nh

efficiency = optimize_fuel_efficiency(thrust, drag, sfc)
print(f"Fuel Efficiency: {efficiency} km/kg")
```

### Handling Units

The package uses `pint` for unit handling. You can create quantities with units using the provided wrappers.

```python
from opt_fuel.units import newtons, kilograms_per_newton_hour

thrust = newtons(12000.0)
sfc = kilograms_per_newton_hour(0.6)

print(f"Thrust: {thrust}")
print(f"Specific Fuel Consumption: {sfc}")
```

## Contributing

Contributions are welcome! Please follow the guidelines below:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Write tests for your changes.
4. Ensure all tests pass.
5. Submit a pull request.

## License

This project is licensed under the MIT License.
