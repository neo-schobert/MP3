

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

temps_Tapis_1_Sortie_vert=10
temps_Tapis_1_Sortie_jaune_rose_1=30
temps_Tapis_1_Sortie_jaune_rose_2=30
temps_Tapis_1_Sortie_jaune_rose_3=30
temps_Tapis_1_Sortie_jaune_rose_4=30
temps_Tapis_1_Sortie_bleu=120

temps_Tapis_1_Stock_bas=5
temps_Tapis_1_Stock_haut=10

temps_Tapis_2_Sortie_vert=10
temps_Tapis_2_Sortie_jaune_rose_1=30
temps_Tapis_2_Sortie_jaune_rose_2=30
temps_Tapis_2_Sortie_jaune_rose_3=30
temps_Tapis_2_Sortie_jaune_rose_4=30
temps_Tapis_2_Sortie_bleu=120



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

# Liste des états:
# Tapis_1
# Tapis_2
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
                print(L)
                diminution_temps(n-x,k)
    else:
        k[0]=0



def file_pleine_vidage_stock(jeton,etat):
    return



def temps_transport(etat):
    """
    Entrée: état du chariot

    ----------------------------------------------------

    Sortie: Renvoit la variation de temps nécessaire à aller de cet état à l'état "Tapis 1".
    """
    match etat:
        case "Tapis_1":
            return 0
        case "Tapis_2":
            return 0
        case "Stock_bas":
            return temps_Tapis_1_Stock_bas
        case "Stock_haut":
            return temps_Tapis_1_Stock_haut
        case "Sortie_vert":
            return temps_Tapis_1_Sortie_vert
        case "Sortie_jaune_rose_1":
            return temps_Tapis_1_Sortie_jaune_rose_1
        case "Sortie_jaune_rose_2":
            return temps_Tapis_1_Sortie_jaune_rose_2
        case "Sortie_jaune_rose_3":
            return temps_Tapis_1_Sortie_jaune_rose_3
        case "Sortie_jaune_rose_4":
            return temps_Tapis_1_Sortie_jaune_rose_4
        case "Sortie_bleu":
            return temps_Tapis_1_Sortie_bleu



def vidage_chariot(jeton,etat):
    temps=temps_transport(etat)
    match etat:
        case "Tapis 1":
            match jeton:
                case 1:
                    if len(Sortie_1)==4: # Si la file verte est pleine
                        print("probleme de temps")
                    else:
                        diminution_temps(temps_Tapis_1_Sortie_vert-temps) # Diminution du temps
                        Sortie_1.append(jeton) # Ajout du jeton dans la file sortie bleu
                        Chariot[0]="Sortie_vert" # Reset de l'état du chariot (il est à la sortie bleue)
                case 2 | 3 | 4:
                    if len(Sortie_2)==4: # Si la file jaune / rose numéro 2 est pleine
                        if len(Sortie_3)==4: # Si la file jaune / rose numéro 3 est pleine
                            if len(Sortie_4)==4: # Si la file jaune / rose numéro 4 est pleine 
                                if len(Sortie_5)==4:
                                    print("probleme de temps") # Cas du problème
                                else: # Si il y a de la place
                                    diminution_temps(temps_Tapis_1_Sortie_jaune_rose_4-temps) # Diminution du temps
                                    Sortie_5.append(jeton)  # Ajout du jeton dans la file sortie jaune / rose numéro 4
                                    Chariot[0]="Sortie_jaune_rose_4"  # Reset de l'état du chariot (il est à la sortie jaune / rose numéro 4)
                            else: # Si il y a de la place
                                diminution_temps(temps_Tapis_1_Sortie_jaune_rose_3-temps) # Diminution du temps
                                Sortie_4.append(jeton)  # Ajout du jeton dans la file sortie jaune / rose numéro 4
                                Chariot[0]="Sortie_jaune_rose_3"  # Reset de l'état du chariot (il est à la sortie jaune / rose numéro 4)
                        else: # Si il y a de la place
                            diminution_temps(temps_Tapis_1_Sortie_jaune_rose_2-temps) # Diminution du temps
                            Sortie_3.append(jeton)  # Ajout du jeton dans la file sortie jaune / rose numéro 3
                            Chariot[0]="Sortie_jaune_rose_2"  # Reset de l'état du chariot (il est à la sortie jaune / rose numéro 3)
                    else: # Si il y a de la place
                        diminution_temps(temps_Tapis_1_Sortie_jaune_rose_1-temps) # Diminution du temps
                        Sortie_2.append(jeton) # Ajout du jeton dans la file sortie jaune / rose numéro 2
                        Chariot[0]="Sortie_jaune_rose_1" # Reset de l'état du chariot (il est à la sortie jaune / rose numéro 2)
                case 5:
                    if len(Sortie_6)==4:
                        print("probleme de temps")
                    else:
                        diminution_temps(temps_Tapis_1_Sortie_bleu-temps) # Diminution du temps
                        Sortie_6.append(jeton) # Ajout du jeton dans la file sortie bleu
                        Chariot[0]="Sortie_bleu" # Reset de l'état du chariot (il est à la sortie bleue)
        case "Tapis_2":
            match jeton:
                case 1:
                    if len(Sortie_1)==4: # Si la file verte est pleine
                        print("probleme de temps")
                    else:
                        diminution_temps(temps_Tapis_2_Sortie_vert-temps) # Diminution du temps
                        Sortie_1.append(jeton) # Ajout du jeton dans la file sortie bleu
                        Chariot[0]="Sortie_vert" # Reset de l'état du chariot (il est à la sortie bleue)
                case 2 | 3 | 4:
                    if len(Sortie_2)==4: # Si la file jaune / rose numéro 2 est pleine
                        if len(Sortie_3)==4: # Si la file jaune / rose numéro 3 est pleine
                            if len(Sortie_4)==4: # Si la file jaune / rose numéro 4 est pleine 
                                if len(Sortie_5)==4:
                                    print("probleme de temps") # Cas du problème
                                else: # Si il y a de la place
                                    diminution_temps(temps_Tapis_2_Sortie_jaune_rose_4-temps) # Diminution du temps
                                    Sortie_5.append(jeton)  # Ajout du jeton dans la file sortie jaune / rose numéro 4
                                    Chariot[0]="Sortie_jaune_rose_4"  # Reset de l'état du chariot (il est à la sortie jaune / rose numéro 4)
                            else: # Si il y a de la place
                                diminution_temps(temps_Tapis_2_Sortie_jaune_rose_3-temps) # Diminution du temps
                                Sortie_4.append(jeton)  # Ajout du jeton dans la file sortie jaune / rose numéro 4
                                Chariot[0]="Sortie_jaune_rose_3"  # Reset de l'état du chariot (il est à la sortie jaune / rose numéro 4)
                        else: # Si il y a de la place
                            diminution_temps(temps_Tapis_2_Sortie_jaune_rose_2-temps) # Diminution du temps
                            Sortie_3.append(jeton)  # Ajout du jeton dans la file sortie jaune / rose numéro 3
                            Chariot[0]="Sortie_jaune_rose_2"  # Reset de l'état du chariot (il est à la sortie jaune / rose numéro 3)
                    else: # Si il y a de la place
                        diminution_temps(temps_Tapis_2_Sortie_jaune_rose_1-temps) # Diminution du temps
                        Sortie_2.append(jeton) # Ajout du jeton dans la file sortie jaune / rose numéro 2
                        Chariot[0]="Sortie_jaune_rose_1" # Reset de l'état du chariot (il est à la sortie jaune / rose numéro 2)
                case 5:
                    if len(Sortie_6)==4:
                        print("probleme de temps")
                    else:
                        diminution_temps(temps_Tapis_1_Sortie_bleu-temps) # Diminution du temps
                        Sortie_6.append(jeton) # Ajout du jeton dans la file sortie bleu
                        Chariot[0]="Sortie_bleu" # Reset de l'état du chariot (il est à la sortie bleue)



def file_pleine(jeton,etat):
    return



def remplissage_chariot(jeton,etat):
    return





