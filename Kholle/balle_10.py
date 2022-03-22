from calendar import c
import tkinter as tk

##################
# Constantes

LARGEUR = 600
HAUTEUR = 400
x0,y0,x1,y1=0,0,LARGEUR,HAUTEUR
ite=0
###################
# Fonctions
def div(event):
    """divise le canvas en 4 carré selon la pos grace a event"""
    global balle
    #affection de la position du clic a des variable (posx,posy)
    posx,posy=event.x,event.y

    #creation des rectangle et coloration selon le clic
    canvas.create_rectangle(x0,y0,posx,posy,fill="red")
    canvas.create_rectangle(posx,posy,x1,y1,fill="red")
    canvas.create_rectangle(x0,posy,posx,y1,fill="white")
    canvas.create_rectangle(posx,y0,x1,posy,fill="white")

    #creation de la balle et mise en mouvement apres le clic 
    balle = creer_balle()
    mouvement()
    return

def creer_balle():
    global dx,dy
    ##"Dessine un disque bleu et retourne son identifiant
    ## et les valeurs de déplacements dans une liste"
    x, y = LARGEUR // 2, HAUTEUR // 2
    dx, dy = 3, 5
    rayon = 20
    cercle = canvas.create_oval((x-rayon, y-rayon),(x+rayon, y+rayon),fill="blue")
    return [cercle, dx, dy]


def mouvement():
    global ite
    """Déplace la balle et ré-appelle la fonction avec un compte-à-rebours"""
    if ite<29:
        #recupération couleur de l'item le plus proche 

        coordb=canvas.coords(balle[0])
        objet = canvas.find_closest(coordb[0],coordb[1])
        couleur = canvas.itemcget(objet[0], 'fill') 

        #Condition de changement de couleur
        if couleur == "red":
            canvas.itemconfig(balle[0], fill="white")
        elif couleur == "white":
            canvas.itemconfig(balle[0], fill="red")
        else:
            pass

        #mouvement
        rebond()
        canvas.move(balle[0], balle[1], balle[2])
        #creation de l'animation ici une iteration toute les 20ms
        canvas.after(10, mouvement)
    else:
        pass

def rebond():
    """Fait rebondir la balle sur les bords du canevas"""
    global balle
    global ite

    x0, y0, x1, y1 = canvas.coords(balle[0])
    if x0 <= 0 or x1 >= 600:
        balle[1] = -balle[1]
        #ajout(+1) de la varibale itération pour la limite a 30
        ite+=1
    if y0 <= 0 or y1 >= 400:
        balle[2] = -balle[2]
        #ajout (+1) de la variable itération pour la limite a 30
        ite+=1


######################
# programme principal

# création des widgets
racine = tk.Tk()
canvas = tk.Canvas(racine, bg="black", width=LARGEUR, height=HAUTEUR)
canvas.grid()


# initialisation de la balle


# déplacement de la balle

#bind de la souris + liaison avec la fonction DIV

canvas.bind("<Button-1>",div)

# boucle principale
racine.mainloop()
