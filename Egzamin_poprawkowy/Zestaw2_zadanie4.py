import matplotlib.pyplot as plt
import pandas as pd

dane = pd.read_csv("dosw.csv")

plt.title("Wymagany tytuł")
plt.plot(dane["Czas"], dane["Zmienna1"], color = 'brown', label = 'Zmienna x', linestyle = '--')
plt.plot(dane["Czas"], dane["Zmienna2"], color = 'red', label = 'Zmienna y')

plt.yticks([-5, -10, -15])
plt.xticks([2, 3, 4, 5])
plt.ylabel("Zmienna")
plt.xlabel("Czas")
plt.legend(loc = 'center left')
plt.grid()
plt.savefig("wykres.png")
plt.show()