# Seção 38 - Python e Controle de Versionamento com Git

## 📌 Objetivo

Esta seção tem como objetivo ensinar:

1. **Execução de Scripts Python**: Como executar arquivos Python e notebooks Jupyter
2. **Controle de Versionamento**: Como usar Git e GitHub para versionamento de código

---

## 📁 Estrutura da Pasta

```
seçao_38/
├── README.md                    # Este arquivo - Documentação do projeto
├── git_comandos_basicos.txt     # Guia com comandos básicos do Git
├── comandos_python.txt          # Referência de comandos Python úteis
├── exemplo.py                   # Script Python simples de exemplo
├── exemplo2.ipynb               # Notebook Jupyter com exemplos
├── executar.bat                 # Script para executar Jupyter Notebook
├── requirements.txt             # Dependências do projeto
└── .venv/                       # Ambiente virtual Python (não versionado)
```

---

## 📚 Descrição dos Arquivos

### 📄 Arquivos de Documentação

| Arquivo | Descrição |
|---------|-----------|
| `README.md` | Documentação principal do projeto |
| `git_comandos_basicos.txt` | Guia de comandos Git essenciais |
| `comandos_python.txt` | Referência de comandos Python e pip |

### 🐍 Arquivos Python

| Arquivo | Descrição |
|---------|-----------|
| `exemplo.py` | Script Python simples com print e variáveis |
| `exemplo2.ipynb` | Notebook Jupyter interativo para testes rápidos |

### ⚙️ Arquivos de Configuração

| Arquivo | Descrição |
|---------|-----------|
| `requirements.txt` | Lista de bibliotecas Python necessárias |
| `executar.bat` | Script para iniciar o Jupyter Notebook |
| `.venv/` | Ambiente virtual Python (não deve ser versionado) |

---

## 📦 Dependências

As seguintes bibliotecas estão configuradas no projeto:

```
numpy==2.5.2
pandas==3.0.5
matplotlib==3.11.1
contourpy==1.3.3
cycler==0.12.1
fonttools==4.63.0
kiwisolver==1.5.0
packaging==26.3
pillow==12.3.0
pyparsing==3.3.2
python-dateutil==2.9.0.post0
six==1.17.0
tzdata==2026.3
```

---

## 🚀 Como Começar

### 1. Preparar o Ambiente Virtual

```bash
# Criar ambiente virtual
python -m venv .venv

# Ativar ambiente virtual (Windows)
.venv\Scripts\activate

# Ativar ambiente virtual (macOS/Linux)
source .venv/Scripts/activate
```

### 2. Instalar Dependências

```bash
# Com o ambiente virtual ativado
pip install -r requirements.txt
```

### 3. Verificar Instalação

```bash
# Listar todos os pacotes instalados
pip freeze
```

---

## 🐍 Como Executar Arquivos Python

### Executar Script Python

```bash
# Execute o arquivo Python
python exemplo.py

# Saída esperada:
# Hello, World!
# Idade: 25
```

### Executar Jupyter Notebook

**Opção 1 - Usando o script (Windows)**
```bash
executar.bat
```

**Opção 2 - Comando manual**
```bash
python -m jupyter notebook
```

Isso abrirá o Jupyter em seu navegador padrão. Clique em `exemplo2.ipynb` para abrir o notebook.

---

## 📝 Como Usar Git e GitHub

### Passo 1: Inicializar Git no Projeto

```bash
git init
```

### Passo 2: Configurar Seu Usuário

```bash
git config --global user.name "Seu Nome"
git config --global user.email "seu.email@exemplo.com"
```

### Passo 3: Criar Arquivo .gitignore

Já deve existir um `.gitignore` na raiz do projeto. Certifique-se que inclui:
```
.venv/
__pycache__/
*.pyc
.ipynb_checkpoints/
.env
```

### Passo 4: Adicionar e Comitar Arquivos

```bash
# Adicionar todos os arquivos
git add .

# Fazer o primeiro commit
git commit -m "Commit inicial - Seção 38"
```

### Passo 5: Criar Repositório no GitHub

1. Acesse [GitHub.com](https://github.com)
2. Clique em "+" (canto superior direito) > "New repository"
3. Nomeie como `seçao_38` ou similar
4. Clique em "Create repository"

### Passo 6: Vincular Repositório Remoto

```bash
# Copie a URL do seu repositório GitHub e execute:
git remote add origin https://github.com/seu_usuario/seu_repositorio.git

# Enviar para GitHub
git push -u origin main
```

### Passo 7: Trabalhar em Novas Funcionalidades

```bash
# Criar nova branch
git checkout -b feature/sua_funcionalidade

# Fazer mudanças nos arquivos...

# Adicionar mudanças
git add .

# Comitar
git commit -m "Descrição das mudanças"

# Enviar para GitHub
git push -u origin feature/sua_funcionalidade
```

---

## 📖 Referências Rápidas

Para mais detalhes sobre cada comando Git, consulte `git_comandos_basicos.txt`.

Para referência de comandos Python, consulte `comandos_python.txt`.

---

## 💡 Boas Práticas

### Python
- ✅ Use ambiente virtual para cada projeto
- ✅ Instale dependências do `requirements.txt`
- ✅ Escreva código legível e bem comentado
- ✅ Use nomes descritivos para variáveis e funções

### Git
- ✅ Faça commits frequentes com mensagens descritivas
- ✅ Use branches para novas funcionalidades
- ✅ Nunca faça commit de arquivos sensíveis (senhas, tokens, etc.)
- ✅ Atualize regularmente com `git pull`
- ✅ Revise o status antes de comitar com `git status`

---

## 🔧 Troubleshooting

### Erro: "ModuleNotFoundError"
- Certifique-se que o ambiente virtual está ativado
- Execute: `pip install -r requirements.txt`

### Erro: "python: command not found"
- Verifique se Python está instalado e no PATH
- Execute: `python --version`

### Erro: "Permission denied" ao rodar executar.bat
- Clique com botão direito e selecione "Executar como administrador"

---

## 📞 Suporte

Para dúvidas sobre Git, consulte:
- [Documentação oficial do Git](https://git-scm.com/doc)
- [GitHub Learning Lab](https://lab.github.com)

Para dúvidas sobre Python, consulte:
- [Documentação oficial do Python](https://docs.python.org)
- [Documentação do Jupyter](https://jupyter.org/documentation)

---

**Versão:** 1.0  
**Última atualização:** 2026-08-13  
**Autor:** Leonardo Costa
