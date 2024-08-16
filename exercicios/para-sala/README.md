# Exercício de Sala 🏫  

# Primeira do Dia

ter conta no Kaggle. para continuação dos estudos, e me segue lá
[https://www.kaggle.com/davinyleticia](https://www.kaggle.com/davinyleticia)

---

Revisão:

**Dataframe**: DataFrames são a outra estrutura de dados fundamental em Pandas. Trata-se de uma estrutura bidimensional com linhas e colunas nomeadas, similar a uma tabela.

**Serie**: Acessando valores individuais : Podemos acessar um valor específico utilizando a chave associada a esse valor.


---

# Apostila: Análise de Dados com Pandas e NumPy

## 1. Pensamento Analítico

### O que é Pensamento Analítico?
Pensamento analítico é a habilidade de decompor problemas complexos em partes menores e manejáveis. Na análise de dados, isso significa identificar as perguntas certas que precisamos responder e entender como os dados podem ajudar a resolver essas questões.

### Exemplo Prático:
Imagine que você trabalha no setor de vendas de uma empresa e quer entender quais produtos são mais populares em diferentes regiões. O primeiro passo é identificar as variáveis (produto, região, quantidade vendida) e como elas se relacionam.

---

## 2. Visualização de Dados

### Introdução
A visualização de dados é uma ferramenta poderosa para comunicar informações de maneira clara e impactante. Utilizaremos bibliotecas como Matplotlib e Seaborn para criar visualizações.

### Exemplo Prático:
Vamos criar um DataFrame com dados fictícios de vendas:

```python
import pandas as pd

# Criando o DataFrame
dados_vendas = {
    'Produto': ['Produto A', 'Produto B', 'Produto C', 'Produto A', 'Produto B'],
    'Região': ['Norte', 'Sul', 'Norte', 'Sul', 'Norte'],
    'Quantidade': [150, 200, 300, 120, 100],
    'Receita': [4500, 6000, 9000, 3600, 3000]
}

df_vendas = pd.DataFrame(dados_vendas)
print(df_vendas)
```

**Saída esperada:**

| Produto   | Região | Quantidade | Receita |
|-----------|--------|------------|---------|
| Produto A | Norte  | 150        | 4500    |
| Produto B | Sul    | 200        | 6000    |
| Produto C | Norte  | 300        | 9000    |
| Produto A | Sul    | 120        | 3600    |
| Produto B | Norte  | 100        | 3000    |

Agora, vamos visualizar esses dados:

```python
import matplotlib.pyplot as plt
import seaborn as sns

# Gráfico de dispersão para Quantidade vs Receita
sns.scatterplot(x='Quantidade', y='Receita', data=df_vendas)
plt.title('Quantidade vs Receita por Produto')
plt.show()
```

---

## 3. Pandas: Consultas e Filtros

### Introdução
Com o Pandas, podemos realizar consultas e filtros para extrair informações específicas dos nossos dados.

### Exemplo Prático:
Vamos filtrar o DataFrame `df_vendas` para mostrar apenas as vendas do "Produto A":

```python
filtro_produto_a = df_vendas[df_vendas['Produto'] == 'Produto A']
print(filtro_produto_a)
```

**Saída esperada:**

| Produto   | Região | Quantidade | Receita |
|-----------|--------|------------|---------|
| Produto A | Norte  | 150        | 4500    |
| Produto A | Sul    | 120        | 3600    |

---

## 4. Pandas: Agrupamento / Agregação

### Introdução
O agrupamento e a agregação nos permitem resumir e calcular estatísticas sobre os nossos dados.

### Exemplo Prático:
Vamos agrupar os dados por `Produto` e calcular a média de `Quantidade` e `Receita`:

```python
agrupado = df_vendas.groupby('Produto').mean()
print(agrupado)
```

**Saída esperada:**

| Produto   | Quantidade | Receita |
|-----------|------------|---------|
| Produto A | 135.0      | 4050.0  |
| Produto B | 150.0      | 4500.0  |
| Produto C | 300.0      | 9000.0  |

---

## 5. Pandas: Gerando Gráficos

### Introdução
Além das funções de visualização do Matplotlib e Seaborn, o Pandas também permite criar gráficos diretamente dos DataFrames.

### Exemplo Prático:
Vamos criar um gráfico de barras para a média de `Receita` por `Produto`:

```python
agrupado['Receita'].plot(kind='bar')
plt.title('Média de Receita por Produto')
plt.ylabel('Receita Média')
plt.show()
```

---

## 6. Pandas: Juntando forças com o pacote NumPy

### Introdução
NumPy é uma biblioteca poderosa para operações numéricas. Podemos combinar o uso de Pandas com NumPy para realizar cálculos mais avançados.

### Exemplo Prático:
Vamos calcular a raiz quadrada da `Receita` utilizando o NumPy:

```python
import numpy as np

df_vendas['Raiz_Receita'] = np.sqrt(df_vendas['Receita'])
print(df_vendas)
```

**Saída esperada:**

| Produto   | Região | Quantidade | Receita | Raiz_Receita |
|-----------|--------|------------|---------|--------------|
| Produto A | Norte  | 150        | 4500    | 67.08        |
| Produto B | Sul    | 200        | 6000    | 77.46        |
| Produto C | Norte  | 300        | 9000    | 94.87        |
| Produto A | Sul    | 120        | 3600    | 60.00        |
| Produto B | Norte  | 100        | 3000    | 54.77        |


---

Terminou o exercício? Dá uma olhada nessa checklist e confere se tá tudo certinho, combinado?!

- [ ] Fiz o fork do repositório.
- [ ] Clonei o fork na minha máquina (`git clone url-do-meu-fork`).
- [ ] Resolvi o exercício.
- [ ] Adicionei as mudanças. (`git add .` para adicionar todos os arquivos, ou `git add nome_do_arquivo` para adicionar um arquivo específico)
- [ ] Commitei a cada mudança significativa ou na finalização do exercício (`git commit -m "Mensagem do commit"`)
- [ ] Pushei os commits na minha branch (`git push origin nome-da-branch`)
