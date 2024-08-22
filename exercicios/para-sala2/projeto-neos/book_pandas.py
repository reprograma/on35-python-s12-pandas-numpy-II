# %%
import pandas as pd
# %%
dados = pd.read_csv('book.csv',sep=';')
dados
# %%
df = pd.DataFrame(dados)
# %%
df.head()
# %%
df.isnull().sum()
# %%
df = df[['COD_CLIENTE','CLIENTE','PORTFOLIO','DATAPOS','CATEGORIA','PAPEL','PATRIM_LIQUIDO']]
df
# %%
df['PAPEL'] = df['PAPEL'].fillna('---')
df
# %%
