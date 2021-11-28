# Liens utiles pour vérifier vos résultats :
# Convertit un nombre de secondes en une date depuis le 01/01/1970
# https://www.epochconverter.com/

# Numéros des jours de l'année 2021
# https://www.calendar-365.com/day-numbers/2021.html

# Somme d'une date et d'un nombre de jours
# https://www.timeanddate.com/date/dateadd.html

import time


def tempsEnSeconde(temps: tuple) -> int:
    """ Renvoie le nombre de secondes du temps donné
        comme jour, heure, minute, seconde."""
    return temps[0] * 86400 + temps[1] * 3600 + temps[2] * 60 + temps[3]


mon_temps = (3, 23, 1, 34)
print(type(mon_temps))
print(tempsEnSeconde(mon_temps))


def secondesEnTemps(secondes: int) -> tuple:
    """ Renvoie le temps (jour, heure, minute, seconde) qui
        correspond au nombre de secondes passé en argument."""
    jours = secondes // 86400
    reste = secondes % 86400

    heures = reste // 3600
    reste = reste % 3600

    minutes = reste // 60
    reste = reste % 60

    return (jours, heures, minutes, reste)


mon_temps = secondesEnTemps(100000)
print(mon_temps[0], "jours", mon_temps[1], "heures", mon_temps[2], "minutes",
      mon_temps[3], "secondes")


def affichePluriel(mot: str, nombre: int) -> None:
    """ Affiche (ou non) un mot en fonction du paramètre nombre.
        Met le mot au pluriel si nécessaire."""
    if nombre > 0:
        print(" ", nombre, mot, end="")

    if nombre > 1:
        print("s", end="")


def afficheTemps(temps: tuple) -> None:
    """ Affiche le tuple temps sous la forme :
        X jour(s), X heure(s), X minute(s), X seconde(s)"""
    affichePluriel("jour", temps[0])
    affichePluriel("heure", temps[1])
    affichePluriel("minute", temps[2])
    affichePluriel("seconde", temps[3])
    print()


afficheTemps((1, 0, 14, 23))


def demandeTemps() -> tuple:
    """Demande à l'utilisateur un nombre de jours, d'heures, de minutes
    et de secondes et les renvoie sous la forme d'un tuple de temps."""
    jours = -1
    heures = -1
    minutes = -1
    secondes = -1

    while (jours < 0):
        jours = int(input("Entrez un nombre de jour "))

    while (heures < 0 or heures >= 24):
        heures = int(input("Entrez un nombre d'heures "))

    while (minutes < 0 or minutes >= 60):
        minutes = int(input("Entrez un nombre de minutes "))

    while (secondes < 0 or secondes >= 60):
        secondes = int(input("Entrez un nombre de secondes "))

    return (jours, heures, minutes, secondes)


afficheTemps(demandeTemps())


def sommeTemps(temps1: tuple, temps2: tuple) -> tuple:
    """Retourne la somme des deux temps passés en paramètres."""
    return secondesEnTemps(tempsEnSeconde(temps1) + tempsEnSeconde(temps2))


afficheTemps(sommeTemps((2, 3, 4, 25), (5, 22, 57, 1)))


def proportionTemps(temps: tuple, proportion: float) -> tuple:
    """Retourne un temps egal au temps passé en paramètre après
    application de la proportion."""
    return secondesEnTemps(int(tempsEnSeconde(temps) * proportion))


afficheTemps(proportionTemps((2, 0, 36, 0), 0.2))
afficheTemps(proportionTemps(proportion=0.2, temps=(2, 0, 36, 0)))


def tempsEnDate(temps: tuple) -> tuple:
    """ Retourne un tuple contenant la date obtenue en ajoutant la
        durée stockée dans le paramètre temps au 1er Janvier 1970.
        Ne prend pas en compte les années bisextiles."""
    annee = 1970 + temps[0] // 365
    numero_du_jour = 1 + temps[0] % 365
    return (annee, numero_du_jour, temps[1], temps[2], temps[3])


# afficheDate(date: tuple = ()) : Cela signifie que la fonction
# prend un paramètre nommé date de type tuple. Ce paramètre peut être
# omis et dans ce cas il prendra la valeur par défaut () qui est
# un tuple vide.
def afficheDate(date: tuple = ()) -> None:
    """ Affiche la date passée en paramètre. Si aucune date n'est passée,
        affiche la date du jour. Ne gère pas les mois."""
    if len(date) == 0:
        date = tempsEnDate(secondesEnTemps(int(time.time())))
    print("Jour numéro", date[1], "de l'année", date[0], "à",
          str(date[2]) + ":" + str(date[3]) + ":" + str(date[4]))


mon_temps = secondesEnTemps(86401)
afficheTemps(mon_temps)
afficheDate(tempsEnDate(mon_temps))
afficheDate()

print(time.time())


def estBisextile(annee: int) -> bool:
    """Retourne True si l'année passée en paramètre est bisextile,
       False sinon."""
    return annee % 4 == 0 and (annee % 100 != 0 or annee % 400 == 0)


def bisextile(jours: int) -> None:
    """ Affiche toutes les années bisextiles entre le 1er Janvier 1970
        et le nombre de jours passé en paramètre."""
    annee = 1970
    while(jours >= 365):
        if estBisextile(annee):
            print("L'année " + str(annee) + " est bisextile")
            jours -= 366
        else:
            jours -= 365
        annee += 1


bisextile(20000)


def nombreBisextile(jours: int) -> int:
    """ Retourne le nombre d'années bisextiles entre le 1er Janvier 1970
    et le nombre de jours passé en paramètre."""
    annee = 1970
    compteur_bisextile = 0
    while(jours >= 365):
        if estBisextile(annee):
            compteur_bisextile += 1
            jours -= 366
        else:
            jours -= 365
        annee += 1
    return compteur_bisextile


def tempsEnDateBisextile(temps: tuple) -> tuple:
    """ Retourne un tuple contenant la date obtenue en ajoutant la
        durée stockée dans le paramètre temps au 1er Janvier 1970,
        en prenant en compte les années bisextiles."""
    jour, heure, minute, seconde = temps
    jour = jour - nombreBisextile(jour)
    temps_ajuste = (jour, heure, minute, seconde)
    return tempsEnDate(temps_ajuste)


afficheDate(tempsEnDateBisextile(secondesEnTemps(int(time.time()))))


# Question optionnelle : Gestion des mois dans afficheDate

def afficheDateV2(date: tuple = ()) -> None:
    """ Affiche la date passée en paramètre. Si aucune date n'est passée,
    affiche la date du jour. Gère les mois et les années bisextiles."""
    if len(date) == 0:
        date = tempsEnDateBisextile(secondesEnTemps(int(time.time())))

    # On établit deux listes :
    # Une liste des noms de chaque mois
    nom_des_mois = ["Janvier", "Février", "Mars", "Avril", "Mai", "Juin",
                    "Juillet", "Aout", "Septembre", "Octobre", "Novembre",
                    "Décembre"]
    # Ainsi qu'une liste des numéros du jour final de chaque mois
    fin_des_mois = [31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365]
    # Si l'année est bisextile, augmenter les fins des mois de 1 (sauf janvier)
    if estBisextile(date[0]):
        for i in range(1, 12):
            fin_des_mois[i] += 1

    mois = ""
    jour = date[1]

    for i in range(12):
        if jour <= fin_des_mois[i]:
            mois = nom_des_mois[i]
            jour -= fin_des_mois[i-1]
            break

    print(jour, mois, date[0], "à", str(date[2]) + ":" + str(date[3])
          + ":" + str(date[4]))


afficheDateV2()
afficheDateV2((2020, 60, 12, 0, 0))
