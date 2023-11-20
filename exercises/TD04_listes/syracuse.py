
def syracuse(n):
    L=[n]
    while n!=1:
        if n%2==0:
            n=n//2
        else:
            n=n*3+1
        L.append(n)
    return L
print(syracuse(3))



def testeConjecture(n_max):
    if syracuse(n_max)[-1]==1:
        return True
    else:
        return False
print(testeConjecture(10000))

import time
def tempsVol(n):
    return len(syracuse(n))-1
print("Le temps de vol de", 3, "est", tempsVol(3))

def tempsVolListe(n_max):
    return [tempsVol(n)for n in range (1,n_max-1)]
print(tempsVolListe(100))

liste_t=tempsVolListe(10000)
liste_temps_max=max(liste_t)
print("l'entier",liste_t.index(liste_temps_max)+1,"a le plus grand temps de vol égal à ",liste_temps_max)

def alt_max(n):
    return mx(syracuse(n))
def al_max_list(n_max):
    return [alt_max(n)for n in range (n,n_max+1)]

list_alt=al_max_list(10000)
altitude=max(list_alt)
print("l'entier", list_alt.index(altitude)+1,"le plus grand temps vol égal à ",altitude)


carre_mag=[[4,14,15,1],[9,7,6,12],[5,11,10,8],[16,2,3,13]]

afficheCarre(carre_mag)
afficheCarre(carre_pas_mag)
carree_pasmag=[]
for ligne in range (carre_mag):
    carree_pasmag.append(ligne.copy())
carre_mag[3][2]=7

def afficheCarre(carre):
    for ligne in carre:
        print(ligne)
    print()

afficheCarre(carre_mag)
afficheCarre(carree_pasmag)

def testLignesEgales(carre):
    """ Renvoie la somme des éléments d'une ligne de la liste 2D carre si toutes les lignes ont la même somme, et -1 sinon """
    pass

print(testLignesEgales(carre_mag))
print(testLignesEgales(carre_pas_mag))

def test_ligneEgale(carre):
    sommeligne=sum(carre[0])
    for ligne in carre:
        if sommeligne!=sum(carre(ligne)):
            return -1
    return (sommeligne)

def testColonnesEgales(carre):
    """ Renvoie la somme des éléments d'une colonne de la liste 2D carre si toutes les colonnes ont la même somme, et -1 sinon """
    pass

print(testColonnesEgales(carre_mag))
print(testColonnesEgales(carre_pas_mag))

def TestcolonneEgale(carre):
    Colonne_1=[ligne[0] for ligne in carre]
    somme_colonne_1=sum(Colonne_1)
    for num_colonne in range (1,len(carre)):
        colonne=[ligne[num_colonne] for ligne in carre]
        if sum(colonne)!=somme_colonne_1:
            return -1
    return somme_colonne_1

def TestDiagonalEgales(carre):
    D1=[carre[i][i] for i in range (len(carre))]
    D2=[carre[i][len(carre)-i-1] for i in range (len(carre))]
    somme_D1=sum(D1)
    if somme_D1 != sum(D2):
        return -1
    else:
        return somme_D1
    
def est_carre_mag(carre):
    return test_ligneEgale(carre)==testColonnesEgales(carre)and test_ligneEgale(carre)==TestDiagonalEgales(carre) and testLignesEgales(carre)!=-1
