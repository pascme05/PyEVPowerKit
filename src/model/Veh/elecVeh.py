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
    V_max = setup['Par']['HVS']['V_max']
    V_min = setup['Par']['HVS']['V_min']
    V_nom = setup['Par']['HVS']['V_nom']
    SOC = setup['Exp']['SOC']
    N = len(data['t'])

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
        dataTime['VEH']['Vdc'] = (V_max - (V_max - V_min) * (1 - SOC / 100)) * np.ones((N, 1))
        dataTime['VEH']['SOC'] = SOC * np.ones((N, 1))

    # ==============================================================================
    # Constant
    # ==============================================================================
    else:
        print("INFO: Using constant nominal HVS voltage")
        dataTime['VEH']['Vdc'] = V_nom * np.ones((N, 1))
        dataTime['VEH']['SOC'] = (V_nom - V_min) / (V_max - V_min) * np.ones((N, 1))

    ###################################################################################################################
    # Return
    ###################################################################################################################

    return dataTime

    ###################################################################################################################
    # References
    ###################################################################################################################
