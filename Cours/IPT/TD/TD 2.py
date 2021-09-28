import time as t
import numpy as np
from math import *
import random
import copy

# Exercice 1
# 1)
# n=301, res=0, aux=1, b=1
# res=1, aux=2, n=30, b=0
# res=1, aux=4, n=3, b=3


# n=1010, res=0, aux=1, b=0
# res=0, aux=2, n=101, b=1
# res=2, aux=4, n=10, b=0
# res=2, aux=8, n=1, b=1
# res=10, aux=16, n=0




# def mystere(n):
    # res = 0
    # aux = 1
    # while ( n != 0) :
    #     b = n % 10
    #     if b<2:
    #         res = res  + aux *b
    #         aux = aux *2
    #         n=n//10
    #     else:
    #         print("Erreur")
            # return None
    # return res

# for k in range(200,300):
    # print(k, mystere(k))


# 2)
# Il s'agit d'un bin_to_nat.



# Exercice 2

# 1)
# \displaystyle\sum_{k=1}^{2n} \frac{(-1)^{k-1}}{k}= \displaystyle\sum_{k=1}^n -\frac{1}{2k} + \displaystyle\sum_{k=1}^n \frac{1}{2k-1}
# =\displaystyle\sum_{k=1}^n \frac{1}{(2k-1)2k}= \frac{1}{2} \displaystyle\sum_{k=1}^n \frac{1}{(2k-1)k}


#2)

def S1(n):
    s=0
    for k in range(1,2*n+1):
        s+= ((-1)**(k-1))/k
    return s


def S2(n):
    s=0
    for k in range(1,n+1):
        s+= 1/((2*k-1)*k)
    return s/2


#3)







#4)
# Les sommes convergent vers ln(2)






def ln2(n):
    for p in range(n,n+2):
        t0=t.time()
        print(S1(2*p))
        print(S2(p))
        print(S1(2*p+1))
        print( np.log(2))
        print(u"temps d’exécution t=",t.time()-t0)
        print("−−−−−−−−−−−−−−−−−−−−−")



# Exercice 3
# 1)
# Le nombre en base x s'écrit avec un polynôme en x. Un polynôme étant comparable à une suite, chaque coefficient est alors un terme de la suite.
# Cette suite est alors le nombre exprimé en base x.

# 2)
def hexa_to_dec(hexa):
    L=["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]
    s=0
    for k in range(len(hexa)):
        ind=0
        while hexa[k]!=L[ind]:
            ind+=1
        s+=(s + ind)*16
    return s

# En faisant ainsi, le changement de base est simple et ne nécessite que peu de ressources (on supprime les puissances en factorisant -> moins de calculs à faire)



# Exercice 4

# 1)
# (a12f)_{16}= (((10*16+1)*16+2)*16+15)_{10}=(41263)_{10}

# 2) Ce script fait la conversion inverse : de décimal vers hexadécimal


# Le script renvois une liste comportant des éléments de l'ensemble [\![0;15]\!]. Il faut des éléments de la liste L=["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"].


def Chiffre(n):
    c=[]
    L=["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]
    while n!=0:
        c=c.append(L[n%16])
        n//=16
    c.reverse()
    return c



# Exercice 5
def frac_egypt(x,y):
    L=[]
    while x!=0: 
        a,x,y=ceil(y/x),(-y)%x,y*ceil(y/x)
        L.append((1,a))
    return L


# Exercice 6
# 1)
def sum_ln(x):
    s=0
    k=1
    while s<=x:
        s+=1/k
        k+=1
    return k

# print(sum_ln(5),sum_ln(10),sum_ln(15),sum_ln(17.4))


# 2)
# a)




# b)




# c)





# 3)






# Exercice 7









# Exercice 8
# 1)
def max(L,deb):
    max,ind=L[deb],deb
    for k in range(deb,len(L)):
        if L[k]>max:
            max,ind=L[k],k
    return ind,max

# 2)
# a) La dernière instruction est return None, cette fonction est de type list -> unit. La liste L est globale à la fonction car il s'agit d'une liste.
# Cette fonction tri donc la liste mais ne renvoit rien.

# b) On a une boucle for avec un nombre fini d'itérations (n n'est pas modifié dans la boucle). Donc le boucle se termine forcément. L'algorithme aussi.


# c)
# Initialisation :

# P_1: A la 1 ere itération, CLF. 
# Par hérédité, si L_j[0]>= L_j[1]>=...>=L_j[j-1] et \forall i>=j, L_j[i]<=L_j[j-1]

# Au rang j+1, CLF encore...



# Exercice 9
# 1)
def app(e,T):
    for k in T:
        if k==e:
            return True
    return False


# 2) Le nombre maximum d'intérations est len(T).


# 3)
# a)


def dicho(e,T):
    g,d=0,len(T)-1
    while g<=d:
        m=(g+d)//2
        if T[m] == e:
            return True
        if T[m]<e:
            g=m+1
        else:
            d=m-1
    return False


# b)
# A chaque tour de boucle, on a soit dk+1=(dk+gk)//2 et gk+1=gk; soit dk+1=dk et gk+1=(dk+gk)//2.
# Finalement, par récurrence, En 0,d0-g0=n-1<n.

# Si c'est bon en k,dans les deux cas, dk+1-gk+1=(dk+gk)//2 -gk=(dk-gk)//2=n/2**k ou dk+1-gk+1=dk-(dk+gk)//2=n/2**k



# c) La boucle se termine quand gk>dk; c'est à dire quand dk-gk< 0 C'est à dire, car on prend des parties entieres, quand 2**k>n.

# Donc on a ln(n)/ln(2) itérations.


# d) A chaque tour de boucle, dk-gk est divisé par 2. Donc forcément, à partir d'un certain moment, dk-gk va être inférieur strict à 1. (suite géométrique de raison 1/2 tend vers 0.)
# Donc la partie entiere de dk-gk va être nul à partir d'un certain rang. C'est à ce rang que la boucle va se terminer. La terminaison est alors assurée.



# e)

# Exercice 10







# Exercice 11
# 1)

# 0<=random.random()<1
# 0<= (h+2)/2 * random.random()<(h+2)/2
# 1<=n< int((h+2))/2 +1<=(h+2)/2 +1

# 2)
def calcul_n(h):
    return int((h+2)/2 * random.random())+1


print(calcul_n(2))

# 3)
def initialisation(P):
    piles=[0 for k in range(P+1)]
    return piles

# 4)
def actualise(piles,perdus):
    n=len(piles)
    piles_actualisee=copy.deepcopy(piles + [0])
    for k in range(n):
        piles_actualisee[k+1]=calcul_n(piles[k])
    piles_actualisee[0]=piles_actualisee[0]-piles_actualisee[1]
    perdus = piles_actualisee[n]
    return piles_actualisee[:n] ,perdus


# 5)





# Exercice 12