def analyze_trade_offs(emission, efficiency):
    """
    Calculate environmental trade-off score based on emission and efficiency.

    Parameters:
    emission (float): CO₂ emission in kg
    efficiency (float): Fuel efficiency in km/kg

    Returns:
    float: Environmental trade-off score
    """
    if emission <= 0.0 or efficiency <= 0.0:
        return -1.0
    return efficiency / emission
