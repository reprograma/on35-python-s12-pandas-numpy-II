# %%
import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt
# %%
# Dados fictícios para exemplo
dados = {
    'ID_Consulta': [1, 2, 3, 4, 5],
    'Nome_Paciente': ['João Silva', 'Maria Oliveira', 'Carlos Souza', 'Ana Paula', 'Marcos Lima'],
    'Data_Consulta': ['2024-08-01', '2024-08-02', '2024-08-03', '2024-08-04', '2024-08-05'],
    'Sintomas': ['Febre, Tosse', 'Dor de Cabeça', 'Náusea, Vômito', 'Dor de Garganta', 'Cansaço, Falta de Ar'],
    'Diagnostico': ['Gripe', 'Enxaqueca', 'Gastrite', 'Amigdalite', 'Bronquite'],
    'Prescricao': ['Antitérmico, Repouso', 'Analgésico', 'Antiácido, Dieta', 'Antibiótico', 'Broncodilatador'],
    'Duracao_Consulta_Minutos': [30, 45, 25, 40, 35],  # Duração em minutos
    'Gravidade_Sintomas': [4, 6, 5, 7, 8]  # Gravidade dos sintomas em uma escala de 1 a 10
}

df = pd.DataFrame(dados)
# %%
# Limpeza = Transformation
# %%
df.isnull().sum()
# %%
df.shape
# %%
df = df.drop_duplicates()
df
# %%
df.shape
# %%
df.dtypes
# %%
df.info()
# %%
df.info(memory_usage='deep')
# %%
df.info
# %%
df.describe()
# %%
df['Data_Consulta'] = pd.to_datetime(df['Data_Consulta'])
# %%
df.dtypes
# %%
df.head()
# %%
df['Duracao_Consulta_Minutos'] = pd.to_numeric(df['Duracao_Consulta_Minutos'],errors='coerce')#errors serao transformados em NaN
df['Gravidade_Sintomas'] = pd.to_numeric(df['Gravidade_Sintomas'], errors='coerce')
# %%
df.dtypes
# %%
df.isnull().sum()
# %%
df.head()
# %%
#Gráfico de dispersão
# %%
plt.figure(figsize=(10,6))
plt.scatter(df['Duracao_Consulta_Minutos'], df['Gravidade_Sintomas'],color='blue')
plt.title('Duração da Consulta x Gravidade dos Sintomas')
plt.xlabel('Duração da Consulta (minutos)')
plt.ylabel('Gravidade dos Sintomas (1 a 10)')
plt.grid(True)
plt.show()
# %%
#Analise do grafico: 
#Não necessariamente o tempo e a gravidade tem correlação devido a pessoas com sintomas mais graves serem atendidas mais rapidos do que pessoas com sintomas menos graves
# %%
colors = df['Gravidade_Sintomas']

plt.figure(figsize=(10, 6))
scatter = plt.scatter(df['Duracao_Consulta_Minutos'], df['Gravidade_Sintomas'], c=colors, cmap='viridis')
plt.title('Duração da Consulta x Gravidade dos Sintomas')
plt.xlabel('Duração da Consulta (minutos)')
plt.ylabel('Gravidade dos Sintomas (1 a 10)')
plt.colorbar(scatter, label='Gravidade dos Sintomas')
plt.grid(True)
plt.show()
