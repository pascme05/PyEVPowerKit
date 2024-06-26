#######################################################################################################################
#######################################################################################################################
# Title:        Python Electric Vehicle Power Toolkit (PyEVPowerKit)
# Topic:        EV Modeling
# File:         plotVeh
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
import numpy as np
import copy

#######################################################################################################################
# Additional Functions
#######################################################################################################################


#######################################################################################################################
# Main Function
#######################################################################################################################
def plotVeh(data, dataTime, setup):
    print("INFO: Plotting vehicle data")

    eff = setup['Par']['VEH']['eta'] * 100
    etaT = dataTime['GBX']['T']['eta'] * dataTime['EMA']['T']['eta'] * dataTime['INV']['T']['eta'] * dataTime['HVS']['eta']
    etaT2 = np.zeros((len(data['t'])))

    for i in range(len(data['t'])):
        if dataTime['HVS']['Idc'][i] < 0:
            etaT2[i] = etaT[i] ** 2
        else:
            etaT2[i] = etaT[i]
    # etaTmean = np.nanmean(etaT) * 100
    etaTmean2 = np.nanmean(etaT2) * 100

    time = data['t']

    fig, axs = plt.subplots(4, 1, sharex=True)

    axs[0].plot(time, dataTime['VEH']['F']['t'] / 1000)
    axs[0].set_ylabel('F (kN)')
    axs[0].set_title('Vehicle Forces')
    axs[0].grid(True)

    axs[1].plot(time, dataTime['VEH']['P']['t'] / 1000)
    axs[1].set_ylabel('P (kW)')
    axs[1].set_title('Vehicle Power')
    axs[1].grid(True)

    axs[2].plot(time, dataTime['VEH']['E']['t'] / 3.6e6, label='Vehicle Energy (100% Rec Efficiency)')
    axs[2].plot(time, dataTime['VEH']['E']['rec_on'] / 3.6e6, label='Vehicle Energy (' + str(int(eff)) + '% Rec Efficiency)')
    axs[2].plot(time, dataTime['VEH']['E']['t'] / etaTmean2 / 3.6e6 * 100, label='Vehicle Energy (' + str(int(etaTmean2)) + '% Rec Efficiency)')
    axs[2].plot(time, dataTime['VEH']['E']['rec_off'] / 3.6e6, label='Vehicle Energy (0% Rec Efficiency)')
    axs[2].set_ylabel('E (kWh)')
    axs[2].set_title('Vehicle Energy')
    axs[2].legend()
    axs[2].grid(True)

    axs[3].plot(time, dataTime['VEH']['eta']['t'], label='Vehicle Consumption (100% Rec Efficiency)')
    axs[3].plot(time, dataTime['VEH']['eta']['rec_on'], label='Vehicle Consumption (' + str(int(eff)) + '% Rec Efficiency)')
    axs[3].plot(time, dataTime['VEH']['eta']['t'] / etaTmean2 * 100, label='Vehicle Consumption (' + str(int(etaTmean2)) + '% Rec Efficiency)')
    axs[3].plot(time, dataTime['VEH']['eta']['rec_off'], label='Vehicle Consumption (0% Rec Efficiency)')
    axs[3].set_ylabel('Eta (kWh/100 km)')
    axs[3].set_xlabel('time (sec)')
    axs[3].set_title('Vehicle Consumption')
    axs[3].legend()
    axs[3].grid(True)

    fig.suptitle("Vehicle Forces, Power, Energies, and Efficiencies", size=18)
    plt.subplots_adjust(hspace=0.35, wspace=0.35, left=0.075, right=0.925, top=0.90, bottom=0.075)

    return []
