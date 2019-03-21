def cg(n, a1=1, q=2):
    if n == 1:
        return a1
    return a1 * pow(q, n - 1)

print(cg(8))
print(cg(2))