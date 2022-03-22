import tkinter as tk

##################
# Constantes

LARGEUR = 600
HAUTEUR = 400

###################
# Fonctions

def creer_balle():
    """Dessine un disque bleu et retourne son identifiant
     et les valeurs de déplacements dans une liste"""
    global compteur_mur
    x, y = LARGEUR // 2, HAUTEUR // 2
    dx, dy = 3, 5
    rayon = 20
    compteur_mur = 0
    cercle = canvas.create_oval((x-rayon, y-rayon),
                                (x+rayon, y+rayon),
                                fill="blue")
    return [cercle, dx, dy]


def mouvement():
    """Déplace la balle et ré-appelle la fonction avec un compte-à-rebours"""
    global id_after
    rebond()
    canvas.move(balle[0], balle[1], balle[2])
    id_after = canvas.after(20, mouvement)


def rebond():
    """Fait rebondir la balle sur les bords du canevas"""
    global balle, compteur_mur, id_after
    x0, y0, x1, y1 = canvas.coords(balle[0])
    if x0 <= 0 or x1 >= 600:
        balle[1] = -balle[1]
    if compteur_mur < 10:
        if y0 <= 0 :
            canvas.moveto(balle[0],y=400)
            compteur_mur += 1
        elif y1 >= 400:
            canvas.moveto(balle[0],y=0)
            compteur_mur += 1
    elif 10 <= compteur_mur <= 20:
        if y0 <= 0 or y1 >= 400:
            balle[2] = -balle[2]
            compteur_mur += 1
            if compteur_mur == 11:
                canvas.create_line(0,5,600,5,fill='white',width=3)
                canvas.create_line(0,395,600,395,fill='white',width=3)
    else:
        balle[1] = 0
        balle[2] = 0
        canvas.after_cancel(id_after)




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
