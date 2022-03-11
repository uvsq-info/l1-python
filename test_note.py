def moyenne(liste):
    return (int(liste[1]) + int(liste[2]) + int(liste[3])) /3

fic_in = open("notes_test.txt", "r")
fic_out = open("moyenne","w")

for ligne in fic_in:
    liste = ligne.split()
    moy = moyenne(liste)
    fic_out.write(ligne[:-1] + " " + str(moy) + "/n")

fic_in.close()
fic_out.close()