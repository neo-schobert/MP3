

# Exercice 6 :

# 1
def compte(L,n):
    liste_occurence = [0] * n
    for k in L:
        liste_occurence[k]+=1
    return liste_occurence

# 2
def tri(L,n):
    liste_occurences = compte(L,n)
    return [liste_occurences[k]*[k] for k in range(n)]


# 3


