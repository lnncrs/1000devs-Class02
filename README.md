# 1000devs - AI/ML Aula 02

**Iniciativa 1000devs Aula 02 - Montagem do Ambiente de desenvolvimento Python**

Este repositório contém exemplos práticos da **montagem de um ambiente de desenvolvimento** focado em tarefas de **aprendizado de máquina**, um segundo ambiente de desenvolvimento para **APIs RESTful** e finalmente um ambiente que **integra os dois** numa **API RESTful de inferência que usa o modelo já treinado**.

## Conteúdo

- `./samples-2-ml`: Pasta com os exemplos de **Aprendizado de Máquina**.

- `./samples-1-api`: Pasta com os exemplos de **APIs RESTful**.

- `./samples-3-ai`: Pasta com os exemplos de **APIs RESTful para Inferência**.

## 🛠️ Como usar

Clone este repositório

```bash
git clone https://github.com/lnncrs/1000devs-Class02.git
```

Entre no diretório do projeto

```bash
cd 1000devs-Class02
```

## 🛠️ Instalação das ferramentas base

### 💻 Instalando o Visual Studio Code

Baixe o instalador do Visual Studio Code aqui [Visual Studio Code](https://code.visualstudio.com/) para seu sistema operacional (Windows, Linux, MacOS) e siga as instruções de instalação.

### 🔌 Instalando extensões base para o Visual Studio Code

[Python Data Science](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.python-ds-extension-pack)

[Jupyter](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter)

### ⭐ Extensões adicionais recomendadas para o Visual Studio Code

[Portuguese (Brazil) Language Pack for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=MS-CEINTL.vscode-language-pack-pt-BR)

[VS Code Speech](https://marketplace.visualstudio.com/items?itemName=ms-vscode.vscode-speech)

[.gitignore Generator](https://marketplace.visualstudio.com/items?itemName=piotrpalarz.vscode-gitignore-generator)

[Black Formatter](https://marketplace.visualstudio.com/items?itemName=ms-python.black-formatter)

[GitLens — Git supercharged](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens)

[Git Graph](https://marketplace.visualstudio.com/items?itemName=mhutchie.git-graph)

[Gremlins tracker for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=nhoizey.gremlins)

[XML](https://marketplace.visualstudio.com/items?itemName=redhat.vscode-xml)

[YAML](https://marketplace.visualstudio.com/items?itemName=redhat.vscode-yaml)

### 📦 Instalando o Git

Baixe o instalador do git aqui [Git Downloads](https://git-scm.com/downloads) para seu sistema operacional (Windows, Linux, MacOS) e siga as instruções de instalação.

### 🐍 Instalando o Anaconda ou CondaForge (Gerenciador de ambientes Python)

**Para usar [Anaconda](https://www.anaconda.com/)** como gerenciador de ambientes:

Baixe o instalador aqui [Anaconda Downloads](https://www.anaconda.com/products/distribution) escolha Miniconda como distribuição, selecione o seu sistema operacional (Windows, Linux, MacOS) e siga as instruções de instalação.

**Para usar [CondaForge](https://conda-forge.org/)** como gerenciador de ambientes:

Baixe o instalador aqui [CondaForge Downloads](https://conda-forge.org/download/) selecione o seu sistema operacional (Windows, Linux, MacOS) e siga as instruções de instalação.

Após a instalação, inicialize o ambiente com o comando:

```bash
conda init
```

Verifique se o conda foi instalado corretamente com o comando:

```bash
conda --version
```

Verifique a versão do Python instalada no ambiente base com o comando:

```bash
python --version
```

### 🤖 Criando seu ambiente virtual para AI/ML

Vamos criar um ambiente virtual chamado `py12ml` com Python 3.12

```bash
conda create -n py12ml python=3.12
```

Ative o ambiente virtual com o comando:

```bash
conda activate py12ml
```

Verifique se o ambiente virtual está ativo com o comando:

```bash
conda info --envs
```

#### 📚 Instalando pacotes essenciais para AI/ML

Com o ambiente virtual `py12ml` ativo, instale os pacotes essenciais para desenvolvimento em Machine Learning com o comando:

```bash
pip install numpy pandas matplotlib scikit-learn jupyter seaborn requests faker jupyterlab notebook ipywidgets pyarrow
```

#### 📓 Usando notebooks Jupyter através do utilitário Jupyter Notebook

Inicie o Jupyter Notebook com o comando:

```bash
jupyter notebook
```

Navegue até o diretório `./samples-2-ml` para acessar os notebooks de exemplo.

#### 📝 Usando notebooks Jupyter através do Visual Studio Code

Localize na aba `Explorador de arquivos` o diretório `./samples-2-ml` para acessar os notebooks de exemplo.

Veja mais detalhes no [README do ML](samples-2-ml/README.md).

### 🌐 Criando seu ambiente virtual para APIs RESTful

Vamos criar um ambiente virtual chamado `py12api` com Python 3.12

```bash
conda create -n py12api python=3.12
```

Ative o ambiente virtual com o comando:

```bash
conda activate py12api
```

Verifique se o ambiente virtual está ativo com o comando:

```bash
conda info --envs
```

#### 📦 Instalando pacotes essenciais para API RESTful

Com o ambiente virtual `py12api` ativo, instale os pacotes essenciais para desenvolvimento de APIs RESTful com o comando:

```bash
pip install fastapi uvicorn pytz
```

#### 🚀 Executando o exemplo de API RESTful

Acesse a pasta de exemplos e execute:

```bash
cd samples-1-api
uvicorn main:app --reload
```

A API estará disponível em **http://localhost:8000**

Acesse a documentação interativa em **http://localhost:8000/docs**

Veja mais detalhes no [README da API](samples-1-api/README.md).

### 🧠 Criando seu ambiente virtual para APIs de Inferência (AI)

Vamos criar um ambiente virtual chamado `py12ai` com Python 3.12

```bash
conda create -n py12ai python=3.12
```

Ative o ambiente virtual com o comando:

```bash
conda activate py12ai
```

Verifique se o ambiente virtual está ativo com o comando:

```bash
conda info --envs
```

#### 📦 Instalando pacotes essenciais para API de Inferência

Com o ambiente virtual `py12ai` ativo, instale os pacotes essenciais para servir modelos de Machine Learning via API RESTful com o comando:

```bash
pip install fastapi uvicorn scikit-learn pandas numpy joblib
```

#### 🚀 Executando o exemplo de API de Inferência

Acesse a pasta de exemplos e execute:

```bash
cd samples-3-ai
uvicorn main:app --reload
```

A API estará disponível em **http://localhost:8000**

Acesse a documentação interativa em **http://localhost:8000/docs**

Esta API carrega automaticamente o modelo treinado em `outputs/best_classification_model.pkl` e permite fazer predições de classificação de câncer de mama através de endpoints REST.

Veja mais detalhes no [README da API de Inferência](samples-3-ai/README.md).

## 🤝 Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests com melhorias, correções ou novos exemplos.
