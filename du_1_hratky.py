# \n\

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

# print(R*math.radians(u)) # = x
# print(R*math.sin(math.radians(u))) # = y, pro lambertovo zobrazeni
# x je poloha na rovniku a urcuje, kde mam kolmo na to nakreslit POLEDNIK
# y je poloha na nultym poledniku a urcuje, kde mam kolmo na to nakreslit ROVNOBEZKU (tech je min a ty se meni)

import math
R = 6371.11
"""
v = 10
u = 180 # dosadim "u" a zjistim, kam mam udelat carku na ose y a tam na to budu kolmo dělat rovnobezky
d = 90 - u

print(R*math.radians(v)) # = x, platici pro vsechny zobrazeni
# vypocita polohu na rovniku (osa x), kde kolmo nacrtne polednik

print(R*math.sin(math.radians(u))) # = y, pro lambertovo zobrazeni
print(R*(math.radians(u))) # = y, pro marinovo zobrazeni
print(2*R*math.tan(math.radians(u/2))) # = y, pro braunovo zobrazeni
print(R*math.log(1/math.tan(math.radians(d/2))))  # = y, pro mercatorovo zobrazeni
"""
# jak resit meritko
# x = ((input("Zadej měřítko, ve kterém chceš výsledek, \n\
# ve formě 1 : x, celočíselně, zadej pouze x, bez mezer: "))
# meritko = x/100000
# uzivatel mi zada meritko, ja ho vydelim 100000 a vznikne mi x/100000
# tim kdyz si vydelim vysledek vzorce, dostanu ho v [cm]

# vypisovani rovnobezek ci poledniku v seznamu
"""
rovnobezky = [] #seznam rovnobezek, jen stupne
deg_r = -100
for _ in range(19):
    deg_r = (deg_r + 10)
    rovnobezky.append(deg_r)
print(rovnobezky)


poledniky = [] #seznam poledniku, jenom stupne
deg_p = -190
for i in range(37):
    deg_p = (deg_p + 10)
    poledniky.append(deg_p)
print(poledniky)
"""

# vybirani zobrazeni
"""
zobrazeni = str(input("Vyber si zobrazení! Pro Lambertovo napiš L, pro Marinovo napiš A,\
 pro Braunovo napiš B, pro Mercatorovo napiš M :" )).upper()

while True:
    if zobrazeni == "L":
        print("LAMBERT")
        break
    if zobrazeni == "A":
        print("MARIN")
        break
    if zobrazeni == "B":
        print("BRAUN")
        break
    if zobrazeni == "M":
        print("MERCATOR")
        break
    else:
        print("SPATNE JSI TO ZADAL")
        break
"""

# print(float(input("PISVOLE: ")))

# x = (float((input("Zadej měřítko, ve kterém chceš výsledek, ve formě 1 : x, celočíselně, zadej pouze x, bez mezer: ")))/100000)
meritko = input("Zadej měřítko, ve kterém chceš výsledek, ve formě 1 : x, celočíselně, zadej pouze x, bez mezer: ")
try:
    val = int(meritko)
    print("Zadal jsi správně měřítko, zvolené měřítko je 1 :", meritko)
except ValueError:
    print("Zadal jsi špatně měřítko, zkus to znovu! Napsal jsi: ", meritko)

x = int(meritko) / 100000

# pocitadlo rovnobezek pro LAMBERT
"""
for _ in range(19):     # tohle je vzorec x, ten stejnej
    deg_r = (deg_r + 10)
    rovnobezka = (R*(math.sin(math.radians(deg_r))))
    rovnobezky.append(rovnobezka)

rovnobezky_cm = [_ / x for _ in rovnobezky]
rovnobezky_zaokr = [round(_, 1) for _ in rovnobezky_cm]
print(rovnobezky)
print(rovnobezky_cm)
print(rovnobezky_zaokr)
"""

"""
def vzorec_lambertovo():
    rovnobezky_L=[]
    deg_r = -100
    for _ in range(19):
        deg_r = (deg_r + 10)
        rovnobezka = round(((R*(math.sin(math.radians(deg_r))))/x), ndigits=1)
        if abs(rovnobezka) > 100:
            rovnobezka = "-"
        rovnobezky_L.append(rovnobezka)
    print("Rovnoběžky: ", rovnobezky_L)

vzorec_lambertovo()


def vzorec_marinovo():
    rovnobezky_A = []          ###
    deg_r = -100
    for _ in range(19):
        deg_r = (deg_r + 10)
        rovnobezka = round(((R*(math.radians(deg_r)))/x), ndigits=1)
        if abs(rovnobezka) > 100:
            rovnobezka = "-"
        rovnobezky_A.append(rovnobezka)
    print("Rovnoběžky: ", rovnobezky_A)

vzorec_marinovo()


def vzorec_braunovo():
    rovnobezky_B = []
    deg_r = -100
    for _ in range(19):
        deg_r = (deg_r + 10)
        rovnobezka = round(((2*R*(math.tan(math.radians(deg_r/2))))/x), ndigits=1)
        if abs(rovnobezka) > 100:
            rovnobezka = "-"
        rovnobezky_B.append(rovnobezka)
    print("Rovnoběžky: ", rovnobezky_B)

vzorec_braunovo()
"""


def vzorec_mercatorovo():
    rovnobezky_M = []
    deg_r_poz = 0
    for _ in range(8):
        deg_r_poz = (deg_r_poz + 10)
        rovnobezka = round(((R*(math.log(1/math.tan(math.radians((90-deg_r_poz)/2)))))/x), ndigits=1)
        if abs(rovnobezka) > 100:
            rovnobezka = "-"
        rovnobezky_M.append(rovnobezka)

        rovnobezky_M_rev = list(reversed(rovnobezky_M))
        if
            rovnobezky_M_neg = [_ / -1 for _ in rovnobezky_M_rev]
    print("Rovnoběžky: ", rovnobezky_M_rev, 0, rovnobezky_M, ", -")

vzorec_mercatorovo()


# asi vyhozena cast z Mercatora

"""
rovnobezky_M_rev = list(reversed(rovnobezky_M))
        rovnobezky_M_neg = [_ / -1 for _ in rovnobezky_M_rev]

        Srovnobezky = [str(_) for _ in rovnobezky_M]
        Srovnobezky_neg = [str(_) for _ in rovnobezky_M_neg]

    print("-,", (", ".join(Srovnobezky_neg)), 0,  (", ".join(Srovnobezky)), ", -")
"""