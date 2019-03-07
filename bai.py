nazwisko1 = input("Napisz nazwisko: ")
nazwisko2 = input("Napisz nazwisko: ")
nazwisko3 = input("Napisz nazwisko: ")
nazwisko4 = input("Napisz nazwisko: ")
nazwisko5 = input("Napisz nazwisko: ")
tablica = [nazwisko1, nazwisko2, nazwisko3, nazwisko4, nazwisko5]
for x in range(5):
    if 'P' <= tablica[x][0] <= 'Z':
        print(tablica[x])
print("___________")
for x in range(5):
    if 6 < len(tablica[x]):
        print(tablica[x])