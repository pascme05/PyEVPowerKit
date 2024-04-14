#######################################################################################################################
#######################################################################################################################
# Title:        Python Electric Vehicle Power Toolkit (PyEVPowerKit)
# Topic:        EV Modeling
# File:         reliaSim
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
This function calculates the reliability of each component

Inputs:     1) GBX:         GBX instance
            2) EMA:         EMA instance
            3) INV:         INV instance
            4) HVS:         HVS instance
            5) dataTime:    internal time dependent variables
            6) setup:       includes all simulation variables
Outputs:    1) dataLife:    lifetime results

"""

#######################################################################################################################
# Import libs
#######################################################################################################################
# ==============================================================================
# Internal
# ==============================================================================
from src.model.calcDmg import calcDmgArr, calcDmgPro, calcDmgCof

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
def reliaSim(GBX, EMA, INV, HVS, dataTime, setup):
    ###################################################################################################################
    # MSG Out
    ###################################################################################################################
    print("INFO: Calculating reliability")

    ###################################################################################################################
    # Initialisation
    ###################################################################################################################
    # ==============================================================================
    # Parameters
    # ==============================================================================
    Ts = 1 / setup['Dat']['fs']
    Vdc = dataTime['HVS']['Vdc']

    # ==============================================================================
    # Variables
    # ==============================================================================
    # ------------------------------------------
    # GBX
    # ------------------------------------------
    T_GBX_F = dataTime['GBX']['F']['T']
    V_GBX_F = np.zeros((len(T_GBX_F)))
    T_GBX_R = dataTime['GBX']['R']['T']
    V_GBX_R = np.zeros((len(T_GBX_F)))

    # ------------------------------------------
    # EMA
    # ------------------------------------------
    T_EMA_F = dataTime['EMA']['F']['T']
    V_EMA_F = dataTime['EMA']['F']['Vs']
    T_EMA_R = dataTime['EMA']['R']['T']
    V_EMA_R = dataTime['EMA']['R']['Vs']

    # ------------------------------------------
    # INV
    # ------------------------------------------
    T_INV_F = dataTime['INV']['F']['T']
    V_INV_F = Vdc
    T_INV_R = dataTime['INV']['R']['T']
    V_INV_R = Vdc

    # ------------------------------------------
    # HVS
    # ------------------------------------------
    T_HVS = dataTime['HVS']['T']
    V_HVS = dataTime['HVS']['Vdc']

    # ==============================================================================
    # Output
    # ==============================================================================
    dataLife = {'GBX': {'F': {'Arr': {}, 'Cof': {}, 'Pro': {}}, 'R': {'Arr': {}, 'Cof': {}, 'Pro': {}}},
                'EMA': {'F': {'Arr': {}, 'Cof': {}, 'Pro': {}}, 'R': {'Arr': {}, 'Cof': {}, 'Pro': {}}},
                'INV': {'F': {'Arr': {}, 'Cof': {}, 'Pro': {}}, 'R': {'Arr': {}, 'Cof': {}, 'Pro': {}}},
                'HVS': {'Arr': {}, 'Cof': {}, 'Pro': {}}}

    ###################################################################################################################
    # Calculation
    ###################################################################################################################
    # ==============================================================================
    # GBX
    # ==============================================================================
    # ------------------------------------------
    # Front
    # ------------------------------------------
    [L_GBX_F_Arr, D_GBX_F_Arr, F_GBX_F_Arr, pdf_GBX_F_Arr, cdf_GBX_F_Arr, x_GBX_F_Arr] = calcDmgArr(GBX, Ts, T_GBX_F, setup)
    [L_GBX_F_Cof, D_GBX_F_Cof, F_GBX_F_Cof, pdf_GBX_F_Cof, cdf_GBX_F_Cof, x_GBX_F_Cof] = calcDmgCof(GBX, Ts, T_GBX_F, setup)
    [L_GBX_F_Pro, D_GBX_F_Pro, F_GBX_F_Pro, pdf_GBX_F_Pro, cdf_GBX_F_Pro, x_GBX_F_Pro] = calcDmgPro(GBX, Ts, T_GBX_F, V_GBX_F, setup)

    # ------------------------------------------
    # Rear
    # ------------------------------------------
    [L_GBX_R_Arr, D_GBX_R_Arr, F_GBX_R_Arr, pdf_GBX_R_Arr, cdf_GBX_R_Arr, x_GBX_R_Arr] = calcDmgArr(GBX, Ts, T_GBX_R, setup)
    [L_GBX_R_Cof, D_GBX_R_Cof, F_GBX_R_Cof, pdf_GBX_R_Cof, cdf_GBX_R_Cof, x_GBX_R_Cof] = calcDmgCof(GBX, Ts, T_GBX_R, setup)
    [L_GBX_R_Pro, D_GBX_R_Pro, F_GBX_R_Pro, pdf_GBX_R_Pro, cdf_GBX_R_Pro, x_GBX_R_Pro] = calcDmgPro(GBX, Ts, T_GBX_R, V_GBX_R, setup)

    # ==============================================================================
    # EMA
    # ==============================================================================
    # ------------------------------------------
    # Front
    # ------------------------------------------
    [L_EMA_F_Arr, D_EMA_F_Arr, F_EMA_F_Arr, pdf_EMA_F_Arr, cdf_EMA_F_Arr, x_EMA_F_Arr] = calcDmgArr(EMA, Ts, T_EMA_F, setup)
    [L_EMA_F_Cof, D_EMA_F_Cof, F_EMA_F_Cof, pdf_EMA_F_Cof, cdf_EMA_F_Cof, x_EMA_F_Cof] = calcDmgCof(EMA, Ts, T_EMA_F, setup)
    [L_EMA_F_Pro, D_EMA_F_Pro, F_EMA_F_Pro, pdf_EMA_F_Pro, cdf_EMA_F_Pro, x_EMA_F_Pro] = calcDmgPro(EMA, Ts, T_EMA_F, V_EMA_F, setup)

    # ------------------------------------------
    # Rear
    # ------------------------------------------
    [L_EMA_R_Arr, D_EMA_R_Arr, F_EMA_R_Arr, pdf_EMA_R_Arr, cdf_EMA_R_Arr, x_EMA_R_Arr] = calcDmgArr(EMA, Ts, T_EMA_R, setup)
    [L_EMA_R_Cof, D_EMA_R_Cof, F_EMA_R_Cof, pdf_EMA_R_Cof, cdf_EMA_R_Cof, x_EMA_R_Cof] = calcDmgCof(EMA, Ts, T_EMA_R, setup)
    [L_EMA_R_Pro, D_EMA_R_Pro, F_EMA_R_Pro, pdf_EMA_R_Pro, cdf_EMA_R_Pro, x_EMA_R_Pro] = calcDmgPro(EMA, Ts, T_EMA_R, V_EMA_R, setup)

    # ==============================================================================
    # INV
    # ==============================================================================
    # ------------------------------------------
    # Front
    # ------------------------------------------
    [L_INV_F_Arr, D_INV_F_Arr, F_INV_F_Arr, pdf_INV_F_Arr, cdf_INV_F_Arr, x_INV_F_Arr] = calcDmgArr(INV, Ts, T_INV_F, setup)
    [L_INV_F_Cof, D_INV_F_Cof, F_INV_F_Cof, pdf_INV_F_Cof, cdf_INV_F_Cof, x_INV_F_Cof] = calcDmgCof(INV, Ts, T_INV_F, setup)
    [L_INV_F_Pro, D_INV_F_Pro, F_INV_F_Pro, pdf_INV_F_Pro, cdf_INV_F_Pro, x_INV_F_Pro] = calcDmgPro(INV, Ts, T_INV_F, V_INV_F, setup)

    # ------------------------------------------
    # Rear
    # ------------------------------------------
    [L_INV_R_Arr, D_INV_R_Arr, F_INV_R_Arr, pdf_INV_R_Arr, cdf_INV_R_Arr, x_INV_R_Arr] = calcDmgArr(INV, Ts, T_INV_R, setup)
    [L_INV_R_Cof, D_INV_R_Cof, F_INV_R_Cof, pdf_INV_R_Cof, cdf_INV_R_Cof, x_INV_R_Cof] = calcDmgCof(INV, Ts, T_INV_R, setup)
    [L_INV_R_Pro, D_INV_R_Pro, F_INV_R_Pro, pdf_INV_R_Pro, cdf_INV_R_Pro, x_INV_R_Pro] = calcDmgPro(INV, Ts, T_INV_R, V_INV_R, setup)

    # ==============================================================================
    # HVS
    # ==============================================================================
    [L_HVS_Arr, D_HVS_Arr, F_HVS_Arr, pdf_HVS_Arr, cdf_HVS_Arr, x_HVS_Arr] = calcDmgArr(HVS, Ts, T_HVS, setup)
    [L_HVS_Cof, D_HVS_Cof, F_HVS_Cof, pdf_HVS_Cof, cdf_HVS_Cof, x_HVS_Cof] = calcDmgCof(HVS, Ts, T_HVS, setup)
    [L_HVS_Pro, D_HVS_Pro, F_HVS_Pro, pdf_HVS_Pro, cdf_HVS_Pro, x_HVS_Pro] = calcDmgPro(HVS, Ts, T_HVS, V_HVS, setup)

    ###################################################################################################################
    # Post-Processing
    ###################################################################################################################
    # ==============================================================================
    # GBX
    # ==============================================================================
    # ------------------------------------------
    # Front
    # ------------------------------------------
    # Arrhenius
    dataLife['GBX']['F']['Arr']['L']     = L_GBX_F_Arr
    dataLife['GBX']['F']['Arr']['D']     = D_GBX_F_Arr
    dataLife['GBX']['F']['Arr']['F']     = F_GBX_F_Arr
    dataLife['GBX']['F']['Arr']['pdf'] = pdf_GBX_F_Arr
    dataLife['GBX']['F']['Arr']['cdf'] = cdf_GBX_F_Arr
    dataLife['GBX']['F']['Arr']['x']     = x_GBX_F_Arr

    # Coffin
    dataLife['GBX']['F']['Cof']['L']     = L_GBX_F_Cof
    dataLife['GBX']['F']['Cof']['D']     = D_GBX_F_Cof
    dataLife['GBX']['F']['Cof']['F']     = F_GBX_F_Cof
    dataLife['GBX']['F']['Cof']['pdf'] = pdf_GBX_F_Cof
    dataLife['GBX']['F']['Cof']['cdf'] = cdf_GBX_F_Cof
    dataLife['GBX']['F']['Cof']['x']     = x_GBX_F_Cof

    # Prokopovic
    dataLife['GBX']['F']['Pro']['L']     = L_GBX_F_Pro
    dataLife['GBX']['F']['Pro']['D']     = D_GBX_F_Pro
    dataLife['GBX']['F']['Pro']['F']     = F_GBX_F_Pro
    dataLife['GBX']['F']['Pro']['pdf'] = pdf_GBX_F_Pro
    dataLife['GBX']['F']['Pro']['cdf'] = cdf_GBX_F_Pro
    dataLife['GBX']['F']['Pro']['x']     = x_GBX_F_Pro

    # ------------------------------------------
    # Rear
    # ------------------------------------------
    # Arrhenius
    dataLife['GBX']['R']['Arr']['L']     = L_GBX_R_Arr
    dataLife['GBX']['R']['Arr']['D']     = D_GBX_R_Arr
    dataLife['GBX']['R']['Arr']['F']     = F_GBX_R_Arr
    dataLife['GBX']['R']['Arr']['pdf'] = pdf_GBX_R_Arr
    dataLife['GBX']['R']['Arr']['cdf'] = cdf_GBX_R_Arr
    dataLife['GBX']['R']['Arr']['x']     = x_GBX_R_Arr

    # Coffin
    dataLife['GBX']['R']['Cof']['L']     = L_GBX_R_Cof
    dataLife['GBX']['R']['Cof']['D']     = D_GBX_R_Cof
    dataLife['GBX']['R']['Cof']['F']     = F_GBX_R_Cof
    dataLife['GBX']['R']['Cof']['pdf'] = pdf_GBX_R_Cof
    dataLife['GBX']['R']['Cof']['cdf'] = cdf_GBX_R_Cof
    dataLife['GBX']['R']['Cof']['x']     = x_GBX_R_Cof

    # Prokopovic
    dataLife['GBX']['R']['Pro']['L']     = L_GBX_R_Pro
    dataLife['GBX']['R']['Pro']['D']     = D_GBX_R_Pro
    dataLife['GBX']['R']['Pro']['F']     = F_GBX_R_Pro
    dataLife['GBX']['R']['Pro']['pdf'] = pdf_GBX_R_Pro
    dataLife['GBX']['R']['Pro']['cdf'] = cdf_GBX_R_Pro
    dataLife['GBX']['R']['Pro']['x']     = x_GBX_R_Pro

    # ==============================================================================
    # EMA
    # ==============================================================================
    # ------------------------------------------
    # Front
    # ------------------------------------------
    # Arrhenius
    dataLife['EMA']['F']['Arr']['L']     = L_EMA_F_Arr
    dataLife['EMA']['F']['Arr']['D']     = D_EMA_F_Arr
    dataLife['EMA']['F']['Arr']['F']     = F_EMA_F_Arr
    dataLife['EMA']['F']['Arr']['pdf'] = pdf_EMA_F_Arr
    dataLife['EMA']['F']['Arr']['cdf'] = cdf_EMA_F_Arr
    dataLife['EMA']['F']['Arr']['x']     = x_EMA_F_Arr

    # Coffin
    dataLife['EMA']['F']['Cof']['L']     = L_EMA_F_Cof
    dataLife['EMA']['F']['Cof']['D']     = D_EMA_F_Cof
    dataLife['EMA']['F']['Cof']['F']     = F_EMA_F_Cof
    dataLife['EMA']['F']['Cof']['pdf'] = pdf_EMA_F_Cof
    dataLife['EMA']['F']['Cof']['cdf'] = cdf_EMA_F_Cof
    dataLife['EMA']['F']['Cof']['x']     = x_EMA_F_Cof

    # Prokopovic
    dataLife['EMA']['F']['Pro']['L']     = L_EMA_F_Pro
    dataLife['EMA']['F']['Pro']['D']     = D_EMA_F_Pro
    dataLife['EMA']['F']['Pro']['F']     = F_EMA_F_Pro
    dataLife['EMA']['F']['Pro']['pdf'] = pdf_EMA_F_Pro
    dataLife['EMA']['F']['Pro']['cdf'] = cdf_EMA_F_Pro
    dataLife['EMA']['F']['Pro']['x']     = x_EMA_F_Pro

    # ------------------------------------------
    # Rear
    # ------------------------------------------
    # Arrhenius
    dataLife['EMA']['R']['Arr']['L']     = L_EMA_R_Arr
    dataLife['EMA']['R']['Arr']['D']     = D_EMA_R_Arr
    dataLife['EMA']['R']['Arr']['F']     = F_EMA_R_Arr
    dataLife['EMA']['R']['Arr']['pdf'] = pdf_EMA_R_Arr
    dataLife['EMA']['R']['Arr']['cdf'] = cdf_EMA_R_Arr
    dataLife['EMA']['R']['Arr']['x']     = x_EMA_R_Arr

    # Coffin
    dataLife['EMA']['R']['Cof']['L']     = L_EMA_R_Cof
    dataLife['EMA']['R']['Cof']['D']     = D_EMA_R_Cof
    dataLife['EMA']['R']['Cof']['F']     = F_EMA_R_Cof
    dataLife['EMA']['R']['Cof']['pdf'] = pdf_EMA_R_Cof
    dataLife['EMA']['R']['Cof']['cdf'] = cdf_EMA_R_Cof
    dataLife['EMA']['R']['Cof']['x']     = x_EMA_R_Cof

    # Prokopovic
    dataLife['EMA']['R']['Pro']['L']     = L_EMA_R_Pro
    dataLife['EMA']['R']['Pro']['D']     = D_EMA_R_Pro
    dataLife['EMA']['R']['Pro']['F']     = F_EMA_R_Pro
    dataLife['EMA']['R']['Pro']['pdf'] = pdf_EMA_R_Pro
    dataLife['EMA']['R']['Pro']['cdf'] = cdf_EMA_R_Pro
    dataLife['EMA']['R']['Pro']['x']     = x_EMA_R_Pro

    # ==============================================================================
    # INV
    # ==============================================================================
    # ------------------------------------------
    # Front
    # ------------------------------------------
    # Arrhenius
    dataLife['INV']['F']['Arr']['L']     = L_INV_F_Arr
    dataLife['INV']['F']['Arr']['D']     = D_INV_F_Arr
    dataLife['INV']['F']['Arr']['F']     = F_INV_F_Arr
    dataLife['INV']['F']['Arr']['pdf'] = pdf_INV_F_Arr
    dataLife['INV']['F']['Arr']['cdf'] = cdf_INV_F_Arr
    dataLife['INV']['F']['Arr']['x']     = x_INV_F_Arr

    # Coffin
    dataLife['INV']['F']['Cof']['L']     = L_INV_F_Cof
    dataLife['INV']['F']['Cof']['D']     = D_INV_F_Cof
    dataLife['INV']['F']['Cof']['F']     = F_INV_F_Cof
    dataLife['INV']['F']['Cof']['pdf'] = pdf_INV_F_Cof
    dataLife['INV']['F']['Cof']['cdf'] = cdf_INV_F_Cof
    dataLife['INV']['F']['Cof']['x']     = x_INV_F_Cof

    # Prokopovic
    dataLife['INV']['F']['Pro']['L']     = L_INV_F_Pro
    dataLife['INV']['F']['Pro']['D']     = D_INV_F_Pro
    dataLife['INV']['F']['Pro']['F']     = F_INV_F_Pro
    dataLife['INV']['F']['Pro']['pdf'] = pdf_INV_F_Pro
    dataLife['INV']['F']['Pro']['cdf'] = cdf_INV_F_Pro
    dataLife['INV']['F']['Pro']['x']     = x_INV_F_Pro

    # ------------------------------------------
    # Rear
    # ------------------------------------------
    # Arrhenius
    dataLife['INV']['R']['Arr']['L']     = L_INV_R_Arr
    dataLife['INV']['R']['Arr']['D']     = D_INV_R_Arr
    dataLife['INV']['R']['Arr']['F']     = F_INV_R_Arr
    dataLife['INV']['R']['Arr']['pdf'] = pdf_INV_R_Arr
    dataLife['INV']['R']['Arr']['cdf'] = cdf_INV_R_Arr
    dataLife['INV']['R']['Arr']['x']     = x_INV_R_Arr

    # Coffin
    dataLife['INV']['R']['Cof']['L']     = L_INV_R_Cof
    dataLife['INV']['R']['Cof']['D']     = D_INV_R_Cof
    dataLife['INV']['R']['Cof']['F']     = F_INV_R_Cof
    dataLife['INV']['R']['Cof']['pdf'] = pdf_INV_R_Cof
    dataLife['INV']['R']['Cof']['cdf'] = cdf_INV_R_Cof
    dataLife['INV']['R']['Cof']['x']     = x_INV_R_Cof

    # Prokopovic
    dataLife['INV']['R']['Pro']['L']     = L_INV_R_Pro
    dataLife['INV']['R']['Pro']['D']     = D_INV_R_Pro
    dataLife['INV']['R']['Pro']['F']     = F_INV_R_Pro
    dataLife['INV']['R']['Pro']['pdf'] = pdf_INV_R_Pro
    dataLife['INV']['R']['Pro']['cdf'] = cdf_INV_R_Pro
    dataLife['INV']['R']['Pro']['x']     = x_INV_R_Pro

    # ==============================================================================
    # HVS
    # ==============================================================================
    # Arrhenius
    dataLife['HVS']['Arr']['L']     = L_HVS_Arr
    dataLife['HVS']['Arr']['D']     = D_HVS_Arr
    dataLife['HVS']['Arr']['F']     = F_HVS_Arr
    dataLife['HVS']['Arr']['pdf'] = pdf_HVS_Arr
    dataLife['HVS']['Arr']['cdf'] = cdf_HVS_Arr
    dataLife['HVS']['Arr']['x']     = x_HVS_Arr

    # Coffin
    dataLife['HVS']['Cof']['L']     = L_HVS_Cof
    dataLife['HVS']['Cof']['D']     = D_HVS_Cof
    dataLife['HVS']['Cof']['F']     = F_HVS_Cof
    dataLife['HVS']['Cof']['pdf'] = pdf_HVS_Cof
    dataLife['HVS']['Cof']['cdf'] = cdf_HVS_Cof
    dataLife['HVS']['Cof']['x']     = x_HVS_Cof

    # Prokopovic
    dataLife['HVS']['Pro']['L']     = L_HVS_Pro
    dataLife['HVS']['Pro']['D']     = D_HVS_Pro
    dataLife['HVS']['Pro']['F']     = F_HVS_Pro
    dataLife['HVS']['Pro']['pdf'] = pdf_HVS_Pro
    dataLife['HVS']['Pro']['cdf'] = cdf_HVS_Pro
    dataLife['HVS']['Pro']['x']     = x_HVS_Pro

    ###################################################################################################################
    # MSG Out
    ###################################################################################################################
    print("DONE: Reliability calculated")

    ###################################################################################################################
    # Return
    ###################################################################################################################
    return dataLife

#######################################################################################################################
# References
#######################################################################################################################
