import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split


arquivo = pd.read_csv("2_advertising.csv")
print(arquivo.info())

sns.pairplot(arquivo)
plt.show()

sns.heatmap(arquivo.corr(), cmap='Wistia', annot=True)
plt.show()

# IA

x = arquivo.drop("Vendas", axis=1)
y = arquivo["Vendas"]

x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size=0.25)

from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor

linear = LinearRegression()
randomforest = RandomForestRegressor()

linear.fit(x_treino, y_treino)
randomforest.fit(x_treino, y_treino)

from sklearn import metrics

teste_linear = linear.predict(x_teste)
teste_randomforest = randomforest.predict(x_teste)

# R2 - diz a porcentagem que nossa previsão se aproximou do valor real
r2_linear = metrics.r2_score(y_teste, teste_linear)
r2_randomforest = metrics.r2_score(y_teste, teste_randomforest)
print(f"R2 linear = {r2_linear}")
print(f"R2 Random Forest = {r2_randomforest}")

# MSE - Erro Quadratico Médio - Diz o quanto o nosso modelo erra ao fazer a previsão
mse_linear = metrics.mean_squared_error(y_teste, teste_linear)
mse_randomforest = metrics.mean_squared_error(y_teste, teste_randomforest)
print(f"MSE Linear = {mse_linear}")
print(f"MSE Random Forest = {mse_randomforest}")

tabela_comparacao = pd.DataFrame()

tabela_comparacao["Vendas Reais"] = y_teste
tabela_comparacao["Previsão Linear"] = teste_linear
tabela_comparacao["Previsão Random"] = teste_randomforest
tabela_comparacao = tabela_comparacao.reset_index(drop=True)

sns.lineplot(data=tabela_comparacao)
plt.show()

print(randomforest.feature_importances_)
