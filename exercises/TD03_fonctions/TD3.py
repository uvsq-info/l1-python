#temps[0] : jours, temps[1]: heures, temps[2]: minutes, temps[3]: secondes

def tempsEnSeconde(temps):
    """ Renvoie la valeur en seconde de temps donné comme jour, heure, minute, seconde."""
    seconde = temps[0]*3600*24+temps[1]*3600+temps[2]*60+temps[3]
    return seconde

mon_temps = (3,23,1,34)
print(tempsEnSeconde(mon_temps))   

def secondeEnTemps(seconde):
    """Renvoie le temps (jour, heure, minute, seconde) qui correspond au nombre de seconde passé en argument"""
    pass
    
temps = secondeEnTemps(100000)
print(temps[0],"jours",temps[1],"heures",temps[2],"minutes",temps[3],"secondes")