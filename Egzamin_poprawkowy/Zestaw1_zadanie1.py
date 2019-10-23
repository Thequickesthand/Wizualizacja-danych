import math as m


def pierwiastek():
    print("Podaj wspolczynnik a")
    a = int(input())
    print("Podaj wspolczynnik b")
    b = int(input())
    print("Podaj wyraz c")
    c = int(input())

    if a != 0:
        delta = m.pow(b, 2) - (4 * a * c)
        if delta < 0:
            print("Brak pierwiastkow")
        elif delta == 0:
            print("x_0 jest rowne:", -b / 2 * a)
        else:
            print("x_1 jest rowne:", -b - m.sqrt(delta) / 2 * a)
            print("x_2 jest rowne:", -b + m.sqrt(delta) / 2 * a)
    else:
        if b != 0:
            print("Pierwiastek: " + str(-c / b))
        else:
            if c == 0:
                print("Rownanie tożsamościowe")
            else:
                print("Rownanie sprzeczne")


pierwiastek()
