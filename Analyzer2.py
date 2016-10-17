import numpy as np
import matplotlib.pyplot as plt

Bs=0.17
Bp=0.5

#z, y, x = np.mgrid[0:3:100j, -1.5:1.5:100j, -1.5:1.5:100j]

#usol = 0*x*y*z

#vsol = 0*x*y*z

#wsol = B

Bsol = []
for z in range(10):
    thisz = []
    for y in range(10):
        thisy = []
        for x in range(10):
            thisy.append(np.array([0+0j, 0+0j, Bs+0j]))
        thisz.append(thisy)
    Bsol.append(thisz)

Bperm = []
for z in range(10):
    thisz = []
    for y in range(10):
        thisy = []
        for x in range(10):
            thisy.append(np.array([Bp+0j, np.complex(0, Bp), 0+0j]))
        thisz.append(thisy)
    Bperm.append(thisz)
B = []
for z in range(10):
    thisz = []
    for y in range(10):
        thisy = []
        for x in range(10):
            thisy.append(Bsol[z][y][x]+Bperm[z][y][x])
        thisz.append(thisy)
    B.append(thisz)
print B[5]
