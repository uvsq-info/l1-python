fic_in=open("/Users/bastien/Desktop/l1-python/notes_test.txt", "r")
fic_out=open("moyenne","w")
for ligne in fic_in:
    print(ligne)

fic_in.close()
fic_out.close()