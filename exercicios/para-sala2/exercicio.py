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
filtro = df[(df['Categoria'] == 'A') & (df['Valor_1'] > 60)]
filtro.head(20)
# %%
df['Data'] = pd.to_datetime(df['Data'])
df['Data']
# %%
df = df[(df['Data'] > '2023-05-01') & (df['Data'] < '2023-05-31')]
df.head()
# %%
condiction = (df['Data'] > '2023-05-01') & (df['Data'] < '2023-05-31')
df[condiction].head(10)
# %%
df.rename(columns={'Valor_1':'estoque da loja1',
                   'Valor_2':'estoque da loja2',
                   'Valor_3':'vendas'
                   }, inplace=True
         )
# %%
df.head()
# %%
agrupado_media = df.groupby('Categoria')[['estoque da loja1','estoque da loja2']].mean()
# %%
agrupado_media
# %%
agrupado_max = df.groupby('Categoria')[['estoque da loja1','estoque da loja2']].max()
agrupado_max
# %%
agrupado_min = df.groupby('Categoria')[['estoque da loja1','estoque da loja2']].min()
agrupado_min
# %%
agrupado_custom = df.groupby('Categoria').agg({'vendas':'sum', 'Categoria':'count'}).rename(columns={'Categoria':'contagem de pessoa'})
agrupado_custom
#com o metodo agg vc consegue especificar o que vc vai fazer com cada coluna
# %%
import matplotlib.pyplot as plt

# %%
media_valor_1 = df.groupby('Categoria')['estoque da loja1'].mean()
# %%
media_valor_1.plot(kind='bar',color='b', title='Média de estoque da loja 1 por categoria')
#cor hexadecimal vai de 0 a F
plt.xlabel('Categoria')
plt.ylabel('Média de estoque da loja1')
plt.show()
# %%

# %%
