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
    global zone1,zone2,zone3,zone4,compteur_rebonds
    x, y = LARGEUR // 2, HAUTEUR // 2
    dx, dy = 3, 5
    rayon = 20
    compteur_rebonds = 0
    zone1 = 0,LARGEUR/2,0,HAUTEUR/2
    zone2 = LARGEUR/2,LARGEUR,0,HAUTEUR/2
    zone3 = 0,LARGEUR/2,HAUTEUR/2,HAUTEUR
    zone4 = LARGEUR/2,LARGEUR,HAUTEUR/2,HAUTEUR
    canvas.create_rectangle(zone1[0],zone1[2],zone1[1],zone1[3],fill='red')
    canvas.create_rectangle(zone2[0],zone2[2],zone2[1],zone2[3],fill='green')
    canvas.create_rectangle(zone3[0],zone3[2],zone3[1],zone3[3],fill='blue')
    canvas.create_rectangle(zone4[0],zone4[2],zone4[1],zone4[3],fill='yellow')
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
    """Fait rebondir la balle sur les bords du canevas,
    contient aussi l'appel d'une fonction de gestion de zone"""
    global balle, centre_balle,compteur_rebonds,id_after
    if compteur_rebonds < 5 :
        x0, y0, x1, y1 = canvas.coords(balle[0])
        centre_balle = (x0+x1)/2, (y0+y1)/2
        zone_manager(centre_balle)
        if x0 <= 0 or x1 >= 600:
            balle[1] = -balle[1]
            compteur_rebonds+=1
        if y0 <= 0 or y1 >= 400:
            balle[2] = -balle[2]
            compteur_rebonds+=1
    else:
        balle[1], balle[2] = 0, 0
        canvas.after_cancel(id_after)

def zone_manager(centre_balle:tuple):
    global balle,zone1,zone2,zone3,zone4
    if zone1[0] < centre_balle[0] < zone1[1] and zone1[2] < centre_balle[1] < zone1[3]:
        canvas.itemconfigure(balle[0],fill='red')
    elif zone2[0] < centre_balle[0] < zone2[1] and zone2[2] < centre_balle[1] < zone2[3]:
        canvas.itemconfigure(balle[0],fill='green')
    elif zone3[0] < centre_balle[0] < zone3[1] and zone3[2] < centre_balle[1] < zone3[3]:
        canvas.itemconfigure(balle[0],fill='blue')
    elif zone4[0] < centre_balle[0] < zone4[1] and zone4[2] < centre_balle[1] < zone4[3]:
        canvas.itemconfigure(balle[0],fill='yellow')


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
