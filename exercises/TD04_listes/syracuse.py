def syracuse(n):
    liste= []
    liste.append(n)
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = (n * 3) + 1
        liste.append(n)
    return(liste)

print(syracuse(3))

def testeConjecture(n_max):
    for i in range (2,n_max):
        syracuse(i)
    return True
print(testeConjecture(10000))

def tempsVol(n):
    vol = len(syracuse(n))-1
    return(vol)

print("Le temps de vol de", 3, "est", tempsVol(3))