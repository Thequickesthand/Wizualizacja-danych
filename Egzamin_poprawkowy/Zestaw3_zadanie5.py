import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dane = pd.read_csv("medale.csv", sep = ";", index_col = 0)
suma = dane["Złote"] + dane["Srebrne"] + dane["Brązowe"]
letnie = suma[dane["Rodzaj"] == "Letnie"]
zimowe = suma[dane["Rodzaj"] == "Zimowe"]
x = np.arange(len(letnie))

plt.subplot(2, 1, 1)
plt.title("Medale Olimpijskie Polski\nLato")
plt.bar(x, letnie, color = "orange")
plt.yticks([2,4,6,8,10,12,14,16])
plt.xticks(x, letnie.index)
plt.subplot(2, 1, 2)
plt.title("Medale Olimpijskie Polski\nZima")
plt.bar(x, zimowe)
plt.yticks([2,4,6,8,10,12,14,16])
plt.xticks(x, zimowe.index)

plt.savefig("costam.png")
plt.show()
print(dane)