#######################################################################################################################
#######################################################################################################################
# Title:        Python Electric Vehicle Power Toolkit (PyEVPowerKit)
# Topic:        EV Modeling
# File:         initComp
# Date:         18.03.2024
# Author:       Dr. Pascal A. Schirmer
# Version:      V.0.1
# Copyright:    Pascal Schirmer
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
from src.model.Gbx.classGBX import classGBX
from src.model.Ema.classEMA import classPSM
from src.model.Inv.classINV import classB6
from src.model.Bat.classHVS import classBat
from src.model.Veh.classVeh import classVEH

# ==============================================================================
# External
# ==============================================================================

#######################################################################################################################
# Additional Functions
#######################################################################################################################


#######################################################################################################################
# Main Function
#######################################################################################################################
def initComp(setup):
    ###################################################################################################################
    # MSG IN
    ###################################################################################################################
    print("START: Initialise Component Classes")

    ###################################################################################################################
    # Pre-Processing
    ###################################################################################################################
    if setup['Exp']['lim'] == 0 or setup['Exp']['lim'] == 2:
        # ==============================================================================
        # GBX
        # ==============================================================================
        setup['Par']['GBX']['M_max'] = setup['Par']['GBX']['M_max'] * 2
        setup['Par']['GBX']['n_max'] = setup['Par']['GBX']['n_max'] * 2
        setup['Par']['GBX']['P_max'] = setup['Par']['GBX']['P_max'] * 2

        # ==============================================================================
        # EMA
        # ==============================================================================
        setup['Par']['EMA']['I_max'] = setup['Par']['EMA']['I_max'] * 2
        setup['Par']['EMA']['M_max'] = setup['Par']['EMA']['M_max'] * 2
        setup['Par']['EMA']['n_max'] = setup['Par']['EMA']['n_max'] * 2
        setup['Par']['EMA']['P_max'] = setup['Par']['EMA']['P_max'] * 2

        # ==============================================================================
        # INV
        # ==============================================================================
        setup['Par']['INV']['I_max'] = setup['Par']['INV']['I_max'] * 2
        setup['Par']['INV']['P_max'] = setup['Par']['INV']['P_max'] * 2

        # ==============================================================================
        # HVS
        # ==============================================================================
        setup['Par']['HVS']['I_max'] = setup['Par']['HVS']['I_max'] * 2
        setup['Par']['HVS']['P_max'] = setup['Par']['HVS']['P_max'] * 2

        if setup['Exp']['lim'] == 0:
            setup['Par']['HVS']['V_max'] = 1000
            setup['Par']['HVS']['V_min'] = 1000
            setup['Par']['HVS']['V_nom'] = 1000

    ###################################################################################################################
    # Calculation
    ###################################################################################################################
    # ==============================================================================
    # GBX
    # ==============================================================================
    GBX = classGBX(setup['Par']['GBX']['i'], setup['Par']['GBX']['J_gbx'], setup['Par']['GBX']['M_max'], setup['Par']['GBX']['T_max'],
                   setup['Par']['GBX']['n_max'], setup['Par']['GBX']['P_max'], setup['Par']['GBX']['c_m'],
                   setup['Par']['GBX']['c_b'], setup['Par']['GBX']['c_w'], setup['Par']['GBX']['C_th'],
                   setup['Par']['GBX']['R_th'], setup['Par']['GBX']['h_th'], setup['Par']['GBX']['A_th'],
                   setup['Par']['GBX']['Ea'], setup['Par']['GBX']['k'], setup['Par']['GBX']['n'],
                   setup['Par']['GBX']['L0'], setup['Par']['GBX']['Nf0'], setup['Par']['GBX']['T0'],
                   setup['Par']['GBX']['dT0'], setup['Par']['GBX']['V0'], setup['Par']['GBX']['F0'],
                   setup['Par']['GBX']['beta'], setup['Par']['GBX']['CL'], setup['Par']['GBX']['Bx'])

    # ==============================================================================
    # EMA
    # ==============================================================================
    EMA = classPSM(setup['Par']['EMA']['Type'], setup['Par']['EMA']['Mag'], setup['Par']['EMA']['p'],
                   setup['Par']['EMA']['n_0'], setup['Par']['EMA']['J_rot'], setup['Par']['EMA']['M_max'], setup['Par']['EMA']['T_max'],
                   setup['Par']['EMA']['n_max'], setup['Par']['EMA']['P_max'], setup['Par']['EMA']['I_max'],
                   setup['Par']['EMA']['Psi_pm'], setup['Par']['EMA']['L_d'], setup['Par']['EMA']['L_q'],
                   setup['Par']['EMA']['L_sig'], setup['Par']['EMA']['R_s'], setup['Par']['EMA']['c_b'],
                   setup['Par']['EMA']['c_w'], setup['Par']['EMA']['K_h'], setup['Par']['EMA']['K_f'],
                   setup['Par']['EMA']['C_th'], setup['Par']['EMA']['R_th'], setup['Par']['EMA']['h_th'],
                   setup['Par']['EMA']['A_th'], setup['Par']['EMA']['Ea'], setup['Par']['EMA']['k'],
                   setup['Par']['EMA']['n'], setup['Par']['EMA']['L0'], setup['Par']['EMA']['Nf0'],
                   setup['Par']['EMA']['T0'], setup['Par']['EMA']['dT0'], setup['Par']['EMA']['V0'],
                   setup['Par']['EMA']['F0'], setup['Par']['EMA']['beta'], setup['Par']['EMA']['CL'],
                   setup['Par']['EMA']['Bx'])

    # ==============================================================================
    # INV
    # ==============================================================================
    INV = classB6(setup['Par']['INV']['fs'], setup['Par']['INV']['Sw'], setup['Par']['INV']['nSw'],
                  setup['Par']['INV']['nCap'], setup['Par']['INV']['V_0'], setup['Par']['INV']['I_0'],
                  setup['Par']['INV']['T_0'], setup['Par']['INV']['Tj_max'], setup['Par']['INV']['alpha'],
                  setup['Par']['INV']['P_max'], setup['Par']['INV']['T_max'], setup['Par']['INV']['I_max'], setup['Par']['INV']['V_ce0'],
                  setup['Par']['INV']['r_T'], setup['Par']['INV']['V_d0'], setup['Par']['INV']['r_D'],
                  setup['Par']['INV']['E_on'], setup['Par']['INV']['E_off'], setup['Par']['INV']['E_rec'],
                  setup['Par']['INV']['R_g'], setup['Par']['INV']['R_esr'], setup['Par']['INV']['C_dc'],
                  setup['Par']['INV']['R_ac'], setup['Par']['INV']['R_dc'], setup['Par']['INV']['C_th'],
                  setup['Par']['INV']['R_th'], setup['Par']['INV']['h_th'], setup['Par']['INV']['A_th'],
                  setup['Par']['INV']['Ea'], setup['Par']['INV']['k'], setup['Par']['INV']['n'],
                  setup['Par']['INV']['L0'], setup['Par']['INV']['Nf0'], setup['Par']['INV']['T0'],
                  setup['Par']['INV']['dT0'], setup['Par']['INV']['V0'], setup['Par']['INV']['F0'],
                  setup['Par']['INV']['beta'], setup['Par']['INV']['CL'], setup['Par']['INV']['Bx'])

    # ==============================================================================
    # HVS
    # ==============================================================================
    HVS = classBat(setup['Par']['HVS']['P_max'], setup['Par']['INV']['T_max'], setup['Par']['HVS']['I_max'], setup['Par']['HVS']['R_i'],
                   setup['Par']['HVS']['V_nom'], setup['Par']['HVS']['V_max'], setup['Par']['HVS']['V_min'],
                   setup['Par']['HVS']['E_a'], setup['Par']['HVS']['E_bat'], setup['Par']['HVS']['C_th'],
                   setup['Par']['HVS']['R_th'], setup['Par']['HVS']['h_th'], setup['Par']['HVS']['A_th'],
                   setup['Par']['HVS']['Ea'], setup['Par']['HVS']['k'], setup['Par']['HVS']['n'],
                   setup['Par']['HVS']['L0'], setup['Par']['HVS']['Nf0'], setup['Par']['HVS']['T0'],
                   setup['Par']['HVS']['dT0'], setup['Par']['HVS']['V0'], setup['Par']['HVS']['F0'],
                   setup['Par']['HVS']['beta'], setup['Par']['HVS']['CL'], setup['Par']['HVS']['Bx'])

    # ==============================================================================
    # VEH
    # ==============================================================================
    VEH = classVEH(setup['Par']['VEH']['m'], setup['Par']['VEH']['c_r'], setup['Par']['VEH']['A'],
                   setup['Par']['VEH']['c_w'], setup['Par']['VEH']['r_rim'], setup['Par']['VEH']['m_rim'],
                   setup['Par']['VEH']['r_tire'], setup['Par']['VEH']['m_tire'], setup['Par']['VEH']['r_flat'],
                   setup['Par']['VEH']['d_b'], setup['Par']['VEH']['d_a'], setup['Par']['VEH']['eta'],
                   setup['Par']['VEH']['c_Vol'], setup['Par']['VEH']['c_rho'], setup['Par']['VEH']['c_Cp'],
                   setup['Par']['VEH']['c_vis'], setup['Par']['VEH']['A_r'], setup['Par']['VEH']['A_b'])

    ###################################################################################################################
    # Return
    ###################################################################################################################
    return [GBX, EMA, INV, HVS, VEH]

#######################################################################################################################
# References
#######################################################################################################################
