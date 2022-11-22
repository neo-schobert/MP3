import itertools
import random
from tkinter import * 
import copy
import functools
import time
from tkinter.ttk import Progressbar

### INTIALISATION DES VARIABLES ###

# nb_bleu=int(input("Nombre de jetons bleus: "))

# nb_vert=int(input("Nombre de jetons verts: "))

# nb_rose=int(input("Nombre de jetons roses: "))

# nb_jaune_serviette=int(input("Nombre de jetons jaunes: "))

# nb_jaune_draps=int(input("Nombre de jetons jaunes: "))


# Le jeton vert est codé par 1.
# Le jeton jaune de type serviette est codé par 2.
# Le jeton jaune de type draps est codé par 3. 
# Le jeton rose est codé par 4.
# Le jeton bleu est codé par 5.



### Intermédiaires :

Stock_haut=[] # de taille 3
Stock_bas=[] # de taille 2
Tapis_presse=[]
Tapis_essoreuse=[]

### Temps caractéristiques :

# Temps de transport 

Temps_essoreuse_Sortie_vert=20
temps_essoreuse_Sortie_jaune_rose_1=24
temps_essoreuse_Sortie_jaune_rose_2=26
temps_essoreuse_Sortie_jaune_rose_3=28
temps_essoreuse_Sortie_jaune_rose_4=30
temps_essoreuse_Sortie_bleu=34

temps_essoreuse_Stock_bas=14
temps_essoreuse_Stock_haut=17
temps_essoreuse_presse=10


Temps_presse_Sortie_vert=22
temps_presse_Sortie_jaune_rose_1=23
temps_presse_Sortie_jaune_rose_2=25
temps_presse_Sortie_jaune_rose_3=27
temps_presse_Sortie_jaune_rose_4=29
temps_presse_Sortie_bleu=33

temps_presse_Stock_bas=16
temps_presse_Stock_haut=19



# Temps en sortie des jetons :
temps_sortie_vert=300
temps_sortie_jaune_serviette=900
temps_sortie_jaune_drap=2400
temps_sortie_rose=900
temps_sortie_bleue=34


# Temps de passage :

temps_passage=300


### Sorties
Sortie_1=[0] # de taille 3 (jeton vert) Sortie_1[0]=temps restant
Sortie_2=[0] # de taille 4 (jeton jaune / rose) Sortie_2[0]=temps restant
Sortie_3=[0] # de taille 4 (jeton jaune / rose) Sortie_3[0]=temps restant
Sortie_4=[0] # de taille 4 (jeton jaune / rose) Sortie_4[0]=temps restant
Sortie_5=[0] # de taille 4 (jeton jaune / rose) Sortie_5[0]=temps restant
Sortie_6=[0] # de taille 4 (jeton bleu) Sortie_6[0]=temps restant


# Liste des états:
# presse
# essoreuse
# Stock_bas
# Stock_haut
# Sortie_1
# Sortie_2
# Sortie_3
# Sortie_4
# Sortie_5
# Sortie_6

etat_chariot="essoreuse"

### Fin initialisation ###


### Création des listes essoreuses et presse 

essoreuse=[0] # de taille au moins 1 (diminue à chaque cycle)
presse=[0] # de taill au moins 1 (diminue à chaque cycle)
attente_essoreuse = 0
attente_presse = 0



temps_bouchon = 0



def distribution_temps(k):   # Valide 3.9 compatible
    """
    Entrée : k une liste de sortie.

    ---------------------------------------------------

    Sortie : Retourne 0 si k est vide ou ne contient qu'un élément. Retourne le temps associé au prochain jeton de la liste sinon.
    """
    if len(k)>1:
        # match k[1]:
        #     case 1:
        #         return temps_sortie_vert
        #     case 2:
        #         return temps_sortie_jaune_serviette
        #     case 3:
        #         return temps_sortie_jaune_drap
        #     case 4:
        #         return temps_sortie_rose
        #     case 5:
        #         return temps_sortie_bleue
        if k[1] == 1:
            return temps_sortie_vert
        elif k[1] == 2:
            return temps_sortie_jaune_serviette
        elif k[1] == 3:
            return temps_sortie_jaune_drap
        elif k[1] == 4:
            return temps_sortie_rose
        elif k[1] == 5:
            return temps_sortie_bleue
    else:
        return 0


def distribution_temps_presse_essoreuse(k): # Valide 3.9 compatible
    """
    Agit de la même manière que distribution_temps(k) mais pour k = presse ou k = essoreuse.
    """
    if len(k)>1:
        return temps_passage
    else:
        return 0




def diminution_temps(n,k):  # Valide 3.9 compatible
    """
    Applique une diminution de temps n sur la composante temporelle k.
    """
    global Sortie_1
    global Sortie_2
    global Sortie_3
    global Sortie_4
    global Sortie_5
    global Sortie_6
    global essoreuse
    global presse
    global Tapis_presse
    global Tapis_essoreuse
    global Stock_bas
    global Stock_haut
    if len(k)>1:
        # match k[0]:
        #     case x if x>n:
        #         k[0]-=n
        #     case x if x==n:
        #         k.pop(1)
        #         k[0]=distribution_temps(k)
        #     case x:
        #         k.pop(1)
        #         k[0]=distribution_temps(k)
        #         diminution_temps(n-x,k)
        if k[0] > n:
            k[0]-=n
        elif k[0] == n:
            k.pop(1)
            k[0]=distribution_temps(k)
        else:
            k.pop(1)
            k[0]=distribution_temps(k)
            diminution_temps(n-k[0],k)    
    else:
        k[0]=0



def diminution_temps_essoreuse(n,k):  # Valide 3.9 compatible
    """
    Applique une diminution de temps n sur la composante temporelle k.
    """
    global Sortie_1
    global Sortie_2
    global Sortie_3
    global Sortie_4
    global Sortie_5
    global Sortie_6
    global essoreuse
    global presse
    global Tapis_presse
    global Tapis_essoreuse
    global Stock_bas
    global Stock_haut
    global attente_essoreuse
    if len(k)>1:
        # match k[0]:
        #     case x if x>n:
        #         k[0]-=n
        #     case x if x==n:
        #         if len(Tapis_essoreuse)<2:
        #             Tapis_essoreuse.insert(-1,essoreuse.pop(1))
        #             k[0] = distribution_temps_presse_essoreuse(k)
        #         else:
        #             k[0] = 0
        #     case x:
        #         if len(Tapis_essoreuse)<2:
        #             Tapis_essoreuse.insert(-1,essoreuse.pop(1))
        #             k[0]=distribution_temps_presse_essoreuse(k)
        #             diminution_temps_essoreuse(n-x,k)
        #         else:
        #             k[0]=0
        #             attente_essoreuse += n-x
        if k[0] > n:
            k[0] -= n
        elif k[0] == n:
            if len(Tapis_essoreuse)<2:
                Tapis_essoreuse.insert(-1,essoreuse.pop(1))
                k[0] = distribution_temps_presse_essoreuse(k)
            else:
                k[0] = 0
        else:
            if len(Tapis_essoreuse)<2:
                Tapis_essoreuse.insert(-1,essoreuse.pop(1))
                k[0]=distribution_temps_presse_essoreuse(k)
                diminution_temps_essoreuse(n-k[0],k)
            else:
                k[0]=0
                attente_essoreuse += n-k[0]
    else:
        attente_essoreuse += n





def diminution_temps_presse(n,k):  # Valide 3.9 compatible
    """
    Applique une diminution de temps n sur la composante temporelle k.
    """
    global Sortie_1
    global Sortie_2
    global Sortie_3
    global Sortie_4
    global Sortie_5
    global Sortie_6
    global essoreuse
    global presse
    global Tapis_presse
    global Tapis_essoreuse
    global Stock_bas
    global Stock_haut
    global attente_presse
    if len(k)>1:
        # match k[0]:
        #     case x if x>n:
        #         k[0]-=n
        #     case x if x==n:
        #         if len(Tapis_presse)<3:
        #             Tapis_presse.insert(-1,presse.pop(1))
        #             k[0] = distribution_temps_presse_essoreuse(k)
        #         else:
        #             k[0] = 0
        #     case x:
        #         if len(Tapis_presse)<3:
        #             Tapis_presse.insert(-1,presse.pop(1))
        #             k[0]=distribution_temps_presse_essoreuse(k)
        #             diminution_temps_presse(n-x,k)
        #         else:
        #             k[0]=0
        #             attente_presse += n-x
        if k[0] > n:
            k[0] -= n
        elif k[0] == n:
            if len(Tapis_presse)<3:
                Tapis_presse.insert(-1,presse.pop(1))
                k[0] = distribution_temps_presse_essoreuse(k)
            else:
                k[0] = 0
        else:
            if len(Tapis_presse)<3:
                Tapis_presse.insert(-1,presse.pop(1))
                k[0]=distribution_temps_presse_essoreuse(k)
                diminution_temps_presse(n-k[0],k)
            else:
                k[0]=0
                attente_presse += n-k[0]
    else:
        attente_presse += n






def diminution_temps_all(n):  # Valide 3.9 compatible
    """
    Applique la fonction diminution_temps sur chacune des composante temporelle de notre modélisation.
    """
    global Sortie_1
    global Sortie_2
    global Sortie_3
    global Sortie_4
    global Sortie_5
    global Sortie_6
    global essoreuse
    global presse
    global Tapis_presse
    global Tapis_essoreuse
    global Stock_bas
    global Stock_haut
    global temps_global
    global temps_rechargement
    global Sortie_1_end
    global Sortie_2_end
    global Sortie_3_end
    global Sortie_4_end
    global Sortie_5_end
    global Sortie_6_end
    global essoreuse_end
    global presse_end
    global Stock_bas_end
    global Stock_haut_end
    global Tapis_presse_end
    global Tapis_essoreuse_end
    if temps_rechargement>n:
        temps_rechargement-=n
        temps_global += n
        for k in [Sortie_1,Sortie_2,Sortie_3,Sortie_4,Sortie_5,Sortie_6]:
            diminution_temps(n,k)
        diminution_temps_presse(n, presse)
        diminution_temps_essoreuse(n, essoreuse)
    elif temps_rechargement == 0:
        temps_global += n
        for k in [Sortie_1,Sortie_2,Sortie_3,Sortie_4,Sortie_5,Sortie_6]:
            diminution_temps(n,k)
        diminution_temps_presse(n, presse)
        diminution_temps_essoreuse(n, essoreuse)
    elif temps_rechargement <= n:
        temps_global += n
        for k in [Sortie_1,Sortie_2,Sortie_3,Sortie_4,Sortie_5,Sortie_6]:
            diminution_temps(temps_rechargement,k)
        diminution_temps_presse(temps_rechargement, presse)
        diminution_temps_essoreuse(temps_rechargement, essoreuse)
        Sortie_1_end=copy.deepcopy(Sortie_1)
        Sortie_2_end=copy.deepcopy(Sortie_2)
        Sortie_3_end=copy.deepcopy(Sortie_3)
        Sortie_4_end=copy.deepcopy(Sortie_4)
        Sortie_5_end=copy.deepcopy(Sortie_5)
        Sortie_6_end=copy.deepcopy(Sortie_6)
        essoreuse_end=copy.deepcopy(essoreuse)
        presse_end=copy.deepcopy(presse)
        Stock_bas_end=copy.deepcopy(Stock_bas)
        Stock_haut_end=copy.deepcopy(Stock_haut)
        Tapis_presse_end=copy.deepcopy(Tapis_presse)
        Tapis_essoreuse_end=copy.deepcopy(Tapis_essoreuse)
        for k in [Sortie_1,Sortie_2,Sortie_3,Sortie_4,Sortie_5,Sortie_6]:
            diminution_temps(n-temps_rechargement,k)
        diminution_temps_presse(n-temps_rechargement, presse)
        diminution_temps_essoreuse(n-temps_rechargement, essoreuse)
        temps_rechargement = 0
    return




def temps_transport(etat,direction): # Valide 3.9 compatible
    """
    Entrée: état du chariot, direction du chariot (essoreuse / presse / Stock_bas / Stock_haut)

    ----------------------------------------------------

    Sortie: Renvoit la variation de temps nécessaire à aller de cet état à l'état "essoreuse".
    """
    # match direction:
    #     case "essoreuse":
    #         match etat:
    #             case "essoreuse":
    #                 return 0
    #             case "presse":
    #                 return temps_essoreuse_presse
    #             case "Stock_bas":
    #                 return temps_essoreuse_Stock_bas
    #             case "Stock_haut":
    #                 return temps_essoreuse_Stock_haut
    #             case "Sortie_1":
    #                 return Temps_essoreuse_Sortie_vert
    #             case "Sortie_2":
    #                 return temps_essoreuse_Sortie_jaune_rose_1
    #             case "Sortie_3":
    #                 return temps_essoreuse_Sortie_jaune_rose_2
    #             case "Sortie_4":
    #                 return temps_essoreuse_Sortie_jaune_rose_3
    #             case "Sortie_5":
    #                 return temps_essoreuse_Sortie_jaune_rose_4
    #             case "Sortie_6":
    #                 return temps_essoreuse_Sortie_bleu
    #     case "presse":
    #         match etat:
    #             case "presse":
    #                 return 0
    #             case "essoreuse":
    #                 return temps_essoreuse_presse
    #             case "Stock_bas":
    #                 return temps_presse_Stock_bas
    #             case "Stock_haut":
    #                 return temps_presse_Stock_haut
    #             case "Sortie_1":
    #                 return Temps_presse_Sortie_vert
    #             case "Sortie_2":
    #                 return temps_presse_Sortie_jaune_rose_1
    #             case "Sortie_3":
    #                 return temps_presse_Sortie_jaune_rose_2
    #             case "Sortie_4":
    #                 return temps_presse_Sortie_jaune_rose_3
    #             case "Sortie_5":
    #                 return temps_presse_Sortie_jaune_rose_4
    #             case "Sortie_6":
    #                 return temps_presse_Sortie_bleu
    #     case "Stock_bas":
    #         match etat:
    #             case "presse":
    #                 return temps_presse_Stock_bas
    #             case "essoreuse":
    #                 return temps_essoreuse_Stock_bas
    #             case x:
    #                 return (temps_transport(etat, "essoreuse") - 5)
    #     case "Stock_haut": 
    #         match etat:
    #             case "presse":
    #                 return temps_presse_Stock_haut
    #             case "essoreuse":
    #                 return temps_essoreuse_Stock_haut
    #             case x:
    #                 return (temps_transport(etat, "essoreuse") - 8)
    if direction =="essoreuse":
        if etat == "essoreuse":
            return 0
        elif etat == "presse":
            return temps_essoreuse_presse
        elif etat == "Stock_bas":
            return temps_essoreuse_Stock_bas
        elif etat == "Stock_haut":
            return temps_essoreuse_Stock_haut
        elif etat == "Sortie_1":
            return Temps_essoreuse_Sortie_vert
        elif etat == "Sortie_2":
            return temps_essoreuse_Sortie_jaune_rose_1
        elif etat == "Sortie_3":
            return temps_essoreuse_Sortie_jaune_rose_2
        elif etat == "Sortie_4":
            return temps_essoreuse_Sortie_jaune_rose_3
        elif etat == "Sortie_5":
            return temps_essoreuse_Sortie_jaune_rose_4
        elif etat == "Sortie_6":
            return temps_essoreuse_Sortie_bleu
    elif direction == "presse":
        if etat == "presse":
            return 0
        elif etat == "essoreuse":
            return temps_essoreuse_presse
        elif etat == "Stock_bas":
            return temps_presse_Stock_bas
        elif etat == "Stock_haut":
            return temps_presse_Stock_haut
        elif etat == "Sortie_1":
            return Temps_presse_Sortie_vert
        elif etat == "Sortie_2":
            return temps_presse_Sortie_jaune_rose_1
        elif etat == "Sortie_3":
            return temps_presse_Sortie_jaune_rose_2
        elif etat == "Sortie_4":
            return temps_presse_Sortie_jaune_rose_3
        elif etat == "Sortie_5":
            return temps_presse_Sortie_jaune_rose_4
        elif etat == "Sortie_6":
            return temps_presse_Sortie_bleu
    elif direction == "Stock_bas":
        if etat == "presse":
            return temps_presse_Stock_bas
        elif etat == "essoreuse":
            return temps_essoreuse_Stock_bas
        else:
            return (temps_transport(etat, "essoreuse") - 5)
    elif direction == "Stock_haut": 
        if etat == "presse":
            return temps_presse_Stock_haut
        elif etat == "essoreuse":
            return temps_essoreuse_Stock_haut
        else:
            return (temps_transport(etat, "essoreuse") - 8)



def premier_element_non_temp(L):  # Valide 3.9 compatible
    """
    On entend ici par premier élément le premier élément de la liste (pas de composante temporelle).


    Retourne 0 si la liste L est de taille 1 et le premier élément de L sinon.
    """
    if len(L)==0:
        return 0
    else:
        return L[0]



def premier_element_temp(L): # Valide 3.9 compatible
    """
    On entend ici par premier élément le premier élément n'étant pas un temps.


    Retourne 0 si la liste L est de taille 1 et le premier élément de L sinon.
    """
    if len(L)<=1:
        return 0
    else:
        return L[1]



def places_libres():  # Valide 3.9 compatible
    """
    Retourne la liste des Sortie qui ont une place libre.
    """
    global Sortie_1
    global Sortie_2
    global Sortie_3
    global Sortie_4
    global Sortie_5
    global Sortie_6
    global essoreuse
    global presse
    global Tapis_presse
    global Tapis_essoreuse
    global Stock_bas
    global Stock_haut
    libres=[]
    if len(Sortie_1)<3:
        libres.append("Sortie_1")
    if len(Sortie_2)<4:
        libres.append("Sortie_2")
    if len(Sortie_3)<4:
        libres.append("Sortie_3")
    if len(Sortie_4)<4:
        libres.append("Sortie_4")
    if len(Sortie_5)<4:
        libres.append("Sortie_5")
    if len(Sortie_6)<4:
        libres.append("Sortie_6")
    if len(Stock_bas)<4:
        libres.append("Stock_bas")
    if len(Stock_haut)<4:
        libres.append("Stock_haut")
    return libres





def etat(k): # Valide 3.9 compatible
    """
    Décodage simple d'un nombre k comme ci-dessous.
    """
    # match k:
    #     case 0:
    #         return "essoreuse"
    #     case 1:
    #         return "presse"
    #     case 2:
    #         return "Stock_bas"
    #     case 3:
    #         return "Stock_haut"
    if k == 0:
        return "essoreuse"
    elif k == 1:
        return "presse"
    elif k == 2:
        return "Stock_bas"
    elif k == 3:
        return "Stock_haut"





def sortie_ordonnee():  # Valide 3.9 compatible
    """
    
    Sortie : Renvoie la liste des string "Sortie_2","Sortie_3","Sortie_4","Sortie_5" triés selon la longueur des listes Sortie_2, Sortie_3, Sortie_4, sortie_5.
    """
    global Sortie_1
    global Sortie_2
    global Sortie_3
    global Sortie_4
    global Sortie_5
    global Sortie_6
    global essoreuse
    global presse
    global Tapis_presse
    global Tapis_essoreuse
    global Stock_bas
    global Stock_haut
    L=[len(k) for k in [Sortie_2,Sortie_3,Sortie_4,Sortie_5]]
    L_trie = ["Sortie_" + k for k in ["2","3","4","5"]]
    for i in range(1, len(L)): 
        k = L[i] 
        k_trie = L_trie[i]
        j = i-1
        while j >= 0 and k < L[j] : 
                L[j + 1] = L[j] 
                L_trie[j+1] = L_trie[j]
                j -= 1
        L[j + 1] = k
        L_trie[j+1] = k_trie
    return L_trie



def decodage(k):  # Valide 3.9 compatible
    global Sortie_1
    global Sortie_2
    global Sortie_3
    global Sortie_4
    global Sortie_5
    global Sortie_6
    global essoreuse
    global presse
    global Tapis_presse
    global Tapis_essoreuse
    global Stock_bas
    global Stock_haut
    # match k:
    #     case "Sortie_1":
    #         return Sortie_1
    #     case "Sortie_2":
    #         return Sortie_2
    #     case "Sortie_3":
    #         return Sortie_3
    #     case "Sortie_4":
    #         return Sortie_4
    #     case "Sortie_5":
    #         return Sortie_5
    #     case "Sortie_6":
    #         return Sortie_6
    #     case "Stock_bas":
    #         return Stock_bas
    #     case "Stock_haut":
    #         return Stock_haut
    if k == "Sortie_1":
        return Sortie_1
    elif k == "Sortie_2":
        return Sortie_2
    elif k == "Sortie_3":
        return Sortie_3
    elif k == "Sortie_4":
        return Sortie_4
    elif k == "Sortie_5":
        return Sortie_5
    elif k == "Sortie_6":
        return Sortie_6
    elif k == "Stock_bas":
        return Stock_bas
    elif k == "Stock_haut":
        return Stock_haut




def actualisation(etat_chariot):  # Valide 3.9 compatible
    """
    Entrée : On entre l'etat actuel du chariot

    ----------------------------------------

    Sortie : On sort l'etat actuel du chariot ainsi que la direction qu'il doit prendre pour le remplissage. et la direction pour le remplissage ("essoreuse" si aucune place n'est libre)
    """
    global Sortie_1
    global Sortie_2
    global Sortie_3
    global Sortie_4
    global Sortie_5
    global Sortie_6
    global essoreuse
    global presse
    global Tapis_presse
    global Tapis_essoreuse
    global Stock_bas
    global Stock_haut
    global temps_bouchon
    successeurs=[premier_element_non_temp(Tapis_essoreuse),premier_element_non_temp(Tapis_presse),premier_element_non_temp(Stock_bas),premier_element_non_temp(Stock_haut)]
    libres=places_libres()
    cond=True
    k=0
    direction = "essoreuse"
    while cond and k<4:
        # match successeurs[k]:
        #     case 0:
        #         k+=1
        #     case 1:
        #         if "Sortie_1" in libres:
        #             cond=False
        #             direction = "Sortie_1"
        #         else:
        #             k+=1
        #     case 2|3|4:
        #         for i in sortie_ordonnee():
        #             if i in libres:
        #                 cond = False
        #                 direction = i
        #                 break
        #         if cond == True:
        #             k+=1
        #     case 5:
        #         if "Sortie_6" in libres:
        #             cond=False
        #             direction = "Sortie_6"
        #         else:
        #             k+=1
        if successeurs[k] == 0:
            k+=1
        elif successeurs[k] == 1:
            if "Sortie_1" in libres:
                cond=False
                direction = "Sortie_1"
            else:
                k+=1
        elif successeurs[k] == 2 or successeurs[k] == 3 or successeurs[k] == 4:
            for i in sortie_ordonnee():
                if i in libres:
                    cond = False
                    direction = i
                    break
            if cond == True:
                k+=1
        elif successeurs[k] == 5:
            if "Sortie_6" in libres:
                cond=False
                direction = "Sortie_6"
            else:
                k+=1
    if k<4:
        return etat_chariot,etat(k),direction
    else:
        if etat_chariot != "essoreuse":
            diminution_temps_all(temps_transport(etat_chariot,"essoreuse"))
            etat_chariot = "essoreuse"
            return actualisation(etat_chariot)
        if Tapis_essoreuse!= []:
            if "Stock_bas" in libres:
                return etat_chariot,"essoreuse","Stock_bas"
            elif "Stock_haut" in libres:
                return etat_chariot,"essoreuse","Stock_haut"
        if Tapis_presse!= []:
            if "Stock_bas" in libres:
                return etat_chariot,"presse","Stock_bas"
            elif "Stock_haut" in libres:
                return etat_chariot,"presse","Stock_haut"
        attente_mini = Sortie_1[0] + Sortie_2[0] + Sortie_3[0] + Sortie_4[0] + Sortie_5[0] + Sortie_6[0] + essoreuse[0] + presse[0]
        if attente_mini == 0 and len(presse) == 1 and len(essoreuse) == 1 and Stock_bas == [] and Stock_haut == [] and Tapis_presse == [] and Tapis_essoreuse == []:
            return "fin","fin","fin"
        else:
            lst = [Sortie_1,Sortie_2,Sortie_3,Sortie_4,Sortie_5,Sortie_6,essoreuse,presse]
            for k in range(8):
                if lst[k][0] <= attente_mini and lst[k][0]!= 0:
                    attente_mini = lst[k][0]
                    # match k:
                    #     case k if k<6:
                    #         direction = "Sortie_" + str(k+1)
                    #     case k if k == 6:
                    #         direction = "essoreuse"
                    #     case k if k == 7:
                    #         direction = "presse"
                    if k < 6:
                        direction = "Sortie_" + str(k+1)
                    elif k == 6:
                        direction = "essoreuse"
                    elif k == 7:
                        direction = "presse"
            if len(Tapis_presse)!=0 or len(Tapis_essoreuse)!=0:
                temps_bouchon += attente_mini
            diminution_temps_all(attente_mini)
            # match direction:
            #     case "Sortie_1":
            #         cond = False
            #         i = 0
            #         while not cond and i < 4 :
            #             if successeurs[i]==1:
            #                cond = True
            #             i += 1 
            #         if cond:
            #             return etat_chariot,etat(i-1),direction
            #     case "Sortie_2" | "Sortie_3" | "Sortie_4" | "Sortie_5":
            #         cond = False
            #         i = 0
            #         while not cond and i < 4 :
            #             if successeurs[i]==2 or successeurs[i]==3 or successeurs[i]==4:
            #                cond = True
            #             i += 1 
            #         if cond:
            #             return etat_chariot,etat(i-1),direction
            #     case "Sortie_6":
            #         cond = False
            #         i = 0
            #         while not cond and i < 4 :
            #             if successeurs[i]==5:
            #                cond = True
            #             i += 1 
            #         if cond:
            #             return etat_chariot,etat(i-1),direction
            if direction == "Sortie_1":
                cond = False
                i = 0
                while not cond and i < 4 :
                    if successeurs[i]==1:
                       cond = True
                    i += 1 
                if cond:
                    return etat_chariot,etat(i-1),direction
            elif direction == "Sortie_2" or direction == "Sortie_3" or direction == "Sortie_4" or direction == "Sortie_5":
                cond = False
                i = 0
                while not cond and i < 4 :
                    if successeurs[i]==2 or successeurs[i]==3 or successeurs[i]==4:
                       cond = True
                    i += 1 
                if cond:
                    return etat_chariot,etat(i-1),direction
            elif direction == "Sortie_6":
                cond = False
                i = 0
                while not cond and i < 4 :
                    if successeurs[i]==5:
                       cond = True
                    i += 1 
                if cond:
                    return etat_chariot,etat(i-1),direction
            return actualisation(etat_chariot)




def remplissage_vidage(etat_chariot,direction,direction_2):  # Valide 3.9 compatible
    """
    Entrée : On entre l'etat actuel du chariot, sa direction pour récupérer le pion et la direction qu'il doit enmprunter pour déposer le prochain jeton.

    ------------------------------------------

    Sortie : Retourne le nouvel état du chariot après dépot du jeton.

    """
    global Sortie_1
    global Sortie_2
    global Sortie_3
    global Sortie_4
    global Sortie_5
    global Sortie_6
    global essoreuse
    global presse
    global Tapis_presse
    global Tapis_essoreuse
    global Stock_bas
    global Stock_haut
    diminution_temps_all(temps_transport(etat_chariot,direction) + temps_transport(direction_2,direction))
    # match direction:
    #     case "essoreuse":
    #         prochain_jeton=Tapis_essoreuse.pop(0)
    #     case "presse":
    #         prochain_jeton=Tapis_presse.pop(0)
    #     case "Stock_bas":
    #         prochain_jeton=Stock_bas.pop(0)
    #     case "Stock_haut":
    #         prochain_jeton=Stock_haut.pop(0)
    if direction == "essoreuse":
        prochain_jeton=Tapis_essoreuse.pop(0)
    elif direction == "presse":
        prochain_jeton=Tapis_presse.pop(0)
    elif direction == "Stock_bas":
        prochain_jeton=Stock_bas.pop(0)
    elif direction == "Stock_haut":
        prochain_jeton=Stock_haut.pop(0)
    etat_chariot = direction_2
    # match direction_2:
    #     case "Sortie_1":
    #         Sortie_1.append(prochain_jeton)
    #         if Sortie_1[0] == 0:
    #             Sortie_1[0] = distribution_temps(Sortie_1)
    #     case "Sortie_2":
    #         Sortie_2.append(prochain_jeton)
    #         if Sortie_2[0] == 0:
    #             Sortie_2[0] = distribution_temps(Sortie_2)
    #     case "Sortie_3":
    #         Sortie_3.append(prochain_jeton)
    #         if Sortie_3[0] == 0:
    #             Sortie_3[0] = distribution_temps(Sortie_3)
    #     case "Sortie_4":
    #         Sortie_4.append(prochain_jeton)
    #         if Sortie_4[0] == 0:
    #             Sortie_4[0] = distribution_temps(Sortie_4)
    #     case "Sortie_5":
    #         Sortie_5.append(prochain_jeton)
    #         if Sortie_5[0] == 0:
    #             Sortie_5[0] = distribution_temps(Sortie_5)
    #     case "Sortie_6":
    #         Sortie_6.append(prochain_jeton)
    #         if Sortie_6[0] == 0:
    #             Sortie_6[0] = distribution_temps(Sortie_6)
    #     case "Stock_bas":
    #         Stock_bas.insert(0,prochain_jeton)
    #     case "Stock_haut":
    #         Stock_haut.insert(0,prochain_jeton)
    if direction_2 == "Sortie_1":
        Sortie_1.append(prochain_jeton)
        if Sortie_1[0] == 0:
            Sortie_1[0] = distribution_temps(Sortie_1)
    elif direction_2 == "Sortie_2":
        Sortie_2.append(prochain_jeton)
        if Sortie_2[0] == 0:
            Sortie_2[0] = distribution_temps(Sortie_2)
    elif direction_2 == "Sortie_3":
        Sortie_3.append(prochain_jeton)
        if Sortie_3[0] == 0:
            Sortie_3[0] = distribution_temps(Sortie_3)
    elif direction_2 == "Sortie_4":
        Sortie_4.append(prochain_jeton)
        if Sortie_4[0] == 0:
            Sortie_4[0] = distribution_temps(Sortie_4)
    elif direction_2 == "Sortie_5":
        Sortie_5.append(prochain_jeton)
        if Sortie_5[0] == 0:
            Sortie_5[0] = distribution_temps(Sortie_5)
    elif direction_2 == "Sortie_6":
        Sortie_6.append(prochain_jeton)
        if Sortie_6[0] == 0:
            Sortie_6[0] = distribution_temps(Sortie_6)
    elif direction_2 == "Stock_bas":
        Stock_bas.insert(0,prochain_jeton)
    elif direction_2 == "Stock_haut":
        Stock_haut.insert(0,prochain_jeton)
    return etat_chariot




def corps_algo():  # Valide 3.9 compatible
    global attente_presse
    global attente_essoreuse
    """
    Il s'agit ici du corps du programme, que l'on évaluera pour diverse combinaisons de jeton.
    """
    global temps_global
    global temps_bouchon
    global Sortie_1
    global Sortie_2
    global Sortie_3
    global Sortie_4
    global Sortie_5
    global Sortie_6
    global essoreuse
    global presse
    global Tapis_presse
    global Tapis_essoreuse
    global Stock_bas
    global Stock_haut
    global attente_presse
    global attente_essoreuse
    global temps_rechargement
    temps_rechargement = temps_passage
    if len(essoreuse)==1:
        essoreuse = [0]
    if len(presse)==1:
        presse = [0]
    attente_presse=0
    attente_essoreuse=0
    temps_global=0
    temps_bouchon=0
    etat_chariot = "essoreuse"
    etat_chariot , direction , direction_2 = actualisation(etat_chariot)
    while etat_chariot!="fin" or direction!="fin" or direction_2!="fin":
        etat_chariot = remplissage_vidage(etat_chariot,direction,direction_2)
        etat_chariot , direction , direction_2 = actualisation(etat_chariot)
    return attente_presse + attente_essoreuse











def combinaisons(nbr_vert,nbr_jaune_serviette,nbr_jaune_draps,nbr_rose,nbr_bleu): # Valide 3.9 compatible
    """
    Entrée : Prend en entré le nombre de chaque jeton dont dispose l'utilisateur.
    
    -----------------------------------------------------------------
    
    Sortie : Renvoie la liste de 100000 combinaisons possibles essoreuse / presse (Dans cet ordre)

    """
    essoreuse = [5 for k in range(nbr_bleu)]
    presse = [2 for k in range(nbr_jaune_serviette)] + [3 for k in range(nbr_jaune_draps)] + [4 for k in range(nbr_rose)]
    ls_presses = [presse]
    ls_essoreuses = [essoreuse]
    L=[]
    for k in range(nbr_vert):
        essoreuse = essoreuse + [1]
        presse = presse + [1]
        ls_essoreuses = ls_essoreuses + [essoreuse]
        ls_presses = ls_presses + [presse]
    for k in range(nbr_vert + 1):
        L= L + [[ls_essoreuses[nbr_vert-k],ls_presses[k]]]
    ls_finale = []
    ls_k=[[] for k in range(len(L))]
    progress_bar_combinaison_1.start()
    progress_bar_combinaison_2.start()
    progress_window_combinaison.update()
    n = len(L)
    precision = 10000
    for k in range(len(L)):
        progress_1 = int(100 * k/n)
        progress_bar_combinaison_1['value'] = progress_1
        for i in range(precision):
            progress_2 = int(100*i/precision)
            progress_bar_combinaison_2['value'] = progress_2
            fenetre.update_idletasks()
            essoreuse_bis=[]
            presse_bis=[]
            for j in L[k][0]:
                long = len(essoreuse_bis)
                essoreuse_bis.insert(random.randint(0,long),j)
            for j in L[k][1]:
                long = len(presse_bis)
                presse_bis.insert(random.randint(0, long),j)
            if [essoreuse_bis,presse_bis] not in ls_k[k]:
                ls_k[k].append([essoreuse_bis,presse_bis])
    for k in ls_k:
        ls_finale = ls_finale + k
    progress_bar_combinaison_1.stop()
    progress_bar_combinaison_2.stop()
    progress_window_combinaison.destroy()
    return ls_finale

    # for k in L:
    #     ls_finale = ls_finale + list(itertools.permutations(k[0],len(k[0])))
    # new_list_finale = [] 
    # for i in ls_finale: 
    #     if i not in new_list_finale: 
    #         new_list_finale.append(i) 
    # return new_list_finale





def interface_graphique(Tapis_essoreuse,Tapis_presse,essoreuse,presse,Stock_bas,Stock_haut,Sortie_1,Sortie_2,Sortie_3,Sortie_4,Sortie_5,Sortie_6,classement_essoreuse_presse): # Valide 3.9 compatible
    global fenetre
    for widget in fenetre.winfo_children():
        widget.destroy()
    width_canvas_=1000
    height_canvas_=500
    canvas = Canvas(fenetre , width=width_canvas_ , height=height_canvas_ , background='white')
    size = 15
    bouton_quit = Button(fenetre, text="Quitter", command=fenetre.quit)
    width_canvas_debut,height_canvas_debut= 3*width_canvas_/10,3*height_canvas_/20
    while len(essoreuse)>15:
        del essoreuse[-1]
    while len(presse)>16:
        del presse[-1]
    Tapis_essoreuse_txt = canvas.create_text(width_canvas_debut + 4.3 * size, height_canvas_debut - 2* size, text="Tapis Essoreuse", font="CMU", fill="black")
    for k in range(len(Tapis_essoreuse)):
        # match Tapis_essoreuse[k]:
        #     case 1:
        #         canvas.create_oval(width_canvas_debut +  size + 2.1 * size * k , height_canvas_debut + size , width_canvas_debut - size + 2.1 * size * k , height_canvas_debut - size ,  fill="green", outline="")
        #     case 2:
        #         canvas.create_oval(width_canvas_debut +  size + 2.1 * size * k , height_canvas_debut + size , width_canvas_debut - size + 2.1 * size * k , height_canvas_debut - size ,  fill="#DBEA45", outline="")
        #     case 3:
        #         canvas.create_oval(width_canvas_debut +  size + 2.1 * size * k , height_canvas_debut + size , width_canvas_debut - size + 2.1 * size * k , height_canvas_debut - size ,  fill="yellow", outline="")
        #     case 4:
        #         canvas.create_oval(width_canvas_debut +  size + 2.1 * size * k , height_canvas_debut + size , width_canvas_debut - size + 2.1 * size * k , height_canvas_debut - size ,  fill="pink", outline="")
        #     case 5:
        #         canvas.create_oval(width_canvas_debut +  size + 2.1 * size * k , height_canvas_debut + size , width_canvas_debut - size + 2.1 * size * k , height_canvas_debut - size ,  fill="blue", outline="")
        if Tapis_essoreuse[k] == 1:
            canvas.create_oval(width_canvas_debut +  size + 2.1 * size * k , height_canvas_debut + size , width_canvas_debut - size + 2.1 * size * k , height_canvas_debut - size ,  fill="green", outline="")
        elif Tapis_essoreuse[k] == 2:
            canvas.create_oval(width_canvas_debut +  size + 2.1 * size * k , height_canvas_debut + size , width_canvas_debut - size + 2.1 * size * k , height_canvas_debut - size ,  fill="#DBEA45", outline="")
        elif Tapis_essoreuse[k] == 3:
            canvas.create_oval(width_canvas_debut +  size + 2.1 * size * k , height_canvas_debut + size , width_canvas_debut - size + 2.1 * size * k , height_canvas_debut - size ,  fill="yellow", outline="")
        elif Tapis_essoreuse[k] == 4:
            canvas.create_oval(width_canvas_debut +  size + 2.1 * size * k , height_canvas_debut + size , width_canvas_debut - size + 2.1 * size * k , height_canvas_debut - size ,  fill="pink", outline="")
        elif Tapis_essoreuse[k] == 5:
            canvas.create_oval(width_canvas_debut +  size + 2.1 * size * k , height_canvas_debut + size , width_canvas_debut - size + 2.1 * size * k , height_canvas_debut - size ,  fill="blue", outline="")
    width_canvas_debut,height_canvas_debut= 3*width_canvas_/10,7*height_canvas_/20
    Tapis_presse_txt = canvas.create_text(width_canvas_debut + 4 * size, height_canvas_debut - 2* size, text="Tapis Presse", font="CMU", fill="black")
    for k in range(len(Tapis_presse)):
        # match Tapis_presse[k]:
        #     case 1:
        #         canvas.create_oval(width_canvas_debut +  size + 2.1 * size * k , height_canvas_debut + size , width_canvas_debut - size + 2.1 * size * k , height_canvas_debut - size ,  fill="green", outline="")
        #     case 2:
        #         canvas.create_oval(width_canvas_debut +  size + 2.1 * size * k , height_canvas_debut + size , width_canvas_debut - size + 2.1 * size * k , height_canvas_debut - size ,  fill="#DBEA45", outline="")
        #     case 3:
        #         canvas.create_oval(width_canvas_debut +  size + 2.1 * size * k , height_canvas_debut + size , width_canvas_debut - size + 2.1 * size * k , height_canvas_debut - size ,  fill="yellow", outline="")
        #     case 4:
        #         canvas.create_oval(width_canvas_debut +  size + 2.1 * size * k , height_canvas_debut + size , width_canvas_debut - size + 2.1 * size * k , height_canvas_debut - size ,  fill="pink", outline="")
        #     case 5:
        #         canvas.create_oval(width_canvas_debut +  size + 2.1 * size * k , height_canvas_debut + size , width_canvas_debut - size + 2.1 * size * k , height_canvas_debut - size ,  fill="blue", outline="") 
        if Tapis_presse[k] == 1:
            canvas.create_oval(width_canvas_debut +  size + 2.1 * size * k , height_canvas_debut + size , width_canvas_debut - size + 2.1 * size * k , height_canvas_debut - size ,  fill="green", outline="")
        elif Tapis_presse[k] == 2:
            canvas.create_oval(width_canvas_debut +  size + 2.1 * size * k , height_canvas_debut + size , width_canvas_debut - size + 2.1 * size * k , height_canvas_debut - size ,  fill="#DBEA45", outline="")
        elif Tapis_presse[k] == 3:
            canvas.create_oval(width_canvas_debut +  size + 2.1 * size * k , height_canvas_debut + size , width_canvas_debut - size + 2.1 * size * k , height_canvas_debut - size ,  fill="yellow", outline="")
        elif Tapis_presse[k] == 4:
            canvas.create_oval(width_canvas_debut +  size + 2.1 * size * k , height_canvas_debut + size , width_canvas_debut - size + 2.1 * size * k , height_canvas_debut - size ,  fill="pink", outline="")
        elif Tapis_presse[k] == 5:
            canvas.create_oval(width_canvas_debut +  size + 2.1 * size * k , height_canvas_debut + size , width_canvas_debut - size + 2.1 * size * k , height_canvas_debut - size ,  fill="blue", outline="") 
    width_canvas_debut,height_canvas_debut= 5*width_canvas_/10,3*height_canvas_/20
    essoreuse_txt = canvas.create_text(width_canvas_debut + 7 * size, height_canvas_debut - 2* size, text="Essoreuse", font="CMU", fill="black")
    canvas.create_rectangle(width_canvas_debut +  size + 2.1 * size * 14 , height_canvas_debut + size , width_canvas_debut - size + 2.1 * size * 14 , height_canvas_debut - size, outline="black")
    for k in range(1,len(essoreuse)):
        # match essoreuse[k]:
        #     case 1:
        #         canvas.create_oval(width_canvas_debut +  size + 2.1 * size * k , height_canvas_debut + size , width_canvas_debut - size + 2.1 * size * k , height_canvas_debut - size ,  fill="green", outline="")
        #     case 2:
        #         canvas.create_oval(width_canvas_debut +  size + 2.1 * size * k , height_canvas_debut + size , width_canvas_debut - size + 2.1 * size * k , height_canvas_debut - size ,  fill="#DBEA45", outline="")
        #     case 3:
        #         canvas.create_oval(width_canvas_debut +  size + 2.1 * size * k , height_canvas_debut + size , width_canvas_debut - size + 2.1 * size * k , height_canvas_debut - size ,  fill="yellow", outline="")
        #     case 4:
        #         canvas.create_oval(width_canvas_debut +  size + 2.1 * size * k , height_canvas_debut + size , width_canvas_debut - size + 2.1 * size * k , height_canvas_debut - size ,  fill="pink", outline="")
        #     case 5:
        #         canvas.create_oval(width_canvas_debut +  size + 2.1 * size * k , height_canvas_debut + size , width_canvas_debut - size + 2.1 * size * k , height_canvas_debut - size ,  fill="blue", outline="")
        if essoreuse[k] == 1:
            canvas.create_oval(width_canvas_debut +  size + 2.1 * size * k , height_canvas_debut + size , width_canvas_debut - size + 2.1 * size * k , height_canvas_debut - size ,  fill="green", outline="")
        elif essoreuse[k] == 2:
            canvas.create_oval(width_canvas_debut +  size + 2.1 * size * k , height_canvas_debut + size , width_canvas_debut - size + 2.1 * size * k , height_canvas_debut - size ,  fill="#DBEA45", outline="")
        elif essoreuse[k] == 3:
            canvas.create_oval(width_canvas_debut +  size + 2.1 * size * k , height_canvas_debut + size , width_canvas_debut - size + 2.1 * size * k , height_canvas_debut - size ,  fill="yellow", outline="")
        elif essoreuse[k] == 4:
            canvas.create_oval(width_canvas_debut +  size + 2.1 * size * k , height_canvas_debut + size , width_canvas_debut - size + 2.1 * size * k , height_canvas_debut - size ,  fill="pink", outline="")
        elif essoreuse[k] == 5:
            canvas.create_oval(width_canvas_debut +  size + 2.1 * size * k , height_canvas_debut + size , width_canvas_debut - size + 2.1 * size * k , height_canvas_debut - size ,  fill="blue", outline="")
    width_canvas_debut,height_canvas_debut= 5*width_canvas_/10,7*height_canvas_/20
    presse_txt = canvas.create_text(width_canvas_debut + 7 * size, height_canvas_debut - 2* size, text="Presse", font="CMU", fill="black")
    canvas.create_rectangle(width_canvas_debut +  size + 2.1 * size * 15 , height_canvas_debut + size , width_canvas_debut - size + 2.1 * size * 15 , height_canvas_debut - size , outline="black")
    for k in range(1,len(presse)):
        # match presse[k]:
        #     case 1:
        #         canvas.create_oval(width_canvas_debut +  size + 2.1 * size * k , height_canvas_debut + size , width_canvas_debut - size + 2.1 * size * k , height_canvas_debut - size ,  fill="green", outline="")
        #     case 2:
        #         canvas.create_oval(width_canvas_debut +  size + 2.1 * size * k , height_canvas_debut + size , width_canvas_debut - size + 2.1 * size * k , height_canvas_debut - size ,  fill="#DBEA45", outline="")
        #     case 3:
        #         canvas.create_oval(width_canvas_debut +  size + 2.1 * size * k , height_canvas_debut + size , width_canvas_debut - size + 2.1 * size * k , height_canvas_debut - size ,  fill="yellow", outline="")
        #     case 4:
        #         canvas.create_oval(width_canvas_debut +  size + 2.1 * size * k , height_canvas_debut + size , width_canvas_debut - size + 2.1 * size * k , height_canvas_debut - size ,  fill="pink", outline="")
        #     case 5:
        #         canvas.create_oval(width_canvas_debut +  size + 2.1 * size * k , height_canvas_debut + size , width_canvas_debut - size + 2.1 * size * k , height_canvas_debut - size ,  fill="blue", outline="")
        if presse[k] == 1:
            canvas.create_oval(width_canvas_debut +  size + 2.1 * size * k , height_canvas_debut + size , width_canvas_debut - size + 2.1 * size * k , height_canvas_debut - size ,  fill="green", outline="")
        elif presse[k] == 2:
            canvas.create_oval(width_canvas_debut +  size + 2.1 * size * k , height_canvas_debut + size , width_canvas_debut - size + 2.1 * size * k , height_canvas_debut - size ,  fill="#DBEA45", outline="")
        elif presse[k] == 3:
            canvas.create_oval(width_canvas_debut +  size + 2.1 * size * k , height_canvas_debut + size , width_canvas_debut - size + 2.1 * size * k , height_canvas_debut - size ,  fill="yellow", outline="")
        elif presse[k] == 4:
            canvas.create_oval(width_canvas_debut +  size + 2.1 * size * k , height_canvas_debut + size , width_canvas_debut - size + 2.1 * size * k , height_canvas_debut - size ,  fill="pink", outline="")
        elif presse[k] == 5:
            canvas.create_oval(width_canvas_debut +  size + 2.1 * size * k , height_canvas_debut + size , width_canvas_debut - size + 2.1 * size * k , height_canvas_debut - size ,  fill="blue", outline="")
    width_canvas_debut,height_canvas_debut= 3*width_canvas_/10 + 2.1*size ,11*height_canvas_/20
    Stock_bas_txt = canvas.create_text(width_canvas_debut + 2.3 * size, height_canvas_debut - 2* size, text="Stock bas", font="CMU", fill="black")
    for k in range(len(Stock_bas)):
        # match Stock_bas[k]:
        #     case 1:
        #         canvas.create_oval(width_canvas_debut +  size + 2.1 * size * k , height_canvas_debut + size , width_canvas_debut - size + 2.1 * size * k , height_canvas_debut - size ,  fill="green", outline="")
        #     case 2:
        #         canvas.create_oval(width_canvas_debut +  size + 2.1 * size * k , height_canvas_debut + size , width_canvas_debut - size + 2.1 * size * k , height_canvas_debut - size ,  fill="#DBEA45", outline="")
        #     case 3:
        #         canvas.create_oval(width_canvas_debut +  size + 2.1 * size * k , height_canvas_debut + size , width_canvas_debut - size + 2.1 * size * k , height_canvas_debut - size ,  fill="yellow", outline="")
        #     case 4:
        #         canvas.create_oval(width_canvas_debut +  size + 2.1 * size * k , height_canvas_debut + size , width_canvas_debut - size + 2.1 * size * k , height_canvas_debut - size ,  fill="pink", outline="")
        #     case 5:
        #         canvas.create_oval(width_canvas_debut +  size + 2.1 * size * k , height_canvas_debut + size , width_canvas_debut - size + 2.1 * size * k , height_canvas_debut - size ,  fill="blue", outline="")
        if Stock_bas[k] == 1:
            canvas.create_oval(width_canvas_debut +  size + 2.1 * size * k , height_canvas_debut + size , width_canvas_debut - size + 2.1 * size * k , height_canvas_debut - size ,  fill="green", outline="")
        elif Stock_bas[k] == 2:
            canvas.create_oval(width_canvas_debut +  size + 2.1 * size * k , height_canvas_debut + size , width_canvas_debut - size + 2.1 * size * k , height_canvas_debut - size ,  fill="#DBEA45", outline="")
        elif Stock_bas[k] == 3:
            canvas.create_oval(width_canvas_debut +  size + 2.1 * size * k , height_canvas_debut + size , width_canvas_debut - size + 2.1 * size * k , height_canvas_debut - size ,  fill="yellow", outline="")
        elif Stock_bas[k] == 4:
            canvas.create_oval(width_canvas_debut +  size + 2.1 * size * k , height_canvas_debut + size , width_canvas_debut - size + 2.1 * size * k , height_canvas_debut - size ,  fill="pink", outline="")
        elif Stock_bas[k] == 5:
            canvas.create_oval(width_canvas_debut +  size + 2.1 * size * k , height_canvas_debut + size , width_canvas_debut - size + 2.1 * size * k , height_canvas_debut - size ,  fill="blue", outline="")
    width_canvas_debut,height_canvas_debut= 3*width_canvas_/10 + 2.1 * size,15*height_canvas_/20
    Stock_haut_txt = canvas.create_text(width_canvas_debut + 2.3 * size, height_canvas_debut - 2* size, text="Stock haut", font="CMU", fill="black")
    for k in range(len(Stock_haut)):
        # match Stock_haut[k]:
        #     case 1:
        #         canvas.create_oval(width_canvas_debut +  size + 2.1 * size * k , height_canvas_debut + size , width_canvas_debut - size + 2.1 * size * k , height_canvas_debut - size ,  fill="green", outline="")
        #     case 2:
        #         canvas.create_oval(width_canvas_debut +  size + 2.1 * size * k , height_canvas_debut + size , width_canvas_debut - size + 2.1 * size * k , height_canvas_debut - size ,  fill="#DBEA45", outline="")
        #     case 3:
        #         canvas.create_oval(width_canvas_debut +  size + 2.1 * size * k , height_canvas_debut + size , width_canvas_debut - size + 2.1 * size * k , height_canvas_debut - size ,  fill="yellow", outline="")
        #     case 4:
        #         canvas.create_oval(width_canvas_debut +  size + 2.1 * size * k , height_canvas_debut + size , width_canvas_debut - size + 2.1 * size * k , height_canvas_debut - size ,  fill="pink", outline="")
        #     case 5:
        #         canvas.create_oval(width_canvas_debut +  size + 2.1 * size * k , height_canvas_debut + size , width_canvas_debut - size + 2.1 * size * k , height_canvas_debut - size ,  fill="blue", outline="")
        if Stock_haut[k] == 1:
            canvas.create_oval(width_canvas_debut +  size + 2.1 * size * k , height_canvas_debut + size , width_canvas_debut - size + 2.1 * size * k , height_canvas_debut - size ,  fill="green", outline="")
        elif Stock_haut[k] == 2:
            canvas.create_oval(width_canvas_debut +  size + 2.1 * size * k , height_canvas_debut + size , width_canvas_debut - size + 2.1 * size * k , height_canvas_debut - size ,  fill="#DBEA45", outline="")
        elif Stock_haut[k] == 3:
            canvas.create_oval(width_canvas_debut +  size + 2.1 * size * k , height_canvas_debut + size , width_canvas_debut - size + 2.1 * size * k , height_canvas_debut - size ,  fill="yellow", outline="")
        elif Stock_haut[k] == 4:
            canvas.create_oval(width_canvas_debut +  size + 2.1 * size * k , height_canvas_debut + size , width_canvas_debut - size + 2.1 * size * k , height_canvas_debut - size ,  fill="pink", outline="")
        elif Stock_haut[k] == 5:
            canvas.create_oval(width_canvas_debut +  size + 2.1 * size * k , height_canvas_debut + size , width_canvas_debut - size + 2.1 * size * k , height_canvas_debut - size ,  fill="blue", outline="")
    width_canvas_debut,height_canvas_debut= 2*width_canvas_/10,3*height_canvas_/20
    Sortie_1_txt = canvas.create_text(width_canvas_debut - 4 * size, height_canvas_debut - 1.8* size, text="Sortie 1", font="CMU", fill="black")
    for k in range(1,len(Sortie_1)):
        # match Sortie_1[k]:
        #     case 1:
        #         canvas.create_oval(width_canvas_debut +  size - 2.1 * size * k , height_canvas_debut + size , width_canvas_debut - size - 2.1 * size * k , height_canvas_debut - size ,  fill="green", outline="")
        #     case 2:
        #         canvas.create_oval(width_canvas_debut +  size - 2.1 * size * k , height_canvas_debut + size , width_canvas_debut - size - 2.1 * size * k , height_canvas_debut - size ,  fill="#DBEA45", outline="")
        #     case 3:
        #         canvas.create_oval(width_canvas_debut +  size - 2.1 * size * k , height_canvas_debut + size , width_canvas_debut - size - 2.1 * size * k , height_canvas_debut - size ,  fill="yellow", outline="")
        #     case 4:
        #         canvas.create_oval(width_canvas_debut +  size - 2.1 * size * k , height_canvas_debut + size , width_canvas_debut - size - 2.1 * size * k , height_canvas_debut - size ,  fill="pink", outline="")
        #     case 5:
        #         canvas.create_oval(width_canvas_debut +  size - 2.1 * size * k , height_canvas_debut + size , width_canvas_debut - size - 2.1 * size * k , height_canvas_debut - size ,  fill="blue", outline="")
        if Sortie_1[k] ==1:
            canvas.create_oval(width_canvas_debut +  size - 2.1 * size * k , height_canvas_debut + size , width_canvas_debut - size - 2.1 * size * k , height_canvas_debut - size ,  fill="green", outline="")
        elif Sortie_1[k] == 2:
            canvas.create_oval(width_canvas_debut +  size - 2.1 * size * k , height_canvas_debut + size , width_canvas_debut - size - 2.1 * size * k , height_canvas_debut - size ,  fill="#DBEA45", outline="")
        elif Sortie_1[k] == 3:
            canvas.create_oval(width_canvas_debut +  size - 2.1 * size * k , height_canvas_debut + size , width_canvas_debut - size - 2.1 * size * k , height_canvas_debut - size ,  fill="yellow", outline="")
        elif Sortie_1[k] == 4:
            canvas.create_oval(width_canvas_debut +  size - 2.1 * size * k , height_canvas_debut + size , width_canvas_debut - size - 2.1 * size * k , height_canvas_debut - size ,  fill="pink", outline="")
        elif Sortie_1[k] == 5:
            canvas.create_oval(width_canvas_debut +  size - 2.1 * size * k , height_canvas_debut + size , width_canvas_debut - size - 2.1 * size * k , height_canvas_debut - size ,  fill="blue", outline="")
    width_canvas_debut,height_canvas_debut= 2*width_canvas_/10,6*height_canvas_/20
    Sortie_2_txt = canvas.create_text(width_canvas_debut - 4 * size, height_canvas_debut - 1.8* size, text="Sortie 2", font="CMU", fill="black")    
    for k in range(1,len(Sortie_2)):
        # match Sortie_2[k]:
        #     case 1:
        #         canvas.create_oval(width_canvas_debut +  size - 2.1 * size * k , height_canvas_debut + size , width_canvas_debut - size - 2.1 * size * k , height_canvas_debut - size ,  fill="green", outline="")
        #     case 2:
        #         canvas.create_oval(width_canvas_debut +  size - 2.1 * size * k , height_canvas_debut + size , width_canvas_debut - size - 2.1 * size * k , height_canvas_debut - size ,  fill="#DBEA45", outline="")
        #     case 3:
        #         canvas.create_oval(width_canvas_debut +  size - 2.1 * size * k , height_canvas_debut + size , width_canvas_debut - size - 2.1 * size * k , height_canvas_debut - size ,  fill="yellow", outline="")
        #     case 4:
        #         canvas.create_oval(width_canvas_debut +  size - 2.1 * size * k , height_canvas_debut + size , width_canvas_debut - size - 2.1 * size * k , height_canvas_debut - size ,  fill="pink", outline="")
        #     case 5:
        #         canvas.create_oval(width_canvas_debut +  size - 2.1 * size * k , height_canvas_debut + size , width_canvas_debut - size - 2.1 * size * k , height_canvas_debut - size ,  fill="blue", outline="")
        if Sortie_2[k] == 1:
            canvas.create_oval(width_canvas_debut +  size - 2.1 * size * k , height_canvas_debut + size , width_canvas_debut - size - 2.1 * size * k , height_canvas_debut - size ,  fill="green", outline="")
        elif Sortie_2[k] == 2:
            canvas.create_oval(width_canvas_debut +  size - 2.1 * size * k , height_canvas_debut + size , width_canvas_debut - size - 2.1 * size * k , height_canvas_debut - size ,  fill="#DBEA45", outline="")
        elif Sortie_2[k] == 3:
            canvas.create_oval(width_canvas_debut +  size - 2.1 * size * k , height_canvas_debut + size , width_canvas_debut - size - 2.1 * size * k , height_canvas_debut - size ,  fill="yellow", outline="")
        elif Sortie_2[k] == 4:
            canvas.create_oval(width_canvas_debut +  size - 2.1 * size * k , height_canvas_debut + size , width_canvas_debut - size - 2.1 * size * k , height_canvas_debut - size ,  fill="pink", outline="")
        elif Sortie_2[k] == 5:
            canvas.create_oval(width_canvas_debut +  size - 2.1 * size * k , height_canvas_debut + size , width_canvas_debut - size - 2.1 * size * k , height_canvas_debut - size ,  fill="blue", outline="")
    width_canvas_debut,height_canvas_debut= 2*width_canvas_/10,9*height_canvas_/20
    Sortie_3_txt = canvas.create_text(width_canvas_debut - 4 * size, height_canvas_debut - 1.8* size, text="Sortie 3", font="CMU", fill="black")
    for k in range(1,len(Sortie_3)):
        # match Sortie_3[k]:
        #     case 1:
        #         canvas.create_oval(width_canvas_debut +  size - 2.1 * size * k , height_canvas_debut + size , width_canvas_debut - size - 2.1 * size * k , height_canvas_debut - size ,  fill="green", outline="")
        #     case 2:
        #         canvas.create_oval(width_canvas_debut +  size - 2.1 * size * k , height_canvas_debut + size , width_canvas_debut - size - 2.1 * size * k , height_canvas_debut - size ,  fill="#DBEA45", outline="")
        #     case 3:
        #         canvas.create_oval(width_canvas_debut +  size - 2.1 * size * k , height_canvas_debut + size , width_canvas_debut - size - 2.1 * size * k , height_canvas_debut - size ,  fill="yellow", outline="")
        #     case 4:
        #         canvas.create_oval(width_canvas_debut +  size - 2.1 * size * k , height_canvas_debut + size , width_canvas_debut - size - 2.1 * size * k , height_canvas_debut - size ,  fill="pink", outline="")
        #     case 5:
        #         canvas.create_oval(width_canvas_debut +  size - 2.1 * size * k , height_canvas_debut + size , width_canvas_debut - size - 2.1 * size * k , height_canvas_debut - size ,  fill="blue", outline="")
        if Sortie_3[k] == 1:
            canvas.create_oval(width_canvas_debut +  size - 2.1 * size * k , height_canvas_debut + size , width_canvas_debut - size - 2.1 * size * k , height_canvas_debut - size ,  fill="green", outline="")
        elif Sortie_3[k] == 2:
            canvas.create_oval(width_canvas_debut +  size - 2.1 * size * k , height_canvas_debut + size , width_canvas_debut - size - 2.1 * size * k , height_canvas_debut - size ,  fill="#DBEA45", outline="")
        elif Sortie_3[k] == 3:
            canvas.create_oval(width_canvas_debut +  size - 2.1 * size * k , height_canvas_debut + size , width_canvas_debut - size - 2.1 * size * k , height_canvas_debut - size ,  fill="yellow", outline="")
        elif Sortie_3[k] == 4:
            canvas.create_oval(width_canvas_debut +  size - 2.1 * size * k , height_canvas_debut + size , width_canvas_debut - size - 2.1 * size * k , height_canvas_debut - size ,  fill="pink", outline="")
        elif Sortie_3[k] == 5:
            canvas.create_oval(width_canvas_debut +  size - 2.1 * size * k , height_canvas_debut + size , width_canvas_debut - size - 2.1 * size * k , height_canvas_debut - size ,  fill="blue", outline="")
    width_canvas_debut,height_canvas_debut= 2*width_canvas_/10,12*height_canvas_/20
    Sortie_4_txt = canvas.create_text(width_canvas_debut - 4 * size, height_canvas_debut - 1.8* size, text="Sortie 4", font="CMU", fill="black")
    for k in range(1,len(Sortie_4)):
        # match Sortie_4[k]:
        #     case 1:
        #         canvas.create_oval(width_canvas_debut +  size - 2.1 * size * k , height_canvas_debut + size , width_canvas_debut - size - 2.1 * size * k , height_canvas_debut - size ,  fill="green", outline="")
        #     case 2:
        #         canvas.create_oval(width_canvas_debut +  size - 2.1 * size * k , height_canvas_debut + size , width_canvas_debut - size - 2.1 * size * k , height_canvas_debut - size ,  fill="#DBEA45", outline="")
        #     case 3:
        #         canvas.create_oval(width_canvas_debut +  size - 2.1 * size * k , height_canvas_debut + size , width_canvas_debut - size - 2.1 * size * k , height_canvas_debut - size ,  fill="yellow", outline="")
        #     case 4:
        #         canvas.create_oval(width_canvas_debut +  size - 2.1 * size * k , height_canvas_debut + size , width_canvas_debut - size - 2.1 * size * k , height_canvas_debut - size ,  fill="pink", outline="")
        #     case 5:
        #         canvas.create_oval(width_canvas_debut +  size - 2.1 * size * k , height_canvas_debut + size , width_canvas_debut - size - 2.1 * size * k , height_canvas_debut - size ,  fill="blue", outline="")
        if Sortie_4[k] == 1:
            canvas.create_oval(width_canvas_debut +  size - 2.1 * size * k , height_canvas_debut + size , width_canvas_debut - size - 2.1 * size * k , height_canvas_debut - size ,  fill="green", outline="")
        elif Sortie_4[k] == 2:
            canvas.create_oval(width_canvas_debut +  size - 2.1 * size * k , height_canvas_debut + size , width_canvas_debut - size - 2.1 * size * k , height_canvas_debut - size ,  fill="#DBEA45", outline="")
        elif Sortie_4[k] == 3:
            canvas.create_oval(width_canvas_debut +  size - 2.1 * size * k , height_canvas_debut + size , width_canvas_debut - size - 2.1 * size * k , height_canvas_debut - size ,  fill="yellow", outline="")
        elif Sortie_4[k] == 4:
            canvas.create_oval(width_canvas_debut +  size - 2.1 * size * k , height_canvas_debut + size , width_canvas_debut - size - 2.1 * size * k , height_canvas_debut - size ,  fill="pink", outline="")
        elif Sortie_4[k] == 5:
            canvas.create_oval(width_canvas_debut +  size - 2.1 * size * k , height_canvas_debut + size , width_canvas_debut - size - 2.1 * size * k , height_canvas_debut - size ,  fill="blue", outline="")
    width_canvas_debut,height_canvas_debut= 2*width_canvas_/10,15*height_canvas_/20
    Sortie_5_txt = canvas.create_text(width_canvas_debut - 4 * size, height_canvas_debut - 1.8* size, text="Sortie 5", font="CMU", fill="black")
    for k in range(1,len(Sortie_5)):
        # match Sortie_5[k]:
        #     case 1:
        #         canvas.create_oval(width_canvas_debut +  size - 2.1 * size * k , height_canvas_debut + size , width_canvas_debut - size - 2.1 * size * k , height_canvas_debut - size ,  fill="green", outline="")
        #     case 2:
        #         canvas.create_oval(width_canvas_debut +  size - 2.1 * size * k , height_canvas_debut + size , width_canvas_debut - size - 2.1 * size * k , height_canvas_debut - size ,  fill="#DBEA45", outline="")
        #     case 3:
        #         canvas.create_oval(width_canvas_debut +  size - 2.1 * size * k , height_canvas_debut + size , width_canvas_debut - size - 2.1 * size * k , height_canvas_debut - size ,  fill="yellow", outline="")
        #     case 4:
        #         canvas.create_oval(width_canvas_debut +  size - 2.1 * size * k , height_canvas_debut + size , width_canvas_debut - size - 2.1 * size * k , height_canvas_debut - size ,  fill="pink", outline="")
        #     case 5:
        #         canvas.create_oval(width_canvas_debut +  size - 2.1 * size * k , height_canvas_debut + size , width_canvas_debut - size - 2.1 * size * k , height_canvas_debut - size ,  fill="blue", outline="")
        if Sortie_5[k] == 1:
            canvas.create_oval(width_canvas_debut +  size - 2.1 * size * k , height_canvas_debut + size , width_canvas_debut - size - 2.1 * size * k , height_canvas_debut - size ,  fill="green", outline="")
        elif Sortie_5[k] == 2:
            canvas.create_oval(width_canvas_debut +  size - 2.1 * size * k , height_canvas_debut + size , width_canvas_debut - size - 2.1 * size * k , height_canvas_debut - size ,  fill="#DBEA45", outline="")
        elif Sortie_5[k] == 3:
            canvas.create_oval(width_canvas_debut +  size - 2.1 * size * k , height_canvas_debut + size , width_canvas_debut - size - 2.1 * size * k , height_canvas_debut - size ,  fill="yellow", outline="")
        elif Sortie_5[k] == 4:
            canvas.create_oval(width_canvas_debut +  size - 2.1 * size * k , height_canvas_debut + size , width_canvas_debut - size - 2.1 * size * k , height_canvas_debut - size ,  fill="pink", outline="")
        elif Sortie_5[k] == 5:
            canvas.create_oval(width_canvas_debut +  size - 2.1 * size * k , height_canvas_debut + size , width_canvas_debut - size - 2.1 * size * k , height_canvas_debut - size ,  fill="blue", outline="")
    width_canvas_debut,height_canvas_debut= 2*width_canvas_/10,18*height_canvas_/20
    Sortie_6_txt = canvas.create_text(width_canvas_debut - 4 * size, height_canvas_debut - 1.8* size, text="Sortie 6", font="CMU", fill="black")
    for k in range(1,len(Sortie_6)):
        # match Sortie_6[k]:
        #     case 1:
        #         canvas.create_oval(width_canvas_debut +  size - 2.1 * size * k , height_canvas_debut + size , width_canvas_debut - size - 2.1 * size * k , height_canvas_debut - size ,  fill="green", outline="")
        #     case 2:
        #         canvas.create_oval(width_canvas_debut +  size - 2.1 * size * k , height_canvas_debut + size , width_canvas_debut - size - 2.1 * size * k , height_canvas_debut - size ,  fill="#DBEA45", outline="")
        #     case 3:
        #         canvas.create_oval(width_canvas_debut +  size - 2.1 * size * k , height_canvas_debut + size , width_canvas_debut - size - 2.1 * size * k , height_canvas_debut - size ,  fill="yellow", outline="")
        #     case 4:
        #         canvas.create_oval(width_canvas_debut +  size - 2.1 * size * k , height_canvas_debut + size , width_canvas_debut - size - 2.1 * size * k , height_canvas_debut - size ,  fill="pink", outline="")
        #     case 5:
        #         canvas.create_oval(width_canvas_debut +  size - 2.1 * size * k , height_canvas_debut + size , width_canvas_debut - size - 2.1 * size * k , height_canvas_debut - size ,  fill="blue", outline="")
        if Sortie_6[k] == 1:
            canvas.create_oval(width_canvas_debut +  size - 2.1 * size * k , height_canvas_debut + size , width_canvas_debut - size - 2.1 * size * k , height_canvas_debut - size ,  fill="green", outline="")
        elif Sortie_6[k] == 2:
            canvas.create_oval(width_canvas_debut +  size - 2.1 * size * k , height_canvas_debut + size , width_canvas_debut - size - 2.1 * size * k , height_canvas_debut - size ,  fill="#DBEA45", outline="")
        elif Sortie_6[k] == 3:
            canvas.create_oval(width_canvas_debut +  size - 2.1 * size * k , height_canvas_debut + size , width_canvas_debut - size - 2.1 * size * k , height_canvas_debut - size ,  fill="yellow", outline="")
        elif Sortie_6[k] == 4:
            canvas.create_oval(width_canvas_debut +  size - 2.1 * size * k , height_canvas_debut + size , width_canvas_debut - size - 2.1 * size * k , height_canvas_debut - size ,  fill="pink", outline="")
        elif Sortie_6[k] == 5:
            canvas.create_oval(width_canvas_debut +  size - 2.1 * size * k , height_canvas_debut + size , width_canvas_debut - size - 2.1 * size * k , height_canvas_debut - size ,  fill="blue", outline="")
    bouton_quit.pack(side = TOP)
    canvas.pack(side = LEFT)
    bouton_suite = Button(fenetre, text= "Suite", command=suite)
    bouton_suite.pack(side = BOTTOM)
    return 






fenetre = Tk()
fenetre.title('Optim\'flot')
fenetre.iconbitmap("C:\\Users\Schobert\Desktop\TIPE\Algorithme\Logo_Optim_neo.ico")




temps_global = 0
temps_rechargement = temps_passage



Sortie_1=[0]
Sortie_2=[0]
Sortie_3=[0]
Sortie_4=[0]
Sortie_5=[0]
Sortie_6=[0]
presse=[0]
essoreuse=[0]
Stock_bas=[]
Stock_haut=[]
Tapis_presse=[]
Tapis_essoreuse=[]
jetons_vert = DoubleVar()
jetons_jaune_serviette = DoubleVar()
jetons_jaune_draps = DoubleVar()
jetons_rose = DoubleVar()
jetons_bleu = DoubleVar()
classement_essoreuse_presse=[[1,5],[3,2,4,1]]


Sortie_1_depart=[0]
Sortie_2_depart=[0]
Sortie_3_depart=[0]
Sortie_4_depart=[0]
Sortie_5_depart=[0]
Sortie_6_depart=[0]
Stock_bas_depart=[]
Stock_haut_depart=[]
Tapis_presse_depart=[]
Tapis_essoreuse_depart=[]




Sortie_1_save=[0]
Sortie_2_save=[0]
Sortie_3_save=[0]
Sortie_4_save=[0]
Sortie_5_save=[0]
Sortie_6_save=[0]
essoreuse_save=[0]
presse_save=[0]
Stock_bas_save=[]
Stock_haut_save=[]
Tapis_presse_save=[]
Tapis_essoreuse_save=[]


Sortie_1_end=[0]
Sortie_2_end=[0]
Sortie_3_end=[0]
Sortie_4_end=[0]
Sortie_5_end=[0]
Sortie_6_end=[0]
essoreuse_end=[0]
presse_end=[0]
Stock_bas_end=[]
Stock_haut_end=[]
Tapis_presse_end=[]
Tapis_essoreuse_end=[]


presse_depart=[0]
essoreuse_depart=[0]





def meilleure_combinaison_init(lst_combinaison_init): # Valide 3.9 compatible
    global Sortie_1
    global Sortie_2
    global Sortie_3
    global Sortie_4
    global Sortie_5
    global Sortie_6
    global essoreuse
    global presse
    global Tapis_presse
    global Tapis_essoreuse
    global Stock_bas
    global Stock_haut
    global Sortie_1_end
    global Sortie_2_end
    global Sortie_3_end
    global Sortie_4_end
    global Sortie_5_end
    global Sortie_6_end
    global essoreuse_end
    global presse_end
    global Stock_bas_end
    global Stock_haut_end
    global Tapis_presse_end
    global Tapis_essoreuse_end
    global Sortie_1_save
    global Sortie_2_save
    global Sortie_3_save
    global Sortie_4_save
    global Sortie_5_save
    global Sortie_6_save
    global essoreuse_save
    global presse_save
    global Stock_bas_save
    global Stock_haut_save
    global Tapis_presse_save
    global Tapis_essoreuse_save
    ind_meilleur_combi=0
    attente_mini = 10000000000000000000000
    progression_bar.start()
    progress_window.update()
    n=len(lst_combinaison_init)
    for k in range(len(lst_combinaison_init)):
        progress= int(100* k/n)
        progression_bar['value']= progress
        fenetre.update_idletasks()
        Sortie_1=[0]
        Sortie_2=[0]
        Sortie_3=[0]
        Sortie_4=[0]
        Sortie_5=[0]
        Sortie_6=[0]
        Stock_bas=[]
        Stock_haut=[]
        Tapis_presse=[]
        Tapis_essoreuse=[]
        essoreuse = [300] + list(lst_combinaison_init[k][0])
        presse = [300] + list(lst_combinaison_init[k][1])
        critere = corps_algo()
        if critere < attente_mini:
            attente_mini = critere
            ind_meilleur_combi = k
            if len(lst_combinaison_init[k][0])==14 and len(lst_combinaison_init[k][1])==15:
                Sortie_1_save=copy.deepcopy(Sortie_1_end)
                Sortie_2_save=copy.deepcopy(Sortie_2_end)
                Sortie_3_save=copy.deepcopy(Sortie_3_end)
                Sortie_4_save=copy.deepcopy(Sortie_4_end)
                Sortie_5_save=copy.deepcopy(Sortie_5_end)
                Sortie_6_save=copy.deepcopy(Sortie_6_end)
                essoreuse_save=copy.deepcopy(essoreuse_end)
                presse_save=copy.deepcopy(presse_end)
                Stock_bas_save=copy.deepcopy(Stock_bas_end)
                Stock_haut_save=copy.deepcopy(Stock_haut_end)
                Tapis_presse_save=copy.deepcopy(Tapis_presse_end)
                Tapis_essoreuse_save=copy.deepcopy(Tapis_essoreuse_end)
    if len(lst_combinaison_init[ind_meilleur_combi][0])!=14 or len(lst_combinaison_init[ind_meilleur_combi][1])!=15:
        Sortie_1_save=[0]
        Sortie_2_save=[0]
        Sortie_3_save=[0]
        Sortie_4_save=[0]
        Sortie_5_save=[0]
        Sortie_6_save=[0]
        essoreuse_save=[0]
        presse_save=[0]
        Stock_bas_save=[]
        Stock_haut_save=[]
        Tapis_presse_save=[]
        Tapis_essoreuse_save=[]        
    progression_bar.stop()
    progress_window.destroy()
    return lst_combinaison_init[ind_meilleur_combi]


def valide_init(): # Valide 3.9 compatible  
    global progress_bar_combinaison_1
    global progress_bar_combinaison_2
    global progress_window_combinaison
    global progression_bar
    global progress_window
    global jetons_vert
    global jetons_jaune_serviette
    global jetons_jaune_draps
    global jetons_rose
    global jetons_bleu
    global Sortie_1
    global Sortie_2
    global Sortie_3
    global Sortie_4
    global Sortie_5
    global Sortie_6
    global essoreuse
    global presse
    global Tapis_presse
    global Tapis_essoreuse
    global Stock_bas
    global Stock_haut
    global Sortie_1_save
    global Sortie_2_save
    global Sortie_3_save
    global Sortie_4_save
    global Sortie_5_save
    global Sortie_6_save
    global essoreuse_save
    global presse_save
    global Stock_bas_save
    global Stock_haut_save
    global Tapis_presse_save
    global Tapis_essoreuse_save
    Sortie_1=[0]
    Sortie_2=[0]
    Sortie_3=[0]
    Sortie_4=[0]
    Sortie_5=[0]
    Sortie_6=[0]
    Stock_bas=[]
    Stock_haut=[]
    Tapis_presse=[]
    Tapis_essoreuse=[]
    size = 15
    lst_jetons=[int(jetons_vert.get()),int(jetons_jaune_serviette.get()),int(jetons_jaune_draps.get()),int(jetons_rose.get()),int(jetons_bleu.get())]
    progress_window_combinaison =Toplevel(fenetre)
    generation_combinaison = Label(progress_window_combinaison, text = "Generation des combinaisons")
    progress_bar_combinaison_1 = Progressbar(progress_window_combinaison, length = 200, mode = "determinate")
    progress_bar_combinaison_2 = Progressbar(progress_window_combinaison, length = 200, mode = "determinate")
    demarrer_combinaison = Button(progress_window_combinaison ,text = "Demarrer",command = functools.partial(combinaisons,lst_jetons[0],lst_jetons[1],lst_jetons[2],lst_jetons[3],lst_jetons[4]))
    # demarrer_combinaison.pack(side = BOTTOM) 
    generation_combinaison.pack(side = TOP)
    progress_bar_combinaison_1.pack(side = TOP)
    progress_bar_combinaison_2.pack(side = TOP)
    lst_combinaison_init = demarrer_combinaison.invoke()
    # lst_combinaison_init = combinaisons(lst_jetons[0],lst_jetons[1],lst_jetons[2],lst_jetons[3],lst_jetons[4])
    progress_window = Toplevel(fenetre)
    test_des_combinaisons = Label(progress_window, text = "Recherche de combinaison optimale")
    progression_bar = Progressbar(progress_window, length= 200, mode ="determinate")
    demarrer = Button(progress_window,text = "Demarrer",command = functools.partial(meilleure_combinaison_init,lst_combinaison_init))
    # demarrer.pack(side = BOTTOM)
    test_des_combinaisons.pack(side = TOP)
    progression_bar.pack(side = TOP)
    meilleure_combinaison = demarrer.invoke()
    if len(meilleure_combinaison[0])==14 and len(meilleure_combinaison[1])==15:
        essoreuse = [essoreuse_save[0]] + copy.deepcopy(list(meilleure_combinaison[0]))
        presse = [presse_save[0]] + copy.deepcopy(list(meilleure_combinaison[1]))
    else:
        essoreuse = [300] + copy.deepcopy(list(meilleure_combinaison[0]))
        presse = [300] + copy.deepcopy(list(meilleure_combinaison[1]))
    interface_graphique(Tapis_essoreuse,Tapis_presse,essoreuse,presse,Stock_bas,Stock_haut,Sortie_1,Sortie_2,Sortie_3,Sortie_4,Sortie_5,Sortie_6,classement_essoreuse_presse)
    fenetre.update_idletasks()




def meilleures_combinaison(lst_combinaison):  # Valide 3.9 compatible
    global Sortie_1
    global Sortie_2
    global Sortie_3
    global Sortie_4
    global Sortie_5
    global Sortie_6
    global essoreuse
    global presse
    global Tapis_presse
    global Tapis_essoreuse
    global Stock_bas
    global Stock_haut
    global Sortie_1_end
    global Sortie_2_end
    global Sortie_3_end
    global Sortie_4_end
    global Sortie_5_end
    global Sortie_6_end
    global essoreuse_end
    global presse_end
    global Stock_bas_end
    global Stock_haut_end
    global Tapis_presse_end
    global Tapis_essoreuse_end
    global Sortie_1_save
    global Sortie_2_save
    global Sortie_3_save
    global Sortie_4_save
    global Sortie_5_save
    global Sortie_6_save
    global essoreuse_save
    global presse_save
    global Stock_bas_save
    global Stock_haut_save
    global Tapis_presse_save
    global Tapis_essoreuse_save
    global Sortie_1_depart
    global Sortie_2_depart
    global Sortie_3_depart
    global Sortie_4_depart
    global Sortie_5_depart
    global Sortie_6_depart
    global Stock_bas_depart
    global Stock_haut_depart
    global Tapis_presse_depart
    global Tapis_essoreuse_depart
    global presse_depart
    global essoreuse_depart
    Sortie_1_depart = copy.deepcopy(Sortie_1)
    Sortie_2_depart = copy.deepcopy(Sortie_2)
    Sortie_3_depart = copy.deepcopy(Sortie_3)
    Sortie_4_depart = copy.deepcopy(Sortie_4)
    Sortie_5_depart = copy.deepcopy(Sortie_5)
    Sortie_6_depart = copy.deepcopy(Sortie_6)
    essoreuse_depart = copy.deepcopy(essoreuse)
    presse_depart = copy.deepcopy(presse)
    Tapis_presse_depart = copy.deepcopy(Tapis_presse)
    Tapis_essoreuse_depart = copy.deepcopy(Tapis_essoreuse)
    Stock_bas_depart = copy.deepcopy(Stock_bas)
    Stock_haut_depart = copy.deepcopy(Stock_haut)
    ind_meilleur_combi=0
    attente_mini = 10000000000000000000000
    progression_bar.start()
    progress_window.update()
    n=len(lst_combinaison)
    for k in range(len(lst_combinaison)):
        progress= int(100* k/n)
        progression_bar['value']= progress
        fenetre.update_idletasks()
        Sortie_1=copy.deepcopy(Sortie_1_depart)
        Sortie_2=copy.deepcopy(Sortie_2_depart)
        Sortie_3=copy.deepcopy(Sortie_3_depart)
        Sortie_4=copy.deepcopy(Sortie_4_depart)
        Sortie_5=copy.deepcopy(Sortie_5_depart)
        Sortie_6=copy.deepcopy(Sortie_6_depart)
        Stock_bas=copy.deepcopy(Stock_bas_depart)
        Stock_haut=copy.deepcopy(Stock_haut_depart)
        Tapis_presse=copy.deepcopy(Tapis_presse_depart)
        Tapis_essoreuse=copy.deepcopy(Tapis_essoreuse_depart)
        essoreuse = copy.deepcopy(essoreuse_depart) + list(lst_combinaison[k][0])
        presse = copy.deepcopy(presse_depart) + list(lst_combinaison[k][1])
        critere = corps_algo()
        if critere < attente_mini:
            attente_mini = critere
            ind_meilleur_combi = k
            if len(essoreuse_depart)==15 and len(presse_depart)==16:
                Sortie_1_save=copy.deepcopy(Sortie_1_end)
                Sortie_2_save=copy.deepcopy(Sortie_2_end)
                Sortie_3_save=copy.deepcopy(Sortie_3_end)
                Sortie_4_save=copy.deepcopy(Sortie_4_end)
                Sortie_5_save=copy.deepcopy(Sortie_5_end)
                Sortie_6_save=copy.deepcopy(Sortie_6_end)
                essoreuse_save=copy.deepcopy(essoreuse_end)
                presse_save=copy.deepcopy(presse_end)
                Stock_bas_save=copy.deepcopy(Stock_bas_end)
                Stock_haut_save=copy.deepcopy(Stock_haut_end)
                Tapis_presse_save=copy.deepcopy(Tapis_presse_end)
                Tapis_essoreuse_save=copy.deepcopy(Tapis_essoreuse_end)
    progression_bar.stop()
    progress_window.destroy()
    return lst_combinaison[ind_meilleur_combi]











def valide(): # Valide 3.9 compatible
    global progress_bar_combinaison_1
    global progress_bar_combinaison_2
    global progress_window_combinaison
    global progression_bar
    global progress_window
    global jetons_vert
    global jetons_jaune_serviette
    global jetons_jaune_draps
    global jetons_rose
    global jetons_bleu
    global Sortie_1
    global Sortie_2
    global Sortie_3
    global Sortie_4
    global Sortie_5
    global Sortie_6
    global essoreuse
    global presse
    global Tapis_presse
    global Tapis_essoreuse
    global Stock_bas
    global Stock_haut
    global Sortie_1_save
    global Sortie_2_save
    global Sortie_3_save
    global Sortie_4_save
    global Sortie_5_save
    global Sortie_6_save
    global essoreuse_save
    global presse_save
    global Stock_bas_save
    global Stock_haut_save
    global Tapis_presse_save
    global Tapis_essoreuse_save
    global Sortie_1_depart
    global Sortie_2_depart
    global Sortie_3_depart
    global Sortie_4_depart
    global Sortie_5_depart
    global Sortie_6_depart
    global Stock_bas_depart
    global Stock_haut_depart
    global Tapis_presse_depart
    global Tapis_essoreuse_depart
    global presse_depart
    global essoreuse_depart
    Sortie_1 = copy.deepcopy(Sortie_1_save)
    Sortie_2 = copy.deepcopy(Sortie_2_save)
    Sortie_3 = copy.deepcopy(Sortie_3_save)
    Sortie_4 = copy.deepcopy(Sortie_4_save)
    Sortie_5 = copy.deepcopy(Sortie_5_save)
    Sortie_6 = copy.deepcopy(Sortie_6_save)
    Stock_bas = copy.deepcopy(Stock_bas_save)
    Stock_haut = copy.deepcopy(Stock_haut_save)
    Tapis_presse = copy.deepcopy(Tapis_presse_save)
    Tapis_essoreuse = copy.deepcopy(Tapis_essoreuse_save)
    size = 15
    lst_jetons=[int(jetons_vert.get()),int(jetons_jaune_serviette.get()),int(jetons_jaune_draps.get()),int(jetons_rose.get()),int(jetons_bleu.get())]
    progress_window_combinaison=Toplevel(fenetre)
    generation_combinaison = Label(progress_window_combinaison, text = "Generation des combinaisons")
    progress_bar_combinaison_1= Progressbar(progress_window_combinaison, length = 200, mode = "determinate")
    progress_bar_combinaison_2= Progressbar(progress_window_combinaison, length = 200, mode = "determinate")
    demarrer_combinaison = Button(progress_window_combinaison ,text = "Demarrer",command = functools.partial(combinaisons,lst_jetons[0],lst_jetons[1],lst_jetons[2],lst_jetons[3],lst_jetons[4]))
    # demarrer_combinaison.pack(side = BOTTOM)
    generation_combinaison.pack(side = TOP)
    progress_bar_combinaison_1.pack(side = TOP)
    progress_bar_combinaison_2.pack(side = TOP)
    lst_combinaison = demarrer_combinaison.invoke()
    # lst_combinaison = combinaisons(lst_jetons[0],lst_jetons[1],lst_jetons[2],lst_jetons[3],lst_jetons[4])
    
    progress_window = Toplevel(fenetre)
    test_des_combinaisons = Label(progress_window, text = "Recherche de combinaison optimale")
    progression_bar = Progressbar(progress_window, length= 200, mode ="determinate")
    demarrer = Button(progress_window,text = "Demarrer",command = functools.partial(meilleures_combinaison,lst_combinaison))
    # demarrer.pack(side = BOTTOM)
    test_des_combinaisons.pack(side = TOP)
    progression_bar.pack(side = TOP)
    meilleure_combinaison = demarrer.invoke()
    meilleure_essoreuse = copy.deepcopy(list(meilleure_combinaison[0]))
    meilleure_presse = copy.deepcopy(list(meilleure_combinaison[1]))
    if len(meilleure_essoreuse)!= 0:
        next_essoreuse = [meilleure_essoreuse[0]]
    else:
        next_essoreuse = []
    if len(meilleure_presse)!=0:
        next_presse = [meilleure_presse[0]]
    else: 
        next_presse = []
    essoreuse = copy.deepcopy(essoreuse_depart) + next_essoreuse
    presse = copy.deepcopy(presse_depart) + next_presse
    if len(essoreuse)==16 and len(presse)==17:
        Sortie_1=copy.deepcopy(Sortie_1_depart)
        Sortie_2=copy.deepcopy(Sortie_2_depart)
        Sortie_3=copy.deepcopy(Sortie_3_depart)
        Sortie_4=copy.deepcopy(Sortie_4_depart)
        Sortie_5=copy.deepcopy(Sortie_5_depart)
        Sortie_6=copy.deepcopy(Sortie_6_depart)
        Stock_bas=copy.deepcopy(Stock_bas_depart)
        Stock_haut=copy.deepcopy(Stock_haut_depart)
        Tapis_presse=copy.deepcopy(Tapis_presse_depart)
        Tapis_essoreuse=copy.deepcopy(Tapis_essoreuse_depart)
        corps_algo()
        essoreuse = copy.deepcopy(essoreuse_end)
        presse = copy.deepcopy(presse_end)
    interface_graphique(Tapis_essoreuse_save,Tapis_presse_save,essoreuse,presse,Stock_bas_save,Stock_haut_save,Sortie_1_save,Sortie_2_save,Sortie_3_save,Sortie_4_save,Sortie_5_save,Sortie_6_save,classement_essoreuse_presse)
    fenetre.update_idletasks()










def suite(): # Valide 3.9 compatible
    global fenetre
    global jetons_vert
    global jetons_jaune_serviette
    global jetons_jaune_draps
    global jetons_rose
    global jetons_bleu
    for widget in fenetre.winfo_children():
        widget.destroy()
    size = 15
    bouton_quit = Button(fenetre, text="Quitter", command=fenetre.quit)
    bouton_valide = Button(fenetre, text= "Valider", command=valide)
    choix_jeton = Frame(fenetre)
    choix = Frame(choix_jeton)
    jetons = Frame(choix_jeton )
    jeton_vert_canvas = Canvas(jetons,width = 10*size + 5,height=10*size + 5 )
    jeton_vert_canvas.create_oval(5 , 5 ,  10 * size  + 5,10 * size + 5 ,  fill="green", outline="")
    jeton_jaune_serviette_canvas = Canvas(jetons,width = 10*size + 5,height=10*size + 5)
    jeton_jaune_serviette_canvas.create_oval(5 , 5 ,  10 * size + 5,10 * size + 5 ,  fill="#DBEA45", outline="")
    jeton_jaune_draps_canvas = Canvas(jetons,width = 10*size + 5,height=10*size + 5)
    jeton_jaune_draps_canvas.create_oval(5 , 5 ,  10 * size + 5,10 * size + 5 ,  fill="yellow", outline="")
    jeton_rose_canvas = Canvas(jetons,width = 10*size + 5,height=10*size + 5)
    jeton_rose_canvas.create_oval(5 , 5 ,  10 * size  + 5,10 * size + 5 ,  fill="pink", outline="")
    jeton_bleu_canvas = Canvas(jetons,width = 10*size + 5,height=10*size + 5)
    jeton_bleu_canvas.create_oval(5 , 5 ,  10 * size  + 5,10 * size + 5 ,  fill="blue", outline="")
    jetons_vert = DoubleVar()
    scale_vert = Scale(choix, orient="horizontal", activebackground="green", from_=0, to=10, resolution = 1,tickinterval =1, length = 10 * size + 5, label="Nombre de jetons vert",variable=jetons_vert)
    jetons_jaune_serviette = DoubleVar()
    scale_jaune_serviette = Scale(choix, orient="horizontal", activebackground="#DBEA45", from_=0, to=10, resolution = 1,tickinterval =1, length = 10 * size + 5, label="Nombre de jetons jeune (serviette)",variable=jetons_jaune_serviette)
    jetons_jaune_draps = DoubleVar()
    scale_jaune_draps = Scale(choix, orient="horizontal", activebackground="yellow", from_=0, to=10, resolution = 1,tickinterval =1, length = 10 * size + 5, label="Nombre de jetons jaune (draps",variable=jetons_jaune_draps)
    jetons_rose = DoubleVar()
    scale_rose = Scale(choix, orient="horizontal", activebackground="pink", from_=0, to=10, resolution = 1,tickinterval =1, length = 10 * size + 5, label="Nombre de jetons rose",variable=jetons_rose)
    jetons_bleu = DoubleVar()
    scale_bleu = Scale(choix, orient="horizontal",activebackground="blue", from_=0, to=10, resolution = 1,tickinterval =1, length = 10 * size + 5, label="Nombre de jetons bleu",variable=jetons_bleu)



    jeton_vert_canvas.pack(side = LEFT)
    jeton_jaune_serviette_canvas.pack(side = LEFT)
    jeton_jaune_draps_canvas.pack(side = LEFT)
    jeton_rose_canvas.pack(side = LEFT)
    jeton_bleu_canvas.pack(side = LEFT)
    scale_vert.pack(side = LEFT)
    scale_jaune_serviette.pack(side = LEFT)
    scale_jaune_draps.pack(side = LEFT)
    scale_rose.pack(side = LEFT)
    scale_bleu.pack(side = LEFT)

    bouton_quit.pack(side = TOP)
    jetons.pack(side = TOP)
    choix.pack(side = BOTTOM)
    choix_jeton.pack()
    bouton_valide.pack(side = BOTTOM)







def version_finale(): # Valide 3.9 compatible
    global fenetre
    global jetons_vert
    global jetons_jaune_serviette
    global jetons_jaune_draps
    global jetons_rose
    global jetons_bleu
    size = 15

    bouton_quit = Button(fenetre, text="Quitter", command=fenetre.quit)
    bouton_valide = Button(fenetre, text= "Valider", command=valide_init)
    choix_jeton = Frame(fenetre)
    choix = Frame(choix_jeton)
    jetons = Frame(choix_jeton )
    jeton_vert_canvas = Canvas(jetons,width = 10*size + 5,height=10*size + 5 )
    jeton_vert_canvas.create_oval(5 , 5 ,  10 * size  + 5,10 * size + 5 ,  fill="green", outline="")
    jeton_jaune_serviette_canvas = Canvas(jetons,width = 10*size + 5,height=10*size + 5)
    jeton_jaune_serviette_canvas.create_oval(5 , 5 ,  10 * size + 5,10 * size + 5 ,  fill="#DBEA45", outline="")
    jeton_jaune_draps_canvas = Canvas(jetons,width = 10*size + 5,height=10*size + 5)
    jeton_jaune_draps_canvas.create_oval(5 , 5 ,  10 * size + 5,10 * size + 5 ,  fill="yellow", outline="")
    jeton_rose_canvas = Canvas(jetons,width = 10*size + 5,height=10*size + 5)
    jeton_rose_canvas.create_oval(5 , 5 ,  10 * size  + 5,10 * size + 5 ,  fill="pink", outline="")
    jeton_bleu_canvas = Canvas(jetons,width = 10*size + 5,height=10*size + 5)
    jeton_bleu_canvas.create_oval(5 , 5 ,  10 * size  + 5,10 * size + 5 ,  fill="blue", outline="")
    jetons_vert = DoubleVar()
    scale_vert = Scale(choix, orient="horizontal", activebackground="green", from_=0, to=10, resolution = 1,tickinterval =1, length = 10 * size + 5, label="Nombre de jetons vert",variable=jetons_vert)
    jetons_jaune_serviette = DoubleVar()
    scale_jaune_serviette = Scale(choix, orient="horizontal", activebackground="#DBEA45", from_=0, to=10, resolution = 1,tickinterval =1, length = 10 * size + 5, label="Nombre de jetons jeune (serviette)",variable=jetons_jaune_serviette)
    jetons_jaune_draps = DoubleVar()
    scale_jaune_draps = Scale(choix, orient="horizontal", activebackground="yellow", from_=0, to=10, resolution = 1,tickinterval =1, length = 10 * size + 5, label="Nombre de jetons jaune (draps",variable=jetons_jaune_draps)
    jetons_rose = DoubleVar()
    scale_rose = Scale(choix, orient="horizontal", activebackground="pink", from_=0, to=10, resolution = 1,tickinterval =1, length = 10 * size + 5, label="Nombre de jetons rose",variable=jetons_rose)
    jetons_bleu = DoubleVar()
    scale_bleu = Scale(choix, orient="horizontal",activebackground="blue", from_=0, to=10, resolution = 1,tickinterval =1, length = 10 * size + 5, label="Nombre de jetons bleu",variable=jetons_bleu)



    jeton_vert_canvas.pack(side = LEFT)
    jeton_jaune_serviette_canvas.pack(side = LEFT)
    jeton_jaune_draps_canvas.pack(side = LEFT)
    jeton_rose_canvas.pack(side = LEFT)
    jeton_bleu_canvas.pack(side = LEFT)
    scale_vert.pack(side = LEFT)
    scale_jaune_serviette.pack(side = LEFT)
    scale_jaune_draps.pack(side = LEFT)
    scale_rose.pack(side = LEFT)
    scale_bleu.pack(side = LEFT)

    bouton_quit.pack(side = TOP)
    jetons.pack(side = TOP)
    choix.pack(side = BOTTOM)
    choix_jeton.pack()
    bouton_valide.pack(side = BOTTOM)
    fenetre.mainloop()
    return



version_finale()

