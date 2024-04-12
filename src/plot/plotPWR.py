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
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

#######################################################################################################################
# Additional Functions
#######################################################################################################################


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
    cat = ['HVS', 'INV', 'EMA', 'GBX', 'WHE']
    bar = ['Avg', 'Std', 'Max']

    ###################################################################################################################
    # Pre-Processing
    ###################################################################################################################
    # ==============================================================================
    # Differences
    # ==============================================================================
    Diff_HVS = dataTime['HVS']['Pv'] - (dataTime['HVS']['Pin'] - dataTime['HVS']['Pout'])
    Diff_INV = dataTime['INV'][axis]['Pv'] - (dataTime['INV'][axis]['Pin'] - dataTime['INV'][axis]['Pout'])
    Diff_EMA = dataTime['EMA'][axis]['Pv'] - (dataTime['EMA'][axis]['Pin'] - dataTime['EMA'][axis]['Pout'])
    Diff_GBX = dataTime['GBX'][axis]['Pv'] - (dataTime['GBX'][axis]['Pin'] - dataTime['GBX'][axis]['Pout'])
    Diff_WHE = (dataTime['WHE'][axis]['P'] - dataTime['WHE'][axis]['P'])

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
    # Error
    # ------------------------------------------
    '''
    # Avg
    Err_Avg_HVS = np.nanmean(dataTime['HVS']['eta'])
    Err_Avg_INV = np.nanmean(dataTime['INV'][axis]['eta'])
    Err_Avg_EMA = np.nanmean(dataTime['EMA'][axis]['eta'])
    Err_Avg_GBX = np.nanmean(dataTime['GBX'][axis]['eta'])
    Err_Avg_WHE = 0

    # Std
    Err_Std_HVS = np.nanstd(dataTime['HVS']['eta'])
    Err_Std_INV = np.nanstd(dataTime['INV'][axis]['eta'])
    Err_Std_EMA = np.nanstd(dataTime['EMA'][axis]['eta'])
    Err_Std_GBX = np.nanstd(dataTime['GBX'][axis]['eta'])
    Err_Std_WHE = 0

    # Max
    Err_Max_HVS = np.nanmax(dataTime['HVS']['Pv'])
    Err_Max_INV = np.nanmax(dataTime['INV'][axis]['Pv'])
    Err_Max_EMA = np.nanmax(dataTime['EMA'][axis]['Pv'])
    Err_Max_GBX = np.nanmax(dataTime['GBX'][axis]['Pv'])
    Err_Max_WHE = 0
    '''

    # ------------------------------------------
    # Matrix
    # ------------------------------------------
    # Pin
    Pin_Avg = [Pin_Avg_HVS, Pin_Avg_INV, Pin_Avg_EMA, Pin_Avg_GBX, Pin_Avg_WHE]
    Pin_Std = [Pin_Std_HVS, Pin_Std_INV, Pin_Std_EMA, Pin_Std_GBX, Pin_Std_WHE]
    Pin_Max = [Pin_Max_HVS, Pin_Max_INV, Pin_Max_EMA, Pin_Max_GBX, Pin_Max_WHE]
    Pin = [Pin_Avg, Pin_Std, Pin_Max]

    # Pout
    Pout_Avg = [Pout_Avg_HVS, Pout_Avg_INV, Pout_Avg_EMA, Pout_Avg_GBX, Pout_Avg_WHE]
    Pout_Std = [Pout_Std_HVS, Pout_Std_INV, Pout_Std_EMA, Pout_Std_GBX, Pout_Std_WHE]
    Pout_Max = [Pout_Max_HVS, Pout_Max_INV, Pout_Max_EMA, Pout_Max_GBX, Pout_Max_WHE]
    Pout = [Pout_Avg, Pout_Std, Pout_Max]

    # Pv
    Pv_Avg = [Pv_Avg_HVS, Pv_Avg_INV, Pv_Avg_EMA, Pv_Avg_GBX, Pv_Avg_WHE]
    Pv_Std = [Pv_Std_HVS, Pv_Std_INV, Pv_Std_EMA, Pv_Std_GBX, Pv_Std_WHE]
    Pv_Max = [Pv_Max_HVS, Pv_Max_INV, Pv_Max_EMA, Pv_Max_GBX, Pv_Max_WHE]
    Pv = [Pv_Avg, Pv_Std, Pv_Max]

    # Eta
    Eta_Avg = [Eta_Avg_HVS, Eta_Avg_INV, Eta_Avg_EMA, Eta_Avg_GBX, Eta_Avg_WHE]
    Eta_Std = [Eta_Std_HVS, Eta_Std_INV, Eta_Std_EMA, Eta_Std_GBX, Eta_Std_WHE]
    Eta_Max = [Eta_Max_HVS, Eta_Max_INV, Eta_Max_EMA, Eta_Max_GBX, Eta_Max_WHE]
    Eta = [Eta_Avg, Eta_Std, Eta_Max]

    # ==============================================================================
    # Figure
    # ==============================================================================
    fig = make_subplots(rows=4, cols=2, shared_xaxes=True, vertical_spacing=0.05)

    ###################################################################################################################
    # Calculation
    ###################################################################################################################
    # ==============================================================================
    # Time Series
    # ==============================================================================
    # ------------------------------------------
    # Power Input
    # ------------------------------------------
    fig.add_trace(go.Scatter(x=time, y=dataTime['HVS']['Pin'], mode='lines', name='HVS Input Power'), row=1, col=1)
    fig.add_trace(go.Scatter(x=time, y=dataTime['INV'][axis]['Pin'], mode='lines', name='INV Input Power'), row=1, col=1)
    fig.add_trace(go.Scatter(x=time, y=dataTime['EMA'][axis]['Pin'], mode='lines', name='EMA Input Power'), row=1, col=1)
    fig.add_trace(go.Scatter(x=time, y=dataTime['GBX'][axis]['Pin'], mode='lines', name='GBX Input Power'), row=1, col=1)
    fig.add_trace(go.Scatter(x=time, y=dataTime['WHE'][axis]['P'], mode='lines', name='WEH Input Power'), row=1, col=1)

    # ------------------------------------------
    # Power Output
    # ------------------------------------------
    fig.add_trace(go.Scatter(x=time, y=dataTime['HVS']['Pout'], mode='lines', name='HVS Output Power'), row=2, col=1)
    fig.add_trace(go.Scatter(x=time, y=dataTime['INV'][axis]['Pout'], mode='lines', name='INV Output Power'), row=2, col=1)
    fig.add_trace(go.Scatter(x=time, y=dataTime['EMA'][axis]['Pout'], mode='lines', name='EMA Output Power'), row=2, col=1)
    fig.add_trace(go.Scatter(x=time, y=dataTime['GBX'][axis]['Pout'], mode='lines', name='GBX Output Power'), row=2, col=1)
    fig.add_trace(go.Scatter(x=time, y=dataTime['WHE'][axis]['P'], mode='lines', name='WEH Output Power'), row=2, col=1)

    # ------------------------------------------
    # Losses
    # ------------------------------------------
    fig.add_trace(go.Scatter(x=time, y=dataTime['HVS']['Pv'], mode='lines', name='HVS Losses'), row=3, col=1)
    fig.add_trace(go.Scatter(x=time, y=dataTime['INV'][axis]['Pv'], mode='lines', name='INV Losses'), row=3, col=1)
    fig.add_trace(go.Scatter(x=time, y=dataTime['EMA'][axis]['Pv'], mode='lines', name='EMA Losses'), row=3, col=1)
    fig.add_trace(go.Scatter(x=time, y=dataTime['GBX'][axis]['Pv'], mode='lines', name='GBX Losses'), row=3, col=1)
    fig.add_trace(go.Scatter(x=time, y=dataTime['WHE'][axis]['P']*0, mode='lines', name='WEH Losses'), row=3, col=1)

    # ------------------------------------------
    # Eta
    # ------------------------------------------
    fig.add_trace(go.Scatter(x=time, y=dataTime['HVS']['eta'], mode='lines', name='HVS Eff'), row=4, col=1)
    fig.add_trace(go.Scatter(x=time, y=dataTime['INV'][axis]['eta'], mode='lines', name='INV Eff'), row=4, col=1)
    fig.add_trace(go.Scatter(x=time, y=dataTime['EMA'][axis]['eta'], mode='lines', name='EMA Eff'), row=4, col=1)
    fig.add_trace(go.Scatter(x=time, y=dataTime['GBX'][axis]['eta'], mode='lines', name='GBX Eff'), row=4, col=1)
    fig.add_trace(go.Scatter(x=time, y=dataTime['WHE'][axis]['P'] * 0 + 1, mode='lines', name='WEH Eff'), row=4, col=1)

    # ------------------------------------------
    # Error
    # ------------------------------------------
    '''
    fig.add_trace(go.Scatter(x=time, y=Diff_HVS, mode='lines', name='HVS Error'), row=5, col=1)
    fig.add_trace(go.Scatter(x=time, y=Diff_INV, mode='lines', name='INV Error'), row=5, col=1)
    fig.add_trace(go.Scatter(x=time, y=Diff_EMA, mode='lines', name='EMA Error'), row=5, col=1)
    fig.add_trace(go.Scatter(x=time, y=Diff_GBX, mode='lines', name='GBX Error'), row=5, col=1)
    fig.add_trace(go.Scatter(x=time, y=Diff_WHE, mode='lines', name='WEH Error'), row=5, col=1)
    '''

    # ==============================================================================
    # Average Values
    # ==============================================================================
    # ------------------------------------------
    # Pin
    # ------------------------------------------
    # Create Data
    traces = []
    for i, bar_name in enumerate(bar):
        trace = go.Bar(
            x=[category for category in cat],
            y=[Pin[i][j] for j in range(len(cat))],
            name=bar_name
        )
        traces.append(trace)

    # Add Traces
    for trace in traces:
        fig.add_trace(trace, row=1, col=2)

    # ------------------------------------------
    # Pout
    # ------------------------------------------
    # Create Data
    traces = []
    for i, bar_name in enumerate(bar):
        trace = go.Bar(
            x=[category for category in cat],
            y=[Pout[i][j] for j in range(len(cat))],
            name=bar_name
        )
        traces.append(trace)

    # Add Traces
    for trace in traces:
        fig.add_trace(trace, row=2, col=2)

    # ------------------------------------------
    # Pv
    # ------------------------------------------
    # Create Data
    traces = []
    for i, bar_name in enumerate(bar):
        trace = go.Bar(
            x=[category for category in cat],
            y=[Pv[i][j] for j in range(len(cat))],
            name=bar_name
        )
        traces.append(trace)

    # Add Traces
    for trace in traces:
        fig.add_trace(trace, row=3, col=2)

    # ------------------------------------------
    # Eta
    # ------------------------------------------
    # Create Data
    traces = []
    for i, bar_name in enumerate(bar):
        trace = go.Bar(
            x=[category for category in cat],
            y=[Eta[i][j] for j in range(len(cat))],
            name=bar_name
        )
        traces.append(trace)

    # Add Traces
    for trace in traces:
        fig.add_trace(trace, row=4, col=2)

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
    fig.update_yaxes(title_text="Pi (W)", row=1, col=1)
    fig.update_yaxes(title_text="Po (W)", row=2, col=1)
    fig.update_yaxes(title_text="Pv (W)", row=3, col=1)
    fig.update_yaxes(title_text="Eta (%)", row=4, col=1)
    # fig.update_yaxes(title_text="Er (W)", row=5, col=1)

    # Rear
    fig.update_yaxes(title_text="Pi (W)", row=1, col=2)
    fig.update_yaxes(title_text="Po (W)", row=2, col=2)
    fig.update_yaxes(title_text="Pv (W)", row=3, col=2)
    fig.update_yaxes(title_text="Eta (%)", row=4, col=2)
    # fig.update_yaxes(title_text="Er (W)", row=5, col=2)

    # ------------------------------------------
    # Set x-axis title for the last subplot
    # ------------------------------------------
    fig.update_xaxes(title_text="time (sec)", row=4, col=1)
    fig.update_xaxes(title_text="Category", row=4, col=2)

    # ==============================================================================
    # Title
    # ==============================================================================
    txt = "Comparing Input and Output Power"
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
