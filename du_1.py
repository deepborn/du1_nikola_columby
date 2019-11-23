import math

"""definování funkcí pro výpočet zobrazení
   vypočítávají po deseti rozsah stupňů, které postupně vkládají do vzorce a výsledek ukládají do seznamu, který na konci tisknou
   dva vstupní parametry jsou měřítko a poloměr, které jsou uživatelem vybrané/zadané a na konci programu dosazené do funkce
   výstupem všech funkcí je seznam obsahující rovnoběžky/poledníky
"""
def vzorec_poledniky(meritko_P, polomer_P):
    poledniky = []
    for deg_p in range(-180, 190, 10):
        polednik = round(((polomer_P*(math.radians(deg_p))/meritko_P)), ndigits=1)
        if abs(polednik) > 100:
            polednik = "-"
        poledniky.append(polednik)
    print("Poledníky: ", poledniky)

def vzorec_lambertovo(meritko_L, polomer_L):
    rovnobezky_L=[]
    for deg_r in range(-90, 100, 10):
        rovnobezka = round(((polomer_L*(math.sin(math.radians(deg_r))))/meritko_L), ndigits=1)
        if abs(rovnobezka) > 100:
            rovnobezka = "-"
        rovnobezky_L.append(rovnobezka)
    print("Rovnoběžky: ", rovnobezky_L)

def vzorec_marinovo(meritko_A, polomer_A):
    rovnobezky_A = []
    for deg_r in range(-90, 100, 10):
        rovnobezka = round(((polomer_A*(math.radians(deg_r)))/meritko_A), ndigits=1)
        if abs(rovnobezka) > 100:
            rovnobezka = "-"
        rovnobezky_A.append(rovnobezka)
    print("Rovnoběžky: ", rovnobezky_A)

def vzorec_braunovo(meritko_B, polomer_B):
    rovnobezky_B = []
    for deg_r in range(-90, 100, 10):
        rovnobezka = round(((2*polomer_B*(math.tan(math.radians(deg_r/2))))/meritko_B), ndigits=1)
        if abs(rovnobezka) > 100:
            rovnobezka = "-"
        rovnobezky_B.append(rovnobezka)
    print("Rovnoběžky: ", rovnobezky_B)


def vzorec_mercatorovo(meritko_M, polomer_M):
    rovnobezky_M_poz = []
    for deg_r_poz in range(10, 90, 10):
        rovnobezka_poz = round(((polomer_M*(math.log(1/math.tan(math.radians((90-deg_r_poz)/2)))))/meritko_M), ndigits=1)
        if abs(rovnobezka_poz) > 100:
            rovnobezka_poz = "-"
        rovnobezky_M_poz.append(rovnobezka_poz)

    rovnobezky_M_neg = []
    for deg_r_neg in range(-80, 0, 10):
        rovnobezka_neg = round(((polomer_M*(math.log(1/math.tan(math.radians((90-deg_r_neg)/2)))))/x), ndigits=1)
        if abs(rovnobezka_neg) > 100:
            rovnobezka_neg = "-"
        rovnobezky_M_neg.append(rovnobezka_neg)

    nula = [0]
    pomlcka = ["-"]
    print("Rovnoběžky: ", (pomlcka + rovnobezky_M_neg + nula + rovnobezky_M_poz + pomlcka))

# výběr zobrazení uživatelem, lze použít malé i velké písmeno

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

    if zobrazeni == "M":
        print("Vybral/a sis Mercatorovo válcové tečné zobrazení")
        vzorec_rovnobezky = vzorec_mercatorovo
        break

    else:
        print("Zadal/a jsi neplatný input, nelze vybrat zadání...zkus zadat A, B, L či M ;)")
        exit()


# zadání měřítka uživatelem, jeho input se zhodnotí, zda se skutečně jedná o číslo větší než 1 a pouze poté jej lze použít

meritko = input("Zadej měřítko ve formě 1 : x. Napiš pouze x, celočíselně a bez mezer mezi nulami: ")
try:
    val = int(meritko)
    if val < 1:
        print("Zadal/a jsi '0' nebo číslo menší než '0', to bohužel měřítko být nemůže...zkus to celé znovu.")
        exit()
    print("Zadal/a jsi číslo:", meritko, ", bude použito měčítko 1 :", val)
except ValueError:
    print("Zadal/a jsi špatně měřítko! Napsal jsi: ", meritko, "zkus to znovu.")

x = abs(val / 100000) # dělení 100000 zajišťuje, že číslo "vyplivnuté" funkcí bude v cm

# výběr poloměru Země uživatelem, zadá-li "0", vybere se výchozí poloměr 6371,11 km
# zadá-li jiné číslo větší než 0, bude použit vybraný poloměr v km
polomer = input("Zadej v km poloměr Země, se kterým chceš počítat. Zadáš-li '0', bude použit výchozí poloměr 6371.11 km \n"
"Budeš-li zadávat desetinnou čárku, napiš ji prosím jako tečku: ")

try:
    hod = float(polomer)
    if hod < 0:
        print("Zadal/a jsi číslo menší než '0', to bohužel poloměr být nemůže...zkus to celé znovu.")
        exit()
except ValueError:
    print("Zadal/a jsi špatně poloměr! Napsal jsi: ", polomer, "zkus to znovu.")

while True:
    if polomer == "0":
        R = 6371.11
        print("Vybraný poloměr: ", (R), "km")
    else:
        R = float(polomer)
        print("Vybraný poloměr: ", (R), "km")
    break

# použítí funkcí, pro vypočítání a vypsání rovnoběžek a poledníků s parametry (měřítko, poloměr)
vzorec_rovnobezky(x, R)
vzorec_poledniky(x, R)
