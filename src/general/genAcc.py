import numpy as np

m = 1930
cr = 0.01
cw = 0.23
A = 2.22
Pmax = 230e3
n0 = 5000 / 60
r = 0.344
iGbx = 9
vbase = 2*r*np.pi*n0 / iGbx
t = np.linspace(0, 20, 2001)
dt = t[1] - t[0]
v = np.zeros(len(t))

for i in range(1, len(t)):
    Fa = 0.5 * 1.2 * A * cw * v[i - 1] ** 2
    Fr = cr * m * 9.81

    if v[i - 1] > vbase:
        P = Pmax / v[i - 1]
    else:
        P = Pmax  / vbase

    v[i] = v[i - 1] + ((P - Fa - Fr) / m) * dt

test = 1
np.savetxt("foo.csv", v, delimiter=",")