# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 19:40:33 2017

@author: WenKroy2
"""
from matplotlib import pyplot as plt
##### Méthode d'Euler implicite #####
def Euler_implicite(T,h,x0,v0,f): #def Oscill_Euler_expl(T,h,x0,v0,omega):
    N=int(T/h)
    TPS=[0]
    X=[x0]
    V=[v0]
    maxx,maxv=0,0
    for i in range(N):
        TPS.append(TPS[i]+h) #incrément du temps
        xn1,vn1=Newton(h,X[i],V[i],f) #calcule des valeurs x(n+1) et v(n+1)
        X.append(xn1)
        V.append(vn1)
        if X[i]>maxx:
            maxx=X[i]
        elif V[i]>maxv:
            maxv=V[i]
    return TPS,X,V,maxx,maxv

###############################################
##### Diverses Fonctions associées à la résolution #####
###############################################
## Définition de la fonction F pour le calcul implicite ##
def F(h,x,xn,vn,f):
    return xn+h*vn+h**2*f(x)-x
#### Définition de la fonction f ####
def f(u):
    return -omega**2*u

##### Méthode de Newton #####
def Newton(h,xn,vn,f):
    err=1.0
    eps=1e-9
    x=xn+h*vn #initialisation de x(n+1) à une valeur "type" méthode explicite (il faut bien choisir une valeur!)
    while err>eps:
        dF=(F(h,x+h,xn,vn,f)-F(h,x,xn,vn,f))/h #calcul de la dérivée au point x0 (nouveau candidat)
        x1=x-F(h,x,xn,vn,f)/dF #calcul du nouveau candidat x1
        err=abs(x1-x)
        x=x1
    v1=vn+h*f(x1) #calcul de la nouvelle valeur v(n+1) pour la vitesse
    return x1,v1


##### Lancement calcul et tracé #####
T,h,t0,x0,v0,omega=50,0.1,0.0,1.0,0.0,1
TPS,X,V,maxx,maxv=Euler_implicite(T,h,x0,v0,f)

#### Représentations graphiques ####
plt.subplot(2,1,1)
plt.xlabel(u'$t$(seconde)')
plt.ylabel(r'Amplitude et vitesse')
plt.axis([TPS[0],TPS[-1],-1.1*maxx,1.1*maxx])
Proies=plt.plot(TPS,X,label=u'Amplitude oscillation')
Predateurs=plt.plot(TPS,V,label=u'Vitesse oscillation')
#plt.title(u'Oscillateur harmonique par Euler',size=20)
plt.legend()

plt.subplot(2,1,2)
plt.xlabel(u'Amplitude')
plt.ylabel(u'Vitesse/omega')
plt.axis([-1.1*maxx,1.1*maxx,-1.3*maxv*(1/omega),1.3*maxv*(1/omega)])
plt.plot(X,(1/omega)*V,label=u'Portrait de phase (adimensionné)')
#plt.title(u'Portrait de phase du système de Lotka-Volterra',size=20)
plt.legend(loc=2)

plt.show()











