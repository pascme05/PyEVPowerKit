#######################################################################################################################
#######################################################################################################################
# Title:        Python Electric Vehicle Power Toolkit (PyEVPowerKit)
# Topic:        EV Modeling
# File:         template
# Date:         19.08.2023
# Author:       Dr. Pascal A. Schirmer
# Version:      V.0.1
# Copyright:    Pascal Schirmer
#######################################################################################################################
#######################################################################################################################

#######################################################################################################################
# Function Description
#######################################################################################################################
"""
This function loads the remaining setup parameters from the setup file located under \setup. This includes vehicle
(VEH), gearbox (GBX), machine (EMA), converter (INV), and battery (HVS) parameters. The parameters are summarized in one
common setup variable.
Inputs:     1) setup:   includes all simulation variables
            2) path:    includes all path variables
Outputs:    1) setup:   extended setup variable
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
import pandas as pd
from os.path import join as pjoin


#######################################################################################################################
# Function
#######################################################################################################################
def loadSetup(setup, path):
    ###################################################################################################################
    # MSG IN
    ###################################################################################################################
    print("------------------------------------------")
    print("Loading Setup")
    print("------------------------------------------")
    print("START: Loading setup")

    ###################################################################################################################
    # Initialisation
    ###################################################################################################################
    column = 'Value'

    ###################################################################################################################
    # Loading
    ###################################################################################################################
    # ==============================================================================
    # Path and Filename
    # ==============================================================================
    name = setup['Par']['name'] + '.xlsx'
    path = path['setPath']
    filename = pjoin(path, name)

    # ==============================================================================
    # Loading Config
    # ==============================================================================
    try:
        setupVehRaw = pd.read_excel(filename, sheet_name='VEH')
        setupGBXRaw = pd.read_excel(filename, sheet_name='GBX')
        setupEMARaw = pd.read_excel(filename, sheet_name='EMA')
        setupINVRaw = pd.read_excel(filename, sheet_name='INV')
        setupHVSRaw = pd.read_excel(filename, sheet_name='HVS')
        print("INFO: Setup file loaded")
    except:
        setupVehRaw = []
        setupGBXRaw = []
        setupEMARaw = []
        setupINVRaw = []
        setupHVSRaw = []
        print("ERROR: Setup file could not be loaded")

    ###################################################################################################################
    # Calculation
    ###################################################################################################################
    # ==============================================================================
    # Vehicle struct
    # ==============================================================================
    try:
        for i in range(0, setupVehRaw.shape[0]):
            setup['Par']['VEH'][setupVehRaw['Variable'][i]] = setupVehRaw[column][i]
        print("INFO: VEH setup file loaded")
    except:
        print("ERROR: VEH setup file could not be loaded")

    # ==============================================================================
    # GBX struct
    # ==============================================================================
    try:
        for i in range(0, setupGBXRaw.shape[0]):
            setup['Par']['GBX'][setupGBXRaw['Variable'][i]] = setupGBXRaw[column][i]
        print("INFO: GBX setup file loaded")
    except:
        print("ERROR: GBX setup file could not be loaded")

    # ==============================================================================
    # EMA struct
    # ==============================================================================
    try:
        for i in range(0, setupEMARaw.shape[0]):
            setup['Par']['EMA'][setupEMARaw['Variable'][i]] = setupEMARaw[column][i]
        print("INFO: EMA setup file loaded")
    except:
        print("ERROR: EMA setup file could not be loaded")

    # ==============================================================================
    # INV struct
    # ==============================================================================
    try:
        for i in range(0, setupINVRaw.shape[0]):
            setup['Par']['INV'][setupINVRaw['Variable'][i]] = setupINVRaw[column][i]
        print("INFO: INV setup file loaded")
    except:
        print("ERROR: INV setup file could not be loaded")

    # ==============================================================================
    # HVS struct
    # ==============================================================================
    try:
        for i in range(0, setupHVSRaw.shape[0]):
            setup['Par']['HVS'][setupHVSRaw['Variable'][i]] = setupHVSRaw[column][i]
        print("INFO: HVS setup file loaded")
    except:
        print("ERROR: HVS setup file could not be loaded")

    ###################################################################################################################
    # MSG Out
    ###################################################################################################################
    print("DONE: Loading setup")
    print("\n")

    return setup
