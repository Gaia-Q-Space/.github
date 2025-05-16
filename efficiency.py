def optimize_fuel_efficiency(thrust, drag, sfc):
    """
    Calculate fuel efficiency based on thrust, drag, and specific fuel consumption (sfc).

    Parameters:
    thrust (float): Thrust in Newtons (N)
    drag (float): Drag in Newtons (N)
    sfc (float): Specific fuel consumption in kg/Nh

    Returns:
    float: Fuel efficiency in km/kg
    """
    if drag <= 0.0 or sfc <= 0.0:
        return -1.0
    return thrust / (drag * sfc)
