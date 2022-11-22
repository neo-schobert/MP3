

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

temps_presse_Stock_bas=5
temps_presse_Stock_haut=10

temps_essoreuse_Sortie_vert=10
temps_essoreuse_Sortie_jaune_rose_1=30
temps_essoreuse_Sortie_jaune_rose_2=30
temps_essoreuse_Sortie_jaune_rose_3=30
temps_essoreuse_Sortie_jaune_rose_4=30
temps_essoreuse_Sortie_bleu=120


temps_essoreuse_presse=10





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


### Acteur de distribution :
Chariot=[] # de taille 2 Chariot[0]=etat

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



### Fin initialisation ###


### Distribution :



def distribution_temps(k):
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

def diminution_temps(n,k):
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




def temps_transport(etat):
    """
    Entrée: état du chariot

    ----------------------------------------------------

    Sortie: Renvoit la variation de temps nécessaire à aller de cet état à l'état "essoreuse".
    """
    match etat:
        case "essoreuse":
            return 0
        case "presse":
            return temps_essoreuse_presse
        case "Stock_bas":
            return temps_presse_Stock_bas
        case "Stock_haut":
            return temps_presse_Stock_haut
        case "Sortie_vert":
            return Temps_essoreuse_Sortie_vert
        case "Sortie_jaune_rose_1":
            return temps_essoreuse_Sortie_jaune_rose_1
        case "Sortie_jaune_rose_2":
            return temps_essoreuse_Sortie_jaune_rose_2
        case "Sortie_jaune_rose_3":
            return temps_essoreuse_Sortie_jaune_rose_3
        case "Sortie_jaune_rose_4":
            return temps_essoreuse_Sortie_jaune_rose_4
        case "Sortie_bleu":
            return temps_essoreuse_Sortie_bleu


def is_in_case(k,L):
    for i in range(len(L)):
        if k==L[i]:
            return True,case_successeurs[i]
    return False,"nothing"

def case_successeurs(i):
    match i:
        case 0:
            return "essoreuse"
        case 1:
            return "presse"
        case 2:
            return "Stock_bas"
        case 3:
            return "Stock_haut"



def cycle(successeurs):
    if len(Sortie_1)<3:
        if is_in_case(1,successeurs)[0]:
            Sortie_1.append(1)
