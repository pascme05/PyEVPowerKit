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
This function builds the main part of the driving simulation. It takes the setup files and path variables as input and
executes the program.
Inputs:     1) setup:   includes all simulation variables
            2) path:    includes all path variables
Outputs:    None
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
from src.general.smallFnc import initOutVar
from src.model.Veh.mechVeh import mechVeh
from src.model.Veh.mechWhe import mechWhe
from src.model.Veh.elecVeh import elecVeh
from src.model.Veh.therVeh import therVeh
from src.model.initComp import initComp
from src.model.mechSim import mechSim
from src.plot.plotting import plotting
from src.model.elecSim import elecSim
from src.model.therSim import therSim
from src.model.vehSim import vehSim
from src.general.save import save
from src.general.smallFnc import getCycles
from src.model.reliaSim import reliaSim


# ==============================================================================
# External
# ==============================================================================
from tqdm import tqdm


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

    # ------------------------------------------
    # Get Cycles
    # ------------------------------------------
    setup = getCycles(data, setup)

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
    dataTime = initOutVar(len(data['t']), data['T_C'][0])

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
    [data, dataTime] = elecVeh(data, dataTime, setup)

    # ------------------------------------------
    # Thermal
    # ------------------------------------------
    [data, dataTime] = therVeh(data, dataTime, setup)

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
    # Iterative Simulation
    # ------------------------------------------
    for iter in tqdm(range(len(data['t'])), desc='Mission Profile'):
        # Mechanical
        dataTime = mechSim(iter, GBX, EMA, dataTime, setup)

        # Electrical
        dataTime = elecSim(iter, EMA, INV, HVS, dataTime, setup)

        # Thermal
        dataTime = therSim(iter, GBX, EMA, INV, HVS, VEH, data, dataTime, setup)

        # Vehicle
        dataTime = vehSim(iter, VEH, data, dataTime, setup)

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
    dataLife = reliaSim(GBX, EMA, INV, HVS, dataTime, setup)

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
    if setup['Exp']['save'] == 1:
        save(dataTime, dataLife, path, setup)
    else:
        print("INFO: Saving disabled")

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
    if setup['Exp']['plot'] == 1:
        plotting(data, dataTime, dataLife, setup)
    else:
        print("INFO: Plotting disabled")

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
