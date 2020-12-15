#temps[0] : jours, temps[1]: minutes, temps[2]: minutes, temps[3]: secondes

temps = (3,23,1,34)

def tempsEnSeconde(temps):
    """ Renvoie la valeur en seconde de temps donné comme jour, heure, minute, seconde."""
    return temps [0] * 24 * 3600 + temps [1] * 3600 + temps [2] * 60 + temps [3] 


print(type(temps))
print(tempsEnSeconde(temps))  





def secondeEnTemps(seconde):
    """Renvoie le temps (jour, heure, minute, seconde) qui correspond au nombre de seconde passé en argument"""
    minute = seconde // 60
    seconde %= 60
    heure = minute // 60
    minute %= 60
    jour = heure // 24
    heure %= 24
    return (jour, heure, minute, seconde)

temps = secondeEnTemps(100000)  

print(temps[0],"jours",temps[1],"heures",temps[2],"minutes",temps[3],"secondes")




def affichePluriel (val = 1, mot = "jour"):
    if val != 0:
        print(" ", val, mot , end = "" )
    if val > 1:
        print("s", end = "")



def afficheTemps(temps):
    affichePluriel(temps[0], "jour")
    affichePluriel(temps[1], "heure")
    affichePluriel(temps[2], "minute")
    affichePluriel(temps[3], "seconde")
    print ("")
afficheTemps((1,0,14,23))


def demandeTemps():
    jour = int(input("combien de jours"))
    heure = int(input("combien d'heures'"))
    minute = int(input("combien de minutes"))
    seconde = int(input("combien de secondes"))
    if (seconde > 59 or minute > 59 or heure > 23):
        print ("Entrée mal formée, ce n'est pas une date")
        return (0,0,0,0)
    return (jour, heure, minute, seconde)

afficheTemps(demandeTemps())


def sommeTemps(temps1,temps2):
    return secondeEnTemps(tempsEnSeconde(temps1)+tempsEnSeconde(temps2))

sommeTemps((2,3,4,25),(5,22,57,1))




def proportionTemps(temps,proportion):
    return secondeEnTemps (int(tempsEnSeconde(temps)*proportion))
afficheTemps(proportionTemps((2,0,36,0),0.2))



import time

def tempsEnDate(temps):
    jour, heure, minute, seconde = temps
    annee = 1970 + jour // 365
    jour %= 365
    return (annee, jour, heure, minute, seconde)

def afficheDate (date = -1):
    if date == -1:
        date = tempsEnDate(secondeEnTemps(int(time.time())))
    annee, jour, heure, minute, seconde = date
    print("Année", annee, end = " ")
    afficheTemps((jour%365, heure, minute, seconde))

temps = secondeEnTemps(1000000000)
afficheDate(tempsEnDate(temps))


def bisextile(jour):
    annee = 1970
    b = 0
    while(jour >= 0):
        if (annee % 4 == 0 and (annee % 100 != 0 or annee % 400 == 0)):
            print("Année", annee, "bisextile")
            jour -= 366
        else:
            jour -= 365
        annee +=1
    return b

    