import chardet
import emissions
import efficiency
import tradeoffs

# Detect the encoding of the file
with open("fortran/calculate_emissions.f90", "rb") as file:
    raw_data = file.read()
    encoding = chardet.detect(raw_data)['encoding']

print(f"Detected file encoding: {encoding}")

# Convert to UTF-8 if not already
if encoding.lower() != "utf-8":
    with open("fortran/calculate_emissions.f90", "r", encoding=encoding) as file:
        content = file.read()

    with open("fortran/calculate_emissions.f90", "w", encoding="utf-8") as file:
        file.write(content)

    print("File converted to UTF-8 encoding.")

co2 = emissions.calculate_emissions(1, 500.0)
eff = efficiency.optimize_fuel_efficiency(12000.0, 8000.0, 0.6)
score = tradeoffs.analyze_trade_offs(co2, eff)

print(f"CO2 Emission: {co2:.2f} kg")
print(f"Efficiency: {eff:.2f} km/kg")
print(f"Trade-off Score: {score:.4f}")
