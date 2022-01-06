import tkinter as tk
import random as rd


def get_color(r, g, b) -> str:
    """ Retourne une couleur à partir de ses composantes r, g, b entre 0 et 255"""
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)


def draw_pixel(i, j, color) -> None:
    """ Dessine un pixel de couleur color aux coordonnées i,j"""
    # Par défaut les rectangles ont une bordure de 1px noire.
    # Un rectangle blanc de 1 pixel de large ne se verra donc pas.
    # Mettre width=0 pour supprimer la bordure.
    mon_canvas.create_rectangle(i, j, i+1, j+1, fill=color, width=0)


def ecran_aleatoire() -> None:
    """Remplit l'intégralité du canvas de pixel d'une couleur aléatoire"""
    for x in range(0, CANVAS_WIDTH):
        for y in range(0, CANVAS_HEIGHT):
            color = get_color(rd.randint(0, 255), rd.randint(0, 255), rd.randint(0, 255))
            draw_pixel(x, y, color)


def degrade_gris() -> None:
    """Remplit l'intégralité du canvas avec un dégradé de gris"""
    # Le canvas étant de 256x256, nous pouvons choisir une couleur
    # égale à la coordonnée du pixel.
    # Il faudrait modifier ce code s'il fallait l'adapter à des
    # canvas de taille différente.
    for x in range(0, CANVAS_WIDTH):
        color = get_color(x, x, x)
        for y in range(0, CANVAS_HEIGHT):
            draw_pixel(x, y, color)


def degrade_2D() -> None:
    """Remplit l'intégralité du canvas avec un dégradé en deux dimensions :
    de noir à mauve sur la première diagonale et de bleu à rouge sur la deuxième."""
    for x in range(0, CANVAS_WIDTH):
        for y in range(0, CANVAS_HEIGHT):
            color = get_color(x, 0, y)
            draw_pixel(x, y, color)


racine = tk.Tk()

bouton_aleatoire = tk.Button(racine, text="Aléatoire", command=ecran_aleatoire)
bouton_degrade_gris = tk.Button(racine, text="Dégradé gris", command=degrade_gris)
bouton_degrade_2d = tk.Button(racine, text="Dégradé 2d", command=degrade_2D)
CANVAS_WIDTH = 256
CANVAS_HEIGHT = 256
mon_canvas = tk.Canvas(racine, background="black", width=CANVAS_WIDTH, height=CANVAS_HEIGHT)


bouton_aleatoire.grid(row=0, column=0)
bouton_degrade_gris.grid(row=1, column=0)
bouton_degrade_2d.grid(row=2, column=0)
mon_canvas.grid(row=0, column=1, rowspan=3)

# Test Question 2
draw_pixel(CANVAS_WIDTH//2, CANVAS_HEIGHT//2, "white")


racine.mainloop()
