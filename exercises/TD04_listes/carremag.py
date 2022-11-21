carre_mag=[[4,14,15,1],[9,7,6,12],[5,11,10,8],[16,2,3,13]]
carre_pas_mag=[[4,14,15,1],[9,7,6,12],[5,11,10,8],[16,2,7,13]]

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
    sum0 = carre[0][0] + carre[1][1] + carre[2][2] + carre[3][3]
    sum1 = carre[0][3] + carre[1][2] + carre[2][1] + carre[3][0]
    if sum0 == sum1:
        return sum0
    else:
        return -1

def estCarreMagique(carre):
    """ Renvoie True si c'est un carre magique et False sinon"""
    if testColonnesEgales(carre) == -1 or (testLignesEgales(carre) == -1 or testDiagonalesEgales(carre) == -1):
        return False
    else:
        return True

def estNormal(carre):
    """ Retourne True si contient toutes les valeurs de 1 à n^2 où n est la taille 
        du carré, et False sinon """
    n = len(carre)
    s = 0
    liste_triee = []
    for a in range (0, 4):
        for b in range (0, 4):
            liste_triee.append(carre[a][b])
    liste_triee.sort()
    for x in range(1, n ** 2 + 1):
        if x in liste_triee:
            s += 1
    if s == n**2:
        return True
    else:
        return False


print("affiche carré mag")
afficheCarre(carre_mag)
print("affiche carré pas mag")
afficheCarre(carre_pas_mag)

print("")

print("carré mag lignes égales")
print(testLignesEgales(carre_mag))
print("")
print("carré pas mag lignes égales")
print(testLignesEgales(carre_pas_mag))

print("")

print("carre mag colonnes egales")
print(testColonnesEgales(carre_mag))
print("carre pas mag colonne egales")
print(testColonnesEgales(carre_pas_mag))

print("")

print("carre mag diagonales egales")
print(testDiagonalesEgales(carre_mag))
print("carre pas mag diagonales egales")
print(testDiagonalesEgales(carre_pas_mag))

print("")

print("est carre mag")
print(estCarreMagique(carre_mag))
print("est carré pas mag")
print(estCarreMagique(carre_pas_mag))

print("")

print("est normal carre mag")
print(estNormal(carre_mag))
print("est normal carre pas mag")
print(estNormal(carre_pas_mag))