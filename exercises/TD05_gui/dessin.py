import tkinter as tk

ma_couleur = "blue"
HEIGHT = 800
WIDTH = 800

racine = tk.Tk()

racine.title("mon dessin")
bouton1 = tk.Button(racine, text = "choisir une couleur", bg= "red", fg = "blue", font = "helvetica", command = lambda : choisir())
bouton1.grid(row = 0, column = 1)


bouton2 = tk.Button (racine, text = "cercle", bg= "red", fg = "blue", font = "helvetica", command = lambda :cercle1())
bouton2.grid(row = 1, column = 0)

bouton3 = tk.Button (racine, text = "carré", bg= "red", fg = "blue", font = "helvetica", command = lambda : carré1())
bouton3.grid(row = 2, column = 0)

bouton4 = tk.Button (racine, text = "croix", bg= "red", fg = "blue", font = "helvetica", command = lambda : croix1())
bouton4.grid(row = 3, column = 0)

bouton5 = tk.Button (racine, text = "undo", bg = "red", fg = "blue", font = "helvetica", command = lambda : undo())
bouton5.grid(row = 0, column = 2)

canvas = tk.Canvas (racine, bg = "black", height = HEIGHT - 150, width = WIDTH - 150, bd = 10, relief = "raised")
canvas.grid(row = 1, column = 1, rowspan = 3, columnspan = 2)

import random
objet = []

def cercle1():
    global objet
    a = random.randint(50, 500)
    b = random.randint(50, 500)
    objet.append(canvas.create_oval(a, b, a + 100, b + 100, fill = ma_couleur))

def carré1():
    global objet
    a = random.randint(50, 500)
    b = random.randint(50, 500)
    objet.append(canvas.create_rectangle(a, b, a + 100, b + 100, fill = ma_couleur))

def croix1():
    global objet
    a = random.randint(50, 500)
    b = random.randint(50, 500)
    objet.append(canvas.create_line(a, b, a + 100, b+100, fill = ma_couleur))
    objet.append(canvas.create_line(a + 100, b, a, b + 100, fill = ma_couleur))

def choisir():
    global ma_couleur
    ma_couleur = input("choisir une couleur")

def undo():
    if canvas.type(objet[-1]) == "line":
        canvas.delete(objet[-1])
        del (objet[-1])
        canvas.delete(objet[-1])
        del (objet[-1])
    else:
        canvas.delete(objet[-1])
        del (objet[-1])




racine.mainloop()

