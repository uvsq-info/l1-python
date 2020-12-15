import tkinter as tk

COTE = 500
colors = ["blue", "green", "black", "yellow", "magenta", "red" ]
nb_cercle = 30

racine = tk.Tk()
canvas = tk.Canvas(racine, bg = "black", height =COTE, width =COTE)
canvas.grid()

epaisseur = (COTE // 2) // nb_cercle

for i in range(nb_cercle):
    canvas.create_oval((epaisseur*i,epaisseur*i), (COTE-epaisseur*i, COTE-epaisseur*i),
                        fill = colors[i % len(colors)], outline = colors[i % len(colors)])

racine.mainloop()