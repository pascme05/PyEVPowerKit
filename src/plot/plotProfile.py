#######################################################################################################################
#######################################################################################################################
# Title:        Python Electric Vehicle Power Toolkit (PyEVPowerKit)
# Topic:        EV Modeling
# File:         plotProfile
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
# Plotting
#######################################################################################################################
def plotProfile(data, dataTime, setup):
    print("INFO: Plotting mission profile")

    Ts = 1 / setup['Dat']['fs']
    name = setup['Dat']['name']
    time = data['t']

    fig, axs = plt.subplots(5, 1, sharex=True)

    axs[0].plot(time, data['v'], label='Vehicle Velocity (tar)')
    axs[0].plot(time, dataTime['VEH']['v'], label='Vehicle Velocity (act)')
    axs[0].set_ylabel('v (m/s)')
    axs[0].set_title('Vehicle Velocity')
    axs[0].legend()

    axs[1].plot(time, data['s'], label='Vehicle Distance (tar)')
    axs[1].plot(time, dataTime['VEH']['s'], label='Vehicle Distance (act)')
    axs[1].set_ylabel('s (m)')
    axs[1].set_title('Vehicle Distance')
    axs[1].legend()

    axs[2].plot(time, data['a'], label='Vehicle Acceleration (tar)')
    axs[2].plot(time, dataTime['VEH']['a'], label='Vehicle Acceleration (act)')
    axs[2].set_ylabel('a (m/s2)')
    axs[2].set_title('Vehicle Acceleration')
    axs[2].legend()

    axs[3].plot(time, data['ang'])
    axs[3].set_ylabel('ang (rad)')
    axs[3].set_title('Surface Angle')

    axs[4].plot(time, data['T_A'], label='Ambient Temperature')
    axs[4].plot(time, dataTime['VEH']['Tc'], label='Coolant Temperature')
    axs[4].set_ylabel('T (degC)')
    axs[4].set_xlabel('time (sec)')
    axs[4].set_title('Temperatures')
    axs[4].legend()

    for ax in axs:
        ax.grid(True)

    fig.suptitle("Vehicle Mission Profile: " + str(name) + " with Sampling Rate: " + str(Ts) + " (sec)", size=18)
    plt.subplots_adjust(hspace=0.35, wspace=0.35, left=0.075, right=0.925, top=0.90, bottom=0.075)

    return []
