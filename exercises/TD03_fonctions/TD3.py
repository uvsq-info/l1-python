#temps[0] : jours, temps[1]: heures, temps[2]: minutes, temps[3]: secondes

def tempsEnSeconde(temps):
    """ Renvoie la valeur en seconde de temps donné comme jour, heure, minute, seconde."""
    return temps[0]*86400 + temps[1]*3600 + temps[2]*60 + temps[3]*1


temps = (3,23,1,34)
print(type(temps))
print(tempsEnSeconde(temps))   

#def secondeEnTemps(seconde):
#    """Renvoie le temps (jour, heure, minute, seconde) qui correspond au nombre de seconde passé en argument"""
#    return (seconde//86400, seconde//3600, seconde//60, seconde//1)
#    pass

def secondeEnTemps(seconde):
    """Renvoie le temps (jour, heure, minute, seconde) qui correspond au nombre de seconde passé en argument"""
    jour=seconde//(24*60*60)
    reste=seconde%(24*60*60)
    heure=reste//(60*60)
    reste1=reste%(60*60)
    minute=reste1//60
    seconde=reste1%60
    return(jour,heure,minute,seconde)

temps = secondeEnTemps(100000)
print(temps[0],"jours",temps[1],"heures",temps[2],"minutes",temps[3],"secondes")



def pluriel(mot,nombre):
    if nombre>0:
        print(" ",nombre,mot,end="")
    if nombre>1:
        print("s",end="")

    
def afficheTemps(temps):
    pluriel("jour",temps[0])
    pluriel("heure",temps[1])
    pluriel("minute",temps[2])
    pluriel("seconde",temps[3])
    print()
    
#afficheTemps((1,0,14,23))

def demandeTemps():
    jour1=int(input("donnez nombr de jours"))
    heure1=int(input("donnez nombre d'heures"))
    minute1=int(input("donnez nombre de minutes"))
    seconde1=int(input("donnez nombre de secondes"))
    if heure1>=24:
        while heure1>=24:
            heure1=int(input("ce n'est pas correcte, donne le nombre d'heures"))
    if minute1>=60:
        while minute1>=60:
            minute1=int(input("ce n'est pas correcte, donne nombre de minutes"))
    if seconde1>=60:
        while seconde1>=60:
            seconde1=int(input("ce n'est pas correcte, donnez le nombre de secondes"))
    return((jour1,heure1,minute1,seconde1))
        
afficheTemps(demandeTemps())

def sommeTemps(temps1,temps2):
    return (tempsEnSeconde(temps1)+tempsEnSeconde(temps2))

sommeTemps((2,3,4,25),(5,22,57,1))