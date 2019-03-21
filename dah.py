def a(**kwargs):
    suma = 0
    for x in kwargs:
        suma += kwargs[x]
    return suma / len(kwargs)

print(a(ola=1, jan=5, czarek=12))
print(a(konrad=21, sebek=20, wiktoria=90))