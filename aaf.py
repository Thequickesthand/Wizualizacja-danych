temp = int(input("Podaj temp: "))
konw = (input("Konwekcja(C,K,F): "))

if konw == "C":
    print(temp, "C")
    print(temp+273.15, "K")
    print((temp*9/5)+32, "F")

elif konw == "K":
    print(temp-273.15, "C")
    print(temp, "K")
    print(((temp-273.15) * 9 / 5) + 32, "F")

elif konw == "F":
    print(((temp-32)*5/9), "C")
    print(((temp-32)*5/9)+273.15, "K")
    print(temp, "F")
    
