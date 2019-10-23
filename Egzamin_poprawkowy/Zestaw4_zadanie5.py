import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dane = pd.read_csv("wyksz.csv")
wyzsze = dane[dane["Wykształcenie"] == "wyższe"]
srednie = dane[dane["Wykształcenie"] == "średnie"]
podstawowe = dane[dane["Wykształcenie"] == "podstawowe"]
x = np.arange(3)

plt.title("Tytul")
plt.bar(x, podstawowe['Liczebność'], width = 0.25, color = 'r', label = 'Podstawowe')
plt.bar(x + 0.25, srednie['Liczebność'], width = 0.25, color = 'g', label = 'Średnie')
plt.bar(x + 0.5, wyzsze['Liczebność'], width = 0.25, color = 'b', label = 'Wyższe')
plt.xticks([0.25, 1.25, 2.25], podstawowe['Wiek'])
plt.xlabel("Przedział wiekowy")
plt.ylabel("Liczebnosc")
plt.legend(loc = 'right')

plt.show()
print(podstawowe)