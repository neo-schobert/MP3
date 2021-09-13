#Exercice 1:
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

print(suite_p_q_r(10))



#Exercice 3:
#1
def liste_correcte(L):
    return (len(L)==9 and 1 in L and 2 in L and 3 in L and 4 in L and 5 in L and 6 in L and 7 in L and 8 in L and 9 in L)


print(liste_correcte([k for k in range(1,10)]))



#Exercice 4:










#Exercice 5:









#Exercice 6:












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






#Exercice 8:











#Exercice 9:













#Exercice 10:















#Exercice 11:












#Exercice 12:
















#Exercice 13:


















#Exercice 14:













#Exercice 15: