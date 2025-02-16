import matplotlib.pyplot as plt

# Seus dados de exemplo
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Criar o gráfico com tamanho ajustado
plt.figure(figsize=(8, 6))
plt.plot(x, y, label='Dados de Exemplo')

# Configurar rótulos e título
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.title('Gráfico com Anotações')

# Adicionar anotações à direita do gráfico
anotacoes = [
    "Explicação 1: Alguma informação importante.",
    "Explicação 2: Outra informação relevante.",
    "Explicação 3: Mais detalhes sobre os dados.",
    # Adicione mais explicações conforme necessário
]

# Adicionar as anotações à direita do gráfico
for i, texto in enumerate(anotacoes):
    plt.text(6.2, 10 - i * 1.5, texto, fontsize=10, ha='left', va='center')

# Exibir legenda
plt.legend()

# Exibir o gráfico
plt.tight_layout()  # Ajustar o layout para evitar cortes
plt.show()
