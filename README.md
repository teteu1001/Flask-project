# 🐍 Projeto Flask

Uma aplicação web desenvolvida com Flask, Python e SQLAlchemy para gerenciamento de dados.

## 🚀 Tecnologias Utilizadas

- **[Flask](https://flask.palletsprojects.com/)** - Framework web Python
- **[SQLAlchemy](https://www.sqlalchemy.org/)** - ORM para banco de dados
- **[Flask-WTF](https://flask-wtf.readthedocs.io/)** - Formulários e validação
- **[SQLite](https://www.sqlite.org/)** - Banco de dados leve

## 📋 Pré-requisitos

- Python 3.9+
- pip (gerenciador de pacotes Python)

## 🛠️ Instalação

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/teteu1001/Flask-project.git
   cd Flask-project
   ```

2. **Crie um ambiente virtual:**
   ```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # Linux/Mac
   source venv/bin/activate
   ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Inicialize o banco de dados:**
   ```bash
   python init_db.py
   ```

## 🏃‍♂️ Executando a Aplicação

```bash
python main.py
```

A aplicação estará disponível em `http://127.0.0.1:5000`

## 📁 Estrutura do Projeto

```
flask/
├── static/                 # Arquivos estáticos (CSS, JS, imagens)
│   ├── styles.css
│   └── login.css
├── templates/              # Templates HTML
│   ├── index.html
│   └── login.html
├── instance/              # Banco de dados SQLite
│   └── database.db
├── main.py               # Ponto de entrada da aplicação
├── models.py             # Modelos de dados
├── views.py              # Rotas e lógica da aplicação
├── database.py           # Configuração do banco
├── init_db.py           # Script de inicialização
├── requirements.txt      # Dependências do projeto
└── README.md            # Este arquivo
```

## 🔧 Configuração

As configurações principais estão em `database.py`:

```python
# Configuração do banco de dados
DATABASE_URL = 'sqlite:///instance/database.db'
```

## 📝 Funcionalidades

- ✅ Autenticação de usuários
- ✅ Interface web responsiva
- ✅ Banco de dados SQLite
- ✅ Formulários validados
- ✅ Gestão de sessões

## 🤝 Como Contribuir

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/NovaFuncionalidade`)
3. Commit suas mudanças (`git commit -m 'Adicionando nova funcionalidade'`)
4. Push para a branch (`git push origin feature/NovaFuncionalidade`)
5. Abra um Pull Request

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 👤 Autor

**[Seu Nome](https://github.com/teteu1001)**

- GitHub: [@teteu1001](https://github.com/teteu1001)

## 🙏 Agradecimentos

- À comunidade Flask pela documentação excelente
- Aos contribuidores das bibliotecas utilizadas

---

⭐ Se este projeto foi útil para você, deixe uma estrela!
