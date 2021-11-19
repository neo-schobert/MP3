# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 11:52:59 2017

@author: WenKroy2
"""

from matplotlib import pyplot as plt
import numpy as np
#### Définition des constantes #####
epsilon=0.1
omega0=1
###### Définition de la fonction d'incrément ######
def vdp(y,epsilon,omega0):
    ypoint = np.array([y[1], epsilon*omega0*(1 - y[0]**2)*y[1] - y[0]])
    return ypoint

##### Procédure itérative selon le schéma RK4
def RK4_Van_der_Pol(T,h):
    N=int(T/h)
    TPS=np.zeros((N+1,1), dtype=float)
    Y=np.zeros((N+1,2), dtype=float)
    Y[0,:]=[1.1,0.0]
    # 2.00861986087484313650940188
    for i in range(N):
        k1 = vdp(Y[i,:],epsilon,omega0)
        k2 = vdp(Y[i,:]+0.5*h*k1,epsilon,omega0)
        k3 = vdp(Y[i,:]+0.5*h*k2,epsilon,omega0)
        k4 = vdp(Y[i,:]+h*k3,epsilon,omega0)
        TPS[i+1]=TPS[i]+h
        Y[i+1,:]=Y[i,:]+(h/6)*(k1+2*k2+2*k3+k4)
    return TPS,Y
###### Lancement de la résolution et tracé de la solution et portrait de phase
T,h=35,0.1
TPS,Y=RK4_Van_der_Pol(T,h)
fig=plt.figure("Oscillateur de Van der Pol")
plt.subplot(2,2,1)
plt.plot(TPS,Y[:,0])
plt.xlabel('$t$')
plt.ylabel('$y_1(t)$')
plt.subplot(2,2,2)
plt.plot(TPS,Y[:,1])
plt.xlabel('$t$')
plt.ylabel('$y_2(t)$')
plt.subplot(2,2,3)
plt.title(u"Portrait de phase de l'oscillateur")
plt.plot(Y[:,0], Y[:,1])
plt.xlabel('$y_1(t)$')
plt.ylabel('$y_2(t)$')
fig.subplots_adjust(hspace=1)
plt.show()