# -*- coding: utf-8 -*-
"""
Created on Sun Oct 01 16:13:55 2017

@author: WenKroy2
"""

import matplotlib.pyplot as plt
import numpy as np
#### Définition du système différentiel par un vecteur ####
def F(a,b,c,d,xy):
    return np.array(....."""à compléter""".....)

#### Implémentation de la fonction Volterra ####
global max
def Volterra(T,h,XY0,a,b,c,d,F):
    N=int(T/h)
    TPS=[0]
    XY=np.zeros((N,2),dtype=float)
    XY[0,:]=XY0 # définition des C.I.
    max=0
    for i in range(1,N):
        XY[i,:]=....."""à compléter""".....
        TPS.append(TPS[i-1]+h)
        print TPS[i]
        if XY[i,0]>max:
            max=XY[i,0]
        elif XY[i,1]>max:
            max=XY[i,1]
    return TPS,XY,max


#### Définition des constantes du problème ####
T,h,XY0,a,b,c,d=50.0,0.01,[5,1],0.6,0.8,0.6,0.3

#### Résolution du système ####
TPS,XY,max=Volterra(T,h,XY0,a,b,c,d,F)


#### Représentations graphiques ####
plt.subplot(2,1,1)
plt.xlabel(u'$t$(année)')
plt.ylabel(r'Population')
plt.axis([TPS[0],TPS[-1],0,1.1*max])
Proies=plt.plot(TPS,XY[:,0],label=u'Population des proies')
Predateurs=plt.plot(TPS,XY[:,1],label=u'Population des predateurs')
plt.title(u'Modèle dynamique de Lotka-Volterra',size=20)
plt.legend()


plt.subplot(2,1,2)
plt.xlabel(u'Population proies')
plt.ylabel(u'Population prédateurs')
plt.axis([0,1.1*max,0,1.1*max])
plt.plot(XY[:,0],XY[:,1],label=u'Portrait de phase')
#plt.title(u'Portrait de phase du système de Lotka-Volterra',size=20)
plt.legend()
plt.show()
