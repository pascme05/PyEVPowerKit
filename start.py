#######################################################################################################################
#######################################################################################################################
# Title:        Python Electric Vehicle Power Toolkit (PyEVPowerKit)
# Topic:        EV Modeling
# File:         start
# Date:         18.03.2024
# Author:       Dr. Pascal A. Schirmer
# Version:      V.0.1
# Copyright:    Pascal Schirmer
#######################################################################################################################
#######################################################################################################################

#######################################################################################################################
# Import external libs
#######################################################################################################################
# ==============================================================================
# Internal
# ==============================================================================
from src.general.smallFnc import initPath, initSetup
from src.main import main

# ==============================================================================
# External
# ==============================================================================
import warnings

#######################################################################################################################
# Format
#######################################################################################################################
warnings.filterwarnings("ignore")

#######################################################################################################################
# Init
#######################################################################################################################
# ==============================================================================
# Path
# ==============================================================================
setupPath = initPath('PyEVPowerKit')

# ==============================================================================
# Setup
# ==============================================================================
setup = initSetup()

#######################################################################################################################
# Setup and Configuration
#######################################################################################################################
# ==============================================================================
# Experiment
# ==============================================================================
# ------------------------------------------
# Files
# ------------------------------------------
setup['Exp']['name'] = 'test'                                                                                            # Name of the simulation
setup['Dat']['name'] = 'data_Test2'                                                                                      # Name of the data file
setup['Par']['name'] = 'setup_Template'                                                                                  # Name of the setup file

# ------------------------------------------
# Settings
# ------------------------------------------
setup['Exp']['SOC'] = 0.8                                                                                                # Starting SOC value of the HVS (p.u.)
setup['Exp']['Vdc'] = 3                                                                                                  # 1) constant nominal voltage, 2) measured voltage, 3) SOC based
setup['Exp']['Cool'] = 1                                                                                                 # 1) constant coolant temperature, 2) measured coolant temperature, 3) coolant temperature calculated
setup['Exp']['Tc'] = 35                                                                                                  # Constant coolant temperature (degC)
setup['Exp']['lim'] = 0                                                                                                  # 0) component limits are not used, 1) component limits enforced

# ------------------------------------------
# Plotting
# ------------------------------------------
setup['Exp']['plot'] = 1                                                                                                 # 1) Plotting reduced, 2) Plotting detail
setup['Exp']['plotAxis'] = 'R'                                                                                           # R) Rear axis, F) Front axis, T) Total values
setup['Exp']['hFig'] = 900                                                                                               # Figure height (px)
setup['Exp']['wFig'] = 2000                                                                                              # Figure width (px)

# ==============================================================================
# Data
# ==============================================================================
setup['Dat']['fs'] = 1                                                                                                   # Sampling frequency of the data (Hz)

# ==============================================================================
# Parameters
# ==============================================================================
# ------------------------------------------
# Architecture
# ------------------------------------------
setup['Par']['xwd'] = 'RWD'                                                                                              # Number of wheels connected to the drive-train: 1) RWD, 2) FWD, 3) AWD

# ------------------------------------------
# Physical
# ------------------------------------------
setup['Par']['p_a'] = 1.2                                                                                                # air density (kg/m3)
setup['Par']['v_w'] = 0                                                                                                  # wind speed (m/s)

# ------------------------------------------
# Numeric
# ------------------------------------------
setup['Par']['sol'] = 2                                                                                                  # 1) numeric (tbi for IMPSM), 2) symbolic
setup['Par']['eps'] = 1e-12                                                                                              # Small numerical value
setup['Par']['err'] = 1e-6                                                                                               # Numerical error
setup['Par']['iterMax'] = 20                                                                                             # Maximum number of iterations

#######################################################################################################################
# Calculations
#######################################################################################################################
if __name__ == "__main__":
    main(setup, setupPath)
