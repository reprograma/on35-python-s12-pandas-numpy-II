# %%
import pandas as pd
# %%
dados = pd.read_csv('book.csv',sep=';', skipinitialspace = True)
dados
# %%
df = pd.DataFrame(dados)
# %%
df.head()
# %%
df.info()
# %%
colunas = ['COD_CLIENTE',
           'CLIENTE',
           'DATAPOS',
           'CATEGORIA',
           'CODIGO',
           'PAPEL',
           'QTDE_TOTAL',
           'PRECO',
           'VALOR_MERC_LIQUIDO']
df = df[colunas]
df
# %% 
df = df.rename(columns={"DATAPOS":"DATA_BOOK",
                        "QTDE_TOTAL":"QTDE_COTAS",
                        "PRECO":"VALOR_COTA",
                        "VALOR_MERC_LIQUIDO":"VALOR/PL"
                        })
df
# %%
df['CLIENTE'] = df['CLIENTE'].replace('NÉOS PREV. COMPLEMENTAR - ','',regex=True)
df['CLIENTE'] = df['CLIENTE'].replace('NÉOS - ','',regex=True)
df['CLIENTE'] = df['CLIENTE'].replace('NÉOS','NEOS',regex=True)
df
# %%
df['COD_CLIENTE'] = df['COD_CLIENTE'].replace(' ','',regex=True)
df['COD_CLIENTE']
# %%
df_pl_tesouraria = df[['COD_CLIENTE','CLIENTE','DATA_BOOK','CATEGORIA','VALOR/PL']]
df_pl_tesouraria
# %%
pl_tesouraria = (df_pl_tesouraria['CATEGORIA'] == 'TESOURARIA') | (df_pl_tesouraria['CATEGORIA'] == 'PATRIMONIO LIQUIDO') 
df_pl_tesouraria = df_pl_tesouraria[pl_tesouraria]
# %%
# %%
df_pl_tesouraria.to_excel('BOOK_2008.xlsx')
# %%
df_pl_tesouraria.to_csv('BOOK_2008.csv')
# %%
