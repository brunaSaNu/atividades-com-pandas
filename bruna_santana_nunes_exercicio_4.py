import pandas as pd
import matplotlib.pyplot as plt

# Função para ler e plotar os dados
def plotar_dados(arquivo):
    # Ler o arquivo CSV
    dados = pd.read_csv(arquivo)
    
    # Filtrar dados relevantes (ano e medalha)
    dados['Year'] = pd.to_datetime(dados['Year'], format='%Y')
    dados['Medal'] = dados['Medal'].apply(lambda x: 1 if x != 'No medal' else 0)
    
    # Agrupar por ano e somar o número de medalhas
    dados_ano = dados.groupby(dados['Year'].dt.year)['Medal'].sum().reset_index()
    dados_ano.rename(columns={'Medal': 'Quantidade de Medalhas'}, inplace=True)
    
    # Calcular a média móvel de 5 anos
    dados_ano['Média Móvel 5 Anos'] = dados_ano['Quantidade de Medalhas'].rolling(window=5).mean()
    
    # Plotar os dados
    plt.figure(figsize=(12, 6))
    plt.plot(dados_ano['Year'], dados_ano['Quantidade de Medalhas'], label='Quantidade de Medalhas')
    plt.plot(dados_ano['Year'], dados_ano['Média Móvel 5 Anos'], label='Média Móvel 5 Anos', linestyle='--')
    plt.xlabel('Ano')
    plt.ylabel('Quantidade de Medalhas')
    plt.title('Quantidade de Medalhas por Ano e Média Móvel dos Últimos 5 Anos')
    plt.legend()
    plt.grid(True)
    plt.show()

# Programa principal
arquivo_csv = "olympics_dataset.csv"  # Nome do arquivo CSV
plotar_dados(arquivo_csv)
