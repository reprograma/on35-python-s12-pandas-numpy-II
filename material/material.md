# Guia Completo de Comandos do Pandas

## Introdução ao Pandas

### Instalando Pandas
Antes de começar a usar o Pandas, certifique-se de que ele está instalado em seu ambiente:

```bash
pip install pandas
```

### Importando Pandas
Para começar a usar o Pandas, você precisa importá-lo:

```python
import pandas as pd
```

## 1. Criando Estruturas de Dados

### 1.1 Criando uma Series
Uma `Series` é uma estrutura unidimensional, similar a uma lista:

```python
import pandas as pd

# Criando uma Series
s = pd.Series([1, 3, 5, 7, 9])
print(s)
```

### 1.2 Criando um DataFrame
Um `DataFrame` é uma estrutura bidimensional, similar a uma tabela:

```python
import pandas as pd

# Criando um DataFrame
data = {
    'Nome': ['Ana', 'Bruno', 'Carla'],
    'Idade': [25, 30, 28],
    'Cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte']
}

df = pd.DataFrame(data)
print(df)
```

## 2. Carregando Dados

### 2.1 Lendo um arquivo CSV
Para carregar dados de um arquivo CSV, use:

```python
df = pd.read_csv('dados.csv')
```

### 2.2 Lendo outros formatos de arquivo
Pandas suporta a leitura de diversos formatos de arquivo, como Excel, JSON, SQL, entre outros:

```python
# Lendo um arquivo Excel
df_excel = pd.read_excel('dados.xlsx')

# Lendo um arquivo JSON
df_json = pd.read_json('dados.json')
```

## 3. Explorando e Entendendo os Dados

### 3.1 Exibindo as primeiras/últimas linhas
Use `head()` e `tail()` para visualizar as primeiras e últimas linhas:

```python
print(df.head())  # Primeiras 5 linhas
print(df.tail())  # Últimas 5 linhas
```

### 3.2 Verificando a estrutura dos dados
Para entender a estrutura do DataFrame, use:

```python
print(df.shape)      # Dimensões do DataFrame
print(df.info())     # Informações gerais sobre as colunas
print(df.describe()) # Estatísticas descritivas
```

### 3.3 Verificando tipos de dados
Para verificar o tipo de dado de cada coluna, use:

```python
print(df.dtypes)
```

### 3.4 Amostragem dos dados
Para visualizar uma amostra aleatória do DataFrame:

```python
print(df.sample(5))  # 5 linhas aleatórias
```

## 4. Selecionando e Filtrando Dados

### 4.1 Selecionando colunas específicas
Para selecionar uma ou mais colunas:

```python
# Selecionando uma coluna
print(df['Nome'])

# Selecionando múltiplas colunas
print(df[['Nome', 'Cidade']])
```

### 4.2 Selecionando linhas com base em condições
Para filtrar linhas com base em condições específicas:

```python
# Filtrando linhas onde a idade é maior que 25
filtro = df[df['Idade'] > 25]
print(filtro)
```

### 4.3 Selecionando com loc e iloc
`loc` e `iloc` são métodos poderosos para seleção de dados:

```python
# Selecionando com loc (por rótulo)
print(df.loc[0])            # Seleciona a primeira linha
print(df.loc[:, 'Nome'])    # Seleciona todas as linhas da coluna 'Nome'

# Selecionando com iloc (por índice)
print(df.iloc[0])           # Seleciona a primeira linha
print(df.iloc[:, 0])        # Seleciona todas as linhas da primeira coluna
```

## 5. Manipulando Dados

### 5.1 Renomeando colunas
Para renomear colunas:

```python
df.rename(columns={'Nome': 'Nome_Completo'}, inplace=True)
```

### 5.2 Adicionando e removendo colunas
Para adicionar ou remover colunas:

```python
# Adicionando uma nova coluna
df['Salario'] = [5000, 6000, 5500]

# Removendo uma coluna
df.drop('Salario', axis=1, inplace=True)
```

### 5.3 Lidando com valores nulos
Para identificar e tratar valores nulos:

```python
# Identificando valores nulos
print(df.isnull().sum())

# Removendo linhas com valores nulos
df.dropna(inplace=True)

# Preenchendo valores nulos com um valor específico
df.fillna(0, inplace=True)
```

### 5.4 Removendo duplicatas
Para remover linhas duplicadas:

```python
df.drop_duplicates(inplace=True)
```

### 5.5 Ordenando dados
Para ordenar os dados:

```python
# Ordenando por uma coluna
df.sort_values(by='Idade', ascending=False, inplace=True)
```

### 5.6 Resetando o índice
Para resetar o índice do DataFrame:

```python
df.reset_index(drop=True, inplace=True)
```

## 6. Agrupamento e Agregação de Dados

### 6.1 Agrupando dados
Para agrupar dados por uma coluna e realizar operações agregadas:

```python
# Agrupando por 'Cidade' e calculando a média de 'Idade'
agrupado = df.groupby('Cidade')['Idade'].mean()
print(agrupado)
```

### 6.2 Aplicando múltiplas funções de agregação
Você pode aplicar múltiplas funções ao mesmo tempo:

```python
agrupado = df.groupby('Cidade').agg({'Idade': ['mean', 'min', 'max']})
print(agrupado)
```

## 7. Mesclando, Juntando e Concatenando

### 7.1 Concatenando DataFrames
Para concatenar DataFrames:

```python
df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
df2 = pd.DataFrame({'A': [5, 6], 'B': [7, 8]})

df_concatenado = pd.concat([df1, df2])
print(df_concatenado)
```

### 7.2 Mesclando DataFrames
Para mesclar DataFrames com base em colunas comuns:

```python
df1 = pd.DataFrame({'ID': [1, 2], 'Nome': ['Ana', 'Bruno']})
df2 = pd.DataFrame({'ID': [1, 2], 'Salario': [5000, 6000]})

df_mesclado = pd.merge(df1, df2, on='ID')
print(df_mesclado)
```

## 8. Operações Matemáticas e Estatísticas

### 8.1 Operações básicas
Pandas suporta operações matemáticas diretas:

```python
df['Nova_Coluna'] = df['Idade'] + 5
```

### 8.2 Funções estatísticas
Para calcular estatísticas:

```python
print(df['Idade'].mean())  # Média
print(df['Idade'].sum())   # Soma
print(df['Idade'].min())   # Mínimo
print(df['Idade'].max())   # Máximo
print(df['Idade'].std())   # Desvio padrão
```

### 8.3 Aplicando funções personalizadas
Para aplicar funções personalizadas em colunas:

```python
def idade_dobro(x):
    return x * 2

df['Idade_Dobro'] = df['Idade'].apply(idade_dobro)
print(df)
```

## 9. Visualização de Dados

### 9.1 Gráficos básicos com Pandas
Pandas permite criar gráficos básicos diretamente dos DataFrames:

```python
df['Idade'].plot(kind='hist')  # Histograma
df['Cidade'].value_counts().plot(kind='bar')  # Gráfico de barras
```

### 9.2 Visualizações avançadas com Matplotlib e Seaborn
Para criar visualizações mais complexas, use Matplotlib e Seaborn:

```python
import matplotlib.pyplot as plt
import seaborn as sns

# Gráfico de dispersão com Seaborn
sns.scatterplot(x='Idade', y='Salario', data=df)
plt.show()
```

## 10. Integração com NumPy

### 10.1 Operações NumPy em DataFrames Pandas
Você pode aplicar funções do NumPy diretamente em colunas Pandas:

```python
import numpy as np

df['Raiz_Quadrada_Idade'] = np.sqrt(df['Idade'])
print(df)
```

## 11. Salvando e Exportando Dados

### 11.1 Salvando em CSV
Para salvar o DataFrame em um arquivo CSV:

```python
df.to_csv('saida.csv', index=False)
```

### 11.2 Salvando em outros formatos
Pandas permite exportar dados em vários formatos:

---

**Primeiro Conjunto:** Uma distribuição linear simples com pontos bem ajustados ao longo da linha de regressão.

**Segundo Conjunto:** Os pontos formam uma parábola, não uma linha reta, mostrando que a relação linear não é adequada.

**Terceiro Conjunto:** Um caso onde uma relação linear pode ser sugerida pelos números, mas existe um ponto extremo (outlier) que afeta a análise.

**Quarto Conjunto:** Um conjunto de dados em que a linha de regressão é completamente determinada por um único ponto fora da curva, enquanto os outros formam uma linha vertical.