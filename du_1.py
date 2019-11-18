# bude neco, co dovoli vybrat si zobrazeni a meritko
# az si vybere zobrazeni, tak se podle toho zaktivojou ty spravny vzorce
# pro "x" bude dycky stejnej, pro "y" se dovybere
# ulozit si to do seznamu s urcitym poradim, bod 0,0 nejak dat doprostred?
# meritko si vybere, to se jen ulozi do promenny a pak se tim proste vydeli ten vysledek

import math
R = 6371.11

# definovani funkci pro vypocet zobrazeni
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

def vzorec_marinovo():
    rovnobezky_A = []
    deg_r = -100
    for _ in range(19):
        deg_r = (deg_r + 10)
        rovnobezka = round(((R*(math.radians(deg_r)))/x), ndigits=1)
        if abs(rovnobezka) > 100:
            rovnobezka = "-"
        rovnobezky_A.append(rovnobezka)
    print("Rovnoběžky: ", rovnobezky_A)

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


def vzorec_mercatorovo():
    rovnobezky_M_poz = []
    deg_r_poz = 0
    for _ in range(8):
        deg_r_poz = (deg_r_poz + 10)
        rovnobezka_poz = round(((R * (math.log(1 / math.tan(math.radians((90 - deg_r_poz) / 2))))) / x), ndigits=1)
        if abs(rovnobezka_poz) > 100:
            rovnobezka_poz = "-"
        rovnobezky_M_poz.append(rovnobezka_poz)

    rovnobezky_M_neg = []
    deg_r_neg = 0
    for i in range(8):
        deg_r_neg = (deg_r_neg - 10)
        rovnobezka_neg = round(((R * (math.log(1 / math.tan(math.radians((90 - deg_r_neg) / 2))))) / x), ndigits=1)
        if abs(rovnobezka_neg) > 100:
            rovnobezka_neg = "-"
        rovnobezky_M_neg.append(rovnobezka_neg)
    rovnobezky_M_neg_rev = list(reversed(rovnobezky_M_neg))

    print(rovnobezky_M_neg_rev, ",", 0, ",", rovnobezky_M_poz)
# muzu pomoci plus secist seznamy  a z nuly si musim udelat taky seznam
# vyber zobrazeni uzivatelem

zobrazeni_input = input("Nejdřív si vyber zobrazení! Pro Lambertovo napiš L, pro Marinovo napiš A,\
 pro Braunovo napiš B, pro Mercatorovo napiš M :" )
zobrazeni = str(zobrazeni_input.upper())

while True:
    if zobrazeni == "L":
        print("Vybral/a sis Lambertovo válcové tečné zobrazení")

        def vzorec_pouzivany():
            vzorec_lambertovo()
        break

    if zobrazeni == "A":
        print("Vybral/a sis Marinovo válcové tečné zobrazení")

        def vzorec_pouzivany():
            vzorec_marinovo()
        break
    if zobrazeni == "B":
        print("Vybral/a sis Braunovo válcové tečné zobrazení")

        def vzorec_pouzivany():
            vzorec_braunovo()
        break
    if zobrazeni == "M": # mercatorovo zobrazeni
        print("Vybral/a sis Mercatorovo válcové tečné zobrazení")

        def vzorec_pouzivany():
            vzorec_mercatorovo()
        break
    else:
        print("Zadal/a jsi neplatný input, nelze vybrat zadání :(")
        exit()


# uzivatel zada meritko a z se nej vypocita cislo, kterym se vysledek vzorecku prevadi do cm
meritko = input("Zadej měřítko ve formě 1 : x. Napiš pouze x, celočíselně a bez mezer mezi nulami: ")
try:
    val = int(meritko)
    print("Zadal/a jsi správně měřítko, zvolené měřítko je 1 :", meritko)
except ValueError:
    print("Zadal/a jsi špatně měřítko! Napsal jsi: ", meritko)

x = int(meritko) / 100000 # udela z meritko cislo, ktere se pouzije ve vzorci


# pocitadlo poledniku
poledniky = [] #seznam polednkiku

deg_p = -190
for i in range(37):
    deg_p = (deg_p + 10)
    polednik = round(((R*(math.radians(deg_p))/x)), ndigits=1)
    if abs(polednik) > 100:
        polednik = "-"
    poledniky.append(polednik)

# vysledne zobrazeni rovnobezek
vzorec_pouzivany()
print("Poledníky: ", poledniky)