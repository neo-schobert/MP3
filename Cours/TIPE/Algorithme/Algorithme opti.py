

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

### Temps caractéristiques :

# Temps de transport 

Temps_essoreuse_Sortie_vert=10
temps_essoreuse_Sortie_jaune_rose_1=30
temps_essoreuse_Sortie_jaune_rose_2=30
temps_essoreuse_Sortie_jaune_rose_3=30
temps_essoreuse_Sortie_jaune_rose_4=30
temps_essoreuse_Sortie_bleu=120

temps_essoreuse_Stock_bas=5
temps_essoreuse_Stock_haut=10
temps_essoreuse_presse=10


Temps_presse_Sortie_vert=10
temps_presse_Sortie_jaune_rose_1=30
temps_presse_Sortie_jaune_rose_2=30
temps_presse_Sortie_jaune_rose_3=30
temps_presse_Sortie_jaune_rose_4=30
temps_presse_Sortie_bleu=120

temps_presse_Stock_bas=5
temps_presse_Stock_haut=10
temps_presse_presse=10


# Temps en sortie des jetons :
temps_sortie_vert=120
temps_sortie_jaune_serviette=900
temps_sortie_jaune_drap=2400
temps_sortie_rose=900
temps_sortie_bleue=1


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
# Sortie_vert
# Sortie_jaune_rose_1
# Sortie_jaune_rose_2
# Sortie_jaune_rose_3
# Sortie_jaune_rose_4
# Sortie_bleu

etat_chariot="essoreuse"

### Fin initialisation ###


### Création des listes essoreuses et presse 

essoreuse=[0] # de taille au moins 1 (diminue à chaque cycle)
presse=[0] # de taill au moins 1 (diminue à chaque cycle)

attente_presse = 0
attente_essoreuse = 0



### Distribution :




def distribution_temps(k): # Valide
    """
    Entrée : k une liste de sortie.

    ---------------------------------------------------

    Sortie : Retourne 0 si k est vide ou ne contient qu'un élément. Retourne le temps associé au prochain jeton de la liste sinon.
    """
    if len(k)>1:
        match k[1]:
            case 1:
                return temps_sortie_vert
            case 2:
                return temps_sortie_jaune_serviette
            case 3:
                return temps_sortie_jaune_drap
            case 4:
                return temps_sortie_rose
            case 5:
                return temps_sortie_bleue
    else:
        return 0




def diminution_temps(n,k):    # Valide 
    """
    Applique une diminution de temps n sur la composante temporelle k.
    """
    global attente_essoreuse
    global attente_presse
    if k == essoreuse:
        if k[0] >= n:
            k[0]-= n 
        else:
            attente_essoreuse += n - k[0]
            k[0] = 0
    elif k == presse:
        if k[0] >= n:
            k[0]-= n 
        else:
            attente_presse += n - k[0]
            k[0] = 0
    else:
        if len(k)>1:
            match k[0]:
                case x if x>=n:
                    k[0]-=n
                case x:
                    k.pop(1)
                    k[0]=distribution_temps(k)
                    diminution_temps(n-x,k)
        else:
            k[0]=0


def diminution_temps_all(n): # Valide
    """
    Applique la fonction diminution_temps sur chacune des composante temporelle de notre modélisation.
    """
    for k in [Sortie_1,Sortie_2,Sortie_3,Sortie_4,Sortie_5,Sortie_6,essoreuse,presse]:
        diminution_temps(n,k)
    return




def temps_transport(etat,direction): # Valide
    """
    Entrée: état du chariot, direction du chariot (essoreuse / presse / Stock_bas / Stock_haut)

    ----------------------------------------------------

    Sortie: Renvoit la variation de temps nécessaire à aller de cet état à l'état "essoreuse".
    """
    match direction:
        case "essoreuse":
            match etat:
                case "essoreuse":
                    return 0
                case "presse":
                    return temps_essoreuse_presse
                case "Stock_bas":
                    return temps_essoreuse_Stock_bas
                case "Stock_haut":
                    return temps_essoreuse_Stock_haut
                case "Sortie_1":
                    return Temps_essoreuse_Sortie_vert
                case "Sortie_2":
                    return temps_essoreuse_Sortie_jaune_rose_1
                case "Sortie_3":
                    return temps_essoreuse_Sortie_jaune_rose_2
                case "Sortie_4":
                    return temps_essoreuse_Sortie_jaune_rose_3
                case "Sortie_5":
                    return temps_essoreuse_Sortie_jaune_rose_4
                case "Sortie_6":
                    return temps_essoreuse_Sortie_bleu
        case "presse":
            match etat:
                case "presse":
                    return 0
                case "essoreuse":
                    return temps_essoreuse_presse
                case "Stock_bas":
                    return temps_presse_Stock_bas
                case "Stock_haut":
                    return temps_presse_Stock_haut
                case "Sortie_vert":
                    return Temps_presse_Sortie_vert
                case "Sortie_jaune_rose_1":
                    return temps_presse_Sortie_jaune_rose_1
                case "Sortie_jaune_rose_2":
                    return temps_presse_Sortie_jaune_rose_2
                case "Sortie_jaune_rose_3":
                    return temps_presse_Sortie_jaune_rose_3
                case "Sortie_jaune_rose_4":
                    return temps_presse_Sortie_jaune_rose_4
                case "Sortie_bleu":
                    return temps_presse_Sortie_bleu
        case "Stock_bas":
            match etat:
                case "presse":
                    temps_presse_Stock_bas
                case "essoreuse":
                    temps_essoreuse_Stock_bas
                case x:
                    return (temps_transport(etat, "essoreuse") - 5)
        case "Stock_haut": 
            match etat:
                case "presse":
                    temps_presse_Stock_haut
                case "essoreuse":
                    temps_essoreuse_Stock_haut
                case x:
                    return temps_transport(x, "essoreuse") - 8




def premier_element(L): # Valide
    """
    On entend par premier élément le premier élément n'étant pas un temps.


    Retourne 0 si la liste L est de taille 1 et le premier élément de L sinon.
    """
    if len(L)<=1:
        return 0
    else:
        return L[1]





def places_libres(): # Valide
    """
    Retourne la liste des Sortie qui ont une place libre.
    """
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
    return libres


def etat(k):
    """
    Décodage simple d'un nombre k comme ci-dessous.
    """
    match k:
        case 0:
            return "essoreuse"
        case 1:
            return "presse"
        case 2:
            return "Stock_bas"
        case 3:
            return "Stock_haut"




def actualisation(etat_chariot):
    """
    Entrée : On entre l'etat actuel du chariot

    ----------------------------------------

    Sortie : On sort l'etat actuel du chariot ainsi que la direction qu'il doit prendre pour le remplissage. et la direction pour le remplissage ("essoreuse" si aucune place n'est libre)
    """
    successeurs=[premier_element(essoreuse),premier_element(presse),premier_element(Stock_bas),premier_element(Stock_haut)]
    libres=places_libres()
    cond=True
    k=0
    print(successeurs)
    direction = "essoreuse"
    while cond and k<4:
        match successeurs[k]:
            case 0:
                k+=1
            case 1:
                if "Sortie_1" in libres:
                    cond=False
                    direction = "Sortie_1"
                else:
                    k+=1
            case 2|3|4:
                if "Sortie_2" in libres:
                    cond=False    
                    direction = "Sortie_2"      
                elif "Sortie_3" in libres:
                    cond=False
                    direction = "Sortie_3"
                elif "Sortie_4" in libres:
                    cond=False
                    direction = "Sortie_4" 
                elif "Sortie_5" in libres:
                    cond=False
                    direction = "Sortie_5"
                else:
                    k+=1
                if "Sortie_6" in libres:
                    cond=False
                    direction = "Sortie_6"
                else:
                    k+=1
    if k<4:
        return etat_chariot,etat(k),direction
    else:
        attente = Sortie_1[0]
        prochaine_direction_2 = "essoreuse"
        cond = False
        direction = "essoreuse"
        while not cond: 
            lst_sorties = [Sortie_1[0],Sortie_2[0],Sortie_3[0],Sortie_4[0],Sortie_5[0],Sortie_6[0]]
            for k in range(6):
                if lst_sorties[k]< attente:
                    attente = lst_sorties[k]
                    prochaine_direction_2 = "Sortie_" + str(k)
            match prochaine_direction_2[-1]:
                case 1:
                    prochain_jeton = 1
                case 6:
                    prochain_jeton = 5
                case x:
                    prochain_jeton = 3
            if prochain_jeton == 3:
                cond , prochaine_direction = in_ind( 2 , successeurs)
                if not cond:
                    cond , prochaine_direction = in_ind(3,successeurs)
                    if not cond:
                        cond , prochaine_direction = in_ind(4,successeurs)
            elif prochain_jeton == 1:  
                cond , prochaine_direction = in_ind( 1 , successeurs)
            else:
                cond , prochaine_direction = in_ind ( 5, successeurs)
            diminution_temps_all(attente + temps_transport(etat_chariot,"essoreuse"))
            etat_chariot = "essoreuse"
        return etat_chariot,prochaine_direction,prochaine_direction_2
                



def in_ind(n,successeur):
    cond = False
    k=0
    prochaine_direction_validee = "essoreuse"
    while (not cond) and k < len(successeur):
        if successeur[k]==n:
            cond = True
            prochaine_direction_validee = etat(k)
        k+=1
    return k < len(successeur),prochaine_direction_validee





def remplissage_vidage(etat_chariot,direction,direction_2):
    """
    Entrée : On entre l'etat actuel du chariot, sa direction pour récupérer le pion et la direction qu'il doit enmprunter pour déposer le prochain jeton.

    ------------------------------------------

    Sortie : Retourne le nouvel état du chariot après dépot du jeton.

    """
    if direction == "essoreuse" or direction == "presse":
        diminution_temps_all(temps_transport(etat_chariot,direction)+temps_transport(direction_2,direction))
    else:
        diminution_temps_all(temps_transport(etat_chariot,"presse") + temps_transport(direction_2,"presse"))
    etat_chariot= direction_2
    return etat_chariot







def corps_algo():
    """
    Il s'agit ici du corps du programme, que l'on évaluera pour diverse combinaisons de jeton.
    """
    nombre_jeton_systeme = len(Sortie_1) + len(Sortie_2) + len(Sortie_3) + len(Sortie_4) + len(Sortie_5) + len(Sortie_6) + len(presse) + len(essoreuse) - 8
    etat_chariot = "essoreuse"
    while nombre_jeton_systeme > 0:
        etat_chariot , direction , direction_2 = actualisation(etat_chariot)
        etat_chariot = remplissage_vidage(etat_chariot,direction,direction_2)





essoreuse=[3,2]
presse=[1,2]
corps_algo()

print(essoreuse,presse)