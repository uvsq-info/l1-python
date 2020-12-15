def carré (x):
    """ affiche le carré + 1 de x si x<1 sinon affiche 3"""
    if x < 1:
        x = x**2 + 1
    else:
        x = 3


x = int(input("nombre au hasard"))
print (carré(x))
