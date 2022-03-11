import random

def nb_lignes(nom_fichier):
    fic = open(nom_fichier, "r")
    cpt = 0
    for ligne in fic:
        cpt +=1
    fic.close()
    return cpt

def ecrit_liste_mots(n):
    fic_in = open("words.txt" , "r")
    fic_out = open("words" + str(n)+ ".txt", "w")
    for ligne in fic_in:
        if len(ligne) == n+1:
            fic_out.write(ligne)
    fic_in.close()
    fic_out.close()

ecrit_liste_mots(5)
print(nb_lignes("words5.txt"))