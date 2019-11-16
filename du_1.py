# bude neco, co dovoli vybrat si zobrazeni a meritko
# az si vybere zobrazeni, tak se podle toho zaktivojou ty spravny vzorce
# pro "x" bude dycky stejnej, pro "y" se dovybere
# ulozit si to do seznamu s urcitym poradim, bod 0,0 nejak dat doprostred?
# meritko si vybere, to se jen ulozi do promenny a pak se tim proste vydeli ten vysledek

# rovnobezky i poledniky po 10deg --> for cyklus
# ale chci to mit rovnobezky -90 az 90 a poledniky -180 az 180 pres bod [0,0] a to musi bejt stred papiru

# print(R*math.radians(u)) # = x
# print(R*math.sin(math.radians(u))) # = y, pro lambertovo zobrazeni
# x je poloha na rovniku a urcuje, kde mam kolmo na to nakreslit POLEDNIK
# y je poloha na nultym poledniku a urcuje, kde mam kolmo na to nakreslit ROVNOBEZKU (tech je min a ty se meni)jf

import math
R = 6371.11

# vyber zobrazeni uzivatelem

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

# uzivatel zada meritko a hned se z nej vypocita cislo, kterym se prevadi do [cm]

x = (float((input("Zadej měřítko, ve kterém chceš výsledek, ve formě 1 : x, celočíselně, zadej pouze x, bez mezer: ")))/100000)

# pocitadlo rovnobezek pro LAMBERT

rovnobezky = [] #seznam rovnobezek, uz se vzorcem
deg_r = -100

for _ in range(19):     # tohle je vzorec x, ten stejnej
    deg_r = (deg_r + 10)
    rovnobezka = round(((R*(math.sin(math.radians(deg_r))))/x), ndigits=1)
    rovnobezky.append(rovnobezka)
print(rovnobezky)
print(deg_r)

# pocitadlo poledniku - vsechny zobrazeni STEJNY

poledniky = []
deg_p = -190

for i in range(37):     # tohle je vzorec y, ten, co se meni
    deg_p = (deg_p + 10)
    polednik = round(((R*(math.radians(deg_p))/x)), ndigits=1)
    poledniky.append(polednik)
print(poledniky)
print(deg_p)


