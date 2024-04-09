
import pandas as pd
import matplotlib.pyplot as plt

# carregar dados do arquivo gasolina.csv
data = pd.read_csv('gasolina.csv')

# gerar gráfico de linha
plt.figure(figsize=(10, 6))
plt.plot(data['dia'], data['venda'], marker='o', color='red', linestyle='-')
plt.title('Gasolina em São Paulo nos 10 primeiros dias de Julho/2021')
plt.xlabel('Data')
plt.ylabel('Valor')
plt.grid(True)
plt.savefig('gasolina.png')
plt.show()
