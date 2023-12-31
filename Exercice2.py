import math

def delta(a , b ,c):
    return  b**2 - (4*a*c)

def NombreRacine(a, b, c):
    d = delta(a , b ,c)
    if d>0:
        return 2
    elif d == 0:
        return 1
    else:
        return 0

def AfficheNombreRacine(a , b ,c):
    n = NombreRacine(a, b, c)
    if n == 2:
        print("L'équation admet deux solution")
    elif n == 1:
        print("L'équation admet une seul solution")
    else:
        print("L'équation n'admet pas de solution réelle")

def Racine1(a , b ,c):
    d = delta(a , b ,c)
    if d > 0:
        x1 = (-b + math.sqrt(d)) / (2*a)
        return x1
    else:
        return None
    
def Racine2(a , b ,c):
    d = delta(a , b ,c)
    if d > 0:
        x2 = (-b - math.sqrt(d)) / (2*a)
        return x2
    else:
        return None

def solution_unique(a,b,c):
    d = delta(a,b,c)
    if d == 0:
        x = (-b)/2*a
        return x
    else:
        return None


# **************************** TEST ************************************ #

a  , b , c = 1 , -4 , 4

AfficheNombreRacine(a, b, c)

if NombreRacine(a, b, c) == 2:
    x1 = Racine1(a, b, c)
    x2 = Racine2(a, b, c)
    print(f"Les racines de l'équation sont x1 = {x1} et x2 = {x2}")
elif NombreRacine(a, b, c) == 1:
    x = solution_unique(a, b ,c)
    print(f"La seul solution de l'équation x = {x}")
else:
    print(f"pas de solution")


