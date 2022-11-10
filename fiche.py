x, y, z = 2, 3, 4
x, y, z = y, z, x
print(x, y, z)

Type(2) donne int 
Type(True) donne bool
Type(2.0) donne float
Type("Bonjour") ou type("3") donne str

(5, 2) tuple
[5, 2] liste
{5, 2} dictionnaire

//:division euclidienne
/:division avec virgule

input():réponse en chaine de caractère
int(input()):réponse en nombre

else:
- Le mot clé else doit être au même niveau d'indentation que l'instruction if qu'elle complète.
- Le code de bloc else s'exécute si le code de bloc if ne s'exécute pas.
- elif doit également être suivi d'une condition et de deux points (:).
- Il est possible de mettre autant de elif que l'on souhaite après une condition if.
- Les instructions elif et else sont facultatives : lorsqu'une instruction en if ou elif est définie, il n'est pas obligatoire de prévoir un else après.
- L'instruction else ne peut figurer qu'une seule fois en clôture du bloc de la condition if.

 !=  Différent de

a>= b renvoie True si *a* est supérieur ou égal à b*, False sinon. 

|  False and  False  |   False   |
|  False |  True   |   False   |
|  True  |  False  |   False   |
|  True  |  True   |   True    |

x = 0
if x != 0 and 2 // x == 2 :
    print("Testing lazy evaluation")
print("Fin")

|  False or False  |   False   |
|  False |  True   |   True    |
|  True  |  False  |   True    |
|  True  |  True   |   True    |

x = 0
if x == 0 or 2 // x == 2:
    print("Test de l'évaluation paresseuse.")
print("Fin")

Priorité des opérateurs dans l'ordre décroissant 


|            ()        | 
|            **        |  
|     *, /, //, %      |
|           +, -       |
| ==, !=, <, >, <=, => |
|            not       |
|            and       |
|            or        |

while tant que 
% = il sert à diviser (si un calcul est divisable)