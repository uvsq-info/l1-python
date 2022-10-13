import tkinter as tk

##################
# Constantes

LARGEUR = 600
HAUTEUR = 400
x0,y0,x1,y1=0,0,LARGEUR,HAUTEUR

###################
# Fonctions

def division_canvas(event):
    global balle

    posx,posy=event.x,event.y

    canvas.create_rectangle(x0,y0,posx,posy,fill="red")
    canvas.create_rectangle(posx,posy,x1,y1,fill="red")
    canvas.create_rectangle(x0,posy,posx,y1,fill="white")
    canvas.create_rectangle(posx,y0,x1,posy,fill="white")

    balle = creer_balle()
    mouvement()
    return

def creer_balle():
    """Dessine un disque bleu et retourne son identifiant
     et les valeurs de déplacements dans une liste"""
    x, y = LARGEUR // 2, HAUTEUR // 2
    dx, dy = 3, 5
    rayon = 20
    cercle = canvas.create_oval((x-rayon, y-rayon),
                                (x+rayon, y+rayon),
                                fill="blue")
    return [cercle, dx, dy]


def mouvement():
    """Déplace la balle et ré-appelle la fonction avec un compte-à-rebours"""
    couleur = canvas.itemcget()
    if couleur == "red":
         canvas.itemconfig(balle[0], fill="white")
    elif couleur == "white":
            canvas.itemconfig(balle[0], fill="red")
    else:
        pass
    rebond()
    canvas.move(balle[0], balle[1], balle[2])
    canvas.after(20, mouvement)


def rebond():
    """Fait rebondir la balle sur les bords du canevas"""
    global balle
    x0, y0, x1, y1 = canvas.coords(balle[0])
    if x0 <= 0 or x1 >= 600:
        balle[1] = -balle[1]
    if y0 <= 0 or y1 >= 400:
        balle[2] = -balle[2]


######################
# programme principal

# création des widgets
racine = tk.Tk()
canvas = tk.Canvas(racine, bg="black", width=LARGEUR, height=HAUTEUR)
canvas.grid()

# initialisation de la balle
balle = creer_balle()

# déplacement de la balle
mouvement()

# boucle principale
racine.mainloop()
