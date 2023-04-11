import tkinter as tk

fenetre = tk()
# Ajout d'un titre à la fenêtre principale :
fenetre.title("Cryptanalyse")
# Définir les dimensions par défaut la fenêtre principale :
fenetre.geometry("640x480")
 # = fenetre pas redimensionnable dans longeur et largeur, figer les dimenssions
fenetre.resizable(height=False, width=False)  
# Ajout d'un texte dans la fenêtre :
texte1 = Label (fenetre, text = "Veuillez choisir votre cryptage")
texte1.pack()

# Fonction bouton 1

def create_Cesar ():  

    """Création de la fonction permettant l'affichage du plateau de jeu lorsqu'on
        clique sur le bouton du mode 1 joueur"""

    Cryptanalyse=Toplevel()

    Cryptanalyse.geometry("640x480")#taille de la fenetre

    Cryptanalyse.title("Cryptanalyse")#titre de la fenetre
    texte2 = Label(Cryptanalyse,text ="Mettez votre message et entrez votre clé")
    texte2.pack()
    cle1 = Spinbox(Cryptanalyse, from_=0, to=26)
    cle1.pack()
    # entrée
    value1 = StringVar() 
    value1.set("texte par défaut")
    entree1 = Entry(Cryptanalyse, textvariable= str, width=30)
    entree1.pack()
    bouton_crypter = Button (Cryptanalyse, text = "Crypter", command = cryptage)
    bouton_crypter.pack()
    # entrée
    value2 = StringVar() 
    value2.set("texte par défaut")
    entree2 = Entry(Cryptanalyse, textvariable=str, width=30)
    entree2.pack()
    texte3 = Label(Cryptanalyse, text="Mettez votre message pour le dechiffreret et entrez votre clé")
    texte3.pack()
    cle1 = Spinbox(Cryptanalyse, from_=0, to=26)
    cle1.pack()
    value3 = StringVar() 
    value3.set("texte par défaut")
    entree3 = Entry(Cryptanalyse, textvariable=str, width=30)
    entree3.pack()
    bouton_decrypter = Button (Cryptanalyse, text= "Décrypter", command=decrypt_cesar)
    bouton_decrypter.pack()
    value4 = StringVar() 
    value4.set("texte par défaut")
    entree4 = Entry(Cryptanalyse, textvariable=str, width=30)
    entree4.pack()

def create_Vigenere ():  

    """Création de la fonction permettant l'affichage du plateau de jeu lorsqu'on
        clique sur le bouton du mode 1 joueur"""

    Cryptanalyse=Toplevel()

    Cryptanalyse.geometry("640x480")#taille de la fenetre

    Cryptanalyse.title("Cryptanalyse")#titre de la fenetre
    texte2 = Label(Cryptanalyse,text ="Mettez votre message et entrez votre clé")
    texte2.pack()
    cle1 = Spinbox(Cryptanalyse, from_=0, to=26)
    cle1.pack()
    # entrée
    value1 = StringVar() 
    value1.set("texte par défaut")
    entree1 = Entry(Cryptanalyse, textvariable= str, width=30)
    entree1.pack()
    bouton_crypter = Button (Cryptanalyse, text = "Crypter")
    bouton_crypter.pack()
    # entrée
    value2 = StringVar() 
    value2.set("texte par défaut")
    entree2 = Entry(Cryptanalyse, textvariable=str, width=30)
    entree2.pack()
    texte3 = Label(Cryptanalyse, text="Mettez votre message pour le dechiffreret et entrez votre clé")
    texte3.pack()
    cle1 = Spinbox(Cryptanalyse, from_=0, to=26)
    cle1.pack()
    value3 = StringVar() 
    value3.set("texte par défaut")
    entree3 = Entry(Cryptanalyse, textvariable=str, width=30)
    entree3.pack()
    bouton_decrypter = Button (Cryptanalyse, text= "Décrypter")
    bouton_decrypter.pack()
    value4 = StringVar() 
    value4.set("texte par défaut")
    entree4 = Entry(Cryptanalyse, textvariable=str, width=30)
    entree4.pack()

def create_Scytal ():  

    """Création de la fonction permettant l'affichage du plateau de jeu lorsqu'on
        clique sur le bouton du mode 1 joueur"""

    Cryptanalyse=Toplevel()

    Cryptanalyse.geometry("640x480")#taille de la fenetre

    Cryptanalyse.title("Cryptanalyse")#titre de la fenetre
    texte2 = Label(Cryptanalyse,text ="Mettez votre message et entrez votre clé")
    texte2.pack()
    cle1 = Spinbox(Cryptanalyse, from_=0, to=26)
    cle1.pack()
    # entrée
    value1 = StringVar() 
    value1.set("texte par défaut")
    entree1 = Entry(Cryptanalyse, textvariable= str, width=30)
    entree1.pack()
    bouton_crypter = Button (Cryptanalyse, text = "Crypter")
    bouton_crypter.pack()
    # entrée
    value2 = StringVar() 
    value2.set("texte par défaut")
    entree2 = Entry(Cryptanalyse, textvariable=str, width=30)
    entree2.pack()
    texte3 = Label(Cryptanalyse, text="Mettez votre message pour le dechiffreret et entrez votre clé")
    texte3.pack()
    cle1 = Spinbox(Cryptanalyse, from_=0, to=26)
    cle1.pack()
    value3 = StringVar() 
    value3.set("texte par défaut")
    entree3 = Entry(Cryptanalyse, textvariable=str, width=30)
    entree3.pack()
    bouton_decrypter = Button (Cryptanalyse, text= "Décrypter")
    bouton_decrypter.pack()
    value4 = StringVar() 
    value4.set("texte par défaut")
    entree4 = Entry(Cryptanalyse, textvariable=str, width=30)
    entree4.pack()

def create_Submonoalpha ():  

    """Création de la fonction permettant l'affichage du plateau de jeu lorsqu'on
        clique sur le bouton du mode 1 joueur"""

    Cryptanalyse=Toplevel()

    Cryptanalyse.geometry("640x480")#taille de la fenetre

    Cryptanalyse.title("Cryptanalyse")#titre de la fenetre
    texte2 = Label(Cryptanalyse,text ="Mettez votre message et entrez votre clé")
    texte2.pack()
    cle1 = Spinbox(Cryptanalyse, from_=0, to=26)
    cle1.pack()
    # entrée
    value1 = StringVar() 
    value1.set("texte par défaut")
    entree1 = Entry(Cryptanalyse, textvariable= str, width=30)
    entree1.pack()
    bouton_crypter = Button (Cryptanalyse, text = "Crypter")
    bouton_crypter.pack()
    # entrée
    value2 = StringVar() 
    value2.set("texte par défaut")
    entree2 = Entry(Cryptanalyse, textvariable=str, width=30)
    entree2.pack()
    texte3 = Label(Cryptanalyse, text="Mettez votre message pour le dechiffreret et entrez votre clé")
    texte3.pack()
    cle1 = Spinbox(Cryptanalyse, from_=0, to=26)
    cle1.pack()
    value3 = StringVar() 
    value3.set("texte par défaut")
    entree3 = Entry(Cryptanalyse, textvariable=str, width=30)
    entree3.pack()
    bouton_decrypter = Button (Cryptanalyse, text= "Décrypter")
    bouton_decrypter.pack()
    value4 = StringVar() 
    value4.set("texte par défaut")
    entree4 = Entry(Cryptanalyse, textvariable=str, width=30)
    entree4.pack()
# Ajout d'un bouton dans la fenêtre :
bouton_Cesar = Button (fenetre, text = "Code Cesar", command = create)
bouton_Cesar = Button (fenetre, text = "Code Cesar", command = create_Cesar)
bouton_Cesar.pack()
bouton_Vigenere = Button (fenetre, text = "Chiffre Vigenere", command= create)
bouton_Vigenere = Button (fenetre, text = "Chiffre Vigenere", command= create_Vigenere)
bouton_Vigenere.pack()
bouton_Scytal = Button (fenetre, text = "Scytal", command = create)
bouton_Scytal = Button (fenetre, text = "Scytal", command = create_Scytal)
bouton_Scytal.pack()
bouton_Submonoalpha = Button (fenetre, text = "Substituion Monoalphabetique", command = create)
bouton_Submonoalpha = Button (fenetre, text = "Substituion Monoalphabetique", command = create_Submonoalpha)
bouton_Submonoalpha.pack()

def create():
    newfenetre = tk.Toplevel()
    labelExample = tk.Label(newWindow, text = "New Window")
    buttonExample = tk.Button(newWindow, text = "New Window button")
#def create():
    #newfenetre = Toplevel(fenetre)
    #newfenetre.pack()
    #labelExample = Label(fenetre, text = "New Window")
    #labelExample.pack()
    #buttonExample = Button(fenetre, text = "New Window button")
    #buttonExample.pack()
    #labelExample.grid(column= 0, row = 0)

# Affichage de la fenêtre créée : 
fenetre.mainloop()