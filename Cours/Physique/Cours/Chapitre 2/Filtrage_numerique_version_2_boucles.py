# -*- coding: utf-8 -*-
from math import *
import numpy as np
import matplotlib.pyplot as plt

#ouverture du fichier de donnees source
mesdonnees=open('Donnees_formatees_CSV.csv','r')

#Donnees numeriques 
Te=0.00001 #Période d'échantillonnage
wc=2*np.pi*200.0 #Pulsation de coupure des passe-bas et passe-haut


#Dimensionnement des tableaux vierges pour signal entree pour enregistrement de 4096 donnees
t=np.zeros(4096)
e=np.zeros(4096)

#Lecture en-tete du fichier de donnees
entete=mesdonnees.readline().rstrip('\n\r').split(',')


#Initialisation d'un compteur et du max d'échelle graphique
k,max=(0,0)

#Boucle de construction de e par lecture du fichier source
for Ligne in mesdonnees:
    tL,eL=Ligne.rstrip('\n\r').split(",") #Lit la ligne, supprime espace 
#et retour chariot, coupe a la virgule et stocke le temps et la valeur signal  
    t[k]=float(tL) # affectation de la kième valeur du temps
    e[k]=float(eL) # affectation de la kième valeur du signal
    if e[k]>max:
        max=1.05*e[k] #Max est une variable d'ajustement automatique de l'echelle pour le trace ultérieurement
    k+=1
    
    
#Fermeture du fichier source   
mesdonnees.close()



#Dimensionnement des tableaux vierges pour signal sortie pour enregistrement 4096 donnees
spb1=np.zeros(4096)
sph1=np.zeros(4096)


#ouverture des fichiers de donnees sortie
masortie_PB1=open('Donnee_sortie_PB1_CSV.csv','w')
masortie_PH1=open('Donnee_sortie_PH1_CSV.csv','w')

#Ecriture des signaux de sortie des filtres par récurrence
for k in range(4095):
        spb1[k+1]=((2-wc*Te)/(2+wc*Te))*spb1[k]+((wc*Te)/(2+wc*Te))*(e[k]+e[k+1]) #récurrence du passe-bas
        sph1[k+1]=((2-wc*Te)/(2+wc*Te))*sph1[k]+(2/(2+wc*Te))*(e[k+1]-e[k])  #récurrence du passe-haut
        masortie_PB1.write(str(t[k])+','+str(spb1[k])+'\n') #Ecriture de ligne dans le fichier de sortie Passe bas1 après conversion en chaine de caractere
        masortie_PH1.write(str(t[k])+','+str(sph1[k])+'\n') #Ecriture de ligne dans le fichier de sortie passe haut1 après conversion en chaine de caractere


#Fermeture des fichiers de sortie passe-bas1 et passe-haut1
masortie_PB1.close()
masortie_PH1.close()


#Trace evolution des tensions entree et sortie
plt.grid()
plt.xlabel(r'$t\ (en\ s)$', fontsize=10)
plt.ylabel(r'$s(t)\ (en\ V)$', fontsize=10, rotation=90)
plt.title(r"Tension de sortie du filtre",size=20)
plt.axis([t[2048],t[4095],-max,max])
#plt.legend()
#entree=plt.plot(t,e)
sortie_PB1=plt.plot(t,spb1)
#sortie_PH1=plt.plot(t,sph1)
plt.show()