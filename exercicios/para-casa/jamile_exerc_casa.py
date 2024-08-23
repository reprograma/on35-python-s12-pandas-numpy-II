# %%
import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt

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
df.dtypes
# %%
# 4. **Exibir as primeiras 5 linhas do DataFrame:**
df.head()
# %%
# 5. **Pergunta 3: Quantas categorias únicas de produtos estão presentes no DataFrame?**
#    - Utilize a função `unique` na coluna 'Categoria' para responder.

# 6. **Filtrar os dados para mostrar apenas as vendas da categoria 'Eletrônicos':**
#    ```python
#    eletronicos = df[df['Categoria'] == 'Eletrônicos']
#    print(eletronicos)
#    ```

# 7. **Pergunta 4: Qual é a média do valor total das vendas na categoria 'Eletrônicos'?**
#    - Utilize a média na coluna 'Valor_Total' do DataFrame filtrado.

# 8. **Filtrar as vendas acima de R$ 1000:**
#    ```python
#    vendas_acima_1000 = df[df['Valor_Total'] > 1000]
#    print(vendas_acima_1000)
#    ```

# 9.  **Pergunta 5: Quantas vendas acima de R$ 1000 ocorreram?**
#    - Utilize a função `len` ou `shape` para descobrir a quantidade de registros.

# ### **Parte 3: Agrupamento e Agregação**

# 1. **Agrupar os dados por categoria e calcular o total de vendas por categoria:**
#    ```python
#    total_por_categoria = df.groupby('Categoria')['Valor_Total'].sum().reset_index()
#    print(total_por_categoria)
#    ```

# 2. **Pergunta 6: Qual categoria teve o maior valor total de vendas?**

# 3. **Calcular a quantidade média vendida por categoria:**
#    ```python
#    media_quantidade_categoria = df.groupby('Categoria')['Quantidade_Vendida'].mean().reset_index()
#    print(media_quantidade_categoria)
#    ```

# 4. **Pergunta 7: Qual categoria teve a maior quantidade média vendida?**

# ### **Parte 4: Visualização de Dados**

# 1. **Criar um gráfico de barras mostrando o total de vendas por categoria:**
#    ```python
#    plt.figure(figsize=(10, 6))
#    plt.bar(total_por_categoria['Categoria'], total_por_categoria['Valor_Total'], color='skyblue')
#    plt.xlabel('Categoria')
#    plt.ylabel('Valor Total de Vendas (R$)')
#    plt.title('Total de Vendas por Categoria')
#    plt.show()
#    ```

# 2. **Pergunta 8: Com base no gráfico, qual categoria visualmente se destaca em termos de vendas totais?**

# 3. **Criar um gráfico de linha mostrando a variação diária das vendas de 'Eletrônicos':**
#    ```python
#    vendas_diarias = eletronicos.groupby('Data')['Valor_Total'].sum().reset_index()

#    plt.figure(figsize=(10, 6))
#    plt.plot(vendas_diarias['Data'], vendas_diarias['Valor_Total'], color='purple')
#    plt.xlabel('Data')
#    plt.ylabel('Valor Total de Vendas (R$)')
#    plt.title('Variação Diária das Vendas de Eletrônicos')
#    plt.xticks(rotation=45)
#    plt.show()
#    ```
