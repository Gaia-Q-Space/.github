module tradeoffs_module
  implicit none
contains
  function analyze_trade_offs(emission, efficiency) result(score)
    ! Combines emission and efficiency into an environmental trade-off score

    real(8), intent(in) :: emission, efficiency
    real(8) :: score

    if (emission <= 0.0d0 .or. efficiency <= 0.0d0) then
      score = -1.0d0
    else
      score = efficiency / emission
    end if
  end function analyze_trade_offs
end module tradeoffs_module
