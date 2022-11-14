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
    for i in range (1,n_max+1):
        syracuse(i)
    return True
print(testeConjecture(10000))

def tempsVol(n):
    return (len(syracuse(n))-1)

print("Le temps de vol de", 3, "est", tempsVol(3))



def tempsVolListe(n_max):
    liste_temps_vol = [tempsVol(i) for i in range(1,n_max +1)]
    return (liste_temps_vol)

print(tempsVolListe(100))



l =tempsVolListe(10000)
print(max(l), l.index(max(l))+1)