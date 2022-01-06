import tkinter as tk

racine = tk.Tk()
CANVAS_SIZE = 600
mon_canvas = tk.Canvas(racine, width=CANVAS_SIZE, height=CANVAS_SIZE, background="black")
mon_canvas.grid()

couleurs = ["blue", "green", "black", "yellow", "magenta", "red"]
nb_cercles = 30
epaisseur = (CANVAS_SIZE // 2) // nb_cercles

for i in range(nb_cercles):
    mon_canvas.create_oval(i * epaisseur,
                           i * epaisseur,
                           CANVAS_SIZE - i * epaisseur,
                           CANVAS_SIZE - i * epaisseur,
                           fill=couleurs[i % len(couleurs)],
                           width=0)


racine.mainloop()
