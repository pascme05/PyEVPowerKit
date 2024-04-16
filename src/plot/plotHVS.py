#######################################################################################################################
#######################################################################################################################
# Title:        Python Electric Vehicle Power Toolkit (PyEVPowerKit)
# Topic:        EV Modeling
# File:         plotINV
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
def plotHVS(data, dataTime, setup):
    print("INFO: Plotting HVS data")

    time = data['t']

    fig, axs = plt.subplots(2, 3, sharex=True)

    # Electrical
    axs[0, 0].plot(time, dataTime['HVS']['Vdc'], label='HVS Voltage')
    axs[1, 0].plot(time, dataTime['HVS']['Idc'], label='HVS Current')

    # Charge
    axs[0, 1].plot(time, dataTime['HVS']['SOC'], label='HVS SOC')
    axs[1, 1].plot(time, dataTime['HVS']['dQ']/1000, label='HVS Charge')

    # Thermal
    axs[0, 2].plot(time, dataTime['HVS']['Pv'], label='Total Losses')
    axs[1, 2].plot(time, dataTime['HVS']['T'], label='Hotspot Temperature')
    axs[1, 2].plot(time, dataTime['VEH']['Tc'], label='Coolant Temperature')
    axs[1, 2].legend()

    # Grid activation
    for ax_row in axs:
        for ax in ax_row:
            ax.grid(True)

    # Axis labels
    axs[0, 0].set_ylabel('Vdc (V)')
    axs[1, 0].set_ylabel('Idc RMS (A)')

    axs[0, 1].set_ylabel('SOC (%)')
    axs[1, 1].set_ylabel('dQ (kJ)')

    axs[0, 2].set_ylabel('Pv (W)')
    axs[1, 2].set_ylabel('T (degC)')

    axs[1, 0].set_xlabel('time (sec)')
    axs[1, 1].set_xlabel('time (sec)')
    axs[1, 2].set_xlabel('time (sec)')

    # Titles
    axs[0, 0].set_title('HVS Voltage')
    axs[1, 0].set_title('HVS Current')

    axs[0, 1].set_title('HVS SOC')
    axs[1, 1].set_title('HVS Charge')

    axs[0, 2].set_title('Total Losses')
    axs[1, 2].set_title('Hotspot and Coolant Temperature')

    # Layout adjustments
    fig.suptitle("HVS Electrical, Charge, and Thermal", size=18)
    plt.subplots_adjust(hspace=0.35, wspace=0.35, left=0.075, right=0.925, top=0.90, bottom=0.075)

    return []
