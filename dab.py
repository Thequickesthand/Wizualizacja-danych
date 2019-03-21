def silnia(a):
    if a == 0:
        return 1
    i = 1
    suma = 1
    while i <= a:
        suma = suma * i
        i += 1
    return suma

print(silnia(8))
print(silnia(7))
print(silnia(2))