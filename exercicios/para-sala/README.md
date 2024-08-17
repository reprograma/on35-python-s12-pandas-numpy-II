# Exercício de Sala 🏫  

# Primeira do Dia

ter conta no Kaggle. para continuação dos estudos, e me segue lá
[https://www.kaggle.com/davinyleticia](https://www.kaggle.com/davinyleticia)

---

Revisão:

**Dataframe**: DataFrames são a outra estrutura de dados fundamental em Pandas. Trata-se de uma estrutura bidimensional com linhas e colunas nomeadas, similar a uma tabela.

**Serie**: Acessando valores individuais : Podemos acessar um valor específico utilizando a chave associada a esse valor.

---

### 1. **Visualização de Dados: Explorando o DataFrame**
**Exercício**: Exiba as 10 primeiras linhas do DataFrame gerado. Além disso, exiba informações gerais sobre o DataFrame, como tipos de dados e estatísticas descritivas.

```python
import pandas as pd

# Carregar os dados fictícios
df = pd.read_csv('dados_ficticios.csv')

# Exibir as 10 primeiras linhas
print(df.head(10))

# Exibir informações gerais
print(df.info())

# Exibir estatísticas descritivas
print(df.describe())
```

### 2. **Pandas: Consultas e Filtros Simples**
**Exercício**: Filtre o DataFrame para mostrar apenas os registros onde `Categoria` é 'A' e `Valor_1` é maior que 60.

```python
# Filtrar os registros
filtro = df[(df['Categoria'] == 'A') & (df['Valor_1'] > 60)]
print(filtro.head())
```

### 3. **Pandas: Consultas e Filtros com Datas**
**Exercício**: Filtre os registros para mostrar apenas aqueles com `Data` entre '2023-05-01' e '2023-05-31'.

```python
# Converter a coluna 'Data' para datetime se ainda não estiver
df['Data'] = pd.to_datetime(df['Data'])

# Filtrar pelo intervalo de datas
filtro_data = df[(df['Data'] >= '2023-05-01') & (df['Data'] <= '2023-05-31')]
print(filtro_data.head())
```

### 4. **Pandas: Agrupamento e Agregação Simples**
**Exercício**: Agrupe o DataFrame pela coluna `Categoria` e calcule a média de `Valor_1` e `Valor_2` para cada grupo.

```python
# Agrupamento e cálculo da média
agrupado_media = df.groupby('Categoria')[['Valor_1', 'Valor_2']].mean()
print(agrupado_media)
```

### 5. **Pandas: Agrupamento e Agregação com Funções Personalizadas**
**Exercício**: Agrupe o DataFrame pela coluna `Categoria` e calcule a soma de `Valor_3` para cada grupo. Além disso, conte o número de registros em cada grupo.

```python
# Agrupamento e cálculo da soma e contagem
agrupado_custom = df.groupby('Categoria').agg({
    'Valor_3': 'sum',
    'Categoria': 'count'
}).rename(columns={'Categoria': 'Contagem'})
print(agrupado_custom)
```

### 6. **Pandas: Gerando Gráficos Simples**
**Exercício**: Crie um gráfico de barras mostrando a média de `Valor_1` para cada `Categoria`.

```python
import matplotlib.pyplot as plt

# Agrupamento e cálculo da média
media_valor_1 = df.groupby('Categoria')['Valor_1'].mean()

# Gráfico de barras
media_valor_1.plot(kind='bar', color='skyblue', title='Média de Valor_1 por Categoria')
plt.xlabel('Categoria')
plt.ylabel('Média de Valor_1')
plt.show()
```

### 7. **Pandas: Gerando Gráficos de Linha**
**Exercício**: Crie um gráfico de linha mostrando a variação de `Valor_2` ao longo do tempo (`Data`).

```python
# Gráfico de linha
plt.figure(figsize=(10, 5))
plt.plot(df['Data'], df['Valor_2'], color='green', label='Valor_2')
plt.title('Variação de Valor_2 ao longo do tempo')
plt.xlabel('Data')
plt.ylabel('Valor_2')
plt.legend()
plt.show()
```

### 8. **Pandas: Juntando Forças com NumPy - Funções Básicas**
**Exercício**: Use NumPy para normalizar os valores da coluna `Valor_1`, deixando-os entre 0 e 1.

```python
import numpy as np

# Normalizar os valores de 'Valor_1'
df['Valor_1_normalizado'] = (df['Valor_1'] - np.min(df['Valor_1'])) / (np.max(df['Valor_1']) - np.min(df['Valor_1']))
print(df[['Valor_1', 'Valor_1_normalizado']].head())
```

### 9. **Pandas: Juntando Forças com NumPy - Estatísticas**
**Exercício**: Calcule a mediana e o desvio padrão de `Valor_2` usando funções do NumPy.

```python
# Calcular mediana e desvio padrão
mediana_valor_2 = np.median(df['Valor_2'])
desvio_padrao_valor_2 = np.std(df['Valor_2'])

print(f'Mediana de Valor_2: {mediana_valor_2}')
print(f'Desvio Padrão de Valor_2: {desvio_padrao_valor_2}')
```

### 10. **Pandas: Juntando Forças com NumPy - Operações Aritméticas**
**Exercício**: Crie uma nova coluna `Soma_Valores` que seja a soma de `Valor_1` e `Valor_2`, multiplicada por `Valor_3`.

```python
# Criar a nova coluna
df['Soma_Valores'] = (df['Valor_1'] + df['Valor_2']) * df['Valor_3']
print(df[['Valor_1', 'Valor_2', 'Valor_3', 'Soma_Valores']].head())
```

---

Terminou o exercício? Dá uma olhada nessa checklist e confere se tá tudo certinho, combinado?!

- [ ] Fiz o fork do repositório.
- [ ] Clonei o fork na minha máquina (`git clone url-do-meu-fork`).
- [ ] Resolvi o exercício.
- [ ] Adicionei as mudanças. (`git add .` para adicionar todos os arquivos, ou `git add nome_do_arquivo` para adicionar um arquivo específico)
- [ ] Commitei a cada mudança significativa ou na finalização do exercício (`git commit -m "Mensagem do commit"`)
- [ ] Pushei os commits na minha branch (`git push origin nome-da-branch`)
