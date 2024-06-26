#######################################################################################################################
#######################################################################################################################
# Title:        EVOptiDrive (Optimal Drivetrain Design for Electrical Vehicles)
# Topic:        Electrical Vehicle (EV) Simulation
# File:         sampleData
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
This function resamples the mission profile of the vehicle. The sampling is done using zero order hold (ZOH).
Inputs:     1) data:    mission profile
            2) setup:   includes all simulation variables
Outputs:    1) data:    resampled version of the mission profile
"""

#######################################################################################################################
# Import libs
#######################################################################################################################
# ==============================================================================
# Internal
# ==============================================================================
from src.external.zoh import zoh

# ==============================================================================
# External
# ==============================================================================
import numpy as np
import pandas as pd
from scipy import integrate


#######################################################################################################################
# Function
#######################################################################################################################
def sampleData(data, setup):
    ###################################################################################################################
    # MSG IN
    ###################################################################################################################
    print("START: Resample Data")

    ###################################################################################################################
    # Initialisation
    ###################################################################################################################
    # ==============================================================================
    # Parameters
    # ==============================================================================
    fields = data.columns
    fs_raw = setup['Dat']['fs_raw']
    fs = setup['Dat']['fs']
    N = len(data)

    # ==============================================================================
    # Variables
    # ==============================================================================
    t = np.linspace(data['t'][0], data['t'][N-1], int(np.floor((data['t'][N-1] - data['t'][0])*fs)+1))
    out = np.zeros((len(t), len(fields)))

    ###################################################################################################################
    # Calculation
    ###################################################################################################################
    # ==============================================================================
    # Interpolate
    # ==============================================================================
    if fs == fs_raw:
        print("INFO: Sampling rate of the data is equivalent to target sampling rate: ", fs, " Hz")
        out = data
    else:
        # ------------------------------------------
        # Calc
        # ------------------------------------------
        for i in range(0, len(fields)):
            out[:, i] = zoh(t, data['t'], data[fields[i]])

        # ------------------------------------------
        # Out
        # ------------------------------------------
        out = pd.DataFrame(out, columns=fields)

        # ------------------------------------------
        # Msg
        # ------------------------------------------
        print("INFO: Sampling rate of the data ", fs_raw, " Hz is not equivalent to target sampling rate ", fs, " Hz data is resampled")

    # ==============================================================================
    # Acceleration and Distance
    # ==============================================================================
    a = np.gradient(out['v'], out['t'])
    s = integrate.cumtrapz(out['v'], out['t'], initial=0)
    out.insert(1, "a", a, True)
    out.insert(3, "s", s, True)

    ###################################################################################################################
    # MSG Out
    ###################################################################################################################
    print("DONE: Resample Data")

    return out
