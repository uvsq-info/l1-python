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



def pluriel(nombre,mot):
    if int(nombre)>1:
        return str(nombre) + (mot+"s",end="")
    elif int(nombre)=1:
        return str(nombre) + (mot,end="")
    elif int(nombre)=0:
        return None

    
def afficheTemps(temps):
    return ((pluriel(temps[0],jour)),(pluriel(temps[1],heure)),(pluriel(temps[2],minute)),(pluriel(temps[3],seconde)))
    
    
print(afficheTemps((1,0,14,23)))