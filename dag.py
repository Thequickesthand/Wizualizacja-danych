def suma2(*a):
    suma = 0
    for i in range(len(a)):
        suma += pow(a[i], 2)
    return suma

print(suma2(8, 2, 1))
print(suma2(2, 2, 2))