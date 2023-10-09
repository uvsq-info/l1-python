
def afficheCarre(carre):
    for i in carre:
        print(i)

def testLignesEgales(carre):
    egale = []
    for i in carre:
        egale.append(sum(i))
    if egale.count(egale[0]) == len(egale):
        return(egale[0])
    elif egale.count(egale[0]) != len(egale):
        return(-1)

def testColonnesEgales(carre):
    col0=[carre[i][0]for i in range(len(carre))]
    s0 =sum(col0)
    #print("sum col0 =", s0)
    for i in range(len(carre)):
        col=[carre[j][i]for j in range(len(carre))]
        #print("sum col",i,"=", sum(col))
        if sum(col) != s0:
            return(-1)
    return(s0)

def testDiagonalesEgales(carre):
    """ Renvoie la somme des éléments d'une diagonale de la liste 2D carre si les 2 diagonales ont la même somme, et -1 sinon """
    taille = len(carre)
    diag1 = [carre[i][i] for i in range(taille)]
    diag2 = [carre[i][taille-i-1] for i in range(taille)]
    somme = sum(diag1)
    if sum(diag2) != somme:
        return -1
    else:
        return somme

def estCarreMagique(carre):
    """ Renvoie True si c'est un carre magique et False sinon"""
    if testColonnesEgales(carre) == -1 or (testLignesEgales(carre) == -1 or testDiagonalesEgales(carre) == -1):
        return False
    else:
        return True

def estNormal(carre):
    """ Retourne True si contient toutes les valeurs de 1 à n^2 où n est la taille 
        du carré, et False sinon """
    liste = []
    for lignes in carre :
        liste.extend(lignes)
    taille = len(liste)
    for entier in range(1,taille * taille +1):
        if entier not in liste:
            return False     
    return True
    

carre_mag=[[4,14,15,1],[9,7,6,12],[5,11,10,8],[16,2,3,13]]
carre_pas_mag = []
for i in range(len(carre_mag)):
    carre_pas_mag.append([])
    for j in range(len(carre_mag[i])):
        carre_pas_mag[i].append(carre_mag[i][j])
carre_pas_mag[3][2] = 7

print("affiche carré mag")
afficheCarre(carre_mag)
print("affiche carré pas mag")
afficheCarre(carre_pas_mag)

print("----------------------------")

print("carré mag lignes égales")
print(testLignesEgales(carre_mag))
print("")
print("carré pas mag lignes égales")
print(testLignesEgales(carre_pas_mag))

print("----------------------------")

print("carre mag colonnes egales")
print(testColonnesEgales(carre_mag))
print("carre pas mag colonne egales")
print(testColonnesEgales(carre_pas_mag))

print("----------------------------")

print("carre mag diagonales egales")
print(testDiagonalesEgales(carre_mag))
print("carre pas mag diagonales egales")
print(testDiagonalesEgales(carre_pas_mag))

print("----------------------------")

print("est carre mag")
print(estCarreMagique(carre_mag))
print("est carré pas mag")
print(estCarreMagique(carre_pas_mag))

print("----------------------------")

print("est normal carre mag")
print(estNormal(carre_mag))
print("est normal carre pas mag")
print(estNormal(carre_pas_mag))