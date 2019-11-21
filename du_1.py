# bude neco, co dovoli vybrat si zobrazeni a meritko
# az si vybere zobrazeni, tak se podle toho zaktivojou ty spravny vzorce
# pro "x" bude dycky stejnej, pro "y" se dovybere
# ulozit si to do seznamu s urcitym poradim, bod 0,0 nejak dat doprostred?
# meritko si vybere, to se jen ulozi do promenny a pak se tim proste vydeli ten vysledek

import math
#R = 6371.11

# definovani funkci pro vypocet zobrazeni
def vzorec_poledniky():
    poledniky = []
    for deg_p in range(-180, 190, 10):
        polednik = round(((R*(math.radians(deg_p))/x)), ndigits=1)
        if abs(polednik) > 100:
            polednik = "-"
        poledniky.append(polednik)
    print("Poledníky: ", poledniky)

def vzorec_lambertovo():
    rovnobezky_L=[]
    for deg_r in range(-90, 100, 10):
        rovnobezka = round(((R*(math.sin(math.radians(deg_r))))/x), ndigits=1)
        if abs(rovnobezka) > 100:
            rovnobezka = "-"
        rovnobezky_L.append(rovnobezka)
    print("Rovnoběžky: ", rovnobezky_L)

def vzorec_marinovo():
    rovnobezky_A = []
    for deg_r in range(-90, 100, 10):
        rovnobezka = round(((R*(math.radians(deg_r)))/x), ndigits=1)
        if abs(rovnobezka) > 100:
            rovnobezka = "-"
        rovnobezky_A.append(rovnobezka)
    print("Rovnoběžky: ", rovnobezky_A)

def vzorec_braunovo():
    rovnobezky_B = []
    for deg_r in range(-90, 100, 10):
        rovnobezka = round(((2*R*(math.tan(math.radians(deg_r/2))))/x), ndigits=1)
        if abs(rovnobezka) > 100:
            rovnobezka = "-"
        rovnobezky_B.append(rovnobezka)
    print("Rovnoběžky: ", rovnobezky_B)


def vzorec_mercatorovo():
    rovnobezky_M_poz = []
    for deg_r_poz in range(10, 90, 10):
        rovnobezka_poz = round(((R*(math.log(1/math.tan(math.radians((90-deg_r_poz)/2)))))/x), ndigits=1)
        if abs(rovnobezka_poz) > 100:
            rovnobezka_poz = "-"
        rovnobezky_M_poz.append(rovnobezka_poz)

    rovnobezky_M_neg = []
    for deg_r_neg in range(-80, 0, 10):
        rovnobezka_neg = round(((R*(math.log(1/math.tan(math.radians((90-deg_r_neg)/2)))))/x), ndigits=1)
        if abs(rovnobezka_neg) > 100:
            rovnobezka_neg = "-"
        rovnobezky_M_neg.append(rovnobezka_neg)

    nula = [0]
    print("Rovnoběžky: ", (rovnobezky_M_neg + nula + rovnobezky_M_poz))
# muzu pomoci plus secist seznamy  a z nuly si musim udelat taky seznam
# vyber zobrazeni uzivatelem

zobrazeni_input = input("Nejdřív si vyber zobrazení! Pro Lambertovo napiš L, pro Marinovo napiš A,\
 pro Braunovo napiš B, pro Mercatorovo napiš M :" )
zobrazeni = str(zobrazeni_input.upper())

while True:
    if zobrazeni == "L":
        print("Vybral/a sis Lambertovo válcové tečné zobrazení")
        vzorec_rovnobezky = vzorec_lambertovo
        break

    if zobrazeni == "A":
        print("Vybral/a sis Marinovo válcové tečné zobrazení")
        vzorec_rovnobezky = vzorec_marinovo
        break

    if zobrazeni == "B":
        print("Vybral/a sis Braunovo válcové tečné zobrazení")
        vzorec_rovnobezky = vzorec_braunovo
        break

    if zobrazeni == "M": # mercatorovo zobrazeni
        print("Vybral/a sis Mercatorovo válcové tečné zobrazení")
        vzorec_rovnobezky = vzorec_mercatorovo
        break

    else:
        print("Zadal/a jsi neplatný input, nelze vybrat zadání :(")
        exit()


# uzivatel zada meritko a z se nej vypocita cislo, kterym se vysledek vzorecku prevadi do cm
meritko = input("Zadej měřítko ve formě 1 : x. Napiš pouze x, celočíselně a bez mezer mezi nulami: ")
try:
    val = abs(int(meritko))
    print("Zadal/a jsi číslo:", meritko, ", bude použito měčítko 1 :", abs(val))
except ValueError:
    print("Zadal/a jsi špatně měřítko! Napsal jsi: ", meritko)

x = abs(val / 100000) # udela z meritko cislo, ktere se pouzije ve vzorci

# vyber polomeru zeme
polomer = input("Zadej v km poloměr Země, se kterým chceš počítat. Zadáš-li '0', bude použit výchozí poloměr 6371.11 km \n"
"Budeš-li zadávat desetinnou čárku, napiš ji prosím jako tečku: ")

while True:
    if polomer == "0":
        R = 6371.11
        print("Vybraný poloměr: ", (R), "km")
    else:
        R = float(polomer)
        print("Vybraný poloměr: ", (R), "km")
    break

# vysledne zobrazeni rovnobezek a poledniku
vzorec_rovnobezky()
vzorec_poledniky()
