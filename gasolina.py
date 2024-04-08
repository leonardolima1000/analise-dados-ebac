
import pandas as pd
import matplotlib.pyplot as plt

# carregar dados do arquivo gasolina.csv
data = pd.read_csv('gasolina.csv')

# gerar gráfico de linha
plt.figure(figsize=(10, 6))
plt.plot(data['dia'], data['venda'], marker='o', color='blue', linestyle='-')
plt.title('Preço médio de venda da gasolina em São Paulo - Julho 2021')
plt.xlabel('Dia')
plt.ylabel('Preço (R$)')
plt.grid(True)
plt.savefig('gasolina.png')
plt.show()
