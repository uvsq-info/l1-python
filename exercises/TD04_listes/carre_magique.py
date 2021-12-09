carre_mag = [[4, 14, 15, 1], [9, 7, 6, 12], [5, 11, 10, 8], [16, 2, 3, 13]]

# La ligne suivante ne fonctionne pas. Si vous copiez des listes de cette
# façon, les deux listes partageront la même zone mémoire : Une modification
# de l’une entraine la modification de l’autre.
# Le constater avec https://pythontutor.com/
carre_pas_mag = carre_mag

# La ligne suivante ne fonctionne pas non plus. Les deux listes seront
# distinctes mais les sous-listes qu'elles contiennent partageront la même
# zone mémoire. Le constater avec https://pythontutor.com/
carre_pas_mag = carre_mag.copy()

# Solution de "deep copy" n°1 :
# Avec deux boucles for, nous copions chaque élément un par un.
carre_pas_mag = []
for num_ligne in range(len(carre_mag)):
    carre_pas_mag.append([])
    for num_colonne in range(len(carre_mag[num_ligne])):
        carre_pas_mag[num_ligne].append(carre_mag[num_ligne][num_colonne])

# Solution de "deep copy" n°2 :
# Nous copions chaque sous-liste une par une.
carre_pas_mag = []
for ligne in carre_mag:
    carre_pas_mag.append(ligne.copy())

# Solution de copie profonde n°3 :
# Même chose mais avec l'écriture "en compréhension".
carre_pas_mag = [ligne[:] for ligne in carre_mag]

# Changer le 3 en 7
carre_pas_mag[3][2] = 7


def afficheCarre(carre: list) -> None:
    """ Affiche la liste à 2 dimensions carre comme un carré"""
    for ligne in carre:
        print(ligne)
    print()


afficheCarre(carre_mag)
afficheCarre(carre_pas_mag)


# Solution 1 : Sans utiliser la fonction sum()
def testLignesEgalesv1(carre: list) -> int:
    """ Renvoie la somme des éléments d'une ligne de la liste 2D
        carre si toutes les lignes ont la même somme, et -1 sinon """
    somme = -1
    for ligne in carre:
        somme_courante = 0
        for element in ligne:
            somme_courante += element
        if somme == -1:
            somme = somme_courante
        elif somme_courante != somme:
            return -1
    return somme


# Solution 2 : En utilisant la fonction sum()
def testLignesEgales(carre: list) -> int:
    """ Renvoie la somme des éléments d'une ligne de la liste 2D
        carre si toutes les lignes ont la même somme, et -1 sinon """
    somme = sum(carre[0])
    for ligne in carre:
        if sum(ligne) != somme:
            return -1
    return somme


print(testLignesEgales(carre_mag))
print(testLignesEgales(carre_pas_mag))


def testColonnesEgales(carre: list) -> int:
    """ Renvoie la somme des éléments d'une colonne de la liste 2D
        carre si toutes les colonnes ont la même somme, et -1 sinon """
    colonne_1 = [ligne[0] for ligne in carre]
    somme = sum(colonne_1)
    for num_colonne in range(1, len(carre)):
        colonne = [ligne[num_colonne] for ligne in carre]
        if sum(colonne) != somme:
            return -1
    return somme


print(testColonnesEgales(carre_mag))
print(testColonnesEgales(carre_pas_mag))


def testDiagonalesEgales(carre: list) -> int:
    """ Renvoie la somme des éléments d'une diagonale de la liste 2D
        carre si les 2 diagonales ont la même somme, et -1 sinon """
    taille = len(carre)
    diagonale_1 = [carre[i][i] for i in range(taille)]
    diagonale_2 = [carre[i][taille - i - 1] for i in range(taille)]
    somme_1 = sum(diagonale_1)
    if sum(diagonale_2) != somme_1:
        return -1
    else:
        return somme_1


print(testDiagonalesEgales(carre_mag))
print(testDiagonalesEgales(carre_pas_mag))


def estCarreMagique(carre: list) -> bool:
    """ Renvoie True si c'est un carre magique et False sinon"""
    return testLignesEgales(carre) == testColonnesEgales(carre) \
        and testLignesEgales(carre) == testDiagonalesEgales(carre) \
        and testLignesEgales(carre) != -1


print(estCarreMagique(carre_mag))
print(estCarreMagique(carre_pas_mag))


# Solution 1 : Créer une liste contenant tous les nombres du carré puis tester
# que chaque entier de 1 à n² est présent dans cette liste
def estNormalv1(carre: list) -> bool:
    """ Retourne True si contient toutes les valeurs de 1 à n^2 où n est la taille
        du carré, et False sinon """
    liste = []
    for ligne in carre:
        liste.extend(ligne)
    taille = len(carre)
    for entier in range(1, taille*taille + 1):
        if entier not in liste:
            return False
    return True


# Solution 2 : Tester que chaque entier de 1 à n² est présent dans au moins
# une ligne du carré
def estNormalv2(carre: list) -> bool:
    """ Retourne True si contient toutes les valeurs de 1 à n^2 où n est la taille
        du carré, et False sinon """
    taille = len(carre)
    for entier in range(1, taille*taille + 1):
        est_present = False
        for ligne in carre:
            if entier in ligne:
                est_present = True
                break
        if not est_present:
            return False
    return True


# Solution 3 : Créer une liste contenant tous les entiers de 1 à n²
# et parcourir tout le carré en les retirant de la liste au fur et à mesure.
def estNormalv3(carre: list) -> bool:
    """ Retourne True si contient toutes les valeurs de 1 à n^2 où n est la taille
        du carré, et False sinon """
    taille = len(carre)
    nombres = [i for i in range(1, taille * taille + 1)]
    for i in range(taille):
        for j in range(taille):
            if carre[i][j] in nombres:
                nombres.remove(carre[i][j])
    return len(nombres) == 0


print(estNormalv3(carre_mag))
print(estNormalv3(carre_pas_mag))
