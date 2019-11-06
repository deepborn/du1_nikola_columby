# bude neco, co dovoli vybrat si zobrazeni a meritko
# az si vybere zobrazeni, tak se podle toho zaktivojou ty spravny vzorce
# pro "x" bude dycky stejnej, pro "y" se dovybere
# ulozit si to do seznamu s urcitym poradim, bod 0,0 nejak dat doprostred?
# meritko si vybere, to se jen ulozi do promenny a pak se tim proste vydeli ten vysledek


# rovnobezky i poledniky po 10deg --> for cyklus
# ale chci to mit rovnobezky -90 az 90 a poledniky -180 az 180 pres bod [0,0] a to musi bejt stred papiru

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


