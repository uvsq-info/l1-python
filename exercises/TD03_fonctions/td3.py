#temps[0] : jours, temps[1]: heures, temps[2]: minutes, temps[3]: secondes
from math import*

def tempsEnSeconde(temps):
    secondes = (temps[0]*24*60*60) + (temps[1]*60*60) + (temps[2]*60) + temps[3]
    return(secondes)
    pass

temps = (3,23,1,34)
print(type(temps))
print(tempsEnSeconde(temps))   

def secondeEnTemps(seconde):
    joursd = seconde / (24*60*60)
    jours = int(joursd)
    reste1 = joursd - jours
    heuresd = reste1 * 24
    heures = int(heuresd)
    reste2 = heuresd - heures
    minutesd = reste2 * 60
    minutes = int(minutesd)
    secondes = seconde % 60
    return(jours, heures, minutes, secondes)
    pass
    
temps = secondeEnTemps(342094)
print(temps[0],"jours",temps[1],"heures",temps[2],"minutes",temps[3],"secondes")
