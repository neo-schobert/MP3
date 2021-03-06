#Exercice 1:
import numpy as np
from sympy.solvers import solve
from sympy import Symbol
import random


def parfait(n):
    s=0
    def diviseur(n):
        L=[]
        for k in range(1,(n//2)+1):
            if n%k==0:
                L.append(k)
        return L
    for k in diviseur(n):
        s+=k
    return s==n

def parfait_1_to_100000():
    L=[]
    for k in range(1,100000):
        if parfait(k):
            L.append(k)
    return L



#Exercice 2:
def suite_p_q_r(n):
    def pi(n):
        p=0
        while n%2==0:
            p+=1
            n//=2
        return p,n
    def qi(n):
        q=0
        while n%3==0:
            q+=1
            n//=3
        return q,n
    def ri(n):
        r=0
        while n%5==0:
            r+=1
            n//=5
        return r,n
    s=0
    k=1
    lst=[]
    while s<n:
        p,n2=pi(k)
        q,n3=qi(n2)
        r,n4=ri(n3)
        if n4==1:
            lst.append([k,(p,q,r)])
            s+=1
        k+=1
    return lst

# print(suite_p_q_r(10))



#Exercice 3:
#1
def liste_correcte(L):
    return (len(L)==9 and 1 in L and 2 in L and 3 in L and 4 in L and 5 in L and 6 in L and 7 in L and 8 in L and 9 in L)


# print(liste_correcte([k for k in range(1,10)]))


#2
A=Symbol('A')
B=Symbol('B')
C=Symbol('C')
D=Symbol('D')
E=Symbol('E')
F=Symbol('F')
G=Symbol('G')
H=Symbol('H')
I=Symbol('I')

# print(solve([A+B+C-2*I-F,D+E+F-A-C-I,G+H+I-2*E-B,A+I-8],A,B,C,D))

#3

# import time as t
# debut=t.time()
# ##### Préparation de l'affichage des solutions #####
# s="A={}, B={}, C={}, D={}, E={}, F={}, G={}, H={}, I={}"
# nbessais=nbsol=0
# for E in range(1,10):
#     for F in range(1,10):
#         for G in range(1,10):
#             for H in range(1,10):
#                 for I in range (1,10):
#                     nbessais+=1
#                     A=8-I
#                     B=-2*E+G+H+I
#                     C=2*E+F-G-H+2*I-8
#                     D=E-G-H+2*I
#                     if liste_correcte([A,B,C,D,E,F,G,H,I]):
#                         nbsol+=1
#                         print(s.format(A,B,C,D,E,F,G,H,I))
#                         print('{} solutions pour {} essais'.format(nbsol,nbessais))
#                         print(u"durée du calcul :", t.time()-debut)





#Exercice 4:

def palindrome(ch):
    n=len(ch)
    condition = True
    for k in range(0,n//2):
        condition = (condition and ch[k]==ch[-k-1])
    return condition


#Exercice 5:

#1
def valide(ch):
    alphabet="bdefhijklmnopqrsuvwxyz"
    condition=True
    for k in alphabet:
        condition = condition and (not (k in ch))
    return condition


#2
def saisie():
    ch="z"
    while not valide(ch):
        ch= input("Saisissez la chaine (elle est composée des lettre a,t,c et g) : ")
    return ch


#3
def proportion(ch,seq):
    occurence =0
    n_ch=len(ch)
    n_seq=len(seq)
    for k in range(n_ch):
        if ch[k:k+n_seq]==seq:
            occurence+=1
    return occurence, (n_seq*occurence)/n_ch



#Exercice 6:
#1
def fct_maj(char):
    alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if char in alphabet:
        return char
    else:
        return ord(0)


#2
def compte(s,c):
    occurence=0
    for k in s:
        if k==c:
            occurence+=1
    return occurence


#3

def nb_lettres(s):
    lst=[]
    alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for k in alphabet:
        lst.append(compte(s,k))
    return lst


#4

#En lançant la fonction nb_lettre, on a une boucle imbriquée dans une seconde. La première boucle promet 26 répétitions.
# La seconde en promet len(s) mais compte pour un parcourt de s. Au final, on aura 26 parcourt de s. 


#5
def nb_lettres2(s):
    alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lst=[0 for i in range(26)]
    n=len(alphabet)
    for k in s:
        for i in range(n):
            if alphabet[i] == k:
                lst[i]+=1
    return lst


#Exercice 7

#1


def mot_suivant(expression,i):
    n=len(expression)
    if i>=n:
        return "Error"
    else:
        k=i
        while k<n and expression[k]!=" ":
            k+=1
        mot=expression[i:k]
        while k<n and expression[k]==" ":
            k+=1
        return(mot,k)

expression="Etre ou ne pas être, telle est la question."


#2

def liste_mots(expression):
    lst=[]
    k=0
    m=expression
    n=len(expression)
    while k<n:
        (suivant,k)=mot_suivant(m,k)
        lst.append(suivant)
    return lst

# print(liste_mots(expression))


#3

def mot_suivant2(expression,i,s):
    n=len(expression)
    if i>=n:
        return "Error"
    else:
        k=i
        while k<n and expression[k]!=" "and (not (expression[k] in s)):
            k+=1
        mot=expression[i:k]
        while k<n and (expression[k]==" " or (expression[k] in s)):
            k+=1
        return(mot,k)


s=["'",",",";",".","?","!" ]



#Exercice 8:

#1
def Eratostene(N):
    L=[k for k in range(2,N+1)]
    while L!=[]:
        print(L[0])
        a=L[0]
        b=L[-1]
        for k in range(1,(b//a)+1):
            if a*k in L:
                L.remove(a*k)
    return 



#2
def Eratostene2(N):
    tour_boucle=0
    L=[k for k in range(2,N+1)]
    while L!=[]:
        print(L[0])
        a=L[0]
        b=L[-1]
        for k in range(1,(b//a)+1):
            if a*k in L:
                L.remove(a*k)
            tour_boucle+=1
    return tour_boucle






#3
# Cette algoritme semble être en au moins O(N^2) pas très performant donc...


#Exercice 9:
#1

def nombreZeros(t,i):
    s=0
    k=i
    while k<len(t) and t[k]==0 :
        s+=1
        k+=1
    return s


#2  
#Il faut prendre max_{i\in [\![0,n-1]\!]} nombreZeros(t,i).

def nombreZerosMax(t):
    i=0
    max=0
    n=len(t)
    while i < n:
        nbrzero=nombreZeros(t,i)
        if max < nbrzero:
            max= nbrzero
        i+=nbrzero+1
    return max


t=[0,1,1,1,0,0,0,1,0,1,1,0,0,0,0]



#Exercice 10:
#1
def positions_possibles(p,atteints):
        x=p[0]
        y=p[1]
        positions=[(x+1,y),(x-1,y),(x,y+1),(x,y-1)]
        position_possible=[]
        for k in positions:
            if not (k in atteints):
                position_possible.append(k)
        return position_possible


#2
#En n=7, on forme un presque carré puis on se rend en son centre: alors aucun chemin n'est possible. On a 8 chemins de ce type possibles.



#3
def genere_chemin_naif(n):
    etape=0
    atteints=[]
    position_possible=[[0,0]]
    while etape<=n and position_possible!=[]:
        atteints.append(random.choice(position_possible))
        etape+=1
        position_possible=positions_possibles(atteints[-1],atteints)
    if etape <=n:
        return None
    else:
        return atteints

# print(genere_chemin_naif(10))



#Exercice 11:
#1
#






#2





#Exercice 12:

#1

#Ce script utilise la méthode de monte carlo pour calculer la valeur de pi ici. On sélectionne d'abord une valeur pour l'erreur
# Elle ne doit pas être trop petite afin d'éviter les erreurs liés à la représentation des floats.
# Après initialisation de quelques valeurs, on pose une boucle conditionelle dans laquelle on tente d'approcher pi avec une erreur maximale e 
# que l'on a entré. Dans cette boucle, on prend deux nombres au hasard; si ils sont dans le cercle de rayon 0.5, alors on a +1 pour l'intérieur.
# Sinon, c'est +1 pour l'extérieur.
# Cela est pris en compte par resexp, qui se rapprochera de pi petit à petit.
# Ce script fini par retourner une valeur approchée de pi avec l'approximation telle que l'on a voulu en entrant l'erreur.


#2

#−*− coding: utf−8 −*−
#""" MonteCarlo version 1"""
from random import *
import numpy as np

def monte_carlo():
    pi=np.pi
    erreur =0
    while not (erreur>=1e-9):
        erreur=float(input(u"Entrer la précision desirée pour ce calcul ( e>1E−9): "))
    Nint=0
    N=0
    resexp=0
    while abs(pi-resexp) > erreur:
        x=random ()
        y=random ()
        z=random ()
        if np.sqrt((x-0.5)**2+(y-0.5)**2+(z-0.5)**2)<=0.5:
            Nint=Nint +1
            N=N+1
            resexp=(3*Nint)/(4*N*(0.5)**3)
        else:
            N=N+1
            resexp=(3*Nint)/(4*N*(0.5)**3)
        print(resexp)
    print(u"La valeur approchée recherchée est : " ) , resexp


#monte_carlo()




#Exercice 13:

def bon_formatage(A):
    if A[0]=="1" or A[0]=="2":
        K=97- int(A)%97
    else:
        return "Mauvais formatage"
    return K

A="1460245207352"

print(bon_formatage(A))



#Exercice 14:
#1
A="1234567890128"

def cle(A):
    s_pair=int(A[11])
    s_impaire=int(A[12])
    for k in range(1,6):
        s_pair+=int(A[2*k-1])
        s_impaire+=int(A[2*k])
    i=0
    while (((3*s_pair)+s_impaire)-i)%10!=0:
        i+=1
    cle=-i+10
    return cle

# print(cle(A))


#2

def verif_cle(A):
    s_pair=int(A[11])
    s_impaire=int(A[12])
    for k in range(1,6):
        s_pair+=int(A[2*k-1])
        s_impaire+=int(A[2*k])
    i=0
    while (((3*s_pair)+s_impaire)-i)%10!=0:
        i+=1
    cle=-i+10
    return cle==int(A[0])

# print(verif_cle(A))



#Exercice 15:

#1
def chaine_entier(ch):
    s=0
    n=len(ch)
    for k in range(n):
        s+= ord(ch[k])*(256**(n-k-1))
    return s


# print(chaine_entier("pouet"))



#2

def chaine_entier_Horner(ch):
    x=256
    s=ord(ch[0])
    n=len(ch)
    for k in range(1,n):
        s=s*x + ord(ch[k])
    return s


# print(chaine_entier_Horner("pouet"))


#3

def entier_chaine(n):
    ch=""
    while n >1:
        ai=n%256
        ch=str(chr(int(ai)))+ch
        n=(n-ai)/256
    return ch


# print(entier_chaine(482906301812))


#4
#a
def h(ch):
    x=256
    s=ord(ch[0])
    n=len(ch)
    for k in range(1,n):
        s=s*x + ord(ch[k])
    return s%255


print(h("pouet"))
print(h("chariot"))
print(h("haricot"))


#b
#Ces deux derniers cas forment ce qu'on appelle une collision. Ils ont un même haché pour une chaine de caractère différente.


#5
#Les mots chariot et haricot sont des anagrames. Comme 256**k=1[255], peu importe l'ordre dans lequel sont agencées les lettres. 

#6
def dico_valide(dict):
    L=[]
    condition=True
    for k in dict:
        if h(k) in L:
            condition=False
        L.append(h(k))
    return condition

dict={"Tintin": 25,"Haddock":55,"pouet":"trompette","chariot":234}



# print(dico_valide(dict))
