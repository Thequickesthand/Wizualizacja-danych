def sumacyfr(x):
    if x == 0:
        return 0
    else:
        return (x % 10) + sumacyfr(x // 10)

print(sumacyfr(34512))