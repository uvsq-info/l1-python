import tkinter as tk
import random

def get_color(r, g, b):
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

def draw_pixel(i, j, color):
    canvas.create_rectangle(i,j,i+1,j+1, fill=color, witdh=0)

def ecran_aleatoire():
    for i in range(CANVAS_WIDTH):
        for j in range(CANVAS_HEIGHT):
            red= random.randint(0,255)
            green= random.randint(0,255)
            blue= random.randint(0,255)
            couleur=get_color(red,blue,green)

            draw_pixel(i,j,couleur)

def degrade_gris():
    for i in range(CANVAS_WIDTH):
        for j in range(CANVAS_HEIGHT):
            couleur=get_color(i,i,i)
            draw_pixel(i,j,couleur)


def degrade_2D():

racine = tk.Tk()
racine.title("couleurs")

bouton_aléatoire = tk.Button(racine, text="Aléatoire", command=ecran_aleatoire)
bouton_aléatoire.grid(row=0, column=0)

bouton_degrade_gris = tk.Button(racine, text="Dégradé de gris", command=degrade_gris)
bouton_degrade_gris.grid(row=1, column=0)

bouton_degrade_2D = tk.Button(racine, text="Dégradé 2D", command=degrade_2D)
bouton_degrade_2D.grid(row=2, column=0)

CANVAS_WIDTH = 256
CANVAS_HEIGHT = 256
canvas=tk.Canvas(racine, witdh=CANVAS_WIDTH , height=CANVAS_HEIGHT,)
canvas.grid(row=0, column=1, rowspan=3)

draw_pixel(CANVAS_WIDTH/2, CANVAS_HEIGHT/2, "white")

racine.mainloop()