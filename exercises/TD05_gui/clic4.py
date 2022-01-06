import tkinter as tk

nb_clic = 0


def remplir_vider(event) -> None:
    """Modifie la couleur du carré dont l'identifiant est stocké dans la
    variable globale carre en alternant entre blanc et noir. Compte également
    le nombre de fois où cette fonction a été appelée en incrémentant la
    variable globale nb_clic. Après 10 appels, détruit la fenêtre graphique
    stockée dans la variable globale racine."""
    global nb_clic
    nb_clic += 1
    if nb_clic % 2 == 1:
        couleur = "black"
    else:
        couleur = "white"

    mon_canvas.itemconfigure(carre, fill=couleur)

    if nb_clic == 10:
        racine.destroy()


racine = tk.Tk()
CANVAS_WIDTH = 500
CANVAS_HEIGHT = 500
mon_canvas = tk.Canvas(racine, background="black", width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
mon_canvas.grid()
mon_canvas.bind("<Button-1>", remplir_vider)


carre = mon_canvas.create_rectangle(CANVAS_WIDTH // 2 - 50,
                                    CANVAS_HEIGHT // 2 - 50,
                                    CANVAS_WIDTH // 2 + 50,
                                    CANVAS_HEIGHT // 2 + 50,
                                    fill="white")


racine.mainloop()
