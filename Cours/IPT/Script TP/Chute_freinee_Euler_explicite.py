# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 11:52:59 2017

@author: WenKroy2
"""

from matplotlib import pyplot as plt
from math import exp
#Definition de la fonction d'increment
def f(u):
    return 1-u
####### Conditions initiales  #####
U=[0]
V=[0]
TPS=[0]
h=0.1 #pas temporel
T=3 #temps final
N=int(T/h) #nombre de points
##### Itérations sur le schéma d'Euler
for i in range(0,N):
    U.append(U[i]+h*f(U[i]))
    V.append(1-exp(-(TPS[i]+h)))
    TPS.append(TPS[i]+h)
plt.plot(TPS,U,'--',label="Euler",linewidth = 2)
plt.plot(TPS,V,'-.',label= u"Théorique",linewidth = 2, color="blue")
plt.xlabel('temps')
plt.ylabel('vitesse')
plt.legend(loc=1)
plt.show()