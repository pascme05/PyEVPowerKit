#######################################################################################################################
#######################################################################################################################
# Title:        Python Electric Vehicle Power Toolkit (PyEVPowerKit)
# Topic:        EV Modeling
# File:         mechVeh
# Date:         18.03.2024
# Author:       Dr. Pascal A. Schirmer
# Version:      V.0.1
# Copyright:    Pascal Schirmer
#######################################################################################################################
#######################################################################################################################

#######################################################################################################################
# Import libs
#######################################################################################################################
# ==============================================================================
# Internal
# ==============================================================================

# ==============================================================================
# External
# ==============================================================================
import numpy as np
from scipy import integrate


#######################################################################################################################
# Function
#######################################################################################################################
def mechVeh(data, dataTime, setup):
    ###################################################################################################################
    # MSG IN
    ###################################################################################################################
    print("INFO: Calculating Vehicle Forces, Power, and Energy")

    ###################################################################################################################
    # Initialisation
    ###################################################################################################################
    # ==============================================================================
    # Parameters
    # ==============================================================================
    # ------------------------------------------
    # General
    # ------------------------------------------
    N = len(data['t'])

    # ------------------------------------------
    # Physical
    # ------------------------------------------
    g = 9.81

    # ------------------------------------------
    # Vehicle
    # ------------------------------------------
    p_a = setup['Par']['p_a']
    v_w = setup['Par']['v_w']
    A = setup['Par']['VEH']['A']
    c_w = setup['Par']['VEH']['c_w']
    m = setup['Par']['VEH']['m']
    c_r = setup['Par']['VEH']['c_r']
    m_a = setup['Par']['VEH']['m_a']
    eta_sys = setup['Par']['VEH']['eta']

    # ==============================================================================
    # Variables
    # ==============================================================================
    t = data['t'].values
    v = data['v'].values
    a = data['a'].values
    s = data['s'].values
    ang = data['ang'].values

    # ==============================================================================
    # Init
    # ==============================================================================
    state = np.zeros(N)
    rec_on = np.zeros(N)
    rec_off = np.zeros(N)
    out = {'F': {}, 'P': {}, 'E': {}, 'eta': {}}

    ###################################################################################################################
    # Pre-Processing
    ###################################################################################################################
    state[v > 0] = 1

    ###################################################################################################################
    # Calculation
    ###################################################################################################################
    # ==============================================================================
    # Forces
    # ==============================================================================
    dataTime['VEH']['F']['p'] = 0.5 * p_a * A * c_w * (v_w-v)**2
    dataTime['VEH']['F']['r'] = c_r * m * g * np.cos(ang) * state
    dataTime['VEH']['F']['c'] = m * g * np.sin(ang)
    dataTime['VEH']['F']['a'] = (m + m_a) * a
    dataTime['VEH']['F']['t'] = dataTime['VEH']['F']['p'] + dataTime['VEH']['F']['r'] + dataTime['VEH']['F']['c'] + dataTime['VEH']['F']['a']

    # ==============================================================================
    # Power
    # ==============================================================================
    # ------------------------------------------
    # Ideal
    # ------------------------------------------
    for name in dataTime['VEH']['F'].keys():
        dataTime['VEH']['P'][name] = dataTime['VEH']['F'][name] * v

    # ------------------------------------------
    # Efficiency
    # ------------------------------------------
    # Without Recu
    rec_off[dataTime['VEH']['P']['t'] < 0] = 0
    rec_off[dataTime['VEH']['P']['t'] >= 0] = 1 / eta_sys
    dataTime['VEH']['P']['rec_off'] = dataTime['VEH']['P']['t'] * rec_off

    # With Recu
    rec_on[dataTime['VEH']['P']['t'] < 0] = eta_sys
    rec_on[dataTime['VEH']['P']['t'] >= 0] = 1 / eta_sys
    dataTime['VEH']['P']['rec_on'] = dataTime['VEH']['P']['t'] * rec_on

    # ==============================================================================
    # Energy
    # ==============================================================================
    # ------------------------------------------
    # Ideal
    # ------------------------------------------
    for name in dataTime['VEH']['F'].keys():
        dataTime['VEH']['E'][name] = integrate.cumtrapz(dataTime['VEH']['P'][name], t, initial=0)

    # ------------------------------------------
    # Efficiency
    # ------------------------------------------
    # Without Recu
    dataTime['VEH']['E']['rec_off'] = integrate.cumtrapz(dataTime['VEH']['P']['rec_off'], t, initial=0)

    # With Recu
    dataTime['VEH']['E']['rec_on'] = integrate.cumtrapz(dataTime['VEH']['P']['rec_on'], t, initial=0)

    ###################################################################################################################
    # Post-Processing
    ###################################################################################################################
    dataTime['VEH']['eta']['t'] = dataTime['VEH']['E']['t'] / 3.6e6 / (s + 1e-12) * 1e5
    dataTime['VEH']['eta']['rec_on'] = dataTime['VEH']['E']['rec_on'] / 3.6e6 / (s + 1e-12) * 1e5
    dataTime['VEH']['eta']['rec_off'] = dataTime['VEH']['E']['rec_off'] / 3.6e6 / (s + 1e-12) * 1e5

    return dataTime
