# -*- coding: utf-8 -*-

def tah(pole, pozice, symbol):
    'Vrátí nové pole s hracím symbolem na dané pozici'
    return pole[:pozice] + symbol + pole[pozice + 1:]


def tah_hrace(pole, otazka):
    'Umožňuje hráči vybrat pole, na které chce umístit hrací symbol'
    while True:
        pozice=int(input(otazka))
        if pozice<0:
            print ('Nelze zadat zápornou hodnotu')
        elif pozice>19:
            print ('Takové pole neexistuje, Hrej ještě jednou')
        elif '-' not in pole[pozice]:
            print('Pole je obsazeno. Hrej znovu.')
        else:
            return tah(pole, pozice, 'x')


from random import randrange
def tah_pocitace(pole):
    "Vrátí pole s tahem počítače. Ze všech uvedených podmínek se vždy provede pouze 1"
    "Podmínka s nejvyšší prioritou se ověří jako první"

    # zabrání výhře protihráče
    if "-xx-" in pole:
        volba = randrange(1, 2) # náhodně zvolí pozici pro umístění symbolu
        if volba == 1:
            return pole.replace("-xx-", "oxx-", 1) # nahradí první podřetězec duhým 1x a vrátí
        else:
            return pole.replace("-xx-", "-xxo", 1)

    elif "x-x" in pole:
        return pole.replace("x-x", "xox", 1)

    elif "xx-" in pole: # symboly na krajích pole
        return pole.replace("xx-", "xxo", 1)
    elif "-xx" in pole:
        return pole.replace("-xx", "oxx", 1)

    # reaguje na tah protihráče
    elif "-x-" in pole: # symbol uprostřed hracího pole
        volba = randrange(1, 2)
        if volba == 1:
            return pole.replace("-x-", "ox-", 1)
        else:
            return pole.replace("-x-", "-xo", 1)

    elif "x--" in pole: # symbol na kraji hracího pole
        return pole.replace("x--", "xo-", 1)

    elif "--x" in pole:
        return pole.replace("--x", "-ox", 1)

    # zajištění výhry
    elif "-oo-" in pole:
        volba = randrange(1, 2)
        if volba == 1:
            return pole.replace("-oo-", "ooo-", 1)
        else:
            return pole.replace("-oo-", "-ooo", 1)

    elif "-oo" in pole:
        return pole.replace("-oo", "ooo", 1)

    elif "o-o" in pole:
        return pole.replace("o-o", "ooo", 1)

    elif "oo-" in pole: # krajní pozice
        return pole.replace("oo-", "ooo", 1)

    #   umístění vlastních symbolů vedle sebe
    elif "-o-" in pole:
        volba = randrange(1, 2)
        if volba == 1:
            return pole.replace("-o-", "oo-", 1)
        else:
            return pole.replace("-o-", "-oo", 1)

    # zatím prázdné hrací pole (pokud počítač začíná hru) // málo volných polí
    else:
        while "-" in pole: # dokud je v hracím poli volné místo
            pozice=randrange(19) # náhodně zvolí pozici
            if '-' in pole[pozice]: # jestliže je na pozici volno
                return tah(pole, pozice, 'o') # umístí tam symbol
                break # a skončí


def vyhodnot(pole):
    'Vrátí jednoznakový řetezec podle stavu hry'
    if  'xxx' in pole:
        vysledek = 'x' # co se má vrátit
        return vysledek # lokální proměnná, jiná než ve fci piskvorky_1d()
    elif 'ooo' in pole:
        vysledek =  'o'
        return vysledek
    elif '-' not in pole:
        vysledek = '!'
        return vysledek
    else:
        vysledek =  '-' # použito pro přerušení while cyklu v piskvorky_1d()
        return vysledek


def piskvorky1d():
    'Funkce hry piškvorky'
    pole ='-'*20 #  uloží hrací pole
    while '-' in pole:
        print(pole)
        pole = tah_hrace(pole, 'Zadej číslo pole od 0 do 19:')
        print(pole)
        print('Tah počítače:') # pro přehlednost hry
        pole = tah_pocitace(pole) # do proměnné se uloží to, co vrátí tah_pocitace
        vysledek = vyhodnot(pole) # vyhodnocení stavu hry
        if vysledek != '\'-\'': # exit test
            print(vysledek)
            break

piskvorky1d()
