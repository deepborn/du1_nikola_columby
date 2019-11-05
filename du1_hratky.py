# to bude ale prdel

# r = 6371,11 km aka
# L --> Lambertovo zobrazení
# A --> Marinovo zobrazení
# B --> Braunovo zobrazení
# M --> Mercatorovo zobrazení

# mame to delat v radianech, takze z "math" si vezmu potrebny vzorce
# radians(stupne) mi prevede do stupnu
# sin(v radianech) vypocita sinus

import math
help(math)

R = 6371.11


print(R*math.radians(10)) # = x, platici pro vsechny zobrazeni
# vypocita polohu na rovniku (osa x), kde kolmo nacrtne polednik

u = 10 # dosadim zemepisnou delku (polednik) a zjistim, kam mam udelat carku na ose y
#                                            a tam budu dělat kolmo na to rovnobezky
print(R*math.sin(math.radians(10))) # = y, pro lambertovo zobrazeni

print(2*R*math.tan(math.radians(u/2))) # = y, pro braunovo zobrazeni