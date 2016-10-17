import numpy as np
import matplotlib.pyplot as plt

Bsmax = 0.2
rho = 1.

dx = dy = 0.01
width = height = 3.

time = 0.

def dBdt(t):
    #print "dbdt:",-Bsmax*120*np.pi*np.sin(120*np.pi*t)
    return -Bsmax*120*np.pi*np.cos(120*np.pi*t)

def J(r, t):
    return -dBdt(t)*r/(2*rho)

def vecJ(x, y, t):
    r = np.sqrt(x**2+y**2)
    theta = np.arctan2(y,x)
    #print "X: %f, Y: %f, R:%f, T:%f"%(x, y, r, theta)
    mag = J(r, t)
    #print mag
    direction = theta+(np.pi/2.)
    return mag*np.cos(direction), mag*np.sin(direction), mag

X, Y = np.meshgrid(np.arange(-(width/2), width/2, dx), np.arange(-(height/2), height/2, dy))

Ju = []
Jv = []
Jmag = []
F = []
for i, row in enumerate(X):
    uRow = []
    vRow = []
    mRow = []
    fRow = []
    for j, x in enumerate(row):
        y = Y[i][j]
        r = np.sqrt(x**2+y**2)
        u, v, mag = vecJ(x, y, time)
        uRow.append(u)
        vRow.append(v)
        mRow.append(mag)
        f = np.cross([u,v],[0., abs(y-1.5)])
        #print x, y, u, v, f
        fRow.append(f)
    Ju.append(uRow)
    Jv.append(vRow)
    Jmag.append(mRow)
    F.append(fRow)
    
Ju = np.array(Ju)
Jv = np.array(Jv)
F = np.array(F)
#print F
#plt.quiver(X, Y, Ju, Jv)
plt.pcolormesh(X, Y, F)
plt.show()


