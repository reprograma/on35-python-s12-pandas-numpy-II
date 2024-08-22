Parte 1: Preparação do Ambiente
Instalação das bibliotecas necessárias:

Certifique-se de ter as bibliotecas necessárias instaladas. Se necessário, instale usando pip.

Geração de Dados Fictícios:

Use o script abaixo para gerar um conjunto de dados falso que simula informações de vendas de produtos em uma loja:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Configurando a seed para reprodutibilidade
np.random.seed(42)

# Gerando dados falsos
categorias = ['Eletrônicos', 'Roupas', 'Alimentos', 'Livros', 'Brinquedos']
datas = pd.date_range(start='2023-01-01', end='2023-12-31', freq='D')
num_registros = len(datas)

# Criando DataFrame
data = {
    'Data': np.random.choice(datas, num_registros),
    'Categoria': np.random.choice(categorias, num_registros),
    'Quantidade_Vendida': np.random.randint(1, 100, num_registros),
    'Preco_Unitario': np.round(np.random.uniform(10, 500, num_registros), 2)
}
df = pd.DataFrame(data)
df['Valor_Total'] = df['Quantidade_Vendida'] * df['Preco_Unitario']

# Salvando o DataFrame em um arquivo CSV
df.to_csv('dados_vendas.csv', index=False)

print("Conjunto de dados gerado e salvo como 'dados_vendas.csv'.")

Parte 2: Consulta e Filtragem de Dados
Carregar os dados:

df = pd.read_csv('dados_vendas.csv')

Pergunta 1: Quantas linhas e colunas existem no DataFrame carregado?

df.shape    # info tras colunas

Pergunta 2: Quais são os tipos de dados (dtypes) das colunas?

df.dtypes

Exibir as primeiras 5 linhas do DataFrame:

print(df.head())

Pergunta 3: Quantas categorias únicas de produtos estão presentes no DataFrame? 5

#categorias = pd.unique(df['Categoria']) ou
pd.unique(df['Categoria'])   
print(len(categorias))
print(categorias)                     # para trazer os nomes só tirar o len

Filtrar os dados para mostrar apenas as vendas da categoria 'Eletrônicos':

eletronicos = df[df['Categoria'] == 'Eletrônicos']
print(eletronicos)

 Pergunta 4: Qual é a média do valor total das vendas na categoria 'Eletrônicos'?  12291.256301

agrupado = df.groupby('Categoria')['Valor_Total'].mean().reset_index()    # o .reset_index() pode ser tirado mas ai aparece as info Name: Valor_Total, dtype: float64
print(agrupado)


Filtrar as vendas acima de R$ 1000:

vendas_acima_1000 = df[df['Valor_Total'] > 1000]
print(vendas_acima_1000)
print(len(vendas_acima_1000))   # ou print(vendas_acima_1000.count())    ou shape

Pergunta 5: Quantas vendas acima de R$ 1000 ocorreram? 330

Parte 3: Agrupamento e Agregação
Agrupar os dados por categoria e calcular o total de vendas por categoria:

total_por_categoria = df.groupby('Categoria')['Valor_Total'].sum().reset_index()
print(total_por_categoria)

Pergunta 6: Qual categoria teve o maior valor total de vendas?  Eletrônicos

Calcular a quantidade média vendida por categoria:

media_quantidade_categoria = df.groupby('Categoria')['Quantidade_Vendida'].mean().reset_index()
print(media_quantidade_categoria)

Pergunta 7: Qual categoria teve a maior quantidade média vendida? Alimentos

Parte 4: Visualização de Dados
Criar um gráfico de barras mostrando o total de vendas por categoria:

plt.figure(figsize=(10, 6))
plt.bar(total_por_categoria['Categoria'], total_por_categoria['Valor_Total'], color='skyblue')
plt.xlabel('Categoria')
plt.ylabel('Valor Total de Vendas (R$)')
plt.title('Total de Vendas por Categoria')
plt.show()

Pergunta 8: Com base no gráfico, qual categoria visualmente se destaca em termos de vendas totais? Brinquedos

Criar um gráfico de linha mostrando a variação diária das vendas de 'Eletrônicos':

vendas_diarias = eletronicos.groupby('Data')['Valor_Total'].sum().reset_index()

plt.figure(figsize=(20, 10))
plt.plot(vendas_diarias['Data'], vendas_diarias['Valor_Total'], color='purple')
plt.xlabel('Data')
plt.ylabel('Valor Total de Vendas (R$)')
plt.title('Variação Diária das Vendas de Eletrônicos')
plt.xticks(rotation=45)
plt.show()

Pergunta 9: Existe algum padrão ou tendência observável nas vendas diárias de eletrônicos? Maiores picos estão em datas como início e fim do mês, a exceção de junho.


