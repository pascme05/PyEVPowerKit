#######################################################################################################################
#######################################################################################################################
# Title:        Python Electric Vehicle Power Toolkit (PyEVPowerKit)
# Topic:        EV Modeling
# File:         plotVehDetail
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
def plotVehDetail(data, dataTime, setup):
    print("INFO: Plotting vehicle data (detail)")

    time = data['t']

    fig, axs = plt.subplots(5, 3, sharex=True)

    # Forces
    axs[0, 0].plot(time, dataTime['VEH']['F']['p'] / 1000, color='#636EFA', linestyle='solid')
    axs[0, 1].plot(time, dataTime['VEH']['F']['r'] / 1000, color='#EF553B', linestyle='solid')
    axs[0, 2].plot(time, dataTime['VEH']['F']['c'] / 1000, color='#00CC96', linestyle='solid')
    axs[1, 0].plot(time, dataTime['VEH']['F']['a'] / 1000, color='#AB63FA', linestyle='solid')
    axs[2, 0].plot(time, dataTime['VEH']['F']['t'] / 1000, color='#FFA15A', linestyle='solid')

    # Power
    axs[0, 0].plot(time, dataTime['VEH']['P']['p'] / 1000, color='#636EFA', linestyle='dashed')
    axs[0, 1].plot(time, dataTime['VEH']['P']['r'] / 1000, color='#EF553B', linestyle='dashed')
    axs[0, 2].plot(time, dataTime['VEH']['P']['c'] / 1000, color='#00CC96', linestyle='dashed')
    axs[1, 0].plot(time, dataTime['VEH']['P']['a'] / 1000, color='#AB63FA', linestyle='dashed')
    axs[2, 0].plot(time, dataTime['VEH']['P']['t'] / 1000, color='#FFA15A', linestyle='dashed')

    # Energy
    axs[0, 0].plot(time, dataTime['VEH']['E']['p'] / 3.6e6, color='#636EFA', linestyle='dotted')
    axs[0, 1].plot(time, dataTime['VEH']['E']['r'] / 3.6e6, color='#EF553B', linestyle='dotted')
    axs[0, 2].plot(time, dataTime['VEH']['E']['c'] / 3.6e6, color='#00CC96', linestyle='dotted')
    axs[1, 0].plot(time, dataTime['VEH']['E']['a'] / 3.6e6, color='#AB63FA', linestyle='dotted')
    axs[2, 0].plot(time, dataTime['VEH']['E']['t'] / 3.6e6, color='#FFA15A', linestyle='dotted')

    # Grid activation
    for ax_row in axs:
        for ax in ax_row:
            ax.grid(True)

    # Axis labels
    axs[0, 0].set_ylabel('F (kN)')
    axs[1, 0].set_ylabel('F (kN)')
    axs[2, 0].set_ylabel('F (kN)')
    axs[3, 0].set_ylabel('F (kN)')
    axs[4, 0].set_ylabel('F (kN)')

    axs[0, 1].set_ylabel('P (kW)')
    axs[1, 1].set_ylabel('P (kW)')
    axs[2, 1].set_ylabel('P (kW)')
    axs[3, 1].set_ylabel('P (kW)')
    axs[4, 1].set_ylabel('P (kW)')

    axs[0, 2].set_ylabel('E (kWh)')
    axs[1, 2].set_ylabel('E (kWh)')
    axs[2, 2].set_ylabel('E (kWh)')
    axs[3, 2].set_ylabel('E (kWh)')
    axs[4, 2].set_ylabel('E (kWh)')

    axs[4, 0].set_xlabel('time (sec)')
    axs[4, 1].set_xlabel('time (sec)')
    axs[4, 2].set_xlabel('time (sec)')

    # Titles
    axs[0, 0].set_title('Vehicle Forces (Air)')
    axs[0, 1].set_title('Vehicle Forces (Rolling)')
    axs[0, 2].set_title('Vehicle Forces (Climbing)')
    axs[1, 0].set_title('Vehicle Forces (Acceleration)')
    axs[2, 0].set_title('Vehicle Forces (Total)')

    axs[0, 0].set_title('Vehicle Power (Air)')
    axs[0, 1].set_title('Vehicle Power (Rolling)')
    axs[0, 2].set_title('Vehicle Power (Climbing)')
    axs[1, 0].set_title('Vehicle Power (Acceleration)')
    axs[2, 0].set_title('Vehicle Power (Total)')

    axs[0, 0].set_title('Vehicle Energy (Air)')
    axs[0, 1].set_title('Vehicle Energy (Rolling)')
    axs[0, 2].set_title('Vehicle Energy (Climbing)')
    axs[1, 0].set_title('Vehicle Energy (Acceleration)')
    axs[2, 0].set_title('Vehicle Energy (Total)')

    # Layout adjustments
    fig.suptitle("Vehicle Forces, Power, Energies, and Efficiencies (Detail)", size=18)
    plt.subplots_adjust(hspace=0.35, wspace=0.35, left=0.075, right=0.925, top=0.90, bottom=0.075)

    return []
