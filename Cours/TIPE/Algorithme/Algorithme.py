

### INTIALISATION DES VARIABLES ###

nb_bleu=int(input("Nombre de jetons bleus: "))

nb_vert=int(input("Nombre de jetons verts: "))

nb_rose=int(input("Nombre de jetons roses: "))

nb_jaune_serviette=int(input("Nombre de jetons jaunes: "))

nb_jaune_draps=int(input("Nombre de jetons jaunes: "))


# Le jeton vert est codé par 1.
# Le jeton jaune de type serviette est codé par 2.
# Le jeton jaune de type draps est codé par 3. 
# Le jeton rose est codé par 4.
# Le jeton bleu est codé par 5.

### Entrées :
presse=[0] # de taille 15 presse[0]=temps restant
essoreuse=[0] # de taille 14 essoreuse[0]=temps restant


### Intermédiaires :

Tapis_essoreuse=[] # de taille 2
Tapis_presse=[] # de taille 3
Stock_haut=[] # de taille 3
Stock_bas=[] # de taille 2

### Temps caractéristiques :

# Temps de transport 

temps_Tapis_Sortie_1=10
temps_Tapis_Sortie_2=30
temps_Tapis_Sortie_3=30
temps_Tapis_Sortie_4=30
temps_Tapis_Sortie_5=30
temps_Tapis_Sortie_6=120

temps_Tapis_Stock_bas=5
temps_Tapis_Stock_haut=10

temps_Stock_bas_Sortie_1=temps_Tapis_Sortie_1-temps_Tapis_Stock_bas
temps_Stock_bas_Sortie_2=temps_Tapis_Sortie_2-temps_Tapis_Stock_bas
temps_Stock_bas_Sortie_3=temps_Tapis_Sortie_3-temps_Tapis_Stock_bas
temps_Stock_bas_Sortie_4=temps_Tapis_Sortie_4-temps_Tapis_Stock_bas
temps_Stock_bas_Sortie_5=temps_Tapis_Sortie_5-temps_Tapis_Stock_bas
temps_Stock_bas_Sortie_6=temps_Tapis_Sortie_6-temps_Tapis_Stock_bas


temps_Stock_haut_Sortie_1=temps_Tapis_Sortie_1-temps_Tapis_Stock_haut
temps_Stock_haut_Sortie_2=temps_Tapis_Sortie_2-temps_Tapis_Stock_haut
temps_Stock_haut_Sortie_3=temps_Tapis_Sortie_3-temps_Tapis_Stock_haut
temps_Stock_haut_Sortie_4=temps_Tapis_Sortie_4-temps_Tapis_Stock_haut
temps_Stock_haut_Sortie_5=temps_Tapis_Sortie_5-temps_Tapis_Stock_haut
temps_Stock_haut_Sortie_6=temps_Tapis_Sortie_6-temps_Tapis_Stock_haut

# Temps en sortie des jetons :
temps_sortie_vert=120
temps_sortie_jaune_serviette=900
temps_sortie_jaune_drap=2400
temps_sortie_rose=900
temps_sortie_bleue=1


# Temps de passage :

temps_passage=300


### Sorties
Sortie_1=[0] # de taille 4 (jeton vert) Sortie_1[0]=temps restant
Sortie_2=[0] # de taille 4 (jeton jaune / rose) Sortie_2[0]=temps restant
Sortie_3=[0] # de taille 4 (jeton jaune / rose) Sortie_3[0]=temps restant
Sortie_4=[0] # de taille 4 (jeton jaune / rose) Sortie_4[0]=temps restant
Sortie_5=[0] # de taille 4 (jeton jaune / rose) Sortie_5[0]=temps restant
Sortie_6=[0] # de taille 4 (jeton bleu) Sortie_6[0]=temps restant


### Acteur de distribution :
Chariot=[] # de taille 2 Chariot[0]=etat


### Fin initialisation ###


### Distribution :



def remplissage_chariot():
    return None



def diminution_temps(n):
    """
    Entrée: nombre n correspondant au temps à faire diminuer à l'horloge de tous les éléments temporels

    ---------------------------------------

    Sortie: None, mais agit sur toutes les horloges des acteurs temporels.
    """
    def presse(n):
        if presse[0]<=n:
            if presse[0]==0:
                Tapis_presse.append(presse.pop(1))
                presse[0]=temps_passage
                return
            else:
                a=n-presse[0]
                Tapis_presse.append(presse.pop(1))
                presse[0]=temps_passage
                if a<=temps_passage:
                    presse[0]-=a
                    return
                else:
                    presse(a)
        else:
            presse[0]-=n
            return
    def essoreuse(n):
        if essoreuse[0]<=n:
            if essoreuse[0]==0:
                Tapis_essoreuse.append(essoreuse.pop(1))
                essoreuse[0]=temps_passage
                return
            else:
                a=n-essoreuse[0]
                Tapis_essoreuse.append(essoreuse.pop(1))
                essoreuse[0]=temps_passage
                if a<=temps_passage:
                    essoreuse[0]-=a
                    return
                else:
                    essoreuse(a)
        else:
            essoreuse[0]-=n
            return
    def Sortie_1(n):
        if Sortie_1[0]<=n:
            if Sortie_1[0]==0:
                Sortie_1.remove(1)
                Sortie_1[0]=temps_sortie_vert
                return
            else:
                a=n-Sortie_1[0]
                Sortie_1.remove(1)
                Sortie_1[0]=temps_sortie_vert
                if a<=temps_sortie_vert:
                    Sortie_1[0]-=a
                    return
                else:
                    Sortie_1(a)
        else:
            Sortie_1[0]-=n
            return  
    def Sortie_2(n):
        if Sortie_2[0]<=n:
            if Sortie_2[0]==0:
                Sortie_2.remove(1)
                Sortie_2[0]=temps_sechage(Sortie_2[1])
                return
            else:
                a=n-Sortie_2[0]
                Sortie_2.remove(1)
                Sortie_2[0]=temps_sechage(Sortie_2[1])
                if a<=temps_sechage(Sortie_2[1]):
                    Sortie_2[0]-=a
                    return
                else:
                    Sortie_2(a)
        else:
            Sortie_2[0]-=n
            return
    def Sortie_3(n):
        if Sortie_3[0]<=n:
            if Sortie_3[0]==0:
                Sortie_3.remove(1)
                Sortie_3[0]=temps_sechage(Sortie_3[1])
                return
            else:
                a=n-Sortie_3[0]
                Sortie_3.remove(1)
                Sortie_3[0]=temps_sechage(Sortie_3[1])
                if a<=temps_sechage(Sortie_3[1]):
                    Sortie_3[0]-=a
                    return
                else:
                    Sortie_3(a)
        else:
            Sortie_3[0]-=n
            return
    def Sortie_4(n):
        if Sortie_4[0]<=n:
            if Sortie_4[0]==0:
                Sortie_4.remove(1)
                Sortie_4[0]=temps_sechage(Sortie_4[1])
                return
            else:
                a=n-Sortie_4[0]
                Sortie_4.remove(1)
                Sortie_4[0]=temps_sechage(Sortie_4[1])
                if a<=temps_sechage(Sortie_4[1]):
                    Sortie_4[0]-=a
                    return
                else:
                    Sortie_4(a)
        else:
            Sortie_4[0]-=n
            return
    def Sortie_5(n):
        if Sortie_5[0]<=n:
            if Sortie_5[0]==0:
                Sortie_5.remove(1)
                Sortie_5[0]=temps_sechage(Sortie_5[1])
                return
            else:
                a=n-Sortie_5[0]
                Sortie_5.remove(1)
                Sortie_5[0]=temps_sechage(Sortie_5[1])
                if a<=temps_sechage(Sortie_5[1]):
                    Sortie_5[0]-=a
                    return
                else:
                    Sortie_5(a)
        else:
            Sortie_5[0]-=n
            return
    def Sortie_6(n):
        if Sortie_6[0]<=n:
            if Sortie_6[0]==0:
                Sortie_6.remove(1)
                Sortie_6[0]=temps_sortie_bleue
                return
            else:
                a=n-Sortie_6[0]
                Sortie_6.remove(1)
                Sortie_6[0]=temps_sortie_bleue
                if a<=temps_sortie_bleue:
                    Sortie_6[0]-=a
                    return
                else:
                    Sortie_6(a)
        else:
            Sortie_6[0]-=n
            return  
    presse(n)
    essoreuse(n)
    Sortie_1(n)
    Sortie_2(n)
    Sortie_3(n)
    Sortie_4(n)
    Sortie_5(n)
    Sortie_6(n)
    return



def temps_sechage(jeton):
    if jeton==1:
        return temps_sortie_vert
    elif jeton==2:
        return temps_sortie_jaune_serviette
    elif jeton==3:
        return temps_sortie_jaune_drap
    elif jeton==4:
        return temps_sortie_rose
    else:
        return temps_sortie_bleue



def temps_transport(etat):
    """
    Entrée: état du chariot

    ----------------------------------------------------

    Sortie: Renvoit la variation de temps nécessaire à aller de cet état à l'état "Tapis".
    """
    if etat=="Tapis":
        return 0
    elif etat=="Stock_bas":
        return temps_Tapis_Stock_bas
    elif etat=="Stock_haut":
        return temps_Tapis_Stock_haut
    elif etat=="Sortie_1":
        return temps_Tapis_Sortie_1
    elif etat=="Sortie_2":
        return temps_Tapis_Sortie_2
    elif etat=="Sortie_3":
        return temps_Tapis_Sortie_3
    elif etat=="Sortie_4":
        return temps_Tapis_Sortie_4
    elif etat=="Sortie_5":
        return temps_Tapis_Sortie_5        
    elif etat=="Sortie_6":
        return temps_Tapis_Sortie_6



def vidage_jeton_chariot(jeton,etat):
    """
    Entrée: jeton / etat du chariot

    ---------------------------------------------------

    Sortie: None

    Cette fonction permet:
    - de déplacer le chariot de l'endroit où il récupère le jeton vers l'endroit où il doit le poser (chose complètement déterministe)
    - de prendre en compte ce déplacement en terme de temps en faisant diminuer l'horloge de tous les éléments temporels (diminution_temps)
    - de poser le jeton dans la file correspondante bien sûre et finir par rendre le chariot vide. Générant une erreur "problème de temps" si toutes les files
    de sorties sont pleines.
    """
    if jeton==1: # jeton vert
        if len(Sortie_1)==4: # Si la file verte est pleine
            print("probleme de temps") # Cas du problème
        else: # Si il y a de la place
            diminution_temps(temps_Tapis_Sortie_1-temps_transport(etat)) # Diminution du temps
            Sortie_1.append(jeton)  # Ajout du jeton dans la file sortie verte
            Chariot[0]=Sortie_1  # Reset de l'état du chariot (il est à la sortie verte)
    if jeton==2 or jeton==3 or jeton==4: # jeton jaune type serviette ou couette ou rose  
        if len(Sortie_2)==4: # Si la file jaune / rose numéro 2 est pleine
            if len(Sortie_3)==4: # Si la file jaune / rose numéro 3 est pleine
                if len(Sortie_4)==4: # Si la file jaune / rose numéro 4 est pleine 
                    print("probleme de temps") # Cas du problème
                else: # Si il y a de la place
                    diminution_temps(temps_Tapis_Sortie_4-temps_transport(etat)) # Diminution du temps
                    Sortie_4.append(jeton)  # Ajout du jeton dans la file sortie jaune / rose numéro 4
                    Chariot[0]=Sortie_4  # Reset de l'état du chariot (il est à la sortie jaune / rose numéro 4)
            else: # Si il y a de la place
                diminution_temps(temps_Tapis_Sortie_3-temps_transport(etat)) # Diminution du temps
                Sortie_3.append(jeton)  # Ajout du jeton dans la file sortie jaune / rose numéro 3
                Chariot[0]=Sortie_3  # Reset de l'état du chariot (il est à la sortie jaune / rose numéro 3)
        else: # Si il y a de la place
            diminution_temps(temps_Tapis_Sortie_2-temps_transport(etat)) # Diminution du temps
            Sortie_2.append(jeton) # Ajout du jeton dans la file sortie jaune / rose numéro 2
            Chariot[0]=Sortie_2 # Reset de l'état du chariot (il est à la sortie jaune / rose numéro 2)
    else: # jeton bleu
        if len(Sortie_6)==4: # Si la file bleue est pleine
            print("probleme de temps") # Cas du problème
        else: # Si il y a de la place
            diminution_temps(temps_Tapis_Sortie_6-temps_transport(etat)) # Diminution du temps
            Sortie_6.append(jeton) # Ajout du jeton dans la file sortie bleue
            Chariot[0]=Sortie_6 # Reset de l'état du chariot (il est à la sortie bleue)
    Chariot.pop(1) # Suppression du jeton considéré dans le chariot ################################POSSIBLEMENT A ENLEVER 
    return



def retour_chariot(etat):
    return







# Glouton sur 5 générations glissantes






