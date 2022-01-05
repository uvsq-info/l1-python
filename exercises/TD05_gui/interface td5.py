import tkinter as tk
import random

couleur = "orange"

def dessiner_carre():
    x= random.randint(0, CANVAS_WIDTH - 100)
    y= random.randint(0, CANVAS_HEIGHT - 100)
    canvas.create_rectangle(x, y, x+100 , y+100, fill=couleur)

def dessiner_cercle():
    x = random.randint(0, CANVAS_WIDTH - 100)
    y= random.randint(0, CANVAS_HEIGHT - 100)
    canvas.create_oval(x, y, x+100 , y+100 ,fill=couleur)

def dessiner_croix():
    x= random.randint(0, CANVAS_WIDTH - 100)
    y= random.randint(0, CANVAS_HEIGHT - 100)
    canvas.create_line(x, y-50, x , y+50 , fill=couleur)
    canvas.create_line(x-50, y ,x+50, y, fill=couleur)


def choix_couleur():
    global couleur
    choix  = input("choisir une couleur")


racine = tk.Tk()
racine.title("interface td5")

bouton_cercle = tk.Button(racine, text="cercle", command=dessiner_cercle)
bouton_cercle.grid(row=1, column=0)

bouton_carre = tk.Button(racine, text="carré", command=dessiner_carre)
bouton_carre.grid(row=2, column=0)

bouton_croix = tk.Button(racine, text="croix", command=dessiner_croix)
bouton_croix.grid(row=3, column=0)

bouton_couleur = tk.Button(racine, text="choisir couleur" , command=choix_couleur)
bouton_couleur.grid(row=0, column=1)

CANVAS_WIDTH = 500
CANVAS_HEIGHT = 500

canvas =tk.Canvas(racine, width=CANVAS_WIDTH , height=CANVAS_HEIGHT, background="black")
canvas.grid(row=1, column=1 ,rowspan=3)

racine.mainloop()