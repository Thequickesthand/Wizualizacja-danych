import pandas as pd
import matplotlib.pyplot as plt

dane = pd.read_csv("dosw4.csv")
plt.title("Tytuł")
plt.scatter(dane['Czas'], dane['Zmienna'], label = "Zmienna")
plt.xlabel("Czas")
plt.ylabel("Zmienna")
plt.legend(loc = 'lower center')
plt.show()

print(dane)