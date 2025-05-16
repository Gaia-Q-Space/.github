def calculate_emissions(tech_index, fuel_burn):
    emission_factors = [3.15, 2.85, 0.0]  # Jet A, LH2, Electric

    if tech_index < 1 or tech_index > len(emission_factors):
        return -1.0

    return emission_factors[tech_index - 1] * fuel_burn
