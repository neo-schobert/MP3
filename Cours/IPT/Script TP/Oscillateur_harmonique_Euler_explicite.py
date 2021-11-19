# -*- coding: utf-8 -*-
"""
Created on Sun Oct 01 16:13:55 2017

@author: WenKroy2
"""

import matplotlib.pyplot as plt

def Oscill_Euler_expl(T,h,x0,v0,omega):
    N=int(T/h)
    TPS=[0]
    X=[x0]
    V=[v0]
    maxx,maxv=0,0
    for i in range(N):
        X.append(....."""à compléter""".....)
        V.append(....."""à compléter""".....)
        TPS.append(TPS[i]+h)
        if X[i]>maxx:
            maxx=X[i]
        elif V[i]>maxv:
            maxv=V[i]
    return TPS,X,V,maxx,maxv
#### Définition des constantes du problème ####
T,h,x0,v0,omega=50.0,0.01,5,0,1

#### Résolution du système ####
TPS,X,V,maxx,maxv=Oscill_Euler_expl(T,h,x0,v0,omega)

#### Représentations graphiques ####
plt.subplot(2,1,1)
plt.xlabel(u'$t$(seconde)')
plt.ylabel(r'Amplitude et vitesse')
plt.axis([TPS[0],TPS[-1],-1.1*maxx,1.1*maxx])
Proies=plt.plot(TPS,X,label=u'Amplitude oscillation')
Predateurs=plt.plot(TPS,V,label=u'Vitesse oscillation')
plt.title(u"Oscillateur harmonique par méthode d'Euler explicite",size=20)
plt.legend()

plt.subplot(2,1,2)
plt.xlabel(u'Amplitude')
plt.ylabel(u'Vitesse/omega')
plt.axis([-1.1*maxx,1.1*maxx,-1.1*maxv,1.1*maxv])
plt.plot(X,[(1/omega)*i for i in V],label=u'Portrait de phase (adimensionné)')
#plt.title(u'Portrait de phase du système de Lotka-Volterra',size=20)
plt.legend()

plt.show()