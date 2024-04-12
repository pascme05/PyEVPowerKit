#######################################################################################################################
#######################################################################################################################
# Title:        Python Electric Vehicle Power Toolkit (PyEVPowerKit)
# Topic:        EV Modeling
# File:         classEMA
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

# ==============================================================================
# External
# ==============================================================================
import numpy as np
import math as mt
import sympy as sy


#######################################################################################################################
# Class PSM
#######################################################################################################################
class classPSM:
    ###################################################################################################################
    # Constructor
    ###################################################################################################################
    def __init__(self, Type, Mag, p, n_0, J_rot, T_max, n_max, P_max, I_max, Psi, L_d, L_q, L_sig, R_s, c_b, c_w, K_h,
                 K_f, C_th, R_th, h_th, A_th, Ea, k, n, L0, Nf0, F0, beta, CL, Bx):
        self.Type = Type
        self.Mag = Mag
        self.p = p
        self.n_0 = n_0
        self.J_rot = J_rot
        self.T_max = T_max
        self.n_max = n_max
        self.P_max = P_max
        self.I_max = I_max
        self.Psi = Psi
        self.L_d = L_d
        self.L_q = L_q
        self.L_sig = L_sig
        self.R_s = R_s
        self.c_b = c_b
        self.c_w = c_w
        self.K_h = K_h
        self.K_f = K_f
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
    def calc_mech(self, M_Gbx, n_Gbx):
        # ==============================================================================
        # Pre-Processing
        # ==============================================================================
        n_Ema = n_Gbx
        w_m = 2 * np.pi * n_Ema
        Pout = M_Gbx * w_m

        # ==============================================================================
        # Calculation
        # ==============================================================================
        # ------------------------------------------
        # Losses
        # ------------------------------------------
        [Pv, _, _, _] = self.calc_loss(n_Ema, 0, 0, 0, 0, 0)
        Pin = Pout + Pv
        eta = Pout / Pin
        eta = np.nan_to_num(eta, nan=1)

        M_Ema = M_Gbx / (eta + 1e-12)
        P_Ema = 2 * np.pi * n_Ema * M_Ema

        # ==============================================================================
        # Return
        # ==============================================================================
        return [M_Ema, n_Ema, P_Ema, Pv, eta]

    ###################################################################################################################
    # Elec Surface Magnets
    ###################################################################################################################
    def calc_elec_SM(self, n_Ema, M_Ema, Vdc, T):
        # ==============================================================================
        # Init
        # ==============================================================================
        def sat(x, theta):
            return min(theta, max(-theta, x))

        # ==============================================================================
        # Pre-processing
        # ==============================================================================
        Rs = self.R_s * (1 + 0.00393 * (T - 20))
        v_max = Vdc / np.sqrt(3) - Rs * self.I_max
        w_m_base = (1 / self.p) * v_max / (np.sqrt((self.L_q * self.I_max) ** 2 + self.Psi ** 2))
        w_m = 2 * np.pi * n_Ema
        w_e = 2 * np.pi * n_Ema * self.p
        R_Fe = 1 / (self.K_f + self.K_h / (self.p * w_e + 1) + 1e-9)

        # ==============================================================================
        # Calculation
        # ==============================================================================
        # ------------------------------------------
        # Base Speed
        # ------------------------------------------
        if w_m <= w_m_base:
            id_sat = 0
            iq_mtpa = M_Ema / (3 / 2 * self.p * self.Psi)
            iq_sat = sat(iq_mtpa, self.I_max)

        # ------------------------------------------
        # Field Weakening
        # ------------------------------------------
        else:
            id_fw = (self.p * w_m_base - w_e) * self.Psi / (w_e * self.L_d)
            iq_fw = M_Ema / (3 / 2 * self.p * self.Psi)
            id_sat = sat(id_fw, self.I_max)
            iq_lim = np.sqrt(self.I_max ** 2 - id_sat ** 2)
            iq_sat = sat(iq_fw, iq_lim)

        # ==============================================================================
        # Post-processing
        # ==============================================================================
        # ------------------------------------------
        # Flux Current
        # ------------------------------------------
        id0 = id_sat
        iq0 = iq_sat

        # ------------------------------------------
        # Iron Current
        # ------------------------------------------
        vd0 = - w_e * self.L_q * iq0
        vq0 = w_e * self.L_d * id0 + w_e * self.Psi
        id_fe = vd0 / R_Fe
        iq_fe = vq0 / R_Fe
        id = id0 + id_fe
        iq = iq0 + iq_fe

        # ------------------------------------------
        # Stator Quantities
        # ------------------------------------------
        # Current
        Is = np.sqrt(id ** 2 + iq ** 2)

        # Voltage
        vd = Rs * id - w_e * self.L_q * iq + w_e ** 2 / R_Fe * (self.L_q * self.L_d * id + self.L_q * self.Psi)
        vq = Rs * iq + w_e * self.L_d * id + w_e ** 2 / R_Fe * (self.L_q * self.L_d * iq) + w_e * self.Psi
        Vs = np.sqrt(vd ** 2 + vq ** 2)

        # ==============================================================================
        # Return
        # ==============================================================================
        return [id, iq, Is, vd, vq, Vs]

    ###################################################################################################################
    # Elec Interior Magnets
    ###################################################################################################################
    def calc_elec_IM(self, n_Ema, M_Ema, Vdc, T):
        # ==============================================================================
        # Pre-processing
        # ==============================================================================
        Rs = self.R_s * (1 + 0.00393 * (T - 20))
        v_max = Vdc / np.sqrt(3) - Rs * self.I_max
        w_m = 2 * np.pi * n_Ema
        w_e = 2 * np.pi * n_Ema * self.p
        R_Fe = 1 / (self.K_f + self.K_h / (w_e + 1) + 1e-9)

        # ==============================================================================
        # Calculation
        # ==============================================================================
        # ------------------------------------------
        # Magnetizing Current
        # ------------------------------------------
        i_m_ref = M_Ema / (3 / 2 * self.p * self.Psi)
        i_m = min(i_m_ref, self.I_max)
        id_mtpa = self.Psi / (4 * (self.L_q - self.L_d)) - np.sqrt(self.Psi ** 2 / (16 * (self.L_q - self.L_d) ** 2) + i_m ** 2 / 2)
        iq_mtpa = np.sqrt(i_m ** 2 - id_mtpa ** 2)
        iq_mtpa = np.nan_to_num(iq_mtpa, nan=0)

        # ------------------------------------------
        # d/q Currents (stationary)
        # ------------------------------------------
        w_m_base = (1 / self.p) * v_max / (np.sqrt((self.L_q * iq_mtpa) ** 2 + (self.Psi + self.L_d*id_mtpa) ** 2))
        w_m_base = 2 * np.pi * self.n_0 * self.p

        # ------------------------------------------
        # d/q Currents (stationary)
        # ------------------------------------------
        # Base Speed
        if w_m <= w_m_base:
            iq_sat = iq_mtpa
            id_sat = id_mtpa

        # Field Weakening
        else:
            id_fw = (-self.Psi * self.L_d + np.sqrt((self.Psi * self.L_d) ** 2 - (self.L_d ** 2 - self.L_q ** 2) * (
                    self.Psi ** 2 + self.L_q ** 2 * self.I_max ** 2 - v_max ** 2 / w_e ** 2))) / (self.L_d ** 2 - self.L_q ** 2)
            id_sat = max(id_fw, -self.I_max)
            iq_fw = np.sqrt(self.I_max ** 2 - id_fw ** 2)
            if iq_fw < i_m:
                iq_sat = iq_fw
            else:
                iq_sat = i_m

        # ==============================================================================
        # Post-processing
        # ==============================================================================
        # ------------------------------------------
        # Flux Current
        # ------------------------------------------
        id0 = id_sat
        iq0 = iq_sat

        # ------------------------------------------
        # Iron Current
        # ------------------------------------------
        vd0 = - w_e * self.L_q * iq0
        vq0 = w_e * self.L_d * id0 + w_e * self.Psi
        id_fe = vd0 / R_Fe
        iq_fe = vq0 / R_Fe
        id = id0 + id_fe
        iq = iq0 + iq_fe

        # ------------------------------------------
        # Stator Quantities
        # ------------------------------------------
        # Current
        Is = np.sqrt(id ** 2 + iq ** 2)

        # Voltage
        vd = Rs * id - w_e * self.L_q * iq + w_e ** 2 / R_Fe * (self.L_q * self.L_d * id + self.L_q * self.Psi)
        vq = Rs * iq + w_e * self.L_d * id + w_e ** 2 / R_Fe * (self.L_q * self.L_d * iq) + w_e * self.Psi
        Vs = np.sqrt(vd ** 2 + vq ** 2)

        # ==============================================================================
        # Return
        # ==============================================================================
        return [id, iq, Is, vd, vq, Vs]

    ###################################################################################################################
    # Function
    ###################################################################################################################
    def calcEMA_MTPA(self, T, n, Theta, Vdc, verbose=False):
        # ==============================================================================
        # Init
        # ==============================================================================
        erg = {}
        i_d = sy.symbols('i_d')
        Rs = self.R_s * (1 + 0.00393 * (Theta - 20))
        v_max = Vdc / np.sqrt(3) - Rs * self.I_max
        w_e = 2 * sy.pi * n * self.p

        # ==============================================================================
        # Pre-processing
        # ==============================================================================
        R_Fe = 1 / (self.K_f + self.K_h / (w_e + 1) + 1e-9)

        # ==============================================================================
        # Base Speed
        # ==============================================================================
        if T == 0:
            erg["status"] = 'Status: Basic Speed Range'
            erg["i_d"] = 0
            erg["i_q"] = 0
            erg["v_d"] = 0
            erg["v_q"] = 0
            return erg

        # ==============================================================================
        # Above Max Speed
        # ==============================================================================
        if n > self.n_max:
            erg["status"] = 'Error: Rotational limit reached!'
            return erg

        # ==============================================================================
        # MTPA
        # ==============================================================================
        # ------------------------------------------
        # Currents
        # ------------------------------------------
        i_dlist = (sy.solveset(sy.Eq(sy.diff((i_d ** 2 + ((2 * T) / (3 * self.p * (
                self.Psi + (self.L_d - self.L_q) * i_d))) ** 2), i_d), 0), i_d, sy.Interval(-self.I_max, 0)))
        if len(list(i_dlist)) == 0:
            erg["status"] = 'Error: Current limit reached!'
            return (erg)
        i_ds = list(i_dlist)[0]
        erg["i_d"] = i_ds
        i_q = (2 * T) / (3 * self.p * (self.Psi + (self.L_d - self.L_q) * i_ds))
        erg["i_q"] = i_q

        # ------------------------------------------
        # MTPC
        # ------------------------------------------
        if verbose:
            erg["fuc_T"] = sy.lambdify(i_d, (2 * T) / (3 * self.p * (self.Psi + (self.L_d - self.L_q) * i_d)))
            erg["MTPC"] = (i_ds, i_q)
        if i_ds ** 2 + i_q ** 2 > self.I_max ** 2:
            erg["status"] = 'Error: Current limit reached!'
            return erg

        # ------------------------------------------
        # Voltage
        # ------------------------------------------
        v_d = (i_ds * Rs - w_e * self.L_q * i_q).evalf()
        erg["v_d"] = v_d
        v_q = (i_q * Rs + (self.L_d * i_ds + self.Psi) * w_e).evalf()
        erg["v_q"] = v_q

        # ------------------------------------------
        # Current Limits
        # ------------------------------------------
        if verbose:
            if T > 0:
                erg['fuc_Imax'] = sy.lambdify(i_d, sy.sqrt(self.I_max ** 2 - i_d ** 2))
            elif T < 0:
                erg['fuc_Imax'] = sy.lambdify(i_d, -sy.sqrt(self.I_max ** 2 - i_d ** 2))

        # ==============================================================================
        # Voltage Limit
        # ==============================================================================
        if sy.sqrt(v_d ** 2 + v_q ** 2) > v_max:
            # ------------------------------------------
            # Positive Torque
            # ------------------------------------------
            if T > 0:
                func = sy.lambdify(i_d, (2 * T) / (3 * self.p * (self.Psi + (
                        self.L_d - self.L_q) * i_d)) - sy.sqrt((v_max ** 2 - (
                        w_e * self.Psi + w_e * self.L_d * i_d) ** 2) / (w_e ** 2 * self.L_q ** 2)))
                with np.errstate(invalid='ignore'):
                    xx = np.linspace(-self.I_max, 0, 10000)
                    if np.nanmin(func(xx)) > 0:
                        # erg["fuc_V"] = func
                        erg["fuc_V"] = sy.lambdify(i_d, sy.sqrt((v_max ** 2 - (w_e * self.Psi + w_e * self.L_d * i_d) ** 2) / (w_e ** 2 * self.L_q ** 2)))
                        erg["status"] = 'Error: Voltage limit reached!'
                        return erg

                with np.errstate(invalid='ignore'):
                    A = np.diff(np.sign(func(xx)))
                A[np.isnan(A)] = 0
                test = xx[np.where(A)[0]]
                if not test.size > 0:
                    test = [0]
                i_ds = test[0]
                erg["i_d"] = i_ds
                i_q = ((2 * T) / (3 * self.p * (self.Psi + (self.L_d - self.L_q) * list(test)[0])))  # .evalf() )
                erg["i_q"] = i_q
                erg["status"] = 'Status: Field-Weakening!'
                v_d = (i_ds * Rs - w_e * self.L_q * i_q).evalf()
                erg["v_d"] = v_d
                v_q = (i_q * Rs + (self.L_d * i_ds + self.Psi) * w_e).evalf()
                erg["v_q"] = v_q
                if verbose:
                    erg["fuc_V"] = sy.lambdify(i_d, sy.sqrt(
                        (v_max ** 2 - (w_e * self.Psi + w_e * self.L_d * i_d) ** 2) / (w_e ** 2 * self.L_q ** 2)))
                if i_ds ** 2 + i_q ** 2 > self.I_max ** 2:
                    erg["status"] = 'Error: Current limit under voltage limit reached!'
                    return erg
                return erg

            # ------------------------------------------
            # Negative Torque
            # ------------------------------------------
            elif T < 0:
                func = sy.lambdify(i_d, (2 * T) / (3 * self.p * (self.Psi + (
                        self.L_d - self.L_q) * i_d)) + sy.sqrt((v_max ** 2 - (
                        w_e * self.Psi + w_e * self.L_d * i_d) ** 2) / (w_e ** 2 * self.L_q ** 2)))
                with np.errstate(invalid='ignore'):
                    xx = np.linspace(-self.I_max, 0, 10000)
                    if np.nanmax(func(xx)) < 0:
                        # erg["fuc_V"] = func
                        erg["fuc_V"] = sy.lambdify(i_d, sy.sqrt((v_max ** 2 - (w_e * self.Psi + w_e * self.L_d * i_d) ** 2) / (w_e ** 2 * self.L_q ** 2)))
                        erg["status"] = 'Error: Voltage limit reached!'
                        return erg
                with np.errstate(invalid='ignore'):
                    A = np.diff(np.sign(func(xx)))
                A[np.isnan(A)] = 0
                test = xx[np.where(A)[0]]
                if not test.size > 0:
                    test = [0]
                i_ds = test[0]
                erg["i_d"] = i_ds
                i_q = ((2 * T) / (3 * self.p * (self.Psi + (self.L_d - self.L_q) * list(test)[0])))
                erg["i_q"] = i_q
                erg["status"] = 'Status: Field-Weakening!'
                v_d = (i_ds * Rs - w_e * self.L_q * i_q).evalf()
                erg["v_d"] = v_d
                v_q = (i_q * Rs + (self.L_d * i_ds + self.Psi) * w_e).evalf()
                erg["v_q"] = v_q
                if verbose:
                    erg["fuc_V"] = sy.lambdify(i_d, -sy.sqrt(
                        (v_max ** 2 - (w_e * self.Psi + w_e * self.L_d * i_d) ** 2) / (w_e ** 2 * self.L_q ** 2)))
                if i_ds ** 2 + i_q ** 2 > self.I_max ** 2:
                    erg["status"] = 'Error: Current limit under voltage limit reached!'
                    return (erg)
                return (erg)

        erg["status"] = 'Status: Basic Speed Range'

        # ==============================================================================
        # Return
        # ==============================================================================
        return erg

    ###################################################################################################################
    # Electrical
    ###################################################################################################################
    def calc_elec(self, n_Ema, M_Ema, sel, Vdc, fs, T):
        # ==============================================================================
        # Init
        # ==============================================================================
        w_m = 2 * np.pi * n_Ema
        Pout = M_Ema * w_m
        i = 0
        i_max = 50

        # ==============================================================================
        # Pre-processing
        # ==============================================================================
        if n_Ema != 0:
            [_, Pv_fric, _, _] = self.calc_loss(n_Ema, 0, 0, 0, fs, T)
            M_in = M_Ema + Pv_fric / w_m
        else:
            Pv_fric = 0
            M_in = M_Ema

        # ==============================================================================
        # Calculation
        # ==============================================================================
        # ------------------------------------------
        # Currents and Voltages
        # ------------------------------------------
        # Interior Magnet
        if sel == 2:
            #[id, iq, Is, vd, vq, Vs] = self.calc_elec_IM(n_Ema, M_in, Vdc, T)
            while i < i_max:
                erg = self.calcEMA_MTPA(M_in, n_Ema, T, Vdc)
                if not erg['status'][0:5] == 'Error':
                    id = float(erg['i_d'])
                    iq = float(erg['i_q'])
                    vd = float(erg['v_d'])
                    vq = float(erg['v_q'])
                    break
                else:
                    M_in = M_in * 0.99
                    i = i + 1

        # Surface Magnet
        else:
            #[id, iq, Is, vd, vq, Vs] = self.calc_elec_SM(n_Ema, M_in, Vdc, T)
            while i < i_max:
                erg = self.calcEMA_MTPA(M_in, n_Ema, T, Vdc)
                if not erg['status'][0:5] == 'Error':
                    id = float(erg['i_d'])
                    iq = float(erg['i_q'])
                    vd = float(erg['v_d'])
                    vq = float(erg['v_q'])
                    break
                else:
                    M_in = M_in * 0.99
                    i = i + 1
        Is = np.sqrt(id ** 2 + iq ** 2) / np.sqrt(2)
        Vs = np.sqrt(vd ** 2 + vq ** 2) / np.sqrt(2)

        # ------------------------------------------
        # Flux
        # ------------------------------------------
        lam_d = self.L_d * id + self.Psi
        lam_q = self.L_q * iq
        lam_s = np.sqrt(lam_d ** 2 + lam_q ** 2)

        # ------------------------------------------
        # Losses
        # ------------------------------------------
        [Pv, _, _, _] = self.calc_loss(n_Ema, Is, Vs, Vdc, fs, T)

        # ------------------------------------------
        # Inner Torque
        # ------------------------------------------
        Min = 3 / 2 * self.p * (iq * lam_d - id * lam_q)

        # ==============================================================================
        # Post-Processing
        # ==============================================================================
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
        # Torque
        # ------------------------------------------
        if n_Ema != 0:
            Mshaft = Min - Pv_fric / w_m
        else:
            Mshaft = Min

        # ------------------------------------------
        # Efficiency
        # ------------------------------------------
        # Init
        eta = Pout / Pin
        eta = np.nan_to_num(eta, nan=1)

        # Recuperation
        if eta >= 1:
            eta = 1/eta

        # ------------------------------------------
        # Power Factor
        # ------------------------------------------
        try:
            phi = mt.acos(Pin / (3 * Vs * Is + 1e-9))
            PF = np.cos(phi)
        except:
            PF = 1

        # ==============================================================================
        # Return
        # ==============================================================================
        return [id, iq, Is, vd, vq, Vs, lam_s, Pin, Pout, Pv, eta, PF, Min, Mshaft]

    ###################################################################################################################
    # Losses
    ###################################################################################################################
    def calc_loss(self, n_Ema, Is, Vs, Vdc, fs, T):
        # ==============================================================================
        # Init
        # ==============================================================================
        Mi = Vs / ((Vdc + 1e-12) / 2)
        HDF = 3 / 2 * Mi ** 2 - 4 * np.sqrt(3) / np.pi * Mi ** 3 + (27 / 16 - 81 * np.sqrt(3) / (64 * np.pi)) * Mi ** 4

        # ==============================================================================
        # Pre-processing
        # ==============================================================================
        Rs = self.R_s * (1 + 0.00393 * (T - 20))
        w_m = 2 * np.pi * n_Ema
        R_Fe = 1 / (self.K_f + self.K_h / (self.p * w_m + 1) + 1e-9)
        I_s_thd = Vdc / (24 * self.L_sig * fs) * np.sqrt(HDF)

        # ==============================================================================
        # Calculation
        # ==============================================================================
        # ------------------------------------------
        # Mechanical
        # ------------------------------------------
        bear_loss = self.c_b * np.abs(n_Ema)
        wind_loss = self.c_w * n_Ema ** 2
        mech_loss = bear_loss + wind_loss

        # ------------------------------------------
        # Electrical
        # ------------------------------------------
        # Stator
        stator_ohm_loss = 3 * Rs * Is ** 2
        stator_mag_loss = 3 * (Vs - Rs * Is) ** 2 / R_Fe
        stator_har_loss = 3 * Rs * I_s_thd ** 2
        stator_loss = stator_ohm_loss + stator_mag_loss + stator_har_loss

        # Rotor (tbd)
        rotor_ohm_loss = 0
        rotor_mag_loss = 0
        rotor_har_loss = 0
        rotor_loss = rotor_ohm_loss + rotor_mag_loss + rotor_har_loss

        # ==============================================================================
        # Post-Processing
        # ==============================================================================
        Pv = mech_loss + stator_loss + rotor_loss

        # ==============================================================================
        # Return
        # ==============================================================================
        return [Pv, mech_loss, stator_loss, rotor_loss]

    ###################################################################################################################
    # Thermal
    ###################################################################################################################
    def calc_therm(self, dt, Tc, Pv1, Pv2):
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
