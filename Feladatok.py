import math

# Számold meg 10 bekért szám esetében a 3-mal osztható számokat!
def masodikFeladat():
    # bekertSzam:int = int(input("Szeretnek kerni tobb szamot"))
    index = 0
    while index < 9:
        bekertSzam: int = int(input("Szeretnek kerni tobb szamot"))
        if bekertSzam % 3 == 0:
            print("Oszható hárommal")
        else:
            print("Nem oszható 3-mal")
        index+=1

# Addig kérjünk be szám(ok)at, amíg 10-zel osztható nem lesz!*
def harmadikFeladat():
    szam = int(input("Szeretnek kerni egy számot: "))
    while not szam % 10 == 0:
        szam = int(input("Szeretnek kerni egy számot: "))
    print("Sikerült találnod, egy 10-el oszhatót. Gratulálok")
# Addig kérjünk be számokat, amíg nem kapunk kétjegyű és páros számot!*
def negyedikFeladat():
    szam:int = int(input("Szeretnék kérni egy számot, ami kétjegyű és páros"))
    while not ((szam >= 10) and (szam < 100) and (szam % 2 == 0)):
        szam = int(input("Szeretnék kérni egy számot, ami kétjegyű és páros"))
    print("Sikeresen találtál")
 # Addig kérjünk be számokat, amíg pozitív páratlan számot nem kapunk.
def otodikFeladat():
    szam:int = int(input("Szeretnék kérni egy számot"))
    while not ((szam % 2 == 1) and (szam > 0)):
       szam: int = int(input("Szeretnék kérni egy számot"))
    print("Sikeresn találtál")

#Addig kérjünk be számokat, amíg 3-mal osztható vagy négyzetszám nem lesz.*
def hatodikFeladat():
    szam: int = int(input("Szeretnék kérni egy számot"))
    while not ((szam % 3 == 0) or (math.sqrt(szam).is_integer())):
        szam: int = int(input("Szeretnék kérni egy számot"))
    print("Sikerült")

# Kérj be valós 3 számot, amíg szerkeszthető háromszög oldalait nem kapjuk!

def hetedikFeladat():
    haromszogOldalA:int = int(input("Szeretnek kerni A haromszog oldal nagysagat"))
    haromszogOldalB:int = int(input("Szeretnek kerni B haromszog oldal nagysagat"))
    haromszogOldalC:int = int(input("Szeretnek kerni C haromszog oldal nagysagat"))
    while not ((haromszogOldalA + haromszogOldalB > haromszogOldalC) and (haromszogOldalB + haromszogOldalC > haromszogOldalA) and (haromszogOldalC + haromszogOldalB > haromszogOldalA)):
        haromszogOldalA: int = int(input("Szeretnek kerni A haromszog oldal nagysagat"))
        haromszogOldalB: int = int(input("Szeretnek kerni B haromszog oldal nagysagat"))
        haromszogOldalC: int = int(input("Szeretnek kerni C haromszog oldal nagysagat"))
    print("Sikeresen csináltál működött")

# Addig kérjünk be szöveget, amíg legalább 3 karakterest nem írnak be. Majd írjuk ki a szót csupa nagy betűvel!*
def nyolcadikFeladat():
    szoveg:str = input("Szeretnek kerni egy szöveget ami legalább három karakter: ")
    index = 0
    while index < len(szoveg):
       while not (len(szoveg) >= 3):
           szoveg: str = input("Szeretnek kerni egy szöveget ami legalább három karakter: ")
       if len(szoveg) >= 3:
            print(szoveg[index].upper())
       else:
            print("HIBA: nem három karakter")
       index+=1
# Addig kérjünk be szöveget, amíg csupa kis betűs és 4 karakteres szót nem adnak meg!*
def kilencedikFeladat():
    szoveg: str = input("Szeretnek kerni egy szöveget ami legalább három karakter: ")
    index = 0
    while index < len(szoveg):
        while not (len(szoveg) >= 4):
            szoveg: str = input("Szeretnek kerni egy szöveget ami legalább három karakter: ")
        if len(szoveg) >= 4:
            kisBetu = (szoveg[index]).lower()
            print(kisBetu)
        else:
            print("HIBA: nem három karakter")
        index += 1

# Kérj a felhasználótól bizonyos számú egész számot (0-tól eltérő értékeket), és írasd ki az átlagukat 2 tizedes jegy pontossággal (a felhasználó úgy jelzi, hogy többet nem kíván beírni, hogy azt írja: 0)!

def tizedikFeladat():
    szam:int = int(input("Szeretnek kerni atlag szamot: "))
    db = 0
    osszeg = 0
    while not (szam == 0):
        osszeg += szam
        db+=1
        szam: int = int(input("Szeretnek kerni atlag szamot: "))
    print(osszeg / db)
    print("Összeg",osszeg)
    print("Darab",db)

# A fenti feladatot írd meg úgy, hogy csak pozitív számot fogadjon el (ha negatív, addig kérjen új számot, ameddig pozitív nem lesz), illetve ha 0-t ír, akkor legyen vége a bemeneteknek!
def tizenegyedikFeladat():
    szam = int(input("Szeretnek kerni egy számot: "))
    # while not (szam == 0):
    #        while szam > 0:
