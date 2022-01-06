import tkinter as tk


def draw_circle(event) -> None:
    """Dessine un cercle de rayon 50 pixels centré sur les coordonnées données par
    le paramètre event. Le cercle est bleu s'il est situé dans la partie gauche
    du canvas, rouge sinon."""
    posx = event.x
    posy = event.y
    if posx < CANVAS_WIDTH // 2:
        color = "blue"
    else:
        color = "red"
    mon_canvas.create_oval(posx - 50, posy - 50, posx + 50, posy + 50, fill=color)


racine = tk.Tk()
CANVAS_WIDTH = 500
CANVAS_HEIGHT = 500
mon_canvas = tk.Canvas(racine, background="black", width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
mon_canvas.grid()
mon_canvas.bind("<Button-1>", draw_circle)

mon_canvas.create_line(CANVAS_WIDTH // 2, 0, CANVAS_WIDTH // 2, CANVAS_HEIGHT, fill="white")


racine.mainloop()
