#######################################################################################################################
#######################################################################################################################
# Title:        Python Electric Vehicle Power Toolkit (PyEVPowerKit)
# Topic:        EV Modeling
# File:         classGBX
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
Class of the gear box including loss calculation, mechanical calculation, and thermal calculation.

Fnc:
1)  calc_mech:  calculates the mechanical values
2)  calc_loss:  calculates the losses based on the rotational speed
3)  calc_ther:  calculates the self-heating based on the thermal parameters and the losses

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
import numpy as np


#######################################################################################################################
# Class
#######################################################################################################################
class classGBX:
    ###################################################################################################################
    # Constructor
    ###################################################################################################################
    def __init__(self, i, J, T_max, n_max, P_max, c_m, c_b, c_w, C_th, R_th, h_th, A_th, Ea, k, n, L0, Nf0, F0, beta, CL, Bx):
        self.i = i
        self.J = J
        self.T_max = T_max
        self.n_max = n_max
        self.P_max = P_max
        self.c_m = c_m
        self.c_b = c_b
        self.c_w = c_w
        self.C_th = C_th
        self.R_th = R_th
        self.h_th = h_th
        self.A_th = A_th
        self.Ea = Ea
        self.k = k
        self.n = n
        self.L0 = L0
        self.Nf0 = Nf0
        self.F0 = F0
        self.beta = beta
        self.CL = CL
        self.Bx = Bx

    ###################################################################################################################
    # Mechanics
    ###################################################################################################################
    def calc_mech(self, M_Whe, n_Whe, setup):
        # ==============================================================================
        # Description
        # ==============================================================================
        """
        This function calculates the electrical parameters of the battery.

        Input:
        1) M_Whe:   Torque of the wheel (Nm)
        2) n_Whe:   Rotational speed of the wheel (1/s)
        3) setup:   Setup variables

        Output:
        1) M_Gbx:   Torque of the gearbox (Nm)
        2) n_Gbx:   Rotational speed of the gearbox (1/s)
        3) P_Gbx:   Input power (W)
        4) Pout:    Output power (W)
        5) Pv:      Losses (W)
        6) eta:     Efficiency (%)
        """

        # ==============================================================================
        # Fnc
        # ==============================================================================
        def sat(x, theta):
            return min(theta, max(-theta, x))

        # ==============================================================================
        # Pre-Processing
        # ==============================================================================
        # ------------------------------------------
        # Limit
        # ------------------------------------------
        if setup['Exp']['lim'] == 1:
            n_Whe = sat(n_Whe, self.n_max / self.i)
            M_Whe = sat(M_Whe, self.T_max * self.i)
            P_Whe = sat(2 * np.pi * M_Whe * n_Whe, self.P_max)
            if n_Whe != 0:
                M_Whe = P_Whe / (2 * np.pi * n_Whe)

        # ------------------------------------------
        # Output
        # ------------------------------------------
        n_Gbx = n_Whe * self.i
        w_m = 2 * np.pi * n_Whe
        Pout = M_Whe * w_m

        # ==============================================================================
        # Calculation
        # ==============================================================================
        # ------------------------------------------
        # Losses
        # ------------------------------------------
        [Pv, _, _, _] = self.calc_loss(n_Gbx)

        # ------------------------------------------
        # Power
        # ------------------------------------------
        # Driving
        if Pout >= 0:
            Pin = Pout + Pv

        # Recuperation
        else:
            if abs(Pv) < abs(Pout):
                Pin = Pout + Pv
            else:
                Pin = -1e-12

        # ------------------------------------------
        # Efficiency
        # ------------------------------------------
        eta = Pout / Pin
        eta = np.nan_to_num(eta, nan=1)

        # ------------------------------------------
        # Mechanical
        # ------------------------------------------
        M_Gbx = M_Whe / self.i / (eta + 1e-12)
        P_Gbx = 2 * np.pi * n_Gbx * M_Gbx

        # ==============================================================================
        # Post-processing
        # ==============================================================================
        if eta >= 1:
            eta = 1/eta

        # ==============================================================================
        # Return
        # ==============================================================================
        return [M_Gbx, n_Gbx, P_Gbx, Pout, Pv, eta]

    ###################################################################################################################
    # Losses
    ###################################################################################################################
    def calc_loss(self, n_Gbx):
        # ==============================================================================
        # Description
        # ==============================================================================
        """
        This function calculates the losses of the battery.

        Input:
        1) n_Gbx:   Rotational speed gearbox (1/s)

        Output:
        1) Pv:      Total losses (W)
        2) Pv_b:    Bearing losses (W)
        3) Pv_m:    Meshing losses (W)
        4) Pv_w:    Windage losses (W)
        """

        # ==============================================================================
        # Calculation
        # ==============================================================================
        Pv_b = self.c_b * np.abs(n_Gbx)
        Pv_m = self.c_m * np.abs(n_Gbx)
        Pv_w = self.c_w * n_Gbx**2

        # ==============================================================================
        # Post-Processing
        # ==============================================================================
        Pv = Pv_b + Pv_m + Pv_w

        # ==============================================================================
        # Return
        # ==============================================================================
        return [Pv, Pv_b, Pv_m, Pv_w]

    ###################################################################################################################
    # Thermal
    ###################################################################################################################
    def calc_therm(self, dt, T, Pv1, Pv2):
        # ==============================================================================
        # Description
        # ==============================================================================
        """
        This function calculates the self-heating of the gearbox.

        Input:
        1) dt:      discrete time step between two samples (sec)
        2) T:       Temperature of the previous time step (degC)
        3) Pv1:     Losses of the previous time step (W)
        4) Pv2:     Losses of the actual time step (W)

        Output:
        1) dT:      Temperature change (K)
        """

        # ==============================================================================
        # Initialisation
        # ==============================================================================
        tau = self.R_th * self.C_th
        Rth = self.R_th

        # ==============================================================================
        # Calculation
        # ==============================================================================
        dT = (2 * tau - dt) / (2 * tau + dt) * T + (Rth * dt) / (2 * tau + dt) * (Pv1 + Pv2)

        # ==============================================================================
        # Return
        # ==============================================================================
        return dT

#######################################################################################################################
# References
#######################################################################################################################
