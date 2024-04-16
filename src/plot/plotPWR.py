#######################################################################################################################
#######################################################################################################################
# Title:        Python Electric Vehicle Power Toolkit (PyEVPowerKit)
# Topic:        EV Modeling
# File:         plotPWR
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
def grouped_bar_plot(ax, data, categories, bar_labels):
    n_categories = len(categories)
    n_bars = len(data)

    index = np.arange(n_categories) * 1.5  # Adjust the multiplier for the distance between categories
    bar_width = 0.35
    opacity = 0.8
    bar_offsets = np.linspace(-0.35, 0.35, n_bars)

    for i in range(n_bars):
        ax.bar(index + bar_offsets[i], data[i], bar_width,
               alpha=opacity, label=bar_labels[i])

    ax.set_xticks(index)
    ax.set_xticklabels(categories)
    ax.grid(True)
    ax.legend()


#######################################################################################################################
# Main Function
#######################################################################################################################
def plotPWR(data, dataTime, setup):
    ###################################################################################################################
    # MSG IN
    ###################################################################################################################
    print("INFO: Plotting Power Overview")

    ###################################################################################################################
    # Initialisation
    ###################################################################################################################
    time = data['t']
    axis = setup['Exp']['plotAxis']
    cat = ['HVS', 'INV', 'EMA', 'GBX']
    cat2 = ['HVS', 'INV', 'EMA', 'GBX', 'WHE']
    bar = ['Avg', 'Std', 'Max']

    ###################################################################################################################
    # Pre-Processing
    ###################################################################################################################
    # ==============================================================================
    # Statistical Values
    # ==============================================================================
    # ------------------------------------------
    # Power Input
    # ------------------------------------------
    # Avg
    Pin_Avg_HVS = np.nanmean(dataTime['HVS']['Pin'])
    Pin_Avg_INV = np.nanmean(dataTime['INV'][axis]['Pin'])
    Pin_Avg_EMA = np.nanmean(dataTime['EMA'][axis]['Pin'])
    Pin_Avg_GBX = np.nanmean(dataTime['GBX'][axis]['Pin'])
    Pin_Avg_WHE = np.nanmean(dataTime['WHE'][axis]['P'])

    # Std
    Pin_Std_HVS = np.nanstd(dataTime['HVS']['Pin'])
    Pin_Std_INV = np.nanstd(dataTime['INV'][axis]['Pin'])
    Pin_Std_EMA = np.nanstd(dataTime['EMA'][axis]['Pin'])
    Pin_Std_GBX = np.nanstd(dataTime['GBX'][axis]['Pin'])
    Pin_Std_WHE = np.nanstd(dataTime['WHE'][axis]['P'])

    # Max
    Pin_Max_HVS = np.nanmax(dataTime['HVS']['Pin'])
    Pin_Max_INV = np.nanmax(dataTime['INV'][axis]['Pin'])
    Pin_Max_EMA = np.nanmax(dataTime['EMA'][axis]['Pin'])
    Pin_Max_GBX = np.nanmax(dataTime['GBX'][axis]['Pin'])
    Pin_Max_WHE = np.nanmax(dataTime['WHE'][axis]['P'])

    # ------------------------------------------
    # Power Output
    # ------------------------------------------
    # Avg
    Pout_Avg_HVS = np.nanmean(dataTime['HVS']['Pout'])
    Pout_Avg_INV = np.nanmean(dataTime['INV'][axis]['Pout'])
    Pout_Avg_EMA = np.nanmean(dataTime['EMA'][axis]['Pout'])
    Pout_Avg_GBX = np.nanmean(dataTime['GBX'][axis]['Pout'])
    Pout_Avg_WHE = np.nanmean(dataTime['WHE'][axis]['P'])

    # Std
    Pout_Std_HVS = np.nanstd(dataTime['HVS']['Pout'])
    Pout_Std_INV = np.nanstd(dataTime['INV'][axis]['Pout'])
    Pout_Std_EMA = np.nanstd(dataTime['EMA'][axis]['Pout'])
    Pout_Std_GBX = np.nanstd(dataTime['GBX'][axis]['Pout'])
    Pout_Std_WHE = np.nanstd(dataTime['WHE'][axis]['P'])

    # Max
    Pout_Max_HVS = np.nanmax(dataTime['HVS']['Pout'])
    Pout_Max_INV = np.nanmax(dataTime['INV'][axis]['Pout'])
    Pout_Max_EMA = np.nanmax(dataTime['EMA'][axis]['Pout'])
    Pout_Max_GBX = np.nanmax(dataTime['GBX'][axis]['Pout'])
    Pout_Max_WHE = np.nanmax(dataTime['WHE'][axis]['P'])

    # ------------------------------------------
    # Losses
    # ------------------------------------------
    # Avg
    Pv_Avg_HVS = np.nanmean(dataTime['HVS']['Pv'])
    Pv_Avg_INV = np.nanmean(dataTime['INV'][axis]['Pv'])
    Pv_Avg_EMA = np.nanmean(dataTime['EMA'][axis]['Pv'])
    Pv_Avg_GBX = np.nanmean(dataTime['GBX'][axis]['Pv'])
    Pv_Avg_WHE = 0

    # Std
    Pv_Std_HVS = np.nanstd(dataTime['HVS']['Pv'])
    Pv_Std_INV = np.nanstd(dataTime['INV'][axis]['Pv'])
    Pv_Std_EMA = np.nanstd(dataTime['EMA'][axis]['Pv'])
    Pv_Std_GBX = np.nanstd(dataTime['GBX'][axis]['Pv'])
    Pv_Std_WHE = 0

    # Max
    Pv_Max_HVS = np.nanmax(dataTime['HVS']['Pv'])
    Pv_Max_INV = np.nanmax(dataTime['INV'][axis]['Pv'])
    Pv_Max_EMA = np.nanmax(dataTime['EMA'][axis]['Pv'])
    Pv_Max_GBX = np.nanmax(dataTime['GBX'][axis]['Pv'])
    Pv_Max_WHE = 0

    # ------------------------------------------
    # Eta
    # ------------------------------------------
    # Avg
    Eta_Avg_HVS = np.nanmean(dataTime['HVS']['eta'])
    Eta_Avg_INV = np.nanmean(dataTime['INV'][axis]['eta'])
    Eta_Avg_EMA = np.nanmean(dataTime['EMA'][axis]['eta'])
    Eta_Avg_GBX = np.nanmean(dataTime['GBX'][axis]['eta'])
    Eta_Avg_WHE = 1

    # Std
    Eta_Std_HVS = np.nanstd(dataTime['HVS']['eta'])
    Eta_Std_INV = np.nanstd(dataTime['INV'][axis]['eta'])
    Eta_Std_EMA = np.nanstd(dataTime['EMA'][axis]['eta'])
    Eta_Std_GBX = np.nanstd(dataTime['GBX'][axis]['eta'])
    Eta_Std_WHE = 0

    # Max
    Eta_Max_HVS = np.nanmax(dataTime['HVS']['eta'])
    Eta_Max_INV = np.nanmax(dataTime['INV'][axis]['eta'])
    Eta_Max_EMA = np.nanmax(dataTime['EMA'][axis]['eta'])
    Eta_Max_GBX = np.nanmax(dataTime['GBX'][axis]['eta'])
    Eta_Max_WHE = 1

    # ------------------------------------------
    # Matrix
    # ------------------------------------------
    # Pin
    Pin_Avg = [Pin_Avg_HVS / 1000, Pin_Avg_INV / 1000, Pin_Avg_EMA / 1000, Pin_Avg_GBX / 1000, Pin_Avg_WHE / 1000]
    Pin_Std = [Pin_Std_HVS / 1000, Pin_Std_INV / 1000, Pin_Std_EMA / 1000, Pin_Std_GBX / 1000, Pin_Std_WHE / 1000]
    Pin_Max = [Pin_Max_HVS / 1000, Pin_Max_INV / 1000, Pin_Max_EMA / 1000, Pin_Max_GBX / 1000, Pin_Max_WHE / 1000]
    Pin = [Pin_Avg, Pin_Std, Pin_Max]

    # Pout
    Pout_Avg = [Pout_Avg_HVS / 1000, Pout_Avg_INV / 1000, Pout_Avg_EMA / 1000, Pout_Avg_GBX / 1000, Pout_Avg_WHE / 1000]
    Pout_Std = [Pout_Std_HVS / 1000, Pout_Std_INV / 1000, Pout_Std_EMA / 1000, Pout_Std_GBX / 1000, Pout_Std_WHE / 1000]
    Pout_Max = [Pout_Max_HVS / 1000, Pout_Max_INV / 1000, Pout_Max_EMA / 1000, Pout_Max_GBX / 1000, Pout_Max_WHE / 1000]
    Pout = [Pout_Avg, Pout_Std, Pout_Max]

    # Pv
    Pv_Avg = [Pv_Avg_HVS / 1000, Pv_Avg_INV / 1000, Pv_Avg_EMA / 1000, Pv_Avg_GBX / 1000, Pv_Avg_WHE / 1000]
    Pv_Std = [Pv_Std_HVS / 1000, Pv_Std_INV / 1000, Pv_Std_EMA / 1000, Pv_Std_GBX / 1000, Pv_Std_WHE / 1000]
    Pv_Max = [Pv_Max_HVS / 1000, Pv_Max_INV / 1000, Pv_Max_EMA / 1000, Pv_Max_GBX / 1000, Pv_Max_WHE / 1000]
    Pv = [Pv_Avg, Pv_Std, Pv_Max]

    # Eta
    Eta_Avg = [Eta_Avg_HVS * 100, Eta_Avg_INV * 100, Eta_Avg_EMA * 100, Eta_Avg_GBX * 100, Eta_Avg_WHE * 100]
    Eta_Std = [Eta_Std_HVS * 100, Eta_Std_INV * 100, Eta_Std_EMA * 100, Eta_Std_GBX * 100, Eta_Std_WHE * 100]
    Eta_Max = [Eta_Max_HVS * 100, Eta_Max_INV * 100, Eta_Max_EMA * 100, Eta_Max_GBX * 100, Eta_Max_WHE * 100]
    Eta = [Eta_Avg, Eta_Std, Eta_Max]

    ###################################################################################################################
    # Figure Creation
    ###################################################################################################################
    fig, axs = plt.subplots(4, 2, sharex=False)

    ###################################################################################################################
    # Calculation
    ###################################################################################################################
    # Add time series data for input power, output power, losses, and efficiency for each component
    for i, comp in enumerate(cat):
        if comp != 'HVS':
            # Add time series data for input power
            axs[0, 0].plot(time, dataTime[comp][axis]['Pin']/1000, label=f'{comp} Input Power')
            axs[0, 0].grid(True)
            # Add time series data for output power
            axs[1, 0].plot(time, dataTime[comp][axis]['Pout']/1000, label=f'{comp} Output Power')
            axs[1, 0].grid(True)
            # Add time series data for losses
            axs[2, 0].plot(time, dataTime[comp][axis]['Pv']/1000, label=f'{comp} Losses')
            axs[2, 0].grid(True)
            # Add time series data for efficiency
            axs[3, 0].plot(time, dataTime[comp][axis]['eta']*100, label=f'{comp} Efficiency')
            axs[3, 0].grid(True)
        else:
            # Add time series data for input power
            axs[0, 0].plot(time, dataTime[comp]['Pin']/1000, label=f'{comp} Input Power')
            axs[0, 0].grid(True)
            # Add time series data for output power
            axs[1, 0].plot(time, dataTime[comp]['Pout']/1000, label=f'{comp} Output Power')
            axs[1, 0].grid(True)
            # Add time series data for losses
            axs[2, 0].plot(time, dataTime[comp]['Pv']/1000, label=f'{comp} Losses')
            axs[2, 0].grid(True)
            # Add time series data for efficiency
            axs[3, 0].plot(time, dataTime[comp]['eta']*100, label=f'{comp} Efficiency')
            axs[3, 0].grid(True)

    ###################################################################################################################
    # Average Values
    ###################################################################################################################
    # Add bar plots for average input power, output power, losses, and efficiency for each component
    grouped_bar_plot(axs[0, 1], Pin, cat2, bar)
    grouped_bar_plot(axs[1, 1], Pout, cat2, bar)
    grouped_bar_plot(axs[2, 1], Pv, cat2, bar)
    grouped_bar_plot(axs[3, 1], Eta, cat2, bar)

    ###################################################################################################################
    # Post-Processing
    ###################################################################################################################
    # Legend
    axs[0, 0].legend()
    axs[1, 0].legend()
    axs[2, 0].legend()
    axs[3, 0].legend()

    # Set y-axis titles
    axs[0, 0].set_ylabel('Power Inp (kW)')
    axs[1, 0].set_ylabel('Power Out (kW)')
    axs[2, 0].set_ylabel('Losses (kW)')
    axs[3, 0].set_ylabel('Efficiency (%)')

    # Set x-axis titles
    axs[3, 0].set_xlabel('time (sec)')
    axs[3, 1].set_xlabel('Category')

    # Set overall title
    plt.suptitle('Comparing Input and Output Power', size=18)
    plt.subplots_adjust(hspace=0.35, wspace=0.35, left=0.075, right=0.925, top=0.90, bottom=0.075)

    ###################################################################################################################
    # Return
    ###################################################################################################################
    return []
