#######################################################################################################################
#######################################################################################################################
# Title:        Python Electric Vehicle Power Toolkit (PyEVPowerKit)
# Topic:        EV Modeling
# File:         main
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
A short description of the class goes here.
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
from src.data.loadData import loadData
from src.data.loadSetup import loadSetup
from src.data.sampleData import sampleData
from src.general.mechVehPara import mechVehPara
from src.model.Veh.mechVeh import mechVeh
from src.model.Veh.mechWhe import mechWhe
from src.model.Veh.elecVeh import elecVeh
from src.model.Veh.therVeh import therVeh
from src.model.initComp import initComp
from src.model.mechSim import mechSim
from src.plot.plotting import plotting
from src.model.elecSim import elecSim
from src.model.therSim import therSim


# ==============================================================================
# External
# ==============================================================================
from tqdm import tqdm
import numpy as np


#######################################################################################################################
# Function
#######################################################################################################################
def main(setup, path):
    ###################################################################################################################
    # MSG IN
    ###################################################################################################################
    print("----------------------------------------------------------------------------------------------------------")
    print("----------------------------------------------------------------------------------------------------------")
    print("Welcome to the PyEVPowerKit toolkit")
    print("Author:     Dr. Pascal A. Schirmer")
    print("Copyright:  Pascal Schirmer")
    print("Version:    v.0.1")
    print("Date:       18.03.2024")
    print("----------------------------------------------------------------------------------------------------------")
    print("----------------------------------------------------------------------------------------------------------")

    ###################################################################################################################
    # Loading
    ###################################################################################################################
    # ==============================================================================
    # MSG IN
    # ==============================================================================
    print("=======================================================================")
    print("START: Loading")
    print("=======================================================================")

    # ==============================================================================
    # Parameter
    # ==============================================================================
    setup = loadSetup(setup, path)

    # ==============================================================================
    # Data
    # ==============================================================================
    data = loadData(setup, path)

    # ==============================================================================
    # MSG OUT
    # ==============================================================================
    print("=======================================================================")
    print("END: Loading")
    print("=======================================================================")
    print("\n")

    ###################################################################################################################
    # Pre-Processing
    ###################################################################################################################
    # ==============================================================================
    # MSG IN
    # ==============================================================================
    print("=======================================================================")
    print("START: Pre-Processing")
    print("=======================================================================")

    # ==============================================================================
    # Data
    # ==============================================================================
    # ------------------------------------------
    # Msg
    # ------------------------------------------
    print("------------------------------------------")
    print("Pre-processing Data")
    print("------------------------------------------")

    # ------------------------------------------
    # Resampling
    # ------------------------------------------
    data = sampleData(data, setup)

    # ==============================================================================
    # Parameter
    # ==============================================================================
    # ------------------------------------------
    # Msg
    # ------------------------------------------
    print("------------------------------------------")
    print("Pre-processing Parameters")
    print("------------------------------------------")

    # ------------------------------------------
    # Calc
    # ------------------------------------------
    setup = mechVehPara(setup)

    # ==============================================================================
    # MSG OUT
    # ==============================================================================
    print("=======================================================================")
    print("END: Pre-Processing")
    print("=======================================================================")
    print("\n")

    ###################################################################################################################
    # Calculation
    ###################################################################################################################
    # ==============================================================================
    # MSG IN
    # ==============================================================================
    print("=======================================================================")
    print("START: Driving Simulation")
    print("=======================================================================")

    # ==============================================================================
    # Init
    # ==============================================================================
    N = len(data['t'])
    Tinit = data['T_C'][0]
    dataTime = {'VEH': {'Vdc': np.zeros(N), 'Tc': np.zeros(N), 'SOC': np.zeros(N), 'dQ': np.zeros(N),
                        'F': {}, 'P': {}, 'E': {}, 'eta': {}},
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
                              'Vq': np.zeros(N), 'Vs': np.zeros(N), 'lam': np.zeros(N), 'Min': np.zeros(N)},
                        'R': {'T': Tinit * np.ones(N), 'M': np.zeros(N), 'n': np.zeros(N), 'Pm': np.zeros(N),
                              'Pin': np.zeros(N), 'Pout': np.zeros(N), 'Pv': np.zeros(N), 'Pv_m': np.zeros(N),
                              'Pv_s': np.zeros(N), 'Pv_r': np.zeros(N), 'eta': np.zeros(N), 'PF': np.zeros(N),
                              'Id': np.zeros(N), 'Iq': np.zeros(N), 'Is': np.zeros(N), 'Vd': np.zeros(N),
                              'Vq': np.zeros(N), 'Vs': np.zeros(N), 'lam': np.zeros(N), 'Min': np.zeros(N)},
                        'T': {'T': Tinit * np.ones(N), 'M': np.zeros(N), 'n': np.zeros(N), 'Pm': np.zeros(N),
                              'Pin': np.zeros(N), 'Pout': np.zeros(N), 'Pv': np.zeros(N), 'Pv_m': np.zeros(N),
                              'Pv_s': np.zeros(N), 'Pv_r': np.zeros(N), 'eta': np.zeros(N), 'PF': np.zeros(N),
                              'Id': np.zeros(N), 'Iq': np.zeros(N), 'Is': np.zeros(N), 'Vd': np.zeros(N),
                              'Vq': np.zeros(N), 'Vs': np.zeros(N), 'lam': np.zeros(N), 'Min': np.zeros(N)}},
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

    # ==============================================================================
    # Vehicle
    # ==============================================================================
    # ------------------------------------------
    # Msg
    # ------------------------------------------
    print("------------------------------------------")
    print("Vehicle Level Simulation")
    print("------------------------------------------")

    # ------------------------------------------
    # Mechanical
    # ------------------------------------------
    # Vehicle
    dataTime = mechVeh(data, dataTime, setup)

    # Wheels
    dataTime = mechWhe(data, dataTime, setup)

    # ------------------------------------------
    # Electrical
    # ------------------------------------------
    dataTime = elecVeh(data, dataTime, setup)

    # ------------------------------------------
    # Thermal
    # ------------------------------------------
    dataTime = therVeh(data, dataTime, setup)

    # ==============================================================================
    # Components
    # ==============================================================================
    # ------------------------------------------
    # Msg
    # ------------------------------------------
    print("------------------------------------------")
    print("Component Level Simulation")
    print("------------------------------------------")

    # ------------------------------------------
    # Init Components
    # ------------------------------------------
    [GBX, EMA, INV, HVS, VEH] = initComp(setup)

    # ------------------------------------------
    # Target Simulation
    # ------------------------------------------
    for iter in tqdm(range(len(data['t'])), desc='Mission Profile'):
        # Mechanical
        dataTime = mechSim(iter, GBX, EMA, dataTime, setup)

        # Electrical
        dataTime = elecSim(iter, EMA, INV, HVS, dataTime, setup)

        # Thermal
        dataTime = therSim(iter, GBX, EMA, INV, HVS, VEH, data, dataTime, setup)

    # ------------------------------------------
    # Actual Simulation
    # ------------------------------------------

    # ==============================================================================
    # MSG OUT
    # ==============================================================================
    print("=======================================================================")
    print("END: Driving Simulation")
    print("=======================================================================")
    print("\n")

    ###################################################################################################################
    # Post-Processing
    ###################################################################################################################
    # ==============================================================================
    # MSG IN
    # ==============================================================================
    print("=======================================================================")
    print("START: Post-Processing")
    print("=======================================================================")

    # ==============================================================================
    # Reliability
    # ==============================================================================
    # ------------------------------------------
    # Msg
    # ------------------------------------------
    print("------------------------------------------")
    print("Calculating Reliability")
    print("------------------------------------------")

    # ------------------------------------------
    # Start
    # ------------------------------------------

    # ==============================================================================
    # Average
    # ==============================================================================
    # ------------------------------------------
    # Msg
    # ------------------------------------------
    print("------------------------------------------")
    print("Averaging results")
    print("------------------------------------------")

    # ------------------------------------------
    # Start
    # ------------------------------------------

    # ==============================================================================
    # Saving
    # ==============================================================================
    # ------------------------------------------
    # Msg
    # ------------------------------------------
    print("------------------------------------------")
    print("Saving results")
    print("------------------------------------------")

    # ------------------------------------------
    # Start
    # ------------------------------------------

    # ==============================================================================
    # Plotting
    # ==============================================================================
    # ------------------------------------------
    # Msg
    # ------------------------------------------
    print("------------------------------------------")
    print("Plotting results")
    print("------------------------------------------")

    # ------------------------------------------
    # Start
    # ------------------------------------------
    plotting(data, dataTime, setup)

    # ==============================================================================
    # MSG OUT
    # ==============================================================================
    print("=======================================================================")
    print("END: Post-Processing")
    print("=======================================================================")

    ###################################################################################################################
    # Output
    ###################################################################################################################

    return []
