# -*- coding: utf-8 -*-
"""
Created on Sun Oct 01 16:13:55 2017

@author: WenKroy2
"""

import matplotlib.pyplot as plt

#### Définition du système différentiel ####
def fx(a,b,c,d,x,y):
    return ......"""à compléter""".....
def fy(a,b,c,d,x,y):
    return ....."""à compléter""".....

#### Implémentation de la fonction Volterra ####
global max
def Volterra(T,h,x0,y0,a,b,c,d,fx,fy):
    N=int(T/h)
    TPS=[0]
    X=[x0]
    Y=[y0]
    max=0
    for i in range(N):
        X.append(....."""à compléter""".....)
        Y.append(....."""à compléter""".....)
        TPS.append(....."""à compléter""".....)
        if X[i]>max:
            max=X[i]
        elif Y[i]>max:
            max=Y[i]
    return TPS,X,Y,max
#### Définition des constantes du problème ####
T,h,x0,y0,a,b,c,d=50.0,0.01,5,1,0.6,0.8,0.6,0.3

#### Résolution du système ####
TPS,X,Y,max=Volterra(T,h,x0,y0,a,b,c,d,fx,fy)
print TPS[-1]

#### Représentations graphiques ####
plt.subplot(2,1,1)
plt.xlabel(u'$t$(année)')
plt.ylabel(r'Population')
plt.axis([TPS[0],TPS[-1],0,1.1*max])
Proies=plt.plot(TPS,X,label=u'Population des proies')
Predateurs=plt.plot(TPS,Y,label=u'Population des predateurs')
#plt.title(u'Modèle dynamique de Lotka-Volterra',size=20)
plt.legend()


plt.subplot(2,1,2)
plt.xlabel(u'Population proies')
plt.ylabel(u'Population prédateurs')
plt.axis([0,1.1*max,0,1.1*max])
plt.plot(X,Y,label=u'Portrait de phase')
#plt.title(u'Portrait de phase du système de Lotka-Volterra',size=20)
plt.legend()
plt.show()
