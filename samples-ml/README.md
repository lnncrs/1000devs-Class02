# Exemplos de Machine Learning com Python

Este diretório contém exemplos práticos de **Machine Learning** usando bibliotecas populares como scikit-learn, pandas e matplotlib.

## 📋 Pré-requisitos

Certifique-se de ter o ambiente `py12ml` criado e ativado:

```bash
conda activate py12ml
```

Instale as dependências necessárias:

```bash
pip install -r requirements.txt
```

**OU** instale os pacotes essenciais manualmente:

```bash
pip install numpy pandas matplotlib scikit-learn jupyter seaborn requests faker jupyterlab notebook ipywidgets pyarrow
```

## 📓 Notebooks Disponíveis

### 1. PrepararDadosClassificacao.ipynb
Demonstra técnicas de preparação e limpeza de dados para modelos de classificação:
- Carregamento de datasets
- Análise exploratória de dados (EDA)
- Tratamento de valores ausentes
- Normalização e padronização
- Divisão de dados (train/test split)

### 2. ModelosClassificacao.ipynb
Implementação e comparação de diferentes algoritmos de classificação:
- Regressão Logística
- Support Vector Machines (SVM)
- Árvores de Decisão
- Avaliação de modelos (métricas, matriz de confusão)

## 🚀 Como Executar

### Opção 1: Usando Jupyter Notebook

Inicie o Jupyter Notebook com o comando:

```bash
jupyter notebook
```

O navegador abrirá automaticamente. Navegue até o diretório `samples-ml` e clique no notebook desejado.

### Opção 2: Usando JupyterLab (Interface Moderna)

```bash
jupyter lab
```

### Opção 3: Usando Visual Studio Code

1. Abra o VS Code no diretório do projeto
2. Localize na aba **Explorador de arquivos** o diretório `samples-ml`
3. Clique no arquivo `.ipynb` desejado
4. O VS Code abrirá o notebook automaticamente
5. Selecione o kernel `py12ml` no canto superior direito

## 🎯 Estrutura dos Notebooks

Cada notebook está organizado em seções claras:

1. **Importação de Bibliotecas** - Carrega as dependências necessárias
2. **Carregamento de Dados** - Importa e visualiza os dados
3. **Análise Exploratória** - Estatísticas e visualizações
4. **Pré-processamento** - Preparação dos dados
5. **Modelagem** - Criação e treinamento de modelos
6. **Avaliação** - Análise de performance e métricas
7. **Conclusões** - Insights e próximos passos

## 📊 Bibliotecas Utilizadas

- **NumPy**: Computação numérica e arrays
- **Pandas**: Manipulação e análise de dados
- **Matplotlib**: Visualização de dados (gráficos básicos)
- **Seaborn**: Visualização estatística avançada
- **Scikit-learn**: Algoritmos de machine learning
- **Faker**: Geração de dados sintéticos (para exemplos)

## 🧪 Testando os Exemplos

### Executando Células

- **Jupyter Notebook/Lab**: Pressione `Shift + Enter` para executar uma célula
- **VS Code**: Clique no botão ▶️ ao lado da célula ou pressione `Ctrl + Enter`

### Ordem de Execução

⚠️ **Importante**: Execute as células na ordem (de cima para baixo) para evitar erros de dependências.

## 🎓 Conceitos Abordados

- **Classificação Binária e Multiclasse**
- **Validação Cruzada (Cross-Validation)**
- **Overfitting e Underfitting**
- **Feature Engineering**
- **Métricas de Avaliação**:
  - Acurácia (Accuracy)
  - Precisão (Precision)
  - Recall (Sensibilidade)
  - F1-Score
  - Matriz de Confusão
  - Curva ROC e AUC

## 🛠️ Dicas de Uso

### Reiniciar o Kernel

Se encontrar erros inesperados, reinicie o kernel:

- **Jupyter**: Menu `Kernel` → `Restart`
- **VS Code**: Botão de reiniciar no topo do notebook

### Visualizar Todas as Saídas

```python
# Configuração no início do notebook
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"
```

### Melhorar Visualizações

```python
# Configurar estilo de gráficos
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)
```

## 🤝 Contribuindo

Encontrou um erro ou tem sugestões? Abra uma issue ou pull request!
