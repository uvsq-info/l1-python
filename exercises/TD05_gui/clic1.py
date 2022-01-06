import tkinter as tk


def draw_red_pixel(event) -> None:
    """Dessine un rectangle rouge d'un pixel aux coordonnées données par
    le paramètre event."""
    posx = event.x
    posy = event.y
    mon_canvas.create_rectangle(posx, posy, posx + 1, posy + 1, fill="red", width=0)


racine = tk.Tk()
CANVAS_WIDTH = 500
CANVAS_HEIGHT = 500
mon_canvas = tk.Canvas(racine, background="black", width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
mon_canvas.grid()
mon_canvas.bind("<Button-1>", draw_red_pixel)


racine.mainloop()
