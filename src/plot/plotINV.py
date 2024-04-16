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
def plotINV(data, dataTime, setup):
    print("INFO: Plotting INV data")

    time = data['t']
    axis = setup['Exp']['plotAxis']

    fig, axs = plt.subplots(3, 2, sharex=True)

    # Electrical
    axs[0, 0].plot(time, dataTime['INV'][axis]['Mi'], label='Modulation Index')
    axs[1, 0].plot(time, dataTime['INV'][axis]['Idc'], label='Input Current')
    axs[2, 0].plot(time, dataTime['INV'][axis]['Is'], label='Output Current')

    # Thermal
    axs[0, 1].plot(time, dataTime['INV'][axis]['Pv'], label='Total Losses')
    axs[0, 1].plot(time, dataTime['INV'][axis]['Pv_sw'], label='Losses Power Module')
    axs[0, 1].plot(time, dataTime['INV'][axis]['Pv_cap'], label='Losses DC-Link Cap')
    axs[0, 1].plot(time, dataTime['INV'][axis]['Pv_ac'], label='Losses AC Busbars')
    axs[0, 1].plot(time, dataTime['INV'][axis]['Pv_dc'], label='Losses DC Busbars')
    axs[0, 1].legend()

    # Thermal
    axs[1, 1].plot(time, dataTime['INV'][axis]['eta']*100, label='Total Efficiency')
    axs[2, 1].plot(time, dataTime['INV'][axis]['T'], label='Hotspot Temperature')
    axs[2, 1].plot(time, dataTime['VEH']['Tc'], label='Coolant Temperature')
    axs[2, 1].legend()

    # Grid activation
    for ax_row in axs:
        for ax in ax_row:
            ax.grid(True)

    # Axis labels
    axs[0, 0].set_ylabel('Mi (p.u.)')
    axs[1, 0].set_ylabel('Idc RMS (A)')
    axs[2, 0].set_ylabel('Iac RMS (A)')

    axs[0, 1].set_ylabel('Pv (W)')
    axs[1, 1].set_ylabel('Eta (%)')
    axs[2, 1].set_ylabel('T (degC)')

    axs[2, 0].set_xlabel('time (sec)')
    axs[2, 1].set_xlabel('time (sec)')

    # Titles
    axs[0, 0].set_title('Modulation Index')
    axs[1, 0].set_title('Input Current')
    axs[2, 0].set_title('Output Current')

    axs[0, 1].set_title('Total Losses')
    axs[1, 1].set_title('Total Efficiency')
    axs[2, 1].set_title('Hotspot and Coolant Temperature')

    # Layout adjustments
    fig.suptitle("Converter Electrical, Losses, and Thermal (" + axis + ")", size=18)
    plt.subplots_adjust(hspace=0.35, wspace=0.35, left=0.075, right=0.925, top=0.90, bottom=0.075)

    return []
