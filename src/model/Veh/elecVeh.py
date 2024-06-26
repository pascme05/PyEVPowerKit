#######################################################################################################################
#######################################################################################################################
# Title:        Python Electric Vehicle Power Toolkit (PyEVPowerKit)
# Topic:        EV Modeling
# File:         elecVeh
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
This function sets the electrical properties of the battery and the initial state of charge.
Inputs:     1) data:        mission profile of the vehicle
            2) dataTime:    internal time dependent variables
            3) setup:       includes all simulation variables
Outputs:    1) dataTime:    updated state of charge of the battery
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
# Function
#######################################################################################################################
def elecVeh(data, dataTime, setup):
    ###################################################################################################################
    # MSG IN
    ###################################################################################################################
    print("INFO: Parameter Electrical Vehicle")

    ###################################################################################################################
    # Initialisation
    ###################################################################################################################
    V_max = setup['Par']['HVS']['V_max']                                                                                 # maximum battery voltage (V)
    V_min = setup['Par']['HVS']['V_min']                                                                                 # minimum battery voltage (V)
    V_nom = setup['Par']['HVS']['V_nom']                                                                                 # nominal battery voltage (V)
    SOC = setup['Exp']['SOC']                                                                                            # battery state of charge (%)
    N = len(data['t'])                                                                                                   # number of samples

    ###################################################################################################################
    # Calculation
    ###################################################################################################################
    # ==============================================================================
    # Measured V_DC
    # ==============================================================================
    if setup['Exp']['Vdc'] == 2:
        dataTime['VEH']['Vdc'] = data['V_DC']
        dataTime['VEH']['SOC'] = (data['V_DC'] - V_min) / (V_max - V_min)
        print("INFO: Using measured HVS voltage")

    # ==============================================================================
    # SOC based
    # ==============================================================================
    elif setup['Exp']['Vdc'] == 3:
        print("INFO: Using SOC based HVS voltage")
        dataTime['VEH']['Vdc'] = (V_max - (V_max - V_min) * (1 - SOC)) * np.ones(N)
        dataTime['VEH']['SOC'] = SOC * np.ones(N)
        data['V_DC'] = (V_max - (V_max - V_min) * (1 - SOC)) * np.ones((N, 1))

    # ==============================================================================
    # Constant
    # ==============================================================================
    else:
        print("INFO: Using constant nominal HVS voltage")
        dataTime['VEH']['Vdc'] = V_nom * np.ones(N)
        dataTime['VEH']['SOC'] = (V_nom - V_min) / (V_max - V_min) * np.ones(N)
        data['V_DC'] = V_nom * np.ones((N, 1))

    ###################################################################################################################
    # Post-processing
    ###################################################################################################################
    if setup['Exp']['lim'] == 0:
        dataTime['VEH']['Vdc'] = 1000 * np.ones(N)
        data['V_DC'] = 1000 * np.ones(N)

    ###################################################################################################################
    # Return
    ###################################################################################################################

    return [data, dataTime]

    ###################################################################################################################
    # References
    ###################################################################################################################
