import emissions
import efficiency
import tradeoffs

co2 = emissions.calculate_emissions(1, 500.0)
eff = efficiency.optimize_fuel_efficiency(12000.0, 8000.0, 0.6)
score = tradeoffs.analyze_trade_offs(co2, eff)

print(f"CO2 Emission: {co2:.2f} kg")
print(f"Efficiency: {eff:.2f} km/kg")
print(f"Trade-off Score: {score:.4f}")
