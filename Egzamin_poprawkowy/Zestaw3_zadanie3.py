import math as m

def srednia(nap):
    dlugosc = len(nap)-1
    slowa = 1
    litery = 0
    i = 0

    while i <= dlugosc:
        if(nap[i] != ' '):
            litery += 1
        else:
            slowa += 1

        i += 1

    sr = litery/slowa

    return m.floor(sr + 0.5)

def funkcja(zdanie):
    # pomocniczy wektor przechowujący długości wyrazów w zdaniu
    dlugosci = [len(x) for x in zdanie.split()]
    # średnia z wartości na liście długosci
    srednia = sum(dlugosci) / float(len(dlugosci))
    # trik by mieć matematyczne zaokrąglenie
    srednia = m.floor(srednia + 0.5)
    return srednia

napis = "Ala ma kota"
print(srednia(napis))
napis2 = "Wlazł kotek na płotek"
print(srednia(napis2))
napis3 = "Lorem ipsum dolor sit amet"
print(srednia(napis3))