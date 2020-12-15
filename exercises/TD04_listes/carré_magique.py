li1 = [4, 14, 15, 1]
li2 = [9, 7, 6, 12]
li3 = [5, 11, 10, 8]
li4 = [16, 2, 3, 13]
carré_mag = [li1, li2, li3, li4]
print(carré_mag)

carré_pas_mag = [list(l) for l in carré_mag]
print(carré_pas_mag)

carré_pas_mag[3][2] = 7
print(carré_pas_mag)


def afficheCarre(carre):
    """ Affiche la liste à 2 dimensions carre comme un carré"""
    for i in carre:
        print(i)
    print('\n')


afficheCarre(carré_mag)
afficheCarre(carré_pas_mag)


def testLignesEgales(carre):
    """ Renvoie la somme des éléments d'une ligne de la liste 2D carre 
    si toutes les lignes ont la même somme, et -1 sinon """
    som = sum(carre[0])
    for k in carre:
        if sum(k) != som:
            return -1
    return som


print(testLignesEgales(carré_mag))
print(testLignesEgales(carré_pas_mag))


def testColonnesEgales(carre):
    """ Renvoie la somme des éléments d'une colonne de la liste 2D carre
    si toutes les colonnes ont la même somme, et -1 sinon """
    col = [l[0] for l in carre]
    som = sum(col)
    for i in range(1, len(carre)):
        col = [l[i]for l in carre]
        if sum(col) != som:
            return -1
    return som


print(testColonnesEgales(carré_mag))
print(testColonnesEgales(carré_pas_mag))


def testDiagonalesEgales(carre):
    """ Renvoie la somme des éléments d'une diagonale de la liste 2D carre 
    si les 2 diagonales ont la même somme, et -1 sinon """
    n = len(carre)
    diag = [carre[i][i] for i in range(n)]
    anti_diag = [carre[i][n - 1 - i] for i in range(n)]
    som = sum(diag)
    if som == sum(anti_diag):
        return som
    else:
        return -1


print(testDiagonalesEgales(carré_mag))
print(testDiagonalesEgales(carré_pas_mag))

def estCarreMagique(carre):
    """ Renvoie True si c'est un carre magique et False sinon"""
    return testLignesEgales(carre) == testColonnesEgales(carre)\
        and testLignesEgales(carre) == testDiagonalesEgales(carre)\
        and testLignesEgales(carre) != -1

print(estCarreMagique(carré_mag))
print(estCarreMagique(carré_pas_mag))


def estNormal(carre):
    """ Retourne True si contient toutes les valeurs de 1 à n^2 où n est la taille 
        du carré, et False sinon """
    n = len(carre)
    nombres = list(range(1, n*n+1))
    for i in range(n):
        for j in range(n):
            if carre[i][j] in nombres:
                 nombres.remove(carre[i][j])
    return len(nombres) == 0


print(estNormal(carré_mag))
print(estNormal(carré_pas_mag))