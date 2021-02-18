import tkinter as tk

#fenetre

fenetre = tk.Tk()
fenetre.title("somme")

#widgets


colonne_11 = tk.Label(fenetre,texte="25",font= ("helvetica", "26"))
colonne_12 = tk.Label(fenetre,texte="+", font = ("helvetica", "26"))
colonne_13 = tk.Label(fenetre,texte="12", font = ("helvetica", "26"))
colonne_14 = tk.Label(fenetre,texte="=", font = ("helvetica", "26"))
colonne_15 = tk.Label(fenetre,texte="37", font = ("helvetica", "26"))
colonne_21 = tk.Label(fenetre,texte="choisir une valeur pour le paramètre de gauche", font = ("helvetica", "26"))
colonne_22 = tk.Label(fenetre,texte="calculer", font = ("helvetica", "26"))
colonne_31 = tk.Label(fenetre,texte="choisir une valeur pour le paramètre de droite", font = ("helvetica", "26"))

#positionnement 

#ligne 1

colonne_11.grid(column= 2, row=0, padx=10 )
colonne_12.grid(column=4, row=0, padx=10)
colonne_13.grid(column=3, row=0, padx=10)
colonne_14.grid(column=5, row=0, padx=10)
colonne_15.grid(column=6, row=0, padx=10)

#ligne 2

colonne_21.grid(column=1, row=1, padx=50)
colonne_22.grid(column=3, row=1, padx=20, columnspan=3)

#ligne 3

colonne_31.grid(column=1, row=2, padx=10)

fenetre.mainloop()