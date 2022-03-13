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

def compare_mots(m1, m2):
    n = len(m1)
    profil = [0] * n
    for i in range(n):
        if m1[i] == m2[i]:
            profil[i] = 1
    for i in range(n):
        if profil[i] == 0:
            for j in range(n):
                if profil[j] != 1 and m1[i] == m2[j]:
                    profil[i] = 2

    return profil

def ecrit_liste_compatible(fichier, m , profil):
    fic_in = open(fichier, "r")
    fic_out = open(fichier + ".comp", "w")
    for ligne in fic_in:
        if compare_mots(m, ligne[:-1]) == profil:
    fic_in.close()
    fic_out.close()

ecrit_liste_compatible("words5.txt.comp", "width" , [1;0,0,2,1])

#print(nb_lignes("words.txt"))
#ecrit_liste_mots(5)
#print(nb_lignes("words5.txt"))
#print(compare_mots("abcde", "acbfb"))