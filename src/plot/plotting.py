#######################################################################################################################
#######################################################################################################################
# Title:        Python Electric Vehicle Power Toolkit (PyEVPowerKit)
# Topic:        EV Modeling
# File:         plotting
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
from src.plot.plotProfile import plotProfile
from src.plot.plotVeh import plotVeh
from src.plot.plotVehDetail import plotVehDetail
from src.plot.plotGBX import plotGBX
from src.plot.plotEMA import plotEMA
from src.plot.plotINV import plotINV
from src.plot.plotPWR import plotPWR
from src.plot.plotHVS import plotHVS

# ==============================================================================
# External
# ==============================================================================

#######################################################################################################################
# Additional Functions
#######################################################################################################################


#######################################################################################################################
# Main Function
#######################################################################################################################
def plotting(data, dataTime, setup):
    ###################################################################################################################
    # MSG IN
    ###################################################################################################################
    print("START: Plotting")

    ###################################################################################################################
    # Initialisation
    ###################################################################################################################
    # ==============================================================================
    # Parameters
    # ==============================================================================

    # ==============================================================================
    # Variables
    # ==============================================================================

    ###################################################################################################################
    # Calculation
    ###################################################################################################################
    # ==============================================================================
    # Mission Profile
    # ==============================================================================
    plotProfile(data, setup)

    # ==============================================================================
    # Vehicle
    # ==============================================================================
    # ------------------------------------------
    # Overall
    # ------------------------------------------
    if setup['Exp']['plot'] == 1:
        plotVeh(data, dataTime, setup)

    # ------------------------------------------
    # Detail
    # ------------------------------------------
    if setup['Exp']['plot'] == 2:
        plotVehDetail(data, dataTime, setup)

    # ==============================================================================
    # Gearbox
    # ==============================================================================
    plotGBX(data, dataTime, setup)

    # ==============================================================================
    # Electric Machinery
    # ==============================================================================
    plotEMA(data, dataTime, setup)

    # ==============================================================================
    # Electric Converter
    # ==============================================================================
    plotINV(data, dataTime, setup)

    # ==============================================================================
    # Electric Storage
    # ==============================================================================
    plotHVS(data, dataTime, setup)

    ###################################################################################################################
    # Post-Processing
    ###################################################################################################################
    # ==============================================================================
    # Power Overview
    # ==============================================================================
    plotPWR(data, dataTime, setup)

    ###################################################################################################################
    # MSG Out
    ###################################################################################################################
    print("END: Plotting")

    ###################################################################################################################
    # Return
    ###################################################################################################################
    return data

#######################################################################################################################
# References
#######################################################################################################################
