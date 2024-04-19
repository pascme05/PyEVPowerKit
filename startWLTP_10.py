#######################################################################################################################
#######################################################################################################################
# Title:        Python Electric Vehicle Power Toolkit (PyEVPowerKit)
# Topic:        EV Modeling
# File:         startWLTP10
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
setup['Exp']['name'] = 'Tesla3_Vmax'                                                                                     # Name of the simulation
setup['Dat']['name'] = 'data_WLTP_10'                                                                                    # Name of the data file
setup['Par']['name'] = 'setup_Tesla3'                                                                                    # Name of the setup file

# ------------------------------------------
# Operating Time
# ------------------------------------------
setup['Exp']['on'] = 8000                                                                                                # total driving time (hrs)
setup['Exp']['km'] = 300000                                                                                              # total distance (km)
setup['Exp']['life'] = 131400                                                                                            # total lifetime (hrs)

# ------------------------------------------
# Settings
# ------------------------------------------
setup['Exp']['SOC'] = 1                                                                                                  # Starting SOC value of the HVS (p.u.)
setup['Exp']['Vdc'] = 1                                                                                                  # 1) constant nominal voltage, 2) measured voltage, 3) SOC based
setup['Exp']['Cool'] = 3                                                                                                 # 1) constant coolant temperature, 2) measured coolant temperature, 3) calculated coolant temperature
setup['Exp']['Tc'] = 30                                                                                                  # Constant coolant temperature (degC)
setup['Exp']['Ta'] = 20                                                                                                  # Constant ambient temperature (degC)
setup['Exp']['lim'] = 1                                                                                                  # 0) component limits are not used (using Vdc=1000V), 1) component limits enforced, 2) enforce only voltage

# ------------------------------------------
# Plotting
# ------------------------------------------
setup['Exp']['plot'] = 1                                                                                                 # 1) Plotting reduced, 2) Plotting detail, 3) Plotting lifetime
setup['Exp']['plotAxis'] = 'R'                                                                                           # R) Rear axis, F) Front axis, T) Total values

# ------------------------------------------
# Saving
# ------------------------------------------
setup['Exp']['save'] = 0                                                                                                 # 0) files are not saved, 2) files are saved in \results

# ==============================================================================
# Data
# ==============================================================================
setup['Dat']['fs'] = 0.1                                                                                                 # Sampling frequency of the data (Hz)

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
setup['Par']['iterMax'] = 100                                                                                            # Maximum number of iterations

#######################################################################################################################
# Calculations
#######################################################################################################################
if __name__ == "__main__":
    main(setup, setupPath)
