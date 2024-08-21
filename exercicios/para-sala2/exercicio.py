# %%
import pandas as pd
df = pd.read_csv('dados_ficticios.csv')
# %%
df.head(10)
# %%
df.info
# %%
df.info()
# %%
df.describe()
# %%
condicao = (df['Categoria'] == 'A') & (df['Valor_1'] > 60)
df[condicao].head()
# %%
filtro = df[(df['Categoria'] == 'A') & (df['Valor_1'] > 60)]
filtro.head()
# %%
