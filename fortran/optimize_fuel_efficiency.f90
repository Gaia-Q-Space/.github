module efficiency_module
  implicit none
contains
  function optimize_fuel_efficiency(thrust, drag, sfc) result(efficiency)
    ! Input: thrust (N), drag (N), sfc (kg/Nh)
    ! Output: fuel efficiency (km/kg)

    real(8), intent(in) :: thrust, drag, sfc
    real(8) :: efficiency

    if (drag <= 0.0d0 .or. sfc <= 0.0d0) then
      efficiency = -1.0d0
    else
      efficiency = thrust / (drag * sfc)
    end if
  end function optimize_fuel_efficiency
end module efficiency_module
