def silnia(a):
    if a == 0:
        return 1
    return a * silnia(a - 1)

print(silnia(8))
print(silnia(7))
print(silnia(2))