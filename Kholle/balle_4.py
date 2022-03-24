import tkinter as tk

LARGEUR = 600
HAUTEUR = 400

def creer_balle(cercle=0,dx=3,dy=5,x=300,y=200):
    rayon = 20
    cercle = canvas.create_oval((x-rayon, y-rayon),
                                (x+rayon, y+rayon),
                                fill="blue")
    return [cercle, dx, dy, x, y]

def creer_carré(cercle, dx, dy, x, y):
    coté = 20
    cercle = canvas.create_rectangle((x-coté, y-coté),
                                (x+coté, y+coté),
                                fill="blue")
    return [cercle, dx, dy, x, y]

N=0
def mouvement():
    move = [creer_balle, creer_carré]
    global balle
    global N
    global CPT
    rebond()
    if CPT <= 4:
        canvas.move(balle[0], balle[1], balle[2])
        balle[3] += balle[1]
        balle[4] += balle[2]
        canvas.after(20, mouvement)
    elif 5 <= CPT <30:
        if CPT%5 == 0:
            canvas.delete(balle[0])
            balle = move[(CPT//5)%2]( balle[0], balle[1], balle[2], balle[3], balle[4])
        canvas.move(balle[0], balle[1], balle[2])
        balle[3] += balle[1]
        balle[4] += balle[2]
        canvas.after(20, mouvement)

def rebond():
    global CPT
    global balle
    x0, y0, x1, y1 = canvas.coords(balle[0])
    if x0 <= 0 or x1 >= LARGEUR:
        balle[1] = -balle[1]
        CPT += 1
    if  y0 <= 0 or y1 >= HAUTEUR:
        balle[2] = -balle[2]
        CPT += 1

racine = tk.Tk()
canvas = tk.Canvas(racine, bg="black", width=LARGEUR, height=HAUTEUR)
canvas.grid()

balle = creer_balle()
CPT = 0

mouvement()

racine.mainloop()