import tkinter as tk
import random

couleur = "orange"
objet=[]

def dessiner_carre():
    x= random.randint(0, CANVAS_WIDTH - 100)
    y= random.randint(0, CANVAS_HEIGHT - 100)
    identifiant=canvas.create_rectangle(x, y, x+100 , y+100, fill=couleur)
    objet.append(identifiant)
def dessiner_cercle():
    x = random.randint(0, CANVAS_WIDTH - 100)
    y= random.randint(0, CANVAS_HEIGHT - 100)
    identifiant= canvas.create_oval(x, y, x+100 , y+100 ,fill=couleur)
    objet.append(identifiant)

def dessiner_croix():
    x= random.randint(0, CANVAS_WIDTH - 100)
    y= random.randint(0, CANVAS_HEIGHT - 100)
    identifiant=canvas.create_line(x, y-50, x , y+50 , fill=couleur)
    identifiant=canvas.create_line(x-50, y ,x+50, y, fill=couleur)
    objet.append(identifiant)

def choix_couleur():
    global couleur
    choix  = input("choisir une couleur")

def undo():
    if len(objet) == 0:
        return

    identification_objet= objets[-1]
    type = canvas.type(identification_objet)
    if type == "line"
        canvas.delete(identification_objet)
        del objets[-1]
        
    identifiant_objet =objet[-1]
    canvas.delete(identifiant_objet)
    del objet[-1]

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

bouton_undo = tk.Button(racine, text="undo" , command=undo)
bouton_undo.grid(row=0, column=0)

CANVAS_WIDTH = 500
CANVAS_HEIGHT = 500

canvas =tk.Canvas(racine, width=CANVAS_WIDTH , height=CANVAS_HEIGHT, background="black")
canvas.grid(row=1, column=1 ,rowspan=3)

racine.mainloop()