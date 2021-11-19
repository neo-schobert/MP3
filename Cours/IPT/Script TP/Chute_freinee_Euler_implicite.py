# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 19:40:33 2017

@author: WenKroy2
"""
from matplotlib import pyplot as plt
##### Méthode d'Euler implicite #####
def Euler_implicite(T,h,t0,v0,f):
    N=int(T/h)
    TPS=[t0]
    V=[v0]
    for i in range(N):
        TPS.append(TPS[i]+h) #incrément du temps
        vn1=Newton(h,V[i],f) #calcule de la valeur v(n+1)
        V.append(V[i]+h*f(vn1))
    return TPS,V

##### Fonctions associées à la résolution #####
## Définition de la fonction F pour le calcul implicite ##
def F(h,v,vn,f):
    return vn+h*f(v)-v
## Méthode de Newton ###
def Newton(h,vn,f):
    err=1.0
    eps=1e-9
    v=vn+h*f(vn) #initialisation de v(n+1) à une valeur "type" méthode explicite
    while err>eps:
        dF=(F(h,v+h,vn,f)-F(h,v,vn,f))/h #calcul de la dérivée au point x0 (nouveau candidat)
        v1=v-F(h,v,vn,f)/dF
        err=abs(v1-v)
        v=v1
    return v1

##### Lancement calcul et tracé #####
T,h,t0,v0=3.0,0.1,0.0,0.0
def f(u):
    return 1-u
TPS,V=Euler_implicite(T,h,t0,v0,f)

plt.plot(TPS,V,'--',label=u"v(t) par méthode Euler implicite", linewidth=2)
plt.xlabel('temps')
plt.ylabel('vitesse')
plt.legend(loc=2)
plt.show()
