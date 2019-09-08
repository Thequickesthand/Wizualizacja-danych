import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

ramka = pd.read_csv("wyksz.csv", sep = ',')

wyższe = ramka[ramka['Wykształcenie'] == 'wyższe']
średnie = ramka[ramka['Wykształcenie'] == 'średnie']
podstawowe = ramka[ramka['Wykształcenie'] == 'podstawowe']
x = np.arange(3)

plt.title("Wykształcenie a wiek")
plt.bar(x, wyższe['Liczebność'], width = 0.25, label = 'Wyższe', color = 'b')
plt.bar(x + 0.25, średnie['Liczebność'], width = 0.25, label = 'Średnie', color = 'g')
plt.bar(x + 0.5, podstawowe['Liczebność'], width = 0.25, label = 'Podstawowe', color = 'r')

plt.xticks([0.25, 1.25, 2.25], wyższe['Wiek'])
plt.xlabel("Przedział wiekowy")
plt.ylabel('Liczebność')

plt.legend(loc='right')

plt.show()
