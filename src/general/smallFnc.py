#######################################################################################################################
#######################################################################################################################
# Title:        Python Electric Vehicle Power Toolkit (PyEVPowerKit)
# Topic:        EV Modeling
# File:         smallFnc
# Date:         18.03.2024
# Author:       Dr. Pascal A. Schirmer
# Version:      V.0.1
# Copyright:    Pascal Schirmer
#######################################################################################################################
#######################################################################################################################

#######################################################################################################################
# Function Description
#######################################################################################################################
"""
This function summarizes a set of small functions that can be used for different purposes.
Inputs:     none
Outputs:    none
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
from os.path import dirname, join as pjoin
import os
import numpy as np
import copy


#######################################################################################################################
# Init Path
#######################################################################################################################
def initPath(nameFolder):
    basePath = pjoin(dirname(os.getcwd()), nameFolder)
    datPath = pjoin(dirname(os.getcwd()), nameFolder, 'data')
    srcPath = pjoin(dirname(os.getcwd()), nameFolder, 'src')
    resPath = pjoin(dirname(os.getcwd()), nameFolder, 'results')
    setPath = pjoin(dirname(os.getcwd()), nameFolder, 'setup')
    setupPath = {'basePath': basePath,  'datPath': datPath, 'srcPath': srcPath, 'setPath': setPath, 'resPath': resPath}

    return setupPath


#######################################################################################################################
# Init Setup files
#######################################################################################################################
def initSetup():
    setup = {'Exp': {}, 'Dat': {}, 'Par': {'VEH': {}, 'GBX': {}, 'EMA': {}, 'INV': {}, 'HVS': {}}}

    return setup


#######################################################################################################################
# Init Setup files
#######################################################################################################################
def getCycles(data, setup):
    print("INFO: Calculating number of cycles")

    dt = data['t'].values[1] - data['t'].values[0]
    T = data['t'].values[-1]
    s = data['s'].values[-1]
    v = copy.deepcopy(data['v'].values)
    v[v != 0] = 1
    T_drive = np.sum(v) * dt

    N1 = setup['Exp']['on'] * 3600 / T_drive
    N2 = setup['Exp']['km'] * 1000 / s
    N3 = setup['Exp']['life'] * 3600 / T

    setup['Exp']['cyc'] = int(min((N1, N2, N3)))

    print("DONE: Number of cycles is equal to: ", setup['Exp']['cyc'])

    return setup


#######################################################################################################################
# Init Output Variables
#######################################################################################################################
def initOutVar(N, Tinit):
    dataTime = {'VEH': {'Vdc': np.zeros(N), 'Tc': np.zeros(N), 'SOC': np.zeros(N), 'dQ': np.zeros(N),
                        'F': {}, 'P': {}, 'E': {}, 'eta': {}, 'a': np.zeros(N), 'v': np.zeros(N), 's': np.zeros(N)},
                'WHE': {'F': {}, 'R': {}},
                'GBX': {'F': {'T': Tinit * np.ones(N), 'M': np.zeros(N), 'n': np.zeros(N), 'Pin': np.zeros(N),
                              'Pout': np.zeros(N), 'Pv': np.zeros(N), 'Pv_B': np.zeros(N), 'Pv_M': np.zeros(N),
                              'Pv_W': np.zeros(N), 'eta': np.zeros(N)},
                        'R': {'T': Tinit * np.ones(N), 'M': np.zeros(N), 'n': np.zeros(N), 'Pin': np.zeros(N),
                              'Pout': np.zeros(N), 'Pv': np.zeros(N), 'Pv_B': np.zeros(N), 'Pv_M': np.zeros(N),
                              'Pv_W': np.zeros(N), 'eta': np.zeros(N)},
                        'T': {'T': Tinit * np.ones(N), 'M': np.zeros(N), 'n': np.zeros(N), 'Pin': np.zeros(N),
                              'Pout': np.zeros(N), 'Pv': np.zeros(N), 'Pv_B': np.zeros(N), 'Pv_M': np.zeros(N),
                              'Pv_W': np.zeros(N), 'eta': np.zeros(N)}},
                'EMA': {'F': {'T': Tinit * np.ones(N), 'M': np.zeros(N), 'n': np.zeros(N), 'Pm': np.zeros(N),
                              'Pin': np.zeros(N), 'Pout': np.zeros(N), 'Pv': np.zeros(N), 'Pv_m': np.zeros(N),
                              'Pv_s': np.zeros(N), 'Pv_r': np.zeros(N), 'eta': np.zeros(N), 'PF': np.zeros(N),
                              'Id': np.zeros(N), 'Iq': np.zeros(N), 'Is': np.zeros(N), 'Vd': np.zeros(N),
                              'Vq': np.zeros(N), 'Vs': np.zeros(N), 'lam': np.zeros(N), 'Min': np.zeros(N),
                              'Msh': np.zeros(N)},
                        'R': {'T': Tinit * np.ones(N), 'M': np.zeros(N), 'n': np.zeros(N), 'Pm': np.zeros(N),
                              'Pin': np.zeros(N), 'Pout': np.zeros(N), 'Pv': np.zeros(N), 'Pv_m': np.zeros(N),
                              'Pv_s': np.zeros(N), 'Pv_r': np.zeros(N), 'eta': np.zeros(N), 'PF': np.zeros(N),
                              'Id': np.zeros(N), 'Iq': np.zeros(N), 'Is': np.zeros(N), 'Vd': np.zeros(N),
                              'Vq': np.zeros(N), 'Vs': np.zeros(N), 'lam': np.zeros(N), 'Min': np.zeros(N),
                              'Msh': np.zeros(N)},
                        'T': {'T': Tinit * np.ones(N), 'M': np.zeros(N), 'n': np.zeros(N), 'Pm': np.zeros(N),
                              'Pin': np.zeros(N), 'Pout': np.zeros(N), 'Pv': np.zeros(N), 'Pv_m': np.zeros(N),
                              'Pv_s': np.zeros(N), 'Pv_r': np.zeros(N), 'eta': np.zeros(N), 'PF': np.zeros(N),
                              'Id': np.zeros(N), 'Iq': np.zeros(N), 'Is': np.zeros(N), 'Vd': np.zeros(N),
                              'Vq': np.zeros(N), 'Vs': np.zeros(N), 'lam': np.zeros(N), 'Min': np.zeros(N),
                              'Msh': np.zeros(N)}},
                'INV': {'F': {'T': Tinit * np.ones(N), 'Pin': np.zeros(N), 'Pout': np.zeros(N), 'Pv': np.zeros(N),
                              'Pv_sw': np.zeros(N), 'Pv_cap': np.zeros(N), 'Pv_ac': np.zeros(N), 'Pv_dc': np.zeros(N),
                              'eta': np.zeros(N), 'Idc': np.zeros(N), 'Ic': np.zeros(N), 'Is': np.zeros(N),
                              'Mi': np.zeros(N)},
                        'R': {'T': Tinit * np.ones(N), 'Pin': np.zeros(N), 'Pout': np.zeros(N), 'Pv': np.zeros(N),
                              'Pv_sw': np.zeros(N), 'Pv_cap': np.zeros(N), 'Pv_ac': np.zeros(N), 'Pv_dc': np.zeros(N),
                              'eta': np.zeros(N), 'Idc': np.zeros(N), 'Ic': np.zeros(N), 'Is': np.zeros(N),
                              'Mi': np.zeros(N)},
                        'T': {'T': Tinit * np.ones(N), 'Pin': np.zeros(N), 'Pout': np.zeros(N), 'Pv': np.zeros(N),
                              'Pv_sw': np.zeros(N), 'Pv_cap': np.zeros(N), 'Pv_ac': np.zeros(N), 'Pv_dc': np.zeros(N),
                              'eta': np.zeros(N), 'Idc': np.zeros(N), 'Ic': np.zeros(N), 'Is': np.zeros(N),
                              'Mi': np.zeros(N)}},
                'HVS': {'T': Tinit * np.ones(N), 'dQ': np.zeros(N), 'SOC': np.zeros(N), 'Vdc': np.zeros(N),
                        'Pin': np.zeros(N), 'Pout': np.zeros(N), 'Pv': np.zeros(N), 'eta': np.zeros(N),
                        'Idc': np.zeros(N)}}

    return dataTime
