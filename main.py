import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

notas = pd.read_csv("./ml-latest-small/ratings.csv")
filmes = pd.read_csv("./ml-latest-small/movies.csv")
tmdb = pd.read_csv("./ml-latest-small/tmdb_5000_movies.csv")
notas.columns = ['usuarioId', 'filmeId', 'nota', 'momento']
filmes.columns = ['filmeId', 'titulo', 'generos']

print(notas.head())
print(filmes.head())
print(tmdb.head())

print(tmdb.vote_average.unique())

print(notas.nota.describe())

notas.nota.plot(kind='hist')
plt.show()

medias_por_filme = notas.groupby('filmeId').mean()['nota']

sns.distplot(medias_por_filme)
plt.title('histograma das medias dos filmes')
plt.show()

sns.boxplot(y=medias_por_filme)
plt.show()

contagem_de_lingua = tmdb["original_language"].value_counts().to_frame().reset_index()
contagem_de_lingua.columns = ["original_language", "total"]

print(contagem_de_lingua.head())

sns.barplot(data=contagem_de_lingua.head(), x="original_language", y="total")
plt.show()

total_lingua = tmdb["original_language"].value_counts()
total_geral = total_lingua.sum()
total_ingles = total_lingua["en"]
total_resto = total_geral - total_ingles

dados = {
    "lingua": ["ingles", "outros"],
    "total": [total_ingles, total_resto]
}
dados = pd.DataFrame(dados)

sns.barplot(data=dados, x="lingua", y="total")
plt.show()

filmes_em_outros_idiomas = tmdb.query("original_language != 'en'")
contador_filmes_em_outros_idiomas = filmes_em_outros_idiomas.original_language.value_counts()
sns.catplot(data=filmes_em_outros_idiomas,
            x="original_language",
            kind="count",
            palette="GnBu_d",
            order=contador_filmes_em_outros_idiomas.index,
            aspect=2)
plt.show()

sns.set(style="ticks")
df = sns.load_dataset("anscombe")

sns.lmplot(x="x", y="y", col="dataset", hue="dataset", data=df,
           col_wrap=2, ci=None, palette="muted", height=4,
           scatter_kws={"s": 50, "alpha": 1})
plt.show()

