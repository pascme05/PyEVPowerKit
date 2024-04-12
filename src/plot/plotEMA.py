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
import plotly.graph_objects as go
from plotly.subplots import make_subplots

#######################################################################################################################
# Additional Functions
#######################################################################################################################


#######################################################################################################################
# Main Function
#######################################################################################################################
def plotEMA(data, dataTime, setup):
    ###################################################################################################################
    # MSG IN
    ###################################################################################################################
    print("INFO: Plotting EMA data")

    ###################################################################################################################
    # Initialisation
    ###################################################################################################################
    # ==============================================================================
    # Variables
    # ==============================================================================
    time = data['t']
    axis = setup['Exp']['plotAxis']

    ###################################################################################################################
    # Pre-Processing
    ###################################################################################################################
    fig = make_subplots(rows=3, cols=3, shared_xaxes=True, vertical_spacing=0.05)

    ###################################################################################################################
    # Calculation
    ###################################################################################################################
    # ==============================================================================
    # Plotting
    # ==============================================================================
    # ------------------------------------------
    # Mechanical
    # ------------------------------------------
    fig.add_trace(go.Scatter(x=time, y=dataTime['EMA'][axis]['M'], mode='lines', line=dict(color='#636EFA', dash='dash'), name='EMA Torque (tar)'), row=1, col=1)
    fig.add_trace(go.Scatter(x=time, y=dataTime['EMA'][axis]['Min'], mode='lines', line=dict(color='#636EFA', dash='solid'), name='EMA Torque (act)'), row=1, col=1)
    fig.add_trace(go.Scatter(x=time, y=dataTime['EMA'][axis]['n'], mode='lines', line=dict(color='#636EFA', dash='solid'), name='EMA Speed'), row=2, col=1)
    fig.add_trace(go.Scatter(x=time, y=dataTime['EMA'][axis]['Pm'], mode='lines', line=dict(color='#636EFA', dash='solid'), name='EMA Power'), row=3, col=1)

    # ------------------------------------------
    # Losses
    # ------------------------------------------
    fig.add_trace(go.Scatter(x=time, y=dataTime['EMA'][axis]['Is'], mode='lines', line=dict(color='#EF553B', dash='solid'), name='EMA Currents (Is)'), row=1, col=2)
    fig.add_trace(go.Scatter(x=time, y=dataTime['EMA'][axis]['Id'] / np.sqrt(2), mode='lines', line=dict(color='#EF553B', dash='dash'), name='EMA Currents (Id)'), row=1, col=2)
    fig.add_trace(go.Scatter(x=time, y=dataTime['EMA'][axis]['Iq'] / np.sqrt(2), mode='lines', line=dict(color='#EF553B', dash='dot'), name='EMA Currents (Iq)'), row=1, col=2)
    fig.add_trace(go.Scatter(x=time, y=dataTime['EMA'][axis]['Vs'], mode='lines', line=dict(color='#EF553B', dash='solid'), name='EMA Voltages (Vs)'), row=2, col=2)
    fig.add_trace(go.Scatter(x=time, y=dataTime['EMA'][axis]['Vd'] / np.sqrt(2), mode='lines', line=dict(color='#EF553B', dash='dash'), name='EMA Voltages (Vd)'), row=2, col=2)
    fig.add_trace(go.Scatter(x=time, y=dataTime['EMA'][axis]['Vq'] / np.sqrt(2), mode='lines', line=dict(color='#EF553B', dash='dot'), name='EMA Voltages (Vq)'), row=2, col=2)
    fig.add_trace(go.Scatter(x=time, y=dataTime['EMA'][axis]['lam'], mode='lines', line=dict(color='#EF553B', dash='solid'), name='EMA Fluxes'), row=3, col=2)

    # ------------------------------------------
    # Thermal
    # ------------------------------------------
    fig.add_trace(go.Scatter(x=time, y=dataTime['EMA'][axis]['Pv'], mode='lines', line=dict(color='#00CC96', dash='solid'), name='Total Losses'), row=1, col=3)
    fig.add_trace(go.Scatter(x=time, y=dataTime['EMA'][axis]['Pv_m'], mode='lines', line=dict(color='#00CC96', dash='dash'), name='Mech Losses'), row=1, col=3)
    fig.add_trace(go.Scatter(x=time, y=dataTime['EMA'][axis]['Pv_s'], mode='lines', line=dict(color='#00CC96', dash='dot'), name='Stator Losses'), row=1, col=3)
    fig.add_trace(go.Scatter(x=time, y=dataTime['EMA'][axis]['Pv_r'], mode='lines', line=dict(color='#00CC96', dash='dashdot'), name='Rotor Losses'), row=1, col=3)
    fig.add_trace(go.Scatter(x=time, y=dataTime['EMA'][axis]['eta'], mode='lines', line=dict(color='#00CC96', dash='solid'), name='Total Efficiency'), row=2, col=3)
    fig.add_trace(go.Scatter(x=time, y=dataTime['EMA'][axis]['T'], mode='lines', line=dict(color='#00CC96', dash='solid'), name='Hotspot Temperature'), row=3, col=3)
    fig.add_trace(go.Scatter(x=time, y=dataTime['VEH']['Tc'], mode='lines', line=dict(color='#00CC96', dash='dash'), name='Coolant Temperature'), row=3, col=3)

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
    fig.update_yaxes(title_text="M (Nm)", row=1, col=1)
    fig.update_yaxes(title_text="n (1/s)", row=2, col=1)
    fig.update_yaxes(title_text="P (W)", row=3, col=1)

    # Losses
    fig.update_yaxes(title_text="Is RMS (A)", row=1, col=2)
    fig.update_yaxes(title_text="Vs RMS (V)", row=2, col=2)
    fig.update_yaxes(title_text="Lam (Vs)", row=3, col=2)

    # Thermal
    fig.update_yaxes(title_text="Pv (W)", row=1, col=3)
    fig.update_yaxes(title_text="Eta (%)", row=2, col=3)
    fig.update_yaxes(title_text="T (degC)", row=3, col=3)

    # ------------------------------------------
    # Set x-axis title for the last subplot
    # ------------------------------------------
    fig.update_xaxes(title_text="time (sec)", row=4, col=1)
    fig.update_xaxes(title_text="time (sec)", row=4, col=2)
    fig.update_xaxes(title_text="time (sec)", row=4, col=3)

    # ==============================================================================
    # Title
    # ==============================================================================
    txt = "Machine Mechanics, Electrical, Losses, and Thermal (" + axis + ")"
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
