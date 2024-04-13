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
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

#######################################################################################################################
# Additional Functions
#######################################################################################################################


#######################################################################################################################
# Main Function
#######################################################################################################################
def plotMax(data, dataTime, setup):
    ###################################################################################################################
    # MSG IN
    ###################################################################################################################
    print("INFO: Plotting Maximum Loads")

    ###################################################################################################################
    # Initialisation
    ###################################################################################################################
    time = data['t']
    axis = setup['Exp']['plotAxis']
    cat = ['HVS', 'INV', 'EMA', 'GBX']
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']

    ###################################################################################################################
    # Pre-Processing
    ###################################################################################################################
    # ==============================================================================
    # Statistical Values
    # ==============================================================================
    # ------------------------------------------
    # Torque
    # ------------------------------------------
    M_Max_HVS = 0
    M_Max_INV = 0
    M_Max_EMA = np.nanmax(dataTime['EMA'][axis]['Min'])
    M_Max_GBX = np.nanmax(dataTime['GBX'][axis]['M'])

    # ------------------------------------------
    # Power
    # ------------------------------------------
    P_Max_HVS = np.nanmax(dataTime['HVS']['Pout'])
    P_Max_INV = np.nanmax(dataTime['INV'][axis]['Pout'])
    P_Max_EMA = np.nanmax(dataTime['EMA'][axis]['Pout'])
    P_Max_GBX = np.nanmax(dataTime['GBX'][axis]['Pout'])

    # ------------------------------------------
    # Current
    # ------------------------------------------
    I_Max_HVS = np.nanmax(dataTime['HVS']['Idc'])
    I_Max_INV = np.nanmax(dataTime['INV'][axis]['Idc'])
    I_Max_EMA = np.nanmax(dataTime['EMA'][axis]['Is'])
    I_Max_GBX = 0

    # ------------------------------------------
    # Voltage
    # ------------------------------------------
    V_Max_HVS = np.nanmax(dataTime['HVS']['Vdc'])
    V_Max_INV = np.nanmax(dataTime['INV'][axis]['Mi']*dataTime['HVS']['Vdc']/2)
    V_Max_EMA = np.nanmax(dataTime['EMA'][axis]['Vs'])
    V_Max_GBX = 0

    # ------------------------------------------
    # Temperature
    # ------------------------------------------
    T_Max_HVS = np.nanmax(dataTime['HVS']['T'])
    T_Max_INV = np.nanmax(dataTime['INV'][axis]['T'])
    T_Max_EMA = np.nanmax(dataTime['EMA'][axis]['T'])
    T_Max_GBX = np.nanmax(dataTime['GBX'][axis]['T'])

    # ------------------------------------------
    # Matrix
    # ------------------------------------------
    # Maximum
    M_Max = [M_Max_HVS, M_Max_INV, M_Max_EMA, M_Max_GBX]
    P_Max = [P_Max_HVS, P_Max_INV, P_Max_EMA, P_Max_GBX]
    I_Max = [I_Max_HVS, I_Max_INV, I_Max_EMA, I_Max_GBX]
    V_Max = [V_Max_HVS, V_Max_INV, V_Max_EMA, V_Max_GBX]
    T_Max = [T_Max_HVS, T_Max_INV, T_Max_EMA, T_Max_GBX]

    # Limit
    M_Lim = [0, 0, setup['Par']['EMA']['M_max'], setup['Par']['GBX']['M_max']]
    P_Lim = [setup['Par']['HVS']['P_max'], setup['Par']['INV']['P_max'], setup['Par']['EMA']['P_max'], setup['Par']['GBX']['P_max']]
    I_Lim = [setup['Par']['HVS']['I_max'], setup['Par']['INV']['I_max'] / np.sqrt(2), setup['Par']['EMA']['I_max'] / np.sqrt(2), 0]
    V_Lim = [setup['Par']['HVS']['V_max'], setup['Par']['HVS']['V_max'] / np.sqrt(3), setup['Par']['HVS']['V_max'] / np.sqrt(6), 0]
    T_Lim = [setup['Par']['HVS']['T_max'], setup['Par']['INV']['T_max'], setup['Par']['EMA']['T_max'], setup['Par']['GBX']['T_max']]

    # ==============================================================================
    # Figure
    # ==============================================================================
    fig = make_subplots(rows=5, cols=2, shared_xaxes=True, vertical_spacing=0.05)

    ###################################################################################################################
    # Calculation
    ###################################################################################################################
    # ==============================================================================
    # Time Series
    # ==============================================================================
    # ------------------------------------------
    # Torque
    # ------------------------------------------
    fig.add_trace(go.Scatter(x=time, y=dataTime['EMA'][axis]['Min'], mode='lines', name='EMA Inner Torque'), row=1, col=1)
    fig.add_trace(go.Scatter(x=time, y=dataTime['GBX'][axis]['M'], mode='lines', name='GBX Input Torque'), row=1, col=1)

    # ------------------------------------------
    # Power
    # ------------------------------------------
    fig.add_trace(go.Scatter(x=time, y=dataTime['HVS']['Pout'], mode='lines', name='HVS Output Power'), row=2, col=1)
    fig.add_trace(go.Scatter(x=time, y=dataTime['INV'][axis]['Pout'], mode='lines', name='INV Output Power'), row=2, col=1)
    fig.add_trace(go.Scatter(x=time, y=dataTime['EMA'][axis]['Pout'], mode='lines', name='EMA Output Power'), row=2, col=1)
    fig.add_trace(go.Scatter(x=time, y=dataTime['GBX'][axis]['Pout'], mode='lines', name='GBX Output Power'), row=2, col=1)

    # ------------------------------------------
    # Current
    # ------------------------------------------
    fig.add_trace(go.Scatter(x=time, y=dataTime['HVS']['Idc'], mode='lines', name='HVS Input Current'), row=3, col=1)
    fig.add_trace(go.Scatter(x=time, y=dataTime['INV'][axis]['Idc'], mode='lines', name='INV Input Current'), row=3, col=1)
    fig.add_trace(go.Scatter(x=time, y=dataTime['EMA'][axis]['Is'], mode='lines', name='EMA Stator Current'), row=3, col=1)

    # ------------------------------------------
    # Voltage
    # ------------------------------------------
    fig.add_trace(go.Scatter(x=time, y=dataTime['HVS']['Vdc'], mode='lines', name='HVS Voltage'), row=4, col=1)
    fig.add_trace(go.Scatter(x=time, y=dataTime['INV'][axis]['Mi']*dataTime['HVS']['Vdc']/2, mode='lines', name='INV Output Voltage'), row=4, col=1)
    fig.add_trace(go.Scatter(x=time, y=dataTime['EMA'][axis]['Vs'], mode='lines', name='EMA Phase Voltage'), row=4, col=1)

    # ------------------------------------------
    # Temperature
    # ------------------------------------------
    fig.add_trace(go.Scatter(x=time, y=dataTime['HVS']['T'], mode='lines', name='HVS Temperature'), row=5, col=1)
    fig.add_trace(go.Scatter(x=time, y=dataTime['INV'][axis]['T'], mode='lines', name='INV Temperature'), row=5, col=1)
    fig.add_trace(go.Scatter(x=time, y=dataTime['EMA'][axis]['T'], mode='lines', name='EMA Temperature'), row=5, col=1)
    fig.add_trace(go.Scatter(x=time, y=dataTime['GBX'][axis]['T'], mode='lines', name='GBX Temperature'), row=5, col=1)

    # ==============================================================================
    # Average Values
    # ==============================================================================
    # ------------------------------------------
    # Torque
    # ------------------------------------------
    fig.add_trace(go.Bar(
        x=cat,
        y=M_Max,
        name='M_Max',
        marker_color=colors[0],
    ), row=1, col=2)

    fig.add_trace(go.Bar(
        x=cat,
        y=M_Lim,
        name='M_Lim',
        marker_color=colors[1],
    ), row=1, col=2)

    # Update layout for the entire figure
    fig.update_layout(
        title='Maximum Values by Category',
        barmode='group'  # Change the bar mode to 'group'
    )

    # ------------------------------------------
    # Power
    # ------------------------------------------
    fig.add_trace(go.Bar(
        x=cat,
        y=P_Max,
        name='P_Max',
        marker_color=colors[0],
    ), row=2, col=2)

    fig.add_trace(go.Bar(
        x=cat,
        y=P_Lim,
        name='P_Lim',
        marker_color=colors[1],
    ), row=2, col=2)

    # Update layout for the entire figure
    fig.update_layout(
        title='Maximum Values by Category',
        barmode='group'  # Change the bar mode to 'group'
    )

    # ------------------------------------------
    # Current
    # ------------------------------------------
    fig.add_trace(go.Bar(
        x=cat,
        y=I_Max,
        name='I_Max',
        marker_color=colors[0],
    ), row=3, col=2)

    fig.add_trace(go.Bar(
        x=cat,
        y=I_Lim,
        name='I_Lim',
        marker_color=colors[1],
    ), row=3, col=2)

    # Update layout for the entire figure
    fig.update_layout(
        title='Maximum Values by Category',
        barmode='group'  # Change the bar mode to 'group'
    )

    # ------------------------------------------
    # Voltage
    # ------------------------------------------
    fig.add_trace(go.Bar(
        x=cat,
        y=V_Max,
        name='V_Max',
        marker_color=colors[0],
    ), row=4, col=2)

    fig.add_trace(go.Bar(
        x=cat,
        y=V_Lim,
        name='V_Lim',
        marker_color=colors[1],
    ), row=4, col=2)

    # Update layout for the entire figure
    fig.update_layout(
        title='Maximum Values by Category',
        barmode='group'  # Change the bar mode to 'group'
    )

    # ------------------------------------------
    # Temperature
    # ------------------------------------------
    fig.add_trace(go.Bar(
        x=cat,
        y=T_Max,
        name='T_Max',
        marker_color=colors[0],
    ), row=5, col=2)

    fig.add_trace(go.Bar(
        x=cat,
        y=T_Lim,
        name='T_Lim',
        marker_color=colors[1],
    ), row=5, col=2)

    # Update layout for the entire figure
    fig.update_layout(
        title='Maximum Values by Category',
        barmode='group'  # Change the bar mode to 'group'
    )

    ###################################################################################################################
    # Post-Processing
    ###################################################################################################################
    # ==============================================================================
    # Axis
    # ==============================================================================
    # ------------------------------------------
    # Set y-axis titles
    # ------------------------------------------
    # Front
    fig.update_yaxes(title_text="M (Nm)", row=1, col=1)
    fig.update_yaxes(title_text="P (W)", row=2, col=1)
    fig.update_yaxes(title_text="I (A)", row=3, col=1)
    fig.update_yaxes(title_text="V (V)", row=4, col=1)
    fig.update_yaxes(title_text="T (C)", row=5, col=1)

    # Rear
    fig.update_yaxes(title_text="M (Nm)", row=1, col=2)
    fig.update_yaxes(title_text="P (W)", row=2, col=2)
    fig.update_yaxes(title_text="I (A)", row=3, col=2)
    fig.update_yaxes(title_text="V (V)", row=4, col=2)
    fig.update_yaxes(title_text="T (C)", row=5, col=2)

    # ------------------------------------------
    # Set x-axis title for the last subplot
    # ------------------------------------------
    fig.update_xaxes(title_text="time (sec)", row=5, col=1)
    fig.update_xaxes(title_text="Category", row=5, col=2)

    # ==============================================================================
    # Title
    # ==============================================================================
    txt = "Comparing Maximum Component Loading"
    fig.update_layout(height=setup['Exp']['hFig'], width=setup['Exp']['wFig'], title_text=txt)

    # ==============================================================================
    # Plot
    # ==============================================================================
    fig.show()

    ###################################################################################################################
    # Return
    ###################################################################################################################
    return []

#######################################################################################################################
# References
#######################################################################################################################
