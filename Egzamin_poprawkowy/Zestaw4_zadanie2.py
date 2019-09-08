def funkcja(x):
    list.sort(x)
    return x[-1] - x[0]

x = [2, 3, 4, 4, -2, 8, 10]
print(funkcja(x))