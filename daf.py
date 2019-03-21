def sort(a):
    i = 0
    while i < len(a) - 1:
        if a[i] < a[i + 1]:
            return False
        i += 1
    return True

a = [1, 2, 3]
b = [3, 2, 1]

print(sort(a))
print(sort(b))