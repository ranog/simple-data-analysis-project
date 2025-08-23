## 🚀 Como Executar o Projeto Localmente

### Pré-requisitos

- Python 3.13.3 (gerenciado com `pyenv`)
- [Poetry](https://python-poetry.org/docs/#installation)
- Make (para usar os comandos simplificados)

## Instalação das Dependências do Projeto

### LINUX

### Instalar o pyenv
Para gerenciar versões do Python, instale o pyenv seguindo as instruções:
[https://github.com/pyenv/pyenv#installation](https://github.com/pyenv/pyenv#installation)

### Instalar dependências para compilar e instalar o Python
```bash
# Instalar dependências necessárias
sudo apt-get update
sudo apt-get install make gcc build-essential libssl-dev zlib1g-dev \
    libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm \
    libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev \
    libffi-dev liblzma-dev
```

### Instalar e configurar Python com pyenv
```bash
# Instalar Python
pyenv install 3.13.3

# Definir versão do Python para o projeto
pyenv local 3.13.3

# Instalar dependências do Python
pip install --upgrade pip setuptools wheel poetry
```

### Configurar e ativar ambiente virtual
```bash
# Criar ambiente virtual com Poetry
poetry env use 3.13.3

# Ativar ambiente virtual
source $(poetry env info --path)/bin/activate

# Instalar dependências do projeto
make install-deps
```

### Executar o projeto
```bash
# Executar o projeto
make run
```
