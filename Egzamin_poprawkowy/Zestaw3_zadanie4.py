import matplotlib.pyplot as plt
import pandas as pd

dane = pd.read_csv("dosw3.csv", sep = ";")

plt.plot(dane["Czas"], dane["Zmienna"], color = 'g', linestyle = '--', label = "Zmienna")
plt.xlabel("Czas")
plt.ylabel("Zmienna")
plt.title("Tytuł")
plt.legend(loc = 'upper left')
plt.savefig("zadanie.png")
plt.show()
print(dane)