#######################################################################################################################
#######################################################################################################################
# Title:        Python Electric Vehicle Power Toolkit (PyEVPowerKit)
# Topic:        EV Modeling
# File:         vehSim
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
from scipy import integrate
import numpy as np

#######################################################################################################################
# Additional Functions
#######################################################################################################################


#######################################################################################################################
# Main Function
#######################################################################################################################
def vehSim(iter, VEH, data, dataTime, setup):
    ###################################################################################################################
    # Initialisation
    ###################################################################################################################
    # ==============================================================================
    # Parameters
    # ==============================================================================
    ang = data['ang'].values[iter]

    # ==============================================================================
    # Variables
    # ==============================================================================
    v = dataTime['VEH']['v'][iter]
    M_EMA = dataTime['EMA']['T']['Msh'][iter]

    ###################################################################################################################
    # Pre-Processing
    ###################################################################################################################
    if M_EMA > 0:
        M = M_EMA * setup['Par']['GBX']['i'] * dataTime['GBX']['T']['eta'][iter]
    else:
        if setup['Par']['xwd'] == 'FWD':
            M = M_EMA * setup['Par']['GBX']['i'] / dataTime['GBX']['T']['eta'][iter] / setup['Par']['VEH']['d_b']
        elif setup['Par']['xwd'] == 'RWD':
            M = M_EMA * setup['Par']['GBX']['i'] / dataTime['GBX']['T']['eta'][iter] / (1 - setup['Par']['VEH']['d_b'])
        else:
            M = M_EMA * setup['Par']['GBX']['i'] / dataTime['GBX']['T']['eta'][iter]

    ###################################################################################################################
    # Calculation
    ###################################################################################################################
    a = VEH.calc_acc(M, v, ang, setup)

    ###################################################################################################################
    # Post-Processing
    ###################################################################################################################
    # ==============================================================================
    # GBX
    # ==============================================================================
    # ------------------------------------------
    # Init
    # ------------------------------------------
    M_GBX = M / setup['Par']['GBX']['i']
    P_GBX = 2 * np.pi * M_GBX * dataTime['EMA']['T']['n']

    # ------------------------------------------
    # Accelerating
    # ------------------------------------------
    if M_EMA > 0:
        if setup['Par']['xwd'] == 'RWD':
            dataTime['GBX']['T']['M'][iter] = M_GBX
            dataTime['GBX']['F']['M'][iter] = 0
            dataTime['GBX']['R']['M'][iter] = M_GBX
        elif setup['Par']['xwd'] == 'FWD':
            dataTime['GBX']['T']['M'][iter] = M_GBX
            dataTime['GBX']['F']['M'][iter] = M_GBX
            dataTime['GBX']['R']['M'][iter] = 0
        else:
            dataTime['GBX']['T']['M'][iter] = M_GBX
            dataTime['GBX']['F']['M'][iter] = M_GBX * setup['Par']['VEH']['d_a']
            dataTime['GBX']['R']['M'][iter] = M_GBX * (1 - setup['Par']['VEH']['d_a'])

    # ------------------------------------------
    # Breaking
    # ------------------------------------------
    else:
        if setup['Par']['xwd'] == 'RWD':
            dataTime['GBX']['T']['M'][iter] = M_GBX
            dataTime['GBX']['F']['M'][iter] = 0
            dataTime['GBX']['R']['M'][iter] = M_GBX
        elif setup['Par']['xwd'] == 'FWD':
            dataTime['GBX']['T']['M'][iter] = M_GBX
            dataTime['GBX']['F']['M'][iter] = M_GBX
            dataTime['GBX']['R']['M'][iter] = 0
        else:
            dataTime['GBX']['T']['M'][iter] = M_GBX
            dataTime['GBX']['F']['M'][iter] = M_GBX * setup['Par']['VEH']['d_b']
            dataTime['GBX']['R']['M'][iter] = M_GBX * (1 - setup['Par']['VEH']['d_b'])

    # ------------------------------------------
    # Power
    # ------------------------------------------
    dataTime['GBX']['T']['Pout'][iter] = 2 * np.pi * dataTime['EMA']['T']['n'][iter] * dataTime['GBX']['T']['M'][iter]
    dataTime['GBX']['F']['Pout'][iter] = 2 * np.pi * dataTime['EMA']['F']['n'][iter] * dataTime['GBX']['F']['M'][iter]
    dataTime['GBX']['R']['Pout'][iter] = 2 * np.pi * dataTime['EMA']['R']['n'][iter] * dataTime['GBX']['R']['M'][iter]
    dataTime['GBX']['T']['Pin'][iter] = dataTime['GBX']['T']['Pout'][iter] + dataTime['GBX']['T']['Pv'][iter]
    dataTime['GBX']['F']['Pin'][iter] = dataTime['GBX']['F']['Pout'][iter] + dataTime['GBX']['F']['Pv'][iter]
    dataTime['GBX']['R']['Pin'][iter] = dataTime['GBX']['R']['Pout'][iter] + dataTime['GBX']['R']['Pv'][iter]

    # ==============================================================================
    # Vehicle
    # ==============================================================================
    dataTime['VEH']['a'][iter] = a
    dataTime['VEH']['v'] = integrate.cumtrapz(dataTime['VEH']['a'], data['t'].values, initial=0)
    dataTime['VEH']['s'] = integrate.cumtrapz(dataTime['VEH']['v'], data['t'].values, initial=0)

    ###################################################################################################################
    # Return
    ###################################################################################################################
    return dataTime

#######################################################################################################################
# References
#######################################################################################################################
