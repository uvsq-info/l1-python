import tkinter as tk

##################
# Constantes

LARGEUR = 600
HAUTEUR = 400
cpt = 0

###################
# Fonctions

def creer_balle():
    """Dessine un disque bleu et retourne son identifiant
     et les valeurs de déplacements dans une liste"""
    x, y = LARGEUR // 2, HAUTEUR -50
    dx, dy = 3, 5
    rayon = 20
    cercle = canvas.create_oval((x-rayon, y-rayon),
                                (x+rayon, y+rayon),
                                fill="blue")
    return [cercle, dx, dy]

def creer_ligne() :
    x, y = 0, HAUTEUR // 2
    ligne_blanche = canvas.create_line(x, y, LARGEUR, y, fill="white")
    
    return [ligne_blanche, y]



def mouvement():
    """Déplace la balle et ré-appelle la fonction avec un compte-à-rebours"""
    rebond()
    canvas.move(balle[0], balle[1], balle[2])
    canvas.move(ligne[0], 0, 1)
    ligne[1] = ligne[1]+1
    canvas.after(20, mouvement)


def rebond():
    """Fait rebondir la balle sur les bords du canevas"""
    global balle, ligne, cpt
    x0, y0, x1, y1 = canvas.coords(balle[0])

    if x0 <= 0 or x1 >= 600:
        balle[1] = -balle[1]
        cpt += 1
    if y0 <= ligne[1] :
        balle[2] = -balle[2]
        canvas.moveto(ligne[0], 0, ligne[1]-50)
        ligne[1] = ligne[1] -50
        cpt += 1
    if y1 >= 400:
        balle[2] = -balle[2]
        cpt += 1
    if cpt == 30 :
        balle[2], balle[1] = 0, 0

######################
# programme principal

# création des widgets
racine = tk.Tk()
canvas = tk.Canvas(racine, bg="black", width=LARGEUR, height=HAUTEUR)
canvas.grid()

# initialisation de la balle
balle = creer_balle()
ligne = creer_ligne()

# déplacement de la balle
mouvement()

# boucle principale
racine.mainloop()
