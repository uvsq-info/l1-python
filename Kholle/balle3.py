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

    global compteur 
    compteur = 0

    x, y = LARGEUR // 2, HAUTEUR // 2
    dx, dy = 3, 5
    rayon = 20
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
    global balle, id_after, compteur 
    
    x0, y0, x1, y1 = canvas.coords(balle[0])
    if x0 <= 0 or x1 >= 600:
        balle[1] = -balle[1]
        compteur += 1
    if y0 <= 0 or y1 >= 400:
        balle[2] = -balle[2]
        compteur += 1

    if compteur < 30 : 
        rouge = canvas.find_overlapping(0,0,585,0)
        for obj in rouge :
            canvas.itemconfigure(obj, fill= "red")

        vert = canvas.find_overlapping(0,15,0,385)
        for obj in vert :
            canvas.itemconfigure(obj, fill= "green")

        bleu = canvas.find_overlapping(15,385,600,385)
        for obj in bleu :
            canvas.itemconfigure(obj, fill= "blue")

        jaune = canvas.find_overlapping(600,385,600,15)
        for obj in jaune :
            canvas.itemconfigure(obj, fill= "yellow")
        
    else : 
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
gauche = canvas.create_line(0,0,0,400,width=20, fill = "green")
haut = canvas.create_line(0,1,600,0,width=20, fill = "red")
droite =canvas.create_line(600,400,600,0,width=20, fill = "yellow")
bas = canvas.create_line(0,400,600,400,width=20, fill = "blue")
# déplacement de la balle
mouvement()

# boucle principale
racine.mainloop()