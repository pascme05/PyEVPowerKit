#######################################################################################################################
#######################################################################################################################
# Title:        Python Electric Vehicle Power Toolkit (PyEVPowerKit)
# Topic:        EV Modeling
# File:         therSim
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
This function calculates the thermal outputs of the drive train.

Inputs:     1) iter:        iteration number
            2) GBX:         GBX instance
            3) EMA:         EMA instance
            4) INV:         INV instance
            5) HVS:         HVS instance
            6) VEH:         VEH instance
            7) data:        mission profile
            8) dataTime:    internal time dependent variables
            9) setup:       includes all simulation variables
Outputs:    1) dataTime:    updated internal time dependent variables

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
import numpy as np


#######################################################################################################################
# Additional Functions
#######################################################################################################################


#######################################################################################################################
# Main Function
#######################################################################################################################
def therSim(iter, GBX, EMA, INV, HVS, VEH, data, dataTime, setup):
    ###################################################################################################################
    # Initialisation
    ###################################################################################################################
    # ==============================================================================
    # Parameters
    # ==============================================================================
    Ts = 1 / setup['Dat']['fs']

    # ==============================================================================
    # Variables
    # ==============================================================================
    # ------------------------------------------
    # Vehicles
    # ------------------------------------------
    Tc = dataTime['VEH']['Tc'][iter - 1]
    Ta = data['T_A'].to_numpy()[iter - 1]
    Vol = data['Vol_C'].to_numpy()[iter - 1]
    v = data['v'].to_numpy()[iter - 1]

    # ------------------------------------------
    # GBX
    # ------------------------------------------
    # Front
    Pv_Gbx_F = dataTime['GBX']['F']['Pv']
    T_Gbx_F = dataTime['GBX']['F']['T']

    # Rear
    Pv_Gbx_R = dataTime['GBX']['R']['Pv']
    T_Gbx_R = dataTime['GBX']['R']['T']

    # ------------------------------------------
    # EMA
    # ------------------------------------------
    # Front
    Pv_Ema_F = dataTime['EMA']['F']['Pv']
    T_Ema_F = dataTime['EMA']['F']['T']

    # Rear
    Pv_Ema_R = dataTime['EMA']['R']['Pv']
    T_Ema_R = dataTime['EMA']['R']['T']

    # ------------------------------------------
    # INV
    # ------------------------------------------
    # Front
    Pv_Inv_F = dataTime['INV']['F']['Pv']
    T_Inv_F = dataTime['INV']['F']['T']

    # Rear
    Pv_Inv_R = dataTime['INV']['R']['Pv']
    T_Inv_R = dataTime['INV']['R']['T']

    # ------------------------------------------
    # HVS
    # ------------------------------------------
    Pv_Hvs = dataTime['HVS']['Pv']
    T_Hvs = dataTime['HVS']['T']

    ###################################################################################################################
    # Calculation
    ###################################################################################################################
    # ==============================================================================
    # GBX
    # ==============================================================================
    T_GBX_F = GBX.calc_therm(Ts, T_Gbx_F[iter - 1] - Tc, Pv_Gbx_F[iter - 1], Pv_Gbx_F[iter])
    T_GBX_R = GBX.calc_therm(Ts, T_Gbx_R[iter - 1] - Tc, Pv_Gbx_R[iter - 1], Pv_Gbx_R[iter])

    # ==============================================================================
    # EMA
    # ==============================================================================
    T_EMA_F = EMA.calc_therm(Ts, T_Ema_F[iter - 1] - Tc, Pv_Ema_F[iter - 1], Pv_Ema_F[iter])
    T_EMA_R = EMA.calc_therm(Ts, T_Ema_R[iter - 1] - Tc, Pv_Ema_R[iter - 1], Pv_Ema_R[iter])

    # ==============================================================================
    # INV
    # ==============================================================================
    T_INV_F = INV.calc_therm(Ts, T_Inv_F[iter - 1] - Tc, Pv_Inv_F[iter - 1], Pv_Inv_F[iter])
    T_INV_R = INV.calc_therm(Ts, T_Inv_R[iter - 1] - Tc, Pv_Inv_R[iter - 1], Pv_Inv_R[iter])

    # ==============================================================================
    # HVS
    # ==============================================================================
    T_HVS = HVS.calc_therm(Ts, T_Hvs[iter - 1] - Tc, Pv_Hvs[iter - 1], Pv_Hvs[iter])

    # ==============================================================================
    # VEH
    # ==============================================================================
    [Tc, dQ] = VEH.calc_cool(Pv_Hvs[iter - 1], Pv_Inv_F[iter - 1] + Pv_Inv_R[iter - 1],
                             Pv_Ema_F[iter - 1] + Pv_Ema_R[iter - 1], Pv_Gbx_F[iter - 1] + Pv_Gbx_R[iter - 1],
                             v, Vol, Ta, Tc, Ts)

    ###################################################################################################################
    # Post-Processing
    ###################################################################################################################
    # ==============================================================================
    # EMA
    # ==============================================================================
    dataTime['GBX']['F']['T'][iter] = T_GBX_F + Tc
    dataTime['GBX']['R']['T'][iter] = T_GBX_R + Tc
    dataTime['GBX']['T']['T'][iter] = np.max((T_GBX_F, T_GBX_R)) + Tc

    # ==============================================================================
    # EMA
    # ==============================================================================
    dataTime['EMA']['F']['T'][iter] = T_EMA_F + Tc
    dataTime['EMA']['R']['T'][iter] = T_EMA_R + Tc
    dataTime['EMA']['T']['T'][iter] = np.max((T_EMA_F, T_EMA_R)) + Tc

    # ==============================================================================
    # INV
    # ==============================================================================
    dataTime['INV']['F']['T'][iter] = T_INV_F + Tc
    dataTime['INV']['R']['T'][iter] = T_INV_R + Tc
    dataTime['INV']['T']['T'][iter] = np.max((T_EMA_F, T_EMA_R)) + Tc

    # ==============================================================================
    # HVS
    # ==============================================================================
    dataTime['HVS']['T'][iter] = T_HVS + Tc

    # ==============================================================================
    # VEH
    # ==============================================================================
    dataTime['VEH']['Tc'][iter] = Tc
    dataTime['VEH']['dQ'][iter] = dQ

    ###################################################################################################################
    # Return
    ###################################################################################################################
    return dataTime

#######################################################################################################################
# References
#######################################################################################################################
