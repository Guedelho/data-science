import pandas as pd
import matplotlib.pyplot as plt

notas = pd.read_csv("./ml-latest-small/ratings.csv")
print(notas.head())

notas.rating.plot(kind='hist')
plt.show()
