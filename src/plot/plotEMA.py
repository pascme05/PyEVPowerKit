#######################################################################################################################
#######################################################################################################################
# Title:        Python Electric Vehicle Power Toolkit (PyEVPowerKit)
# Topic:        EV Modeling
# File:         plotEMA
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
import numpy as np
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
def plotEMA(data, dataTime, setup):
    print("INFO: Plotting EMA data")

    time = data['t']
    axis = setup['Exp']['plotAxis']

    fig, axs = plt.subplots(3, 3, sharex=True)

    # Mechanical
    axs[0, 0].plot(time, dataTime['EMA'][axis]['M'], label='EMA Torque (tar)')
    axs[0, 0].plot(time, dataTime['EMA'][axis]['Min'], label='EMA Torque (act)')
    axs[0, 0].legend()

    axs[1, 0].plot(time, dataTime['EMA'][axis]['n'], label='EMA Speed')
    axs[2, 0].plot(time, dataTime['EMA'][axis]['Pm']/1000, label='EMA Power')

    # Losses
    axs[0, 1].plot(time, dataTime['EMA'][axis]['Is'], label='EMA Currents (Is)')
    axs[0, 1].plot(time, dataTime['EMA'][axis]['Id'] / np.sqrt(2), label='EMA Currents (Id)')
    axs[0, 1].plot(time, dataTime['EMA'][axis]['Iq'] / np.sqrt(2), label='EMA Currents (Iq)')
    axs[0, 1].legend()

    axs[1, 1].plot(time, dataTime['EMA'][axis]['Vs'], label='EMA Voltages (Vs)')
    axs[1, 1].plot(time, dataTime['EMA'][axis]['Vd'] / np.sqrt(2), label='EMA Voltages (Vd)')
    axs[1, 1].plot(time, dataTime['EMA'][axis]['Vq'] / np.sqrt(2), label='EMA Voltages (Vq)')
    axs[1, 1].legend()

    axs[2, 1].plot(time, dataTime['EMA'][axis]['lam'], label='EMA Fluxes')

    # Losses
    axs[0, 2].plot(time, dataTime['EMA'][axis]['Pv'], label='Total Losses')
    axs[0, 2].plot(time, dataTime['EMA'][axis]['Pv_m'], label='Mech Losses')
    axs[0, 2].plot(time, dataTime['EMA'][axis]['Pv_s'], label='Stator Losses')
    axs[0, 2].plot(time, dataTime['EMA'][axis]['Pv_r'], label='Rotor Losses')
    axs[0, 2].legend()

    # Thermal
    axs[1, 2].plot(time, dataTime['EMA'][axis]['eta']*100, label='Total Efficiency')
    axs[2, 2].plot(time, dataTime['EMA'][axis]['T'], label='Hotspot Temperature')
    axs[2, 2].plot(time, dataTime['VEH']['Tc'], label='Coolant Temperature')
    axs[2, 2].legend()

    # Grid activation
    for ax_row in axs:
        for ax in ax_row:
            ax.grid(True)

    # Axis labels
    axs[0, 0].set_ylabel('M (Nm)')
    axs[1, 0].set_ylabel('n (1/s)')
    axs[2, 0].set_ylabel('P (kW)')

    axs[0, 1].set_ylabel('Is RMS (A)')
    axs[1, 1].set_ylabel('Vs RMS (V)')
    axs[2, 1].set_ylabel('Lam (Vs)')

    axs[0, 2].set_ylabel('Pv (W)')
    axs[1, 2].set_ylabel('Eta (%)')
    axs[2, 2].set_ylabel('T (degC)')

    axs[2, 0].set_xlabel('time (sec)')
    axs[2, 1].set_xlabel('time (sec)')
    axs[2, 2].set_xlabel('time (sec)')

    # Titles
    axs[0, 0].set_title('EMA Torque')
    axs[1, 0].set_title('EMA Speed')
    axs[2, 0].set_title('EMA Power')

    axs[0, 1].set_title('EMA Currents and Voltages')
    axs[1, 1].set_title('EMA Currents and Voltages')
    axs[2, 1].set_title('EMA Fluxes')

    axs[0, 2].set_title('EMA Losses')
    axs[1, 2].set_title('EMA Efficiency')
    axs[2, 2].set_title('EMA Thermal')

    # Layout adjustments
    fig.suptitle("Machine Mechanics, Electrical, Losses, and Thermal (" + axis + ")", size=18)
    plt.subplots_adjust(hspace=0.35, wspace=0.35, left=0.075, right=0.925, top=0.90, bottom=0.075)

    return []
