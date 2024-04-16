#######################################################################################################################
#######################################################################################################################
# Title:        Python Electric Vehicle Power Toolkit (PyEVPowerKit)
# Topic:        EV Modeling
# File:         plotGBX
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
import matplotlib.pyplot as plt

#######################################################################################################################
# Additional Functions
#######################################################################################################################


#######################################################################################################################
# Main Function
#######################################################################################################################
def plotGBX(data, dataTime, setup):
    print("INFO: Plotting GBX data")

    time = data['t']
    axis = setup['Exp']['plotAxis']

    fig, axs = plt.subplots(3, 2, sharex=True)

    # Mechanical
    axs[0, 0].plot(time, dataTime['GBX'][axis]['M'], label='GBX Torque')
    axs[1, 0].plot(time, dataTime['GBX'][axis]['n'], label='GBX Speed')
    axs[2, 0].plot(time, dataTime['GBX'][axis]['Pin']/1000, label='GBX Power')

    # Losses
    axs[0, 1].plot(time, dataTime['GBX'][axis]['Pv'], label='Total Losses')
    axs[0, 1].plot(time, dataTime['GBX'][axis]['Pv_B'], label='Losses Bearing')
    axs[0, 1].plot(time, dataTime['GBX'][axis]['Pv_M'], label='Losses Meshing')
    axs[0, 1].plot(time, dataTime['GBX'][axis]['Pv_W'], label='Losses Windage')
    axs[0, 1].legend()

    # Efficiency
    axs[1, 1].plot(time, dataTime['GBX'][axis]['eta'], label='Total Efficiency')
    axs[2, 1].plot(time, dataTime['GBX'][axis]['T'], label='Hotspot Temperature')
    axs[2, 1].plot(time, dataTime['VEH']['Tc'], label='Coolant Temperature')
    axs[2, 1].legend()

    # Grid activation
    for ax_row in axs:
        for ax in ax_row:
            ax.grid(True)

    # Axis labels
    axs[0, 0].set_ylabel('M (Nm)')
    axs[1, 0].set_ylabel('n (1/s)')
    axs[2, 0].set_ylabel('P (kW)')

    axs[0, 1].set_ylabel('Pv (W)')
    axs[1, 1].set_ylabel('Eta (%)')
    axs[2, 1].set_ylabel('T (degC)')

    axs[2, 0].set_xlabel('time (sec)')
    axs[2, 1].set_xlabel('time (sec)')

    # Titles
    axs[0, 0].set_title('GBX Torque')
    axs[1, 0].set_title('GBX Speed')
    axs[2, 0].set_title('GBX Power')

    axs[0, 1].set_title('GBX Losses')
    axs[1, 1].set_title('GBX Efficiency')
    axs[2, 1].set_title('GBX Thermal')

    # Layout adjustments
    fig.suptitle("Gearbox Mechanics, Losses, and Thermal (" + axis + ")", size=18)
    plt.subplots_adjust(hspace=0.35, wspace=0.35, left=0.075, right=0.925, top=0.90, bottom=0.075)

    return []
