#######################################################################################################################
#######################################################################################################################
# Title:        Python Electric Vehicle Power Toolkit (PyEVPowerKit)
# Topic:        EV Modeling
# File:         plotMax
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

#######################################################################################################################
# Additional Functions
#######################################################################################################################


#######################################################################################################################
# Main Function
#######################################################################################################################
def plotMax(data, dataTime, setup):
    print("INFO: Plotting Maximum Loads")

    time = data['t']
    axis = setup['Exp']['plotAxis']
    cat = ['HVS', 'INV', 'EMA', 'GBX']
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']

    fig, axs = plt.subplots(5, 2, sharex=False)

    # Statistical Values
    M_Max_HVS = 0
    M_Max_INV = 0
    M_Max_EMA = np.nanmax(dataTime['EMA'][axis]['Min'])
    M_Max_GBX = np.nanmax(dataTime['GBX'][axis]['M'])

    P_Max_HVS = np.nanmax(dataTime['HVS']['Pout'])
    P_Max_INV = np.nanmax(dataTime['INV'][axis]['Pout'])
    P_Max_EMA = np.nanmax(dataTime['EMA'][axis]['Pout'])
    P_Max_GBX = np.nanmax(dataTime['GBX'][axis]['Pout'])

    I_Max_HVS = np.nanmax(dataTime['HVS']['Idc'])
    I_Max_INV = np.nanmax(dataTime['INV'][axis]['Idc'])
    I_Max_EMA = np.nanmax(dataTime['EMA'][axis]['Is'])
    I_Max_GBX = 0

    V_Max_HVS = np.nanmax(dataTime['HVS']['Vdc'])
    V_Max_INV = np.nanmax(dataTime['INV'][axis]['Mi']*dataTime['HVS']['Vdc']/2)
    V_Max_EMA = np.nanmax(dataTime['EMA'][axis]['Vs'])
    V_Max_GBX = 0

    T_Max_HVS = np.nanmax(dataTime['HVS']['T'])
    T_Max_INV = np.nanmax(dataTime['INV'][axis]['T'])
    T_Max_EMA = np.nanmax(dataTime['EMA'][axis]['T'])
    T_Max_GBX = np.nanmax(dataTime['GBX'][axis]['T'])

    M_Max = [M_Max_HVS, M_Max_INV, M_Max_EMA, M_Max_GBX]
    P_Max = [P_Max_HVS / 1000, P_Max_INV / 1000, P_Max_EMA / 1000, P_Max_GBX / 1000]
    I_Max = [I_Max_HVS, I_Max_INV, I_Max_EMA, I_Max_GBX]
    V_Max = [V_Max_HVS, V_Max_INV, V_Max_EMA, V_Max_GBX]
    T_Max = [T_Max_HVS, T_Max_INV, T_Max_EMA, T_Max_GBX]

    M_Lim = [0, 0, setup['Par']['EMA']['M_max'], setup['Par']['GBX']['M_max']]
    P_Lim = [setup['Par']['HVS']['P_max'] / 1000, setup['Par']['INV']['P_max'] / 1000, setup['Par']['EMA']['P_max'] / 1000, setup['Par']['GBX']['P_max'] / 1000]
    I_Lim = [setup['Par']['HVS']['I_max'], setup['Par']['INV']['I_max'] / np.sqrt(2), setup['Par']['EMA']['I_max'] / np.sqrt(2), 0]
    V_Lim = [setup['Par']['HVS']['V_max'], setup['Par']['HVS']['V_max'] / np.sqrt(3), setup['Par']['HVS']['V_max'] / np.sqrt(6), 0]
    T_Lim = [setup['Par']['HVS']['T_max'], setup['Par']['INV']['T_max'], setup['Par']['EMA']['T_max'], setup['Par']['GBX']['T_max']]

    # Time Series
    axs[0, 0].plot(time, dataTime['EMA'][axis]['Min'], label='EMA Inner Torque')
    axs[0, 0].plot(time, dataTime['GBX'][axis]['M'], label='GBX Input Torque')
    axs[0, 0].grid(True)
    axs[0, 0].legend()

    axs[1, 0].plot(time, dataTime['HVS']['Pout']/1000, label='HVS Output Power')
    axs[1, 0].plot(time, dataTime['INV'][axis]['Pout']/1000, label='INV Output Power')
    axs[1, 0].plot(time, dataTime['EMA'][axis]['Pout']/1000, label='EMA Output Power')
    axs[1, 0].plot(time, dataTime['GBX'][axis]['Pout']/1000, label='GBX Output Power')
    axs[1, 0].grid(True)
    axs[1, 0].legend()

    axs[2, 0].plot(time, dataTime['HVS']['Idc'], label='HVS Input Current')
    axs[2, 0].plot(time, dataTime['INV'][axis]['Idc'], label='INV Input Current')
    axs[2, 0].plot(time, dataTime['EMA'][axis]['Is'], label='EMA Stator Current')
    axs[2, 0].grid(True)
    axs[2, 0].legend()

    axs[3, 0].plot(time, dataTime['HVS']['Vdc'], label='HVS Voltage')
    axs[3, 0].plot(time, dataTime['INV'][axis]['Mi']*dataTime['HVS']['Vdc']/2, label='INV Output Voltage')
    axs[3, 0].plot(time, dataTime['EMA'][axis]['Vs'], label='EMA Phase Voltage')
    axs[3, 0].grid(True)
    axs[3, 0].legend()

    axs[4, 0].plot(time, dataTime['HVS']['T'], label='HVS Temperature')
    axs[4, 0].plot(time, dataTime['INV'][axis]['T'], label='INV Temperature')
    axs[4, 0].plot(time, dataTime['EMA'][axis]['T'], label='EMA Temperature')
    axs[4, 0].plot(time, dataTime['GBX'][axis]['T'], label='GBX Temperature')
    axs[4, 0].grid(True)
    axs[4, 0].legend()

    # Average Values
    axs[0, 1].bar(cat, M_Lim, color=colors[0], label='M_Lim')
    axs[0, 1].bar(cat, M_Max, color=colors[1], label='M_Max')
    axs[0, 1].grid(True)

    axs[1, 1].bar(cat, P_Lim, color=colors[0], label='P_Lim')
    axs[1, 1].bar(cat, P_Max, color=colors[1], label='P_Max')
    axs[1, 1].grid(True)

    axs[2, 1].bar(cat, I_Lim, color=colors[0], label='I_Lim')
    axs[2, 1].bar(cat, I_Max, color=colors[1], label='I_Max')
    axs[2, 1].grid(True)

    axs[3, 1].bar(cat, V_Lim, color=colors[0], label='V_Lim')
    axs[3, 1].bar(cat, V_Max, color=colors[1], label='V_Max')
    axs[3, 1].grid(True)

    axs[4, 1].bar(cat, T_Lim, color=colors[0], label='T_Lim')
    axs[4, 1].bar(cat, T_Max, color=colors[1], label='T_Max')
    axs[4, 1].grid(True)

    # Title and labels
    axs[0, 0].set_title('Torque (GBX, EMA)')
    axs[1, 0].set_title('Power (GBX, EMA, INV, HVS)')
    axs[2, 0].set_title('Current (EMA, INV, HVS)')
    axs[3, 0].set_title('Voltage (EMA, INV, HVS)')
    axs[4, 0].set_title('Temperature (GBX, EMA, INV, HVS)')

    # Axis
    axs[0, 0].set_ylabel('Torque (Nm)')
    axs[1, 0].set_ylabel('Power (kW)')
    axs[2, 0].set_ylabel('Current (A)')
    axs[3, 0].set_ylabel('Voltage (V)')
    axs[4, 0].set_ylabel('Temperature (degC)')

    axs[4, 0].set_xlabel('Time (sec)')
    axs[4, 1].set_xlabel('Component')

    plt.suptitle('Comparing actual and maximum values', size=18)
    plt.subplots_adjust(hspace=0.35, wspace=0.35, left=0.075, right=0.925, top=0.90, bottom=0.075)
    plt.show()

    return []
