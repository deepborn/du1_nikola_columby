# to bude ale prdel

# L --> Lambertovo zobrazení
# A --> Marinovo zobrazení
# B --> Braunovo zobrazení
# M --> Mercatorovo zobrazení

# u --> zemepisna delka (fi, poledniky)
# v --> zemepisna sirka (lambda, rovnobezky)
# d --> doplnek, = 90 - u

# mame to delat v radianech, takze z "math" si vezmu potrebny vzorce
# radians(stupne) mi prevede do stupnu
# sin(v radianech) vypocita sinus
# tan(v radianech) vypocita tangens
# log(x, ...) kdyz necham ... prazdny, bude zakladni

import math
# help(math)

R = 6371.11
u = 10 # dosadim "u" a zjistim, kam mam udelat carku na ose y a tam na to budu kolmo dělat rovnobezky
d = 90 - u

print(R*math.radians(10)) # = x, platici pro vsechny zobrazeni
# vypocita polohu na rovniku (osa x), kde kolmo nacrtne polednik

print(R*math.sin(math.radians(u))) # = y, pro lambertovo zobrazeni
print(R*(math.radians(u))) # = y, pro marinovo zobrazeni
print(2*R*math.tan(math.radians(u/2))) # = y, pro braunovo zobrazeni
print(R*math.log(1/math.tan(math.radians(d/2))))  # = y, pro mercatorovo zobrazeni

# jak resit meritko
x = ((input("Zadej měřítko, ve kterém chceš výsledek, \n\
 ve formě 1 : x, celočíselně, zadej pouze x, bez mezer: "))
meritko = x/100000
# uzivatel mi zada meritko, ja ho vydelim 100000 a vznikne mi x/100000
# tim kdyz si vydelim vysledek vzorce, dostanu ho v [cm]