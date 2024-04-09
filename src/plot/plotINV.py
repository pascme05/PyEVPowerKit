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
import plotly.graph_objects as go
from plotly.subplots import make_subplots

#######################################################################################################################
# Additional Functions
#######################################################################################################################


#######################################################################################################################
# Main Function
#######################################################################################################################
def plotINV(data, dataTime, setup):
    ###################################################################################################################
    # MSG IN
    ###################################################################################################################
    print("INFO: Plotting INV data")

    ###################################################################################################################
    # Initialisation
    ###################################################################################################################
    time = data['t']
    axis = setup['Exp']['plotAxis']

    ###################################################################################################################
    # Pre-Processing
    ###################################################################################################################
    fig = make_subplots(rows=4, cols=3, shared_xaxes=True, vertical_spacing=0.05)

    ###################################################################################################################
    # Calculation
    ###################################################################################################################
    # ==============================================================================
    # Plotting
    # ==============================================================================
    # ------------------------------------------
    # Electrical
    # ------------------------------------------
    fig.add_trace(go.Scatter(x=time, y=dataTime['INV'][axis]['Mi'], mode='lines', line=dict(color='#636EFA', dash='solid'), name='Modulation Index'), row=1, col=1)
    fig.add_trace(go.Scatter(x=time, y=dataTime['INV'][axis]['Idc'], mode='lines', line=dict(color='#636EFA', dash='solid'), name='Input Current'), row=2, col=1)
    fig.add_trace(go.Scatter(x=time, y=dataTime['INV'][axis]['Ic'], mode='lines', line=dict(color='#636EFA', dash='solid'), name='DC Link Current'), row=3, col=1)
    fig.add_trace(go.Scatter(x=time, y=dataTime['INV'][axis]['Is'], mode='lines', line=dict(color='#636EFA', dash='solid'), name='Output Current'), row=4, col=1)

    # ------------------------------------------
    # Losses
    # ------------------------------------------
    fig.add_trace(go.Scatter(x=time, y=dataTime['INV'][axis]['Pv_sw'], mode='lines', line=dict(color='#EF553B', dash='solid'), name='Losses Power Module'), row=1, col=2)
    fig.add_trace(go.Scatter(x=time, y=dataTime['INV'][axis]['Pv_cap'], mode='lines', line=dict(color='#EF553B', dash='solid'), name='Losses DC-Link Cap'), row=2, col=2)
    fig.add_trace(go.Scatter(x=time, y=dataTime['INV'][axis]['Pv_ac'], mode='lines', line=dict(color='#EF553B', dash='solid'), name='Losses AC Busbars'), row=3, col=2)
    fig.add_trace(go.Scatter(x=time, y=dataTime['INV'][axis]['Pv_dc'], mode='lines', line=dict(color='#EF553B', dash='solid'), name='Losses DC Busbars'), row=4, col=2)

    # ------------------------------------------
    # Thermal
    # ------------------------------------------
    fig.add_trace(go.Scatter(x=time, y=dataTime['INV'][axis]['Pin'], mode='lines', line=dict(color='#00CC96', dash='solid'), name='Input Power'), row=1, col=3)
    fig.add_trace(go.Scatter(x=time, y=dataTime['INV'][axis]['Pout'], mode='lines', line=dict(color='#00CC96', dash='dash'), name='Output Power'), row=1, col=3)
    fig.add_trace(go.Scatter(x=time, y=dataTime['INV'][axis]['Pv'], mode='lines', line=dict(color='#00CC96', dash='solid'), name='Total Losses'), row=2, col=3)
    fig.add_trace(go.Scatter(x=time, y=dataTime['INV'][axis]['eta'], mode='lines', line=dict(color='#00CC96', dash='solid'), name='Total Efficiency'), row=3, col=3)
    fig.add_trace(go.Scatter(x=time, y=dataTime['INV'][axis]['T'], mode='lines', line=dict(color='#00CC96', dash='solid'), name='Temperature'), row=4, col=3)

    ###################################################################################################################
    # Post-Processing
    ###################################################################################################################
    # ==============================================================================
    # Axis
    # ==============================================================================
    # ------------------------------------------
    # Set y-axis titles
    # ------------------------------------------
    # Mechanics
    fig.update_yaxes(title_text="Mi (p.u.)", row=1, col=1)
    fig.update_yaxes(title_text="Idc RMS (A)", row=2, col=1)
    fig.update_yaxes(title_text="Ic RMS (A)", row=3, col=1)
    fig.update_yaxes(title_text="Iac RMS (A)", row=4, col=1)

    # Losses
    fig.update_yaxes(title_text="Pv_swi (W)", row=1, col=2)
    fig.update_yaxes(title_text="Pv_cap (W)", row=2, col=2)
    fig.update_yaxes(title_text="Pv_bac (W)", row=3, col=2)
    fig.update_yaxes(title_text="Pv_bdc (W)", row=4, col=2)

    # Thermal
    fig.update_yaxes(title_text="Pin (W)", row=1, col=3)
    fig.update_yaxes(title_text="Pv (W)", row=2, col=3)
    fig.update_yaxes(title_text="Eta (%)", row=3, col=3)
    fig.update_yaxes(title_text="T (degC)", row=4, col=3)

    # ------------------------------------------
    # Set x-axis title for the last subplot
    # ------------------------------------------
    fig.update_xaxes(title_text="time (sec)", row=4, col=1)
    fig.update_xaxes(title_text="time (sec)", row=4, col=2)
    fig.update_xaxes(title_text="time (sec)", row=4, col=3)

    # ==============================================================================
    # Title
    # ==============================================================================
    txt = "Converter Electrical, Losses, and Thermal (" + axis + ")"
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
