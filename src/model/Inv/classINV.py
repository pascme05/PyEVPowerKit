#######################################################################################################################
#######################################################################################################################
# Title:        Python Electric Vehicle Power Toolkit (PyEVPowerKit)
# Topic:        EV Modeling
# File:         classINV
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
Class of the converter including loss calculation, electrical calculation, and thermal calculation.

Fnc:
1)  calc_elec:  calculates the electrical values
2)  calc_loss:  calculates the losses based on the currents and voltages
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
class classB6:
    ###################################################################################################################
    # Constructor
    ###################################################################################################################
    def __init__(self, fs, Sw, nSw, nCap, V_0, I_0, T_0, Tj_max, alpha, P_max, I_max, V_ce0, r_T, V_d0, r_D, E_on, E_off,
                 E_rec, R_g, R_esr, C_dc, R_ac, R_dc, C_th, R_th, h_th, A_th, Ea, k, n, L0, Nf0, F0, beta, CL, Bx):
        self.fs = fs
        self.Sw = Sw
        self.nSw = nSw
        self.nCap = nCap
        self.V_0 = V_0
        self.I_0 = I_0
        self.T_0 = T_0
        self.Tj_max = Tj_max
        self.alpha = alpha
        self.P_max = P_max
        self.I_max = I_max
        self.V_ce0 = V_ce0
        self.r_T = r_T
        self.V_d0 = V_d0
        self.r_D = r_D
        self.E_on = E_on
        self.E_off = E_off
        self.E_rec = E_rec
        self.R_esr = R_esr
        self.R_g = R_g
        self.C_dc = C_dc
        self.R_ac = R_ac
        self.R_dc = R_dc
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
    # Electrical
    ###################################################################################################################
    def calc_elec(self, cos_phi, Vs, Is, Vdc, Tj, setup):
        # ==============================================================================
        # Description
        # ==============================================================================
        """
        This function calculates the electrical parameters of the converter.

        Input:
        1) cos_phi: Power factor of the electric machine (-)
        2) Vs:      RMS stator voltage (V)
        3) Is:      RMS stator current (A)
        4) Vdc:     DC-link voltage (V)
        5) Tj:      Junction temperature of the power module (degC)
        6) setup:   setup file of the simulation

        Output:
        1) Mi:      Modulation index (-)
        2) Idc:     Inverter input current (A)
        3) Ic:      Capacitor current (A)
        4) Pin:     Input power (W)
        5) Pout:    Output power (W)
        6) Pv:      Losses (W)
        7) eta:     Efficiency (%)
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
            Is = sat(Is, self.I_max)
            P_lim = sat(3 * Is * Vs * cos_phi, self.P_max)
            Is = P_lim / (3 * Vs * cos_phi)

        # ------------------------------------------
        # Modulation Index
        # ------------------------------------------
        Mi = Vs * np.sqrt(2) / (Vdc/2)

        # ==============================================================================
        # Calculation
        # ==============================================================================
        # ------------------------------------------
        # Currents
        # ------------------------------------------
        Idc = 3 / 4 * np.sqrt(2) * Is * Mi * cos_phi
        Ic = np.sqrt(2 * Mi * (np.sqrt(3) / (4 * np.pi) + cos_phi ** 2 * (np.sqrt(3) / np.pi - 9 / 16 * Mi))) * Is

        # ------------------------------------------
        # Losses
        # ------------------------------------------
        [Pv, _, _, _, _] = self.calc_loss(Mi, cos_phi, Is, Ic, Idc, Vdc, Tj)

        # ==============================================================================
        # Post-Processing
        # ==============================================================================
        # ------------------------------------------
        # Power
        # ------------------------------------------
        Pin = Vdc * Idc + Pv
        Idc = Idc + Pv / Vdc
        Pout = 3 * Is * Vs * cos_phi

        # ------------------------------------------
        # Efficiency
        # ------------------------------------------
        # Init
        eta = Pout / Pin
        eta = np.nan_to_num(eta, nan=1)

        # Recuperation
        if eta >= 1:
            eta = 1 / eta

        # ==============================================================================
        # Return
        # ==============================================================================
        return [Mi, Idc, Ic, Pin, Pout, Pv, eta]

    ###################################################################################################################
    # Losses
    ###################################################################################################################
    def calc_loss(self, Mi, cos_phi, Is, Ic, Idc, Vdc, Tj):
        # ==============================================================================
        # Description
        # ==============================================================================
        """
        This function calculates the losses of the converter.

        Input:
        1) Mi:      Modulation index (-)
        2) cos_phi: Power factor of the electric machine (-)
        3) Is:      RMS stator current (A)
        4) Ic:      Capacitor current (A)
        5) Idc:     Inverter input current (A)
        6) Vdc:     DC-link voltage (V)
        7) Tj:      Junction temperature of the power module (degC)

        Output:
        1) Pv:      Total losses (W)
        2) Pv_swi:  Losses power module (W)
        3) Pv_cap:  Losses dc-link capacitor (W)
        4) Pv_ac:   Losses AC busbar (W)
        5) Pv_dc:   Losses DC busbar (W)
        """

        # ==============================================================================
        # Pre-Processing
        # ==============================================================================
        # ------------------------------------------
        # Scale Energies
        # ------------------------------------------
        E_on = self.E_on * np.max(np.abs(Is)) / self.I_0 * np.max(np.abs(Vdc)) / self.V_0 * (1 + self.alpha/100) ** (Tj - self.T_0)
        E_off = self.E_off * np.max(np.abs(Is)) / self.I_0 * np.max(np.abs(Vdc)) / self.V_0 * (1 + self.alpha / 100) ** (Tj - self.T_0)
        E_rec = self.E_rec * np.max(np.abs(Is)) / self.I_0 * np.max(np.abs(Vdc)) / self.V_0 * (1 + self.alpha / 100) ** (Tj - self.T_0)

        # ------------------------------------------
        # Scale Temperature
        # ------------------------------------------
        Rac = self.R_ac * (1 + 0.00393 * (Tj - 20))
        Rdc = self.R_dc * (1 + 0.00393 * (Tj - 20))
        r_T = self.r_T * (1 + self.alpha/100) ** (Tj - self.T_0)
        r_D = self.r_D * (1 + self.alpha / 100) ** (Tj - self.T_0)

        # ------------------------------------------
        # Scale Current
        # ------------------------------------------
        I0 = np.sqrt(2) * Is / self.nSw

        # ==============================================================================
        # Calculation
        # ==============================================================================
        # ------------------------------------------
        # Power Module
        # ------------------------------------------
        # MOSFET
        if self.Sw == 2:
            p_l_sw_con = r_T * I0 ** 2 * (1 / 8 + (Mi * cos_phi) / (3 * np.pi))
            p_l_di_con = self.V_d0 * I0 * (1 / (2 * np.pi) - (Mi * cos_phi) / 8) + r_D * I0 ** 2 * (1 / 8 - (Mi * cos_phi) / (3 * np.pi))
            p_l_sw_swi = (E_on + E_off + E_rec) * self.fs
            Pv_swi = self.nSw * (p_l_sw_con + p_l_di_con + p_l_sw_swi)

        # IGBT
        else:
            p_l_sw_con = self.V_ce0 * I0 * (1 / (2*np.pi) + (Mi * cos_phi) / 8) + r_T * I0**2 * (1/8 + (Mi * cos_phi) / (3*np.pi))
            p_l_di_con = self.V_d0 * I0 * (1 / (2*np.pi) - (Mi * cos_phi) / 8) + r_D * I0**2 * (1/8 - (Mi * cos_phi) / (3*np.pi))
            p_l_sw_swi = (E_on + E_off + E_rec) * self.fs
            Pv_swi = self.nSw * (p_l_sw_con + p_l_di_con + p_l_sw_swi)

        # ------------------------------------------
        # DC-Link Capacitor
        # ------------------------------------------
        Pv_cap = self.nCap * self.R_esr * (Ic / self.nCap) ** 2

        # ------------------------------------------
        # Busbars
        # ------------------------------------------
        Pv_ac = 3 * Rac * Is ** 2
        Pv_dc = 2 * Rdc * Idc ** 2

        # ==============================================================================
        # Post-Processing
        # ==============================================================================
        Pv = Pv_swi + Pv_cap + Pv_ac + Pv_dc

        # ==============================================================================
        # Return
        # ==============================================================================
        return [Pv, Pv_swi, Pv_cap, Pv_ac, Pv_dc]

    ###################################################################################################################
    # Thermal
    ###################################################################################################################
    def calc_therm(self, dt, Tc, Pv1, Pv2):
        # ==============================================================================
        # Description
        # ==============================================================================
        """
        This function calculates the self-heating of the converter.

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
        dT = (2 * tau - dt) / (2 * tau + dt) * Tc + (Rth * dt) / (2 * tau + dt) * (Pv1 + Pv2)

        # ==============================================================================
        # Return
        # ==============================================================================
        return dT

#######################################################################################################################
# References
#######################################################################################################################
