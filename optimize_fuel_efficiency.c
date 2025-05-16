#include <stdio.h>

double optimize_fuel_efficiency(double thrust, double drag, double sfc) {
    if (thrust <= 0.0 || drag <= 0.0 || sfc <= 0.0) {
        return -1.0;
    }
    return thrust / (drag * sfc);
}
