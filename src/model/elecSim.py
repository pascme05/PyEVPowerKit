#######################################################################################################################
#######################################################################################################################
# Title:        Python Electric Vehicle Power Toolkit (PyEVPowerKit)
# Topic:        EV Modeling
# File:         elecSim
# Date:         18.03.2024
# Author:       Dr. Pascal A. Schirmer
# Version:      V.0.1
# Copyright:    Pascal Schirmer
#######################################################################################################################
#######################################################################################################################

#######################################################################################################################
#######################################################################################################################

#######################################################################################################################
# Function Description
#######################################################################################################################
"""
A short description of the function goes here.
Inputs:     1)
            2)
            N)
Outputs:    1)
            2)
            M)
"""

#######################################################################################################################
# Import libs
#######################################################################################################################
# ==============================================================================
# Internal
# ==============================================================================

# ==============================================================================
# External
# ==============================================================================


#######################################################################################################################
# Additional Functions
#######################################################################################################################


#######################################################################################################################
# Main Function
#######################################################################################################################
def elecSim(iter, EMA, INV, HVS, dataTime, setup):
    ###################################################################################################################
    # Initialisation
    ###################################################################################################################
    # ==============================================================================
    # Parameters
    # ==============================================================================
    magType = setup['Par']['EMA']['Mag']
    fsw = setup['Par']['INV']['fs']
    Ts = 1 / setup['Dat']['fs']

    # ==============================================================================
    # Variables
    # ==============================================================================
    # ------------------------------------------
    # Vehicles
    # ------------------------------------------
    Vdc = dataTime['VEH']['Vdc'][iter-1][0]
    SOC = dataTime['VEH']['SOC'][iter-1]

    # ------------------------------------------
    # EMA
    # ------------------------------------------
    # Front
    T_Ema_F = dataTime['EMA']['F']['T'][iter]
    M_Ema_F = dataTime['EMA']['F']['M'][iter]
    n_Ema_F = dataTime['EMA']['F']['n'][iter]

    # Rear
    T_Ema_R = dataTime['EMA']['R']['T'][iter]
    M_Ema_R = dataTime['EMA']['R']['M'][iter]
    n_Ema_R = dataTime['EMA']['R']['n'][iter]

    # ------------------------------------------
    # INV
    # ------------------------------------------
    # Front
    T_Inv_F = dataTime['INV']['F']['T'][iter]

    # Rear
    T_Inv_R = dataTime['INV']['R']['T'][iter]

    # ------------------------------------------
    # HVS
    # ------------------------------------------
    T_HVS = dataTime['HVS']['T'][iter]

    ###################################################################################################################
    # Pre-Processing
    ###################################################################################################################

    ###################################################################################################################
    # Calculation
    ###################################################################################################################
    # ==============================================================================
    # EMA
    # ==============================================================================
    # ------------------------------------------
    # Electrical
    # ------------------------------------------
    [id_F, iq_F, Is_F, vd_F, vq_F, Vs_F, lam_F, Pin_F, Pout_F, _, eta_F, PF_F, Min_F, Msh_F] = EMA.calc_elec(n_Ema_F, M_Ema_F, magType, Vdc, fsw, T_Ema_F)
    [id_R, iq_R, Is_R, vd_R, vq_R, Vs_R, lam_R, Pin_R, Pout_R, _, eta_R, PF_R, Min_R, Msh_R] = EMA.calc_elec(n_Ema_R, M_Ema_R, magType, Vdc, fsw, T_Ema_R)

    # ------------------------------------------
    # Losses
    # ------------------------------------------
    [Pv_F, Pv_m_F, Pv_s_F, Pv_r_F] = EMA.calc_loss(n_Ema_F, Is_F, Vs_F, Vdc, fsw, T_Ema_F)
    [Pv_R, Pv_m_R, Pv_s_R, Pv_r_R] = EMA.calc_loss(n_Ema_R, Is_R, Vs_R, Vdc, fsw, T_Ema_R)

    # ==============================================================================
    # INV
    # ==============================================================================
    # ------------------------------------------
    # Electrical
    # ------------------------------------------
    [Mi_F, Idc_F, Ic_F, Pin_INV_F, Pout_INV_F, Pv_INV_F, eta_INV_F] = INV.calc_elec(PF_F, Vs_F, Is_F, Vdc, T_Inv_F)
    [Mi_R, Idc_R, Ic_R, Pin_INV_R, Pout_INV_R, Pv_INV_R, eta_INV_R] = INV.calc_elec(PF_R, Vs_R, Is_R, Vdc, T_Inv_R)

    # ------------------------------------------
    # Losses
    # ------------------------------------------
    [Pv_INV_F, p_l_swi_F, p_l_cap_F, p_l_ac_F, p_l_dc_F] = INV.calc_loss(Mi_F, PF_F, Is_F, Ic_F, Idc_F - Pv_INV_F / Vdc, Vdc, T_Inv_F)
    [Pv_INV_R, p_l_swi_R, p_l_cap_R, p_l_ac_R, p_l_dc_R] = INV.calc_loss(Mi_R, PF_R, Is_R, Ic_R, Idc_R - Pv_INV_R / Vdc, Vdc, T_Inv_R)

    # ==============================================================================
    # HVS
    # ==============================================================================
    [dQ, SOC, Vdc, Pin_HVS, Pout_HVS, Pv_HVS, eta_HVS] = HVS.calc_elec(Vdc, Idc_F+Idc_R, Ts, SOC, T_HVS)

    ###################################################################################################################
    # Post-Processing
    ###################################################################################################################
    # ==============================================================================
    # EMA
    # ==============================================================================
    # ------------------------------------------
    # Front
    # ------------------------------------------
    dataTime['EMA']['F']['Pin'][iter] = Pin_F
    dataTime['EMA']['F']['Pout'][iter] = Pout_F
    dataTime['EMA']['F']['Pv'][iter] = Pv_F
    dataTime['EMA']['F']['Pv_m'][iter] = Pv_m_F
    dataTime['EMA']['F']['Pv_s'][iter] = Pv_s_F
    dataTime['EMA']['F']['Pv_r'][iter] = Pv_r_F
    dataTime['EMA']['F']['eta'][iter] = eta_F
    dataTime['EMA']['F']['PF'][iter] = PF_F
    dataTime['EMA']['F']['Id'][iter] = id_F
    dataTime['EMA']['F']['Iq'][iter] = iq_F
    dataTime['EMA']['F']['Is'][iter] = Is_F
    dataTime['EMA']['F']['Vd'][iter] = vd_F
    dataTime['EMA']['F']['Vq'][iter] = vq_F
    dataTime['EMA']['F']['Vs'][iter] = Vs_F
    dataTime['EMA']['F']['lam'][iter] = lam_F
    dataTime['EMA']['F']['Min'][iter] = Min_F
    dataTime['EMA']['F']['Msh'][iter] = Msh_F

    # ------------------------------------------
    # Rear
    # ------------------------------------------
    dataTime['EMA']['R']['Pin'][iter] = Pin_R
    dataTime['EMA']['R']['Pout'][iter] = Pout_R
    dataTime['EMA']['R']['Pv'][iter] = Pv_R
    dataTime['EMA']['R']['Pv_m'][iter] = Pv_m_R
    dataTime['EMA']['R']['Pv_s'][iter] = Pv_s_R
    dataTime['EMA']['R']['Pv_r'][iter] = Pv_r_R
    dataTime['EMA']['R']['eta'][iter] = eta_R
    dataTime['EMA']['R']['PF'][iter] = PF_R
    dataTime['EMA']['R']['Id'][iter] = id_R
    dataTime['EMA']['R']['Iq'][iter] = iq_R
    dataTime['EMA']['R']['Is'][iter] = Is_R
    dataTime['EMA']['R']['Vd'][iter] = vd_R
    dataTime['EMA']['R']['Vq'][iter] = vq_R
    dataTime['EMA']['R']['Vs'][iter] = Vs_R
    dataTime['EMA']['R']['lam'][iter] = lam_R
    dataTime['EMA']['R']['Min'][iter] = Min_R
    dataTime['EMA']['R']['Msh'][iter] = Msh_R

    # ------------------------------------------
    # Total
    # ------------------------------------------
    dataTime['EMA']['T']['Pin'][iter] = Pin_F + Pin_R
    dataTime['EMA']['T']['Pout'][iter] = Pout_F + Pout_R
    dataTime['EMA']['T']['Pv'][iter] = Pv_F + Pv_R
    dataTime['EMA']['T']['Pv_m'][iter] = Pv_m_F + Pv_m_R
    dataTime['EMA']['T']['Pv_s'][iter] = Pv_s_F + Pv_s_R
    dataTime['EMA']['T']['Pv_r'][iter] = Pv_r_F + Pv_r_R
    dataTime['EMA']['T']['eta'][iter] = (eta_F + eta_R) / 2
    dataTime['EMA']['T']['PF'][iter] = (PF_F + PF_R) / 2
    dataTime['EMA']['T']['Id'][iter] = id_F + id_R
    dataTime['EMA']['T']['Iq'][iter] = iq_F + iq_R
    dataTime['EMA']['T']['Is'][iter] = Is_F + Is_R
    dataTime['EMA']['T']['Vd'][iter] = (vd_F + vd_R) / 2
    dataTime['EMA']['T']['Vq'][iter] = (vq_F + vq_R) / 2
    dataTime['EMA']['T']['Vs'][iter] = (Vs_F + Vs_R) / 2
    dataTime['EMA']['T']['lam'][iter] = (lam_F + lam_R) / 2
    dataTime['EMA']['T']['Min'][iter] = Min_R + Min_F
    dataTime['EMA']['T']['Msh'][iter] = Msh_R + Msh_F

    # ==============================================================================
    # INV
    # ==============================================================================
    # ------------------------------------------
    # Front
    # ------------------------------------------
    dataTime['INV']['F']['Pin'][iter] = Pin_INV_F
    dataTime['INV']['F']['Pout'][iter] = Pout_INV_F
    dataTime['INV']['F']['Pv'][iter] = Pv_INV_F
    dataTime['INV']['F']['Pv_sw'][iter] = p_l_swi_F
    dataTime['INV']['F']['Pv_cap'][iter] = p_l_cap_F
    dataTime['INV']['F']['Pv_ac'][iter] = p_l_ac_F
    dataTime['INV']['F']['Pv_dc'][iter] = p_l_dc_F
    dataTime['INV']['F']['eta'][iter] = eta_INV_F
    dataTime['INV']['F']['Idc'][iter] = Idc_F
    dataTime['INV']['F']['Ic'][iter] = Ic_F
    dataTime['INV']['F']['Is'][iter] = Is_F
    dataTime['INV']['F']['Mi'][iter] = Mi_F

    # ------------------------------------------
    # Rear
    # ------------------------------------------
    dataTime['INV']['R']['Pin'][iter] = Pin_INV_R
    dataTime['INV']['R']['Pout'][iter] = Pout_INV_R
    dataTime['INV']['R']['Pv'][iter] = Pv_INV_R
    dataTime['INV']['R']['Pv_sw'][iter] = p_l_swi_R
    dataTime['INV']['R']['Pv_cap'][iter] = p_l_cap_R
    dataTime['INV']['R']['Pv_ac'][iter] = p_l_ac_R
    dataTime['INV']['R']['Pv_dc'][iter] = p_l_dc_R
    dataTime['INV']['R']['eta'][iter] = eta_INV_R
    dataTime['INV']['R']['Idc'][iter] = Idc_R
    dataTime['INV']['R']['Ic'][iter] = Ic_R
    dataTime['INV']['R']['Is'][iter] = Is_R
    dataTime['INV']['R']['Mi'][iter] = Mi_R

    # ------------------------------------------
    # Total
    # ------------------------------------------
    dataTime['INV']['T']['Pin'][iter] = Pin_INV_R + Pin_INV_F
    dataTime['INV']['T']['Pout'][iter] = Pout_INV_R + Pout_INV_F
    dataTime['INV']['T']['Pv'][iter] = Pv_INV_R + Pv_INV_F
    dataTime['INV']['T']['Pv_sw'][iter] = p_l_swi_R + p_l_swi_F
    dataTime['INV']['T']['Pv_cap'][iter] = p_l_cap_R + p_l_cap_F
    dataTime['INV']['T']['Pv_ac'][iter] = p_l_ac_R + p_l_ac_F
    dataTime['INV']['T']['Pv_dc'][iter] = p_l_dc_R + p_l_dc_F
    dataTime['INV']['T']['eta'][iter] = (eta_INV_R + eta_INV_F) / 2
    dataTime['INV']['T']['Idc'][iter] = Idc_R + Idc_F
    dataTime['INV']['T']['Ic'][iter] = Ic_R + Ic_F
    dataTime['INV']['T']['Is'][iter] = Is_R + Is_F
    dataTime['INV']['T']['Mi'][iter] = (Mi_R + Mi_F) / 2

    # ==============================================================================
    # HVS
    # ==============================================================================
    dataTime['HVS']['dQ'][iter] = dQ
    dataTime['HVS']['SOC'][iter] = SOC
    dataTime['HVS']['Vdc'][iter] = Vdc
    dataTime['HVS']['Idc'][iter] = Idc_R + Idc_F
    dataTime['HVS']['Pin'][iter] = Pin_HVS
    dataTime['HVS']['Pout'][iter] = Pout_HVS
    dataTime['HVS']['Pv'][iter] = Pv_HVS
    dataTime['HVS']['eta'][iter] = eta_HVS

    # ==============================================================================
    # VEH
    # ==============================================================================
    if setup['Exp']['Vdc'] != 1:
        dataTime['VEH']['Vdc'][iter] = Vdc
        dataTime['VEH']['SOC'][iter] = SOC

    ###################################################################################################################
    # Return
    ###################################################################################################################
    return dataTime

#######################################################################################################################
# References
#######################################################################################################################
