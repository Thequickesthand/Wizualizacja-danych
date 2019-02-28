import math
print("Podaj a,b,c: ")
a = int(input())
b = int(input())
c = int(input())
delta = (b**2-(4*a*c))
if delta < 0:
    print("Delta ujemna (",delta,") brak rozwiazan")
elif delta == 0:
    print("Delta =", delta)
    x=(-b)/2*a
    print("x0", x)
elif delta > 0:
    sqrt = math.sqrt(delta)
    x1 = ((b * -1) + sqrt) / (2 * a)
    x2 = ((b * -1) - sqrt) / (2 * a)
    print("Delta= ", delta)
    print("x1=", x1)
    print("x2=", x2)
