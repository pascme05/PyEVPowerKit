# PyEVPowerKit
Python Electric Vehicle Power Toolkit (PyEVPowerKit) is a Python toolkit designed for engineers and enthusiasts to 
facilitate the design and analysis of electrical power-trains for electric vehicles (EVs). The toolkit implements a
mechanical vehicle model considering all source acting on the vehicle while driving as well as the power train of the 
electric vehicle. It calculates the mechanical, electrical, and thermal loads on the different components of the drive-train
of the vehicle. Additionally, the thermal stress on the different components is evaluated.


# Dependencies
The requirements of the PyEVPowerKit toolkit are summarized in the requirements.txt data file. In detail, the PyEVPowerKit
Toolkit was implemented using the following dependencies:
- Python 3.11
- pandas 2.2.1
- scipy 1.12.0
- numpy
- matplotlib


# Citation 
The symbolic MTPA/MPTV solver has been abstracted from [2].


# Limitations
Since the toolkit is still under development there are several things that need to be improved, are not yet implemented 
or lack verification. In the following a list of known issues and limitations is provided:
- SSM and ASM machine types are not yet implemented
- The model is only defined for positive velocities, i.e. v>0

# Architecture
The presented architecture includes a physical vehicle simulation considering all forces acting on the vehicle. In detail,
these forces including: air friction (Fa), rolling friction (Fr), climbing forces (Fc), and acceleration forces (Facc).
The total force (Ft) is then calculated as the sum of these forces.

$F_{t} = F_{a} + F_{r} + F_{c} + F_{acc}$                                       

In detail, each of these forces can be described using the laws of physics:

$F_{a} = \frac{1}{2} \cdot \rho_{A} \cdot A \cdot c_{w} \cdot v^2$                

$F_{r} = c_{r} \cdot m \cdot g \cdot cos(\alpha)$                             

$F_{c} = m \cdot g \cdot sin(\alpha)$                                          

$F_{acc} = (m + m_{acc}) \cdot \frac{dv}{dt}$                                   

where $\rho_{A}$ is the density of air, $A$ is the vehicle frontal area, $c_{w}$ is the shape factor for the air resistance
$v$ is the vehicle speed, $m$ is the vehicle mass, $m_{acc}$ is the equivalent acceleration mass (e.g. due to rotating 
parts), and $\alpha$ is the slope of the road. Based on the above the required mechanical torque, power, and energy can 
be determined for a lossless system.

$M_{wheel} = \frac{1}{2} \cdot F_{t} \cdot r_{dyn}$     

$P_{veh} = F_{t} \cdot v$  

$E_{veh} = \int_{0}^{T_{end}} P_{veh} \cdot dt$                                                             

where $M_{wheel}$ is the torque per wheel, $P_{veh}$ the mechanical power, and $E_{veh}$ the mechanical energy of the 
lossless vehicle. Additionally $r_{dyn}$ is the dynamic wheel radius. Knowing the required torque per wheel and further
assuming a gearbox with a constant gear ratio $i_{g}$, each operation point can be described by a set of torque and rotational 
speed values. The components can than be calculated according to the architecture presented below:

![img.png](docu/arch.png)

# Results
The results provided in this section have been obtained from a Tesla model 3 [1]. In detail, the acceleration to the 
maximum vehicle speed and the WLTP operation are considered. The parameters and the results are listed below.

## Parameters
All parameters can be found under /setup in the different worksheets of the Excel file. An overview of the most important
parameters is provided below:

| Parameter | Description                      | Value | Unit  |
|-----------|----------------------------------|-------|-------|
| n_max     | Maximum rotational speed machine | 16000 | 1/min |
| n_0       | Nominal rotational speed machine | 5000  | 1/min |
| T_max     | Maximum machine torque           | 420   | Nm    |
| I_max     | Maximum RMS stator current       | 971   | A     |
| P_max     | Maximum machine power            | 239   | kW    |
| Psi       | Magnetic flux linkage            | 0.074 | Vs    |
| L_d       | Inductance d-axis                | 110   | uH    |
| L_q       | Inductance q-axis                | 340   | uH    |
| R_s       | Stator resistance 20 degC        | 4.85  | mOhm  |
| p         | Number of pole pairs             | 3     | -     |
| J_rot     | Inertia rotor                    | 0.12  | kgm2  |

## Maximum Acceleration
In this operating mode the vehicle accelerates from standstill ($v=0$), to its maximum speed ($v=v_{max}$). 

![acc.png](docu/acc.png)

All other results can be obtained by running startAcceleration.py

## WLTP operation
In this operating mode the vehicle is driving the WLTP cycle. The velocity, acceleration, and distance over time is
illustrated in the figure below:

![img_1.png](docu/wltp.png)

All other results can be obtained by running startWLTP.py

# Development
As failure and mistakes are inextricably linked to human nature, the toolkit is obviously not perfect, 
thus suggestions and constructive feedback are always welcome. If you want to contribute to the PyDTS
toolkit or spot any mistake, please contact me via: p.schirmer@herts.ac.uk


# License
The software framework is provided under the MIT License.


# Version History
1) v.0.1: (16.04.2024) Initial version of PyEVPowerKit
2) v.0.2: (21.04.2024) Optimising MTPA and MPTV solver

# References
[1] https://motorxp.com/wp-content/uploads/mxp_analysis_TeslaModel3.pdf

[2] Schlüter, Michael, Marius Gentejohann, and Sibylle Dieckerhoff. "Driving Cycle Power Loss Analysis of SiC-MOSFET 
and Si-IGBT Traction Inverters for Electric Vehicles." 2023 25th European Conference on Power Electronics and
Applications (EPE'23 ECCE Europe). IEEE, 2023.