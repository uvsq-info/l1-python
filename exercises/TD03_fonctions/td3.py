#temps[0] : jours, temps[1]: heures, temps[2]: minutes, temps[3]: secondes
from math import*
from time import*

#appel de fonction
def tempsEnSeconde(temps):
    secondes = (temps[0]*24*60*60) + (temps[1]*60*60) + (temps[2]*60) + temps[3]
    return(secondes)
    pass

def secondeEnTemps(seconde):
    jours = seconde // (24*60*60)
    seconde = seconde % (24*60*60)
    heures = seconde // (60*60)
    seconde = seconde % (60*60)
    minutes = seconde // (60)
    seconde = seconde % 60
    return(jours, heures, minutes, seconde)
    pass


def affichePluriel(val, mot):
    if val != 0:
        print(val, mot,end='')
    if val >= 1:
        print('s ',end='')



def afficheTemps(temps):
    affichePluriel(temps[0],'jour')
    affichePluriel(temps[1],'heure')
    affichePluriel(temps[2],'minute')
    affichePluriel(temps[3],'seconde')
       

def demandeTemps():
    jours = int(input('Entrer un nombre de jours'))
    heures = int(input("Entrer un nombre d'heures"))
    minutes = int(input("Entrer un nombre de minutes"))
    secondes = int(input("Entrer un nombre de secondes"))
    while heures not in range(0,24):
        print('Not a right value for heure')
        heures = int(input("Entre une autre valeur"))
    while minutes not in range(0,60):
        print('Error for minutes')
        minutes = int(input("Entre une autre valeur"))
    while secondes not in range(0,60):
        print("error for secondes7")
        secondes = int(input("Entre une autre valeur"))

    return(jours,heures,minutes,secondes)

def sommeTemps(temps1,temps2):
    addition = secondeEnTemps(tempsEnSeconde(temps1) + tempsEnSeconde(temps2))
    return (addition)
    pass

def proportionTemps(temps,proportion):
    calcul = secondeEnTemps(int(tempsEnSeconde(temps) * proportion))
    return(calcul)
    pass




def tempsEnDate(temps):
    annee = (temps[0] // 365) + 1970
    jours = temps[0] % 365
    
    return(annee,jours,temps[1],temps[2],temps[3])
    

def afficheDate(date = -1):
    affichePluriel(int(date[0]),'année')
    affichePluriel(int(date[1]),'jour')
    affichePluriel(int(date[2]),'heure')
    affichePluriel(int(date[3]),'minute')
    affichePluriel(date[4],'seconde')

def bisextile(jour):
    annee = int(jour // 365)
    debut = annee%4
    print(debut)
    for i in range (debut,annee,4):
        print(1970+i,"est une année bisextile")

def nombreBisextile(jour):
    number = int(jour / 365.25*4)
    return(number)


def tempsEnDateBisextile(temps):
    date = 1970
    jour = int(temps[0])
    while jour >= 364:
        if date % 4 == 0:
            jour = jour-366
            date += 1
        elif date % 4 != 0:
            jour = jour-365
            date += 1
    return(date,jour,temps[1],temps[2],temps[3])
        

#-------------------------------------------------------------------------------------
#programme principal
temps = (3,23,1,34)
print(type(temps))
print(tempsEnSeconde(temps))   

temps = secondeEnTemps(342094)
print(temps[0],"jours",temps[1],"heures",temps[2],"minutes",temps[3],"secondes")

afficheTemps((1,0,14,23)) 

afficheTemps(demandeTemps())

afficheTemps(sommeTemps((6,3,4,25),(5,22,57,1)))

afficheTemps(proportionTemps((2,0,36,0),0.2))
    
temps = secondeEnTemps(1000000000)
afficheTemps(temps)
print("\n")
afficheDate(tempsEnDate(temps))

afficheDate(tempsEnDate(secondeEnTemps(time())))

for multiple in range (1,11):
    a = 100**multiple
    b = 400**multiple
    rapport = b/a - int(b/a)
    if rapport == 0:
        print ("pour multiple",multiple,"et rapport", b//a)
    elif rapport != 0:
        print ("pour multiple",multiple)


bisextile(20000)

temps = secondeEnTemps(1000000000)
afficheTemps(temps)
print("\n")
afficheDate(tempsEnDateBisextile(temps))

afficheDate(tempsEnDateBisextile(secondeEnTemps(time())))
print("\n")
afficheDate(tempsEnDate(secondeEnTemps(time())))