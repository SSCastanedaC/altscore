def get_volumes(pressure):
    """
    y = mx + b
    """

    # Liquid Line
    m_liq = (10-0.05)/(0.0035-0.00105)
    b_liq = 10 - m_liq*0.0035

    # Vapor Line
    m_vap = (10-0.05)/(0.0035-30)
    b_vap = 10 - m_vap*0.0035

    # vol_liq = (pressure - b_liq) / m_liq
    vol_liq = (pressure - 10) / m_liq + 0.0035
    # vol_vap = (pressure - b_vap) / m_vap
    vol_vap = (pressure - 10) / m_vap + 0.0035
    return {
        "specific_volume_liquid": vol_liq,
        "specific_volume_vapor": vol_vap
    }
