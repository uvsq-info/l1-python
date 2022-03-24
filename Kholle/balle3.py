import tkinter as tk

##################
# Constantes

LARGEUR = 600
HAUTEUR = 400
CPT = 0

###################
# Fonctions

def creer_balle():
    """Dessine un disque bleu et retourne son identifiant
     et les valeurs de déplacements dans une liste"""
    global cercle
    dx, dy = 3, 5
    return [cercle, dx, dy]


def mouvement():
    """Déplace la balle et ré-appelle la fonction avec un compte-à-rebours"""
    global CPT
    if CPT < 30:
        rebond()
        canvas.move(balle[0], balle[1], balle[2])
        canvas.after(20, mouvement)


def rebond():
    """Fait rebondir la balle sur les bords du canevas"""
    global balle, CPT, cercle
    x0, y0, x1, y1 = canvas.coords(balle[0])
    if x0 <= 0:
        balle[1] = -balle[1]
        canvas.itemconfig(cercle, fill="yellow")
        CPT += 1
    elif x1 >= 600:
        balle[1] = -balle[1]
        canvas.itemconfig(cercle, fill="green")
        CPT += 1
    elif y0 <= 0:
        balle[2] = -balle[2]
        canvas.itemconfig(cercle, fill="red")
        CPT += 1
    elif y1 >= 400:
        balle[2] = -balle[2]
        canvas.itemconfig(cercle, fill="blue")
        CPT += 1

######################
# programme principal

# création des widgets
racine = tk.Tk()
canvas = tk.Canvas(racine, bg="black", width=LARGEUR, height=HAUTEUR)
canvas.grid()

x, y = LARGEUR // 2, HAUTEUR // 2
rayon = 20
cercle = canvas.create_oval((x-rayon, y-rayon),
                                (x+rayon, y+rayon),
                                fill="blue")

canvas.create_rectangle(0, 395, 600, 400, fill="blue")
canvas.create_rectangle(0, 0, 600, 5, fill="red")
canvas.create_rectangle(0, 400, 5, 0, fill="yellow")
canvas.create_rectangle(595, 0, 600, 400, fill="green")

# initialisation de la balle
balle = creer_balle()

# déplacement de la balle
mouvement()

# boucle principale
racine.mainloop()