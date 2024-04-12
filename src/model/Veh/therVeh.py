#######################################################################################################################
#######################################################################################################################
# Title:        Python Electric Vehicle Power Toolkit (PyEVPowerKit)
# Topic:        EV Modeling
# File:         therVeh
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
def therVeh(data, dataTime, setup):
    ###################################################################################################################
    # MSG IN
    ###################################################################################################################
    print("INFO: Parameter Thermal Vehicle")

    ###################################################################################################################
    # Initialisation
    ###################################################################################################################
    # ==============================================================================
    # Parameters
    # ==============================================================================
    N = len(data['t'])

    # ==============================================================================
    # Variables
    # ==============================================================================
    Tcon = setup['Exp']['Tc']

    ###################################################################################################################
    # Calculation
    ###################################################################################################################
    # ==============================================================================
    # Measured T_C
    # ==============================================================================
    if setup['Exp']['Cool'] == 2:
        Tc = data['T_C'].to_numpy()
        print("INFO: Using measured coolant temperature")

    # ==============================================================================
    # Model based
    # ==============================================================================
    elif setup['Exp']['Cool'] == 3:
        Tc = data['T_C'].to_numpy()
        print("INFO: Using model based coolant temperature")

    # ==============================================================================
    # Constant
    # ==============================================================================
    else:
        # ------------------------------------------
        # Msg
        # ------------------------------------------
        print("INFO: Using constant coolant temperature")

        # ------------------------------------------
        # Calc
        # ------------------------------------------
        Tc = Tcon * np.ones(N)

    ###################################################################################################################
    # Post-Processing
    ###################################################################################################################
    dataTime['VEH']['Tc'] = Tc

    ###################################################################################################################
    # MSG Out
    ###################################################################################################################

    return dataTime

    ###################################################################################################################
    # References
    ###################################################################################################################
