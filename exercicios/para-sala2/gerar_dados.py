import pandas as pd
import numpy as np

# Definir número de registros
num_registros = 1000

# Gerar dados fictícios
np.random.seed(42)  # Para reprodutibilidade

# Colunas categóricas
categorias = ['A', 'B', 'C', 'D']
categorias_coluna = np.random.choice(categorias, num_registros)

# Colunas numéricas
valores_1 = np.random.normal(loc=50, scale=10, size=num_registros)
valores_2 = np.random.normal(loc=100, scale=20, size=num_registros)
valores_3 = np.random.randint(1, 10, num_registros)

# Datas
datas = pd.date_range(start='2023-01-01', periods=num_registros, freq='D')

# DataFrame
df_ficticio = pd.DataFrame({
    'Categoria': categorias_coluna,
    'Valor_1': valores_1,
    'Valor_2': valores_2,
    'Valor_3': valores_3,
    'Data': datas
})

# Exibir as primeiras linhas
print(df_ficticio.head())

# Salvar em CSV
df_ficticio.to_csv('dados_ficticios.csv', index=False)
