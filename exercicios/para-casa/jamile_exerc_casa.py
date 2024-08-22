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
