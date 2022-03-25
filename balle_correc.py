import tkinter as tk
import random as rd

LARGEUR = 600
HAUTEUR = 400

est_arrete = True

def demarrer():
    """questions 4 et 6"""
    global est_arrete, id_after
    if est_arrete:
        mouvement()
        bouton.config(text="Arrêter")
    else:
        canvas.after_cancel(id_after)
        bouton.config(text="Démarrer")
    est_arrete = not est_arrete

def rebond():
    """question 7"""
    x0, y0, x1, y1 = canvas.coords(balle[0])
    if y1 > HAUTEUR or y0 < 0:
        balle[2] = -balle[2]
    if x1 > LARGEUR or x0 < 0:
        balle[1] = -balle[1]

def creer_balle():
    """question 2"""
    r = 20
    xmil = LARGEUR // 2
    ymil = HAUTEUR // 2
    cercle = canvas.create_oval(xmil-r, ymil-r, xmil+r, ymil+r, fill="blue")
    dx = rd.randint(1, 7)
    dy = rd.randint(1, 7)
    return [cercle, dx, dy]


def mouvement():
    """questions 3 et 5"""
    global id_after
    rebond()
    canvas.move(balle[0], balle[1], balle[2])
    id_after = canvas.after(20, mouvement)


racine = tk.Tk()
canvas = tk.Canvas(bg="black", width=LARGEUR, height=HAUTEUR)
bouton = tk.Button(text="Démarrer", command=demarrer)

canvas.grid()
bouton.grid(row=1)

balle = creer_balle()

racine.mainloop()