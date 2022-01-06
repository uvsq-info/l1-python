import tkinter as tk

nb_clic = 0
point1 = (-1, -1)


def draw_line(event) -> None:
    """Dessine une ligne formée par deux points dont les coordonnées sont données
    par le paramètre event. Lors du premier appel de cette fonction
    (i.e. nb_clic == 0), stocker les coordonnées du point dans la variable
    globale point1. Lors du deuxième appel, tracer la ligne."""
    global nb_clic, point1
    if nb_clic == 0:
        point1 = (event.x, event.y)
        nb_clic += 1
    else:
        point2 = (event.x, event.y)
        milieu_canvas = CANVAS_WIDTH // 2
        couleur = "red"
        if (point1[0] < milieu_canvas and point2[0] < milieu_canvas) \
                or (point1[0] > milieu_canvas and point2[0] > milieu_canvas):
            # Les deux points sont du même côté du canvas, la ligne sera bleue.
            couleur = "blue"
        mon_canvas.create_line(point1[0], point1[1],
                               point2[0], point2[1],
                               fill=couleur)
        nb_clic = 0


racine = tk.Tk()
CANVAS_WIDTH = 500
CANVAS_HEIGHT = 500
mon_canvas = tk.Canvas(racine, background="black", width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
mon_canvas.grid()
mon_canvas.bind("<Button-1>", draw_line)


mon_canvas.create_line(CANVAS_WIDTH // 2, 0, CANVAS_WIDTH // 2, CANVAS_HEIGHT, fill="white")


racine.mainloop()
