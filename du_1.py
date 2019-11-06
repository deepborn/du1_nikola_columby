# bude neco, co dovoli vybrat si zobrazeni a meritko
# az si vybere zobrazeni, tak se podle toho zaktivojou ty spravny vzorce
# pro "x" bude dycky stejnej, pro "y" se dovybere
# ulozit si to do seznamu s urcitym poradim, bod 0,0 nejak dat doprostred?
# meritko si vybere, to se jen ulozi do promenny a pak se tim proste vydeli ten vysledek


# rovnobezky i poledniky po 10deg --> for cyklus
# ale chci to mit rovnobezky -90 az 90 a poledniky -180 az 180 pres bod [0,0] a to musi bejt stred papiru

import math

R = 6371.11
# print(R*math.radians(10)) # = x
# print(R*math.sin(math.radians(u))) # = y, pro lambertovo zobrazeni

rovnobezky = [] #seznam rovnobezek, uz se vzorcem
deg_r = -100

x = (float((input("Zadej měřítko, ve kterém chceš výsledek, ve formě 1 : x, celočíselně, zadej pouze x, bez mezer: ")))/100000)
print(x)

for _ in range(19):
    deg_r = (deg_r + 10)
    rovnobezka = round(((R*math.radians(deg_r))/x), ndigits=2)
    rovnobezky.append(rovnobezka)
print(rovnobezky)

poledniky = []
deg_p = -190

for _ in range(37):
    deg_p = (deg_p + 10)
    polednik = round(R*math.sin(math.radians(deg_p)), ndigits=2)
    poledniky.append(polednik)
print(poledniky)