#programme par César Charbey, Kyllian Fauquert et Thomas Brulu.
from tkinter import *
import random

fen=Tk()
fen.title("puissance 4")
fen.geometry("900x800")



Zone=Canvas(fen,width=1000,height=900,bg="white")
Zone.place(x=0,y=0)

#Zone.create_rectangle(100,100,800,700,width = 0, outline="#0019FF", fill="blue")

def initialisation():
    global JEU
    global Joueur
    global total
    JEU = [[0,0,0,0,0,0,0,], #initialisation du tableau de jeu / la grille
            [0,0,0,0,0,0,0,],
            [0,0,0,0,0,0,0,],
            [0,0,0,0,0,0,0,],
            [0,0,0,0,0,0,0,],
            [0,0,0,0,0,0,0,]]
    Joueur=random.randint(1,2)#permet de faire commencer aléatoirement un des deux joueurs
    total=0 #initialise le total à 0 car il n'y a pas de jeton sur la grille

def grille():
    Zone.create_rectangle(100,100,800,700,width = 0, outline="#0019FF", fill="blue")
    x1=110
    y1=110
    x2=190
    y2=190
    for loop in range(6):
        for loop in range(7):
            Zone.create_oval(x1,y1,x2,y2,width = 0, outline="black", fill="white")
            x1 += 100
            x2 += 100
        x1=110
        x2=190
        y1 += 100
        y2 += 100

#déf fonction attendre clic
def Attendre_clic(event):
    global Joueur
    global total
    xClic = event.x #enregistre dans notre variable les coordonnées du clic
    assert type(xClic)==int and xClic >= 100 and xClic <= 800 #empêche le clic de se trouver en dehors de notre grille
    colonne=Recherche_colonne(xClic)  #lance la recherche pour trouve dans quelle colonne se trouve notre clic
    ligne=Recherche_ligne(colonne) #lance la recherche pour savoir sur quelle lignes placer le jeton

    dessin_jeton(ligne,colonne) #lance la fonction qui permet de dessiner les jetons
    #la variable total qui permet de compter chaque jetons sur la grille
    total += 1
    #joueur 1 = rouge
    if Joueur==1:
        print("C'est au tour du joueur 2")
        actualiser_Jeu(ligne,colonne) #actualise le tableau du jeu
        controle_alignement() #contrôle s'il y a 4 jetons d'alignés
        Joueur=2 #passe au prochain joueur
    #joueur 2 = jaune
    elif Joueur==2 :
        print("C'est au tour du joueur 1")
        actualiser_Jeu(ligne,colonne)  #actualise le tableau du jeu
        controle_alignement() #contrôle s'il y a 4 jetons d'alignés
        Joueur=1 #passe au prochain joueur



#déf recherche_colonne
def Recherche_colonne(xClic):
    Dx = 100
    colonne=(xClic-Dx)//100
    return colonne

#def recherche_ligne
def Recherche_ligne(colonne):
    ligne1=5
    for loop in range (6):
        if JEU[ligne1][colonne]==0:
            ligne=ligne1
        else:
            ligne1=ligne1-1
    return ligne

#vainqueur
def vainqueur():
#création d'une nouvelle fenêtre
    fenetre_victoire=Tk()
    fenetre_victoire.title("victoire !!!")
    fenetre_victoire.geometry("900x800")
    fenetre_victoire.config(background="black") #création d'un fond noir
#choix de quel types de victoire c'est
    if total == 42:
        #création d'une texte pour dire qu'il y a une égalité
        print("Il y a égalité !")#écrit dans la console si on ne regarde pas la fenêtre qui s'affiche
        label_eg = Label(fenetre_victoire,text="c'est une égalité !", font=("Courrier",75),bg="black", fg="white")#créer le texte
        label_eg.pack(expand=YES)#centre le texte
    else:
        if Joueur == 1:
            #création d'un texte pour dire que le gagnant est le joueur 1
            print("Le Gagnant est le Joueur" ,1, "(jeton jaune)")#écrit dans la console si on ne regarde pas la fenêtre qui s'affiche
            label_rouge = Label(fenetre_victoire,text="Le joueur 1(jeton jaune) \n a Gagné", font=("Courrier",50),bg="black", fg="yellow")
            label_rouge.pack(expand=YES)
        else:
            #création d'un texte pour dire que le gagnant est le joueur 2
            print("Le Gagnant est le Joueur" ,2, "jeton rouge")#écrit dans la console si on ne regarde pas la fenêtre qui s'affiche
            label_jaune = Label(fenetre_victoire,text="Le joueur 2(jeton rouge) \n a Gagné", font=("Courrier",50),bg="black", fg="red")#créer le texte
            label_jaune.pack(expand=YES)#centre le texte
    #création d'un bouton pour quitter les fenêtres
    bouton_quitter = Button(fenetre_victoire, text="Quitter", font=("Courrier", 30), bg="red", fg="white", command=lambda : [fenetre_victoire.destroy(), fen.destroy()]) #ferme la
    bouton_quitter.pack(expand=YES) #centre le bouton
    #création d'un bouton pour recréer une partie
    bouton_new = Button(fenetre_victoire, text="Nouvelle partie", font=("Courrier", 30), bg="blue", fg="white", command= lambda :[initialisation(),fenetre_victoire.destroy(),grille()])
    bouton_new.pack(expand=YES)#centre le bouton

    mainloop()
#déf dessin jeton
def dessin_jeton(ligne,colonne):
    if Joueur ==2:
        Zone.create_oval(colonne*100+110,ligne*100+190,colonne*100+190,ligne*100+110,width = 5, outline="#A40000", fill="red") #création du jeton rouge
    else:
        Zone.create_oval(colonne*100+110,ligne*100+190,colonne*100+190,ligne*100+110,width = 5, outline="#D3D81A", fill="yellow")#création du jeton jaune




#def actualiser jeu
def actualiser_Jeu(ligne,colonne):
    global JEU
    JEU[ligne][colonne]=Joueur #actualise le tableau JEU grâce au valeur de la ligne et de la colonne et du Joueur (1 ou 2)


#déclaration de la fonction contrôle de l'alignement
def controle_alignement():
    global Vic
    Vic = False
    #vérification alignement vertical
    for ligne in range(0,3):
        for colonne in range(0,7):
            if JEU[ligne][colonne] == Joueur and JEU[ligne+1][colonne] == Joueur and JEU[ligne+2][colonne] == Joueur and JEU[ligne+3][colonne] == Joueur:
                Vic = True


    #vérification alignement horizontal
    for ligne in range(0,6):
        for colonne in range(0,4):
            if JEU[ligne][colonne] == Joueur and JEU[ligne][colonne+1] == Joueur and JEU[ligne][colonne+2] == Joueur and JEU[ligne][colonne+3] == Joueur:
                Vic = True


    #vérification alignement diagonal
    for ligne in range(0,3):
        for colonne in range(0,4):
            if JEU[ligne][colonne] == Joueur and JEU[ligne+1][colonne+1] == Joueur and JEU[ligne+2][colonne+2] == Joueur and JEU[ligne+3][colonne+3] == Joueur:
                Vic = True


    for ligne in range(3,6):
        for colonne in range(0,4):
            if JEU[ligne][colonne] == Joueur and JEU[ligne-1][colonne+1] == Joueur and JEU[ligne-2][colonne+2] == Joueur and JEU[ligne-3][colonne+3] == Joueur:
                Vic = True
    #vérification s'il y a une égalité
    if total == 42:
        Vic = True

    if Vic == True:
        #lancement de la fonction vainqueur si Vic est égale à True
        vainqueur()





#programe principal

grille()#lance la fonction qui permet de créer notre grille
initialisation()#initialise les première variables utile au programme
fen.bind("<Button-1>",Attendre_clic) #vérification si un clic sur le bouton gauche de la souris est appuyé
















fen.mainloop()