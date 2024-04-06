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
import plotly.graph_objects as go
from plotly.subplots import make_subplots

#######################################################################################################################
# Additional Functions
#######################################################################################################################


#######################################################################################################################
# Main Function
#######################################################################################################################
def plotVehDetail(data, dataTime, setup):
    ###################################################################################################################
    # MSG IN
    ###################################################################################################################
    print("INFO: Plotting vehicle data (detail)")

    ###################################################################################################################
    # Initialisation
    ###################################################################################################################
    # ==============================================================================
    # Parameters
    # ==============================================================================
    Ts = 1 / setup['Dat']['fs']
    name = setup['Dat']['name']

    # ==============================================================================
    # Variables
    # ==============================================================================
    time = data['t']

    ###################################################################################################################
    # Loading Data
    ###################################################################################################################
    
    ###################################################################################################################
    # Pre-Processing
    ###################################################################################################################
    fig = make_subplots(rows=5, cols=3, shared_xaxes=True, vertical_spacing=0.05)

    ###################################################################################################################
    # Calculation
    ###################################################################################################################
    # ==============================================================================
    # Forces
    # ==============================================================================
    fig.add_trace(go.Scatter(x=time, y=dataTime['VEH']['F']['p'] / 1000, mode='lines', line=dict(color='#636EFA', dash='solid'), name='Vehicle Forces (Air)'), row=1, col=1)
    fig.add_trace(go.Scatter(x=time, y=dataTime['VEH']['F']['r'] / 1000, mode='lines', line=dict(color='#EF553B', dash='solid'), name='Vehicle Forces (Rolling)'), row=2, col=1)
    fig.add_trace(go.Scatter(x=time, y=dataTime['VEH']['F']['c'] / 1000, mode='lines', line=dict(color='#00CC96', dash='solid'), name='Vehicle Forces (Climbing)'), row=3, col=1)
    fig.add_trace(go.Scatter(x=time, y=dataTime['VEH']['F']['a'] / 1000, mode='lines', line=dict(color='#AB63FA', dash='solid'), name='Vehicle Forces (Acceleration)'), row=4, col=1)
    fig.add_trace(go.Scatter(x=time, y=dataTime['VEH']['F']['t'] / 1000, mode='lines', line=dict(color='#FFA15A', dash='solid'), name='Vehicle Forces (Total)'), row=5, col=1)

    # ==============================================================================
    # Power
    # ==============================================================================
    fig.add_trace(go.Scatter(x=time, y=dataTime['VEH']['P']['p'] / 1000, mode='lines', line=dict(color='#636EFA', dash='dash'), name='Vehicle Power (Air)'), row=1, col=2)
    fig.add_trace(go.Scatter(x=time, y=dataTime['VEH']['P']['r'] / 1000, mode='lines', line=dict(color='#EF553B', dash='dash'), name='Vehicle Power (Rolling)'), row=2, col=2)
    fig.add_trace(go.Scatter(x=time, y=dataTime['VEH']['P']['c'] / 1000, mode='lines', line=dict(color='#00CC96', dash='dash'), name='Vehicle Power (Climbing)'), row=3, col=2)
    fig.add_trace(go.Scatter(x=time, y=dataTime['VEH']['P']['a'] / 1000, mode='lines', line=dict(color='#AB63FA', dash='dash'), name='Vehicle Power (Acceleration)'), row=4, col=2)
    fig.add_trace(go.Scatter(x=time, y=dataTime['VEH']['P']['t'] / 1000, mode='lines', line=dict(color='#FFA15A', dash='dash'), name='Vehicle Power (Total)'), row=5, col=2)

    # ==============================================================================
    # Energy
    # ==============================================================================
    fig.add_trace(go.Scatter(x=time, y=dataTime['VEH']['E']['p'] / 3.6e6, mode='lines', line=dict(color='#636EFA', dash='dot'), name='Vehicle Energy (Air)'), row=1, col=3)
    fig.add_trace(go.Scatter(x=time, y=dataTime['VEH']['E']['r'] / 3.6e6, mode='lines', line=dict(color='#EF553B', dash='dot'), name='Vehicle Energy (Rolling)'), row=2, col=3)
    fig.add_trace(go.Scatter(x=time, y=dataTime['VEH']['E']['c'] / 3.6e6, mode='lines', line=dict(color='#00CC96', dash='dot'), name='Vehicle Energy (Climbing)'), row=3, col=3)
    fig.add_trace(go.Scatter(x=time, y=dataTime['VEH']['E']['a'] / 3.6e6, mode='lines', line=dict(color='#AB63FA', dash='dot'), name='Vehicle Energy (Acceleration)'), row=4, col=3)
    fig.add_trace(go.Scatter(x=time, y=dataTime['VEH']['E']['t'] / 3.6e6, mode='lines', line=dict(color='#FFA15A', dash='dot'), name='Vehicle Energy (Total)'), row=5, col=3)

    ###################################################################################################################
    # Post-Processing
    ###################################################################################################################
    # ==============================================================================
    # Axis
    # ==============================================================================
    # ------------------------------------------
    # Set y-axis titles
    # ------------------------------------------
    # Forces
    fig.update_yaxes(title_text="F (kN)", row=1, col=1)
    fig.update_yaxes(title_text="F (kN)", row=2, col=1)
    fig.update_yaxes(title_text="F (kN)", row=3, col=1)
    fig.update_yaxes(title_text="F (kN)", row=4, col=1)
    fig.update_yaxes(title_text="F (kN)", row=5, col=1)

    # Power
    fig.update_yaxes(title_text="P (kW)", row=1, col=2)
    fig.update_yaxes(title_text="P (kW)", row=2, col=2)
    fig.update_yaxes(title_text="P (kW)", row=3, col=2)
    fig.update_yaxes(title_text="P (kW)", row=4, col=2)
    fig.update_yaxes(title_text="P (kW)", row=5, col=2)

    # Energy
    fig.update_yaxes(title_text="E (kWh)", row=1, col=3)
    fig.update_yaxes(title_text="E (kWh)", row=2, col=3)
    fig.update_yaxes(title_text="E (kWh)", row=3, col=3)
    fig.update_yaxes(title_text="E (kWh)", row=4, col=3)
    fig.update_yaxes(title_text="E (kWh)", row=5, col=3)

    # ------------------------------------------
    # Set x-axis title for the last subplot
    # ------------------------------------------
    fig.update_xaxes(title_text="time (sec)", row=5, col=1)
    fig.update_xaxes(title_text="time (sec)", row=5, col=2)
    fig.update_xaxes(title_text="time (sec)", row=5, col=3)

    # ==============================================================================
    # Title
    # ==============================================================================
    txt = "Vehicle Forces, Power, Energies, and Efficiencies (Detail): "
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
