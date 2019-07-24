import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

notas = pd.read_csv("./ml-latest-small/ratings.csv")
filmes = pd.read_csv("./ml-latest-small/movies.csv")
notas.columns = ['usuarioId', 'filmeId', 'nota', 'momento']
filmes.columns = ['filmeId', 'titulo', 'generos']

print(notas.head())
print(filmes.head())

notas.nota.describe()

notas.nota.plot(kind='hist')
plt.show()

medias_por_filme = notas.groupby('filmeId').mean()['nota']

sns.distplot(medias_por_filme)
plt.title('histograma das medias dos filmes')
plt.show()

sns.boxplot(y=medias_por_filme)
plt.show()

