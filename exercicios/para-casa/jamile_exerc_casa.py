# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# %%
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

# %%
# 1. **Carregar os dados:**
df = pd.read_csv('dados_vendas.csv')
df
# %%
# 2. **Pergunta 1: Quantas linhas e colunas existem no DataFrame carregado?**
#365 linhas e 5 colunas
df.shape
# %%
# 3. **Pergunta 2: Quais são os tipos de dados (dtypes) das colunas?**
# Objeto, ponto fluante e inteiro
df.dtypess.reset_index()
# %%
# 4. **Exibir as primeiras 5 linhas do DataFrame:**
# roupas = 0,2,3,4
# alimentos = 1
df.head()
# %%
# 5. **Pergunta 3: Quantas categorias únicas de produtos estão presentes no DataFrame?**
#    - Utilize a função `unique` na coluna 'Categoria' para responder.
# As categorias unicas são: Roupas, Alimentos, Eletrônicos, Brinquedos, Livros
df_categoria_unico = pd.unique(df['Categoria'])
df_categoria_unico
# %%
# 6. **Filtrar os dados para mostrar apenas as vendas da categoria 'Eletrônicos':**
#    ```python
#    eletronicos = df[df['Categoria'] == 'Eletrônicos']
#    print(eletronicos)
#    ```
# Houve 73 vendas da categoria "Eletrônicos"
eletronicos = (df['Categoria'] == 'Eletrônicos')
df[eletronicos]
# %%
# 7. **Pergunta 4: Qual é a média do valor total das vendas na categoria 'Eletrônicos'?**
#    - Utilize a média na coluna 'Valor_Total' do DataFrame filtrado.
# A média do valor total das vendas na categoria Eletrônicos é 12291.26
eletronicos = df['Categoria'] == 'Eletrônicos'
media_eletronicos = df['Valor_Total'][eletronicos].mean()
media_eletronicos
# %%
# 8. **Filtrar as vendas acima de R$ 1000:**
#    ```python
#    vendas_acima_1000 = df[df['Valor_Total'] > 1000]
#    print(vendas_acima_1000)
#    ```
# Houve 330 vendas com o valor total acima de 1000
vendas_maior_1000 = df['Valor_Total'] > 1000
df[vendas_maior_1000]
# %%
# 9.  **Pergunta 5: Quantas vendas acima de R$ 1000 ocorreram?**
#    - Utilize a função `len` ou `shape` para descobrir a quantidade de registros.
# Houve 330 vendas com o valor total acima de 1000
tamanho = len(df[vendas_maior_1000])
print(f'Valor total de vendas maior que mil: {tamanho}')
df[vendas_maior_1000].shape
# %%
# ### **Parte 3: Agrupamento e Agregação**

# 1. **Agrupar os dados por categoria e calcular o total de vendas por categoria:**
#    ```python
#    total_por_categoria = df.groupby('Categoria')['Valor_Total'].sum().reset_index()
#    print(total_por_categoria)
#    ```
total_categoria = df.groupby('Categoria')['Valor_Total'].sum().reset_index()
total_categoria
# %%
# 2. **Pergunta 6: Qual categoria teve o maior valor total de vendas?**
# Brinquedos é a categoria com o maior valor total de vendas = R$118.7964,04
soma_valor_categoria = df.groupby('Categoria')['Valor_Total'].sum()
max_valor_categoria = df.groupby('Categoria')['Valor_Total'].sum().max()
resultado = soma_valor_categoria ==  max_valor_categoria
soma_valor_categoria[resultado]
# %%
# 3. **Calcular a quantidade média vendida por categoria:**
#    ```python
#    media_quantidade_categoria = df.groupby('Categoria')['Quantidade_Vendida'].mean().reset_index()
#    print(media_quantidade_categoria)
#    ```
media_qtd_categoria = df.groupby('Categoria')['Quantidade_Vendida'].mean().reset_index()
media_qtd_categoria
# %%
# 4. **Pergunta 7: Qual categoria teve a maior quantidade média vendida?**
# alimetos é a categoria que teve a maior qtd media vendida
categoria_qtd_vendidas = df.groupby('Categoria')['Quantidade_Vendida'].mean()
resultado = categoria_qtd_vendidas[df.groupby('Categoria')['Quantidade_Vendida'].mean() == df.groupby('Categoria')['Quantidade_Vendida'].mean().max()].reset_index()
resultado
# %%
# ### **Parte 4: Visualização de Dados**

# 1. **Criar um gráfico de barras mostrando o total de vendas por categoria:**
plt.figure(figsize=(10, 6))
plt.bar(total_categoria['Categoria'], total_categoria['Valor_Total'], color='gray')
plt.xlabel('Categoria')
plt.ylabel('Valor Total de Vendas (R$)')
plt.title('Total de Vendas por Categoria')
plt.show()
# %%
# 2. **Pergunta 8: Com base no gráfico, qual categoria visualmente se destaca em termos de vendas totais?**
#Comprovando os resultados que obtivemos na análise da pergunta 2. **Pergunta 6: Brinquedos
#a categoria com o maior valor de vendas, seguido por roupas, livros, eletopnicos e alimentos
# %%
# 3. **Criar um gráfico de linha mostrando a variação diária das vendas de 'Eletrônicos':**
#    ```python
df['Data'] = pd.to_datetime(df['Data'])

vendas_diarias = df[eletronicos].groupby('Data')['Valor_Total'].sum().reset_index()

plt.figure(figsize=(10, 6))
plt.plot(vendas_diarias['Data'], vendas_diarias['Valor_Total'], color='black')
plt.xlabel('Data')
plt.ylabel('Valor Total de Vendas (R$)')
plt.title('Variação Diária das Vendas de Eletrônicos')
plt.xticks(rotation=45)
plt.show()

# %%
#No grafico podemos analisar a alta variacao das vendas nos diferentes dias
#Essa alta variação é explicado por um alto desvido padrao, destoando bastante entre a media
#os pontos minimos e maximos de valor todal de vendas
vendas_diarias.describe()
