# %%
import pandas as pd
# %%
dados = pd.read_csv('book.csv',sep=';', skipinitialspace = True)
# %%
df = pd.DataFrame(dados)
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

# %%
df[['CLIENTE','PAPEL','CODIGO']] = df[['CLIENTE','PAPEL','CODIGO']].fillna('--')
df
# %%
df = df.fillna(0)
df
# %%
df_pl_tesouraria = df[['COD_CLIENTE','CLIENTE','DATA_BOOK','CATEGORIA','PAPEL','VALOR/PL']]
df_pl_tesouraria

# %%
pl_tesouraria = (df_pl_tesouraria['CATEGORIA'] == 'TESOURARIA') | (df_pl_tesouraria['CATEGORIA'] == 'PATRIMONIO LIQUIDO') | (df_pl_tesouraria['PAPEL'] == 'Taxa de Custódia Apropriada') | (df_pl_tesouraria['PAPEL'] == 'Taxa de Gestão Apropriada') | (df_pl_tesouraria['PAPEL'] == 'Taxa de Administração Apropriada') 
df_pl_tesouraria = df_pl_tesouraria[pl_tesouraria]
# %%
df_pl_tesouraria.loc[df_pl_tesouraria['PAPEL'] =='--', ['PAPEL']] = df_pl_tesouraria['CATEGORIA']
df_pl_tesouraria

# %%
# filtro = ~df_pl_tesouraria['CLIENTE'].str.contains('CONSOLIDADA')
# filtro
# %%
# df_pl_tesouraria[filtro]
# %%
df_pl_tesouraria = df_pl_tesouraria[['COD_CLIENTE','CLIENTE','DATA_BOOK','PAPEL','VALOR/PL']]
df_pl_tesouraria
# %%
df_pl_tesouraria.to_excel(f'book.xlsx')
# %%
df_pl_tesouraria.to_csv(f'book.csv')
# %%
