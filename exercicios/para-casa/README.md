# Exercício de Casa 🏠 


**Obs.:** 📝 *Leia tudo com atenção antes de começar a fazer, ok?* ✨  
Existem explicações importantes no final do arquivo. 💡

Dica da Tia Letícia: *Preste bastante atenção! Não pule etapas e lembre-se de se divertir enquanto aprende!* 😊📚

---

**Trabalho de Casa: Análise e Visualização de Dados com Pandas**

**Objetivo:**
Neste exercício, você vai praticar a manipulação, consulta, filtragem, agregação e visualização de dados usando a biblioteca Pandas e o Matplotlib em Python. Vamos trabalhar com um conjunto de dados fictícios que contém informações sobre vendas de uma loja.

### **Parte 1: Preparação do Ambiente**

1. **Instalação das bibliotecas necessárias:**

   Certifique-se de ter as bibliotecas necessárias instaladas. Se necessário, instale usando pip:
   ```bash
   pip install pandas matplotlib numpy
   ```

2. **Geração de Dados Fictícios:**

   Use o script abaixo para gerar um conjunto de dados falso que simula informações de vendas de produtos em uma loja:

   ```python
   import pandas as pd
   import numpy as np
   import matplotlib.pyplot as plt

   # Configurando a seed para reprodutibilidade
   np.random.seed(42)

   # Gerando dados falsos
   categorias = ['Eletrônicos', 'Roupas', 'Alimentos', 'Livros', 'Brinquedos']
   datas = pd.date_range(start='2023-01-01', end='2023-12-31', freq='D')
   num_registros = len(datas)



   # Salvando o DataFrame em um arquivo CSV
   df.to_csv('dados_vendas.csv', index=False)

   print("Conjunto de dados gerado e salvo como 'dados_vendas.csv'.")
   ```

### **Parte 2: Consulta e Filtragem de Dados**

1. **Carregar os dados:**

  neste parte vc deve caregar o csv gerado para podemos continuar

2. **Pergunta 1: Quantas linhas e colunas existem no DataFrame carregado?**
   - Use a função `shape` para descobrir.

3. **Pergunta 2: Quais são os tipos de dados (dtypes) das colunas?**
   - Use a função `dtypes` para listar os tipos.

4. **Exibir as primeiras 5 linhas do DataFrame:**
   ```python
   print(df.head())
   ```

5. **Pergunta 3: Quantas categorias únicas de produtos estão presentes no DataFrame?**
   - Utilize a função `unique` na coluna 'Categoria' para responder.

6. **Filtrar os dados para mostrar apenas as vendas da categoria 'Eletrônicos':**
   ```python
   eletronicos = df[df['Categoria'] == 'Eletrônicos']
   print(eletronicos)
   ```

7. **Pergunta 4: Qual é a média do valor total das vendas na categoria 'Eletrônicos'?**
   - Utilize a média na coluna 'Valor_Total' do DataFrame filtrado.

8. **Filtrar as vendas acima de R$ 1000:**
   ```python
   vendas_acima_1000 = df[df['Valor_Total'] > 1000]
   print(vendas_acima_1000)
   ```

9.  **Pergunta 5: Quantas vendas acima de R$ 1000 ocorreram?**
   - Utilize a função `len` ou `shape` para descobrir a quantidade de registros.

### **Parte 3: Agrupamento e Agregação**

1. **Agrupar os dados por categoria e calcular o total de vendas por categoria:**
   ```python
   total_por_categoria = df.groupby('Categoria')['Valor_Total'].sum().reset_index()
   print(total_por_categoria)
   ```

2. **Pergunta 6: Qual categoria teve o maior valor total de vendas?**

3. **Calcular a quantidade média vendida por categoria:**
   ```python
   media_quantidade_categoria = df.groupby('Categoria')['Quantidade_Vendida'].mean().reset_index()
   print(media_quantidade_categoria)
   ```

4. **Pergunta 7: Qual categoria teve a maior quantidade média vendida?**

### **Parte 4: Visualização de Dados**

1. **Criar um gráfico de barras mostrando o total de vendas por categoria:**
   ```python
   plt.figure(figsize=(10, 6))
   plt.bar(total_por_categoria['Categoria'], total_por_categoria['Valor_Total'], color='skyblue')
   plt.xlabel('Categoria')
   plt.ylabel('Valor Total de Vendas (R$)')
   plt.title('Total de Vendas por Categoria')
   plt.show()
   ```

2. **Pergunta 8: Com base no gráfico, qual categoria visualmente se destaca em termos de vendas totais?**

3. **Criar um gráfico de linha mostrando a variação diária das vendas de 'Eletrônicos':**
   ```python
   vendas_diarias = eletronicos.groupby('Data')['Valor_Total'].sum().reset_index()

   plt.figure(figsize=(10, 6))
   plt.plot(vendas_diarias['Data'], vendas_diarias['Valor_Total'], color='purple')
   plt.xlabel('Data')
   plt.ylabel('Valor Total de Vendas (R$)')
   plt.title('Variação Diária das Vendas de Eletrônicos')
   plt.xticks(rotation=45)
   plt.show()
   ```

4. **Pergunta 9: Existe algum padrão ou tendência observável nas vendas diárias de eletrônicos?**

### **Entrega:**
- Envie o código em notebook (ipynb) completo que realiza todas as operações acima.
- também deve conter os gráficos gerados.
- Responda às perguntas com base nos resultados obtidos em celulas markdown

---

**Orientações Finais:**
- Use comentários no código para explicar cada parte.
- Não se preocupe com a aparência dos gráficos; foque na funcionalidade.
- Se tiver dúvidas, reveja os conceitos básicos de Pandas e Matplotlib.

Bom trabalho!
---

Terminou o exercício? Dá uma olhada nessa checklist e confere se tá tudo certinho, combinado?!

- [x] Fiz o fork do repositório.
- [x] Clonei o fork na minha máquina (`git clone url-do-meu-fork`).
- [x] Resolvi o exercício.
- [x] Adicionei as mudanças. (`git add .` para adicionar todos os arquivos, ou `git add nome_do_arquivo` para adicionar um arquivo específico)
- [x] Commitei a cada mudança significativa ou na finalização do exercício (`git commit -m "Mensagem do commit"`)
- [x] Pushei os commits na minha branch (`git push origin nome-da-branch`)
- [x] Criei um Pull Request seguindo as orientaçoes que estao nesse [documento](https://github.com/mflilian/repo-example/blob/main/exercicios/para-casa/instrucoes-pull-request.md).
