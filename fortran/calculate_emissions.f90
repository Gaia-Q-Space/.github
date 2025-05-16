module emissions_module
  implicit none
contains
  function calculate_emissions(tech_index, fuel_burn) result(co2_emission)
    ! Input: propulsion tech index and fuel burned (kg)
    ! Output: CO₂ emissions (kg)

    integer, intent(in) :: tech_index
    real(8), intent(in) :: fuel_burn
    real(8) :: co2_emission
    real(8), dimension(3) :: emission_factors

    emission_factors = (/ 3.15d0, 2.85d0, 0.0d0 /) ! Example: Jet A, LH2, Electric

    if (tech_index < 1 .or. tech_index > size(emission_factors)) then
      co2_emission = -1.0d0
    else
      co2_emission = emission_factors(tech_index) * fuel_burn
    end if
  end function calculate_emissions
end module emissions_module
