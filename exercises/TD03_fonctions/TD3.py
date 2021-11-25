#temps[0] : jours, temps[1]: heures, temps[2]: minutes, temps[3]: secondes

def tempsEnSeconde(temps):
    """ Renvoie la valeur en seconde de temps donné comme jour, heure, minute, seconde."""
    seconde = temps[0]*3600*24+temps[1]*3600+temps[2]*60+temps[3]
    return seconde

mon_temps = (3,23,1,34)
print(tempsEnSeconde(mon_temps))   

def secondeEnTemps(seconde):
    """Renvoie le temps (jour, heure, minute, seconde) qui correspond au nombre de seconde passé en argument"""
    jours = seconde// 86400
    reste = seconde % 86400

    heures = reste //60
    reste = reste % 3600

    minutes = reste // 60
    secondes_reste = reste % 60

    return (jours, heures, minutes, secondes_reste)
    
temps = secondeEnTemps(100000)
print(temps[0],"jours",temps[1],"heures",temps[2],"minutes",temps[3],"secondes")


def affichePluriel(mot, nombre):
    if nombre ==1:
        print(nombre, mot)
    elif nombre>1 :
        print(nombre, mot +  "s", end=" ")

def afficheTemps(temps):
    affichePluriel("jouer", temps[0])
    affichePluriel("heure", temps[1])
    affichePluriel("minute", temps[2])
    affichePluriel("seconde", temps[3])
    print(temps[0],"jours",temps[1],"heures",temps[2],"minutes",temps[3],"secondes")
    
afficheTemps((1,0,14,23))    

def demandeTemps():
    if jours= int(input("nombre de jours?"))>= 365:
        print()
    heures= int(input("nombre d'heures?"))
    minutes= int(input("nombre de minutes"))
    secondes= int(input("nombre de secondes?"))
    
    print(jours , heures , minutes , secondes )
afficheTemps(demandeTemps())