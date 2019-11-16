# bude neco, co dovoli vybrat si zobrazeni a meritko
# az si vybere zobrazeni, tak se podle toho zaktivojou ty spravny vzorce
# pro "x" bude dycky stejnej, pro "y" se dovybere
# ulozit si to do seznamu s urcitym poradim, bod 0,0 nejak dat doprostred?
# meritko si vybere, to se jen ulozi do promenny a pak se tim proste vydeli ten vysledek

import math
R = 6371.11

# DEFINUJU FUNKCE, ALE AZ POTOM URCUJU MERITKO?????


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

# vyber zobrazeni uzivatelem

zobrazeni_input = input("Nejdřív si vyber zobrazení! Pro Lambertovo napiš L, pro Marinovo napiš A,\
 pro Braunovo napiš B, pro Mercatorovo napiš M :" )
zobrazeni = str(zobrazeni_input.upper())

while True:
    if zobrazeni == "L":
        print("Vybral sis Lambertovo válcové tečné zobrazení")

        def vzorec_pouzivany():
            vzorec_lambertovo()
        break

    if zobrazeni == "A":
        print("Vybral sis Marinovo válcové tečné zobrazení")

        def vzorec_pouzivany():
            vzorec_marinovo()
        break
    if zobrazeni == "B":
        print("Vybral sis Braunovo válcové tečné zobrazení")

        def vzorec_pouzivany():
            vzorec_braunovo()
        break
    #if zobrazeni == "M": # mercatorovo zobrazeni
     #   print("Vybral sis Mercatorovo válcové tečné zobrazení")
      #  break
    else:
        print("Zadal jsi neplatný input, nelze vybrat zadání :(")
        exit()


# uzivatel zada meritko a z se nej vypocita cislo, kterym se vysledek vzorecku prevadi do cm

meritko = input("Zadej měřítko ve formě 1 : x. Napiš pouze x, celočíselně a bez mezer mezi nulami: ")
try:
    val = int(meritko)
    print("Zadal jsi správně měřítko, zvolené měřítko je 1 :", meritko)
except ValueError:
    print("Zadal jsi špatně měřítko, zkus to znovu! Napsal jsi: ", meritko)

x = int(meritko) / 100000 # udela z meritko cislo, ktere se pouzije ve vzorci

# pocitadlo poledniku - vsechny zobrazeni STEJNY

poledniky = [] #seznam polednkiku
deg_p = -190

for i in range(37):
    deg_p = (deg_p + 10)
    polednik = round(((R*(math.radians(deg_p))/x)), ndigits=1)
    if abs(polednik) > 100:
        polednik = "-"
    poledniky.append(polednik)


vzorec_pouzivany()
print("Poledníky: ", poledniky)



