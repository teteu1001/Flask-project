# Instruções de Uso - Sistema de Pedidos

## 📋 O que foi implementado:

1. ✅ Sistema de login com autenticação
2. ✅ Proteção da página de compras (exige login)
3. ✅ Formulário de pedidos que salva no banco de dados
4. ✅ Integração com WhatsApp (número: 61999836118)

## 🚀 Como usar:

### 1. Instalar dependências:
```bash
pip install -r requirements.txt
```

### 2. Inicializar o banco de dados (execute apenas uma vez):
```bash
python init_db.py
```

Isso criará:
- As tabelas no banco de dados
- Um usuário padrão para teste:
  - **Email:** admin@teste.com
  - **Senha:** 123456

### 3. Executar o aplicativo:
```bash
python main.py
```

### 4. Acessar o sistema:
- Abra o navegador em: `http://127.0.0.1:5000/login`
- Faça login com as credenciais padrão
- Você será redirecionado para a página de compras (`/blog`)

### 5. Fazer um pedido:
- Na página de compras, role até o final
- Preencha o formulário de contato com:
  - Nome
  - Email
  - Telefone (opcional)
  - Mensagem (descreva o pedido)
- Clique em "Enviar Pedido para WhatsApp"
- O pedido será salvo no banco de dados
- Você será redirecionado para o WhatsApp com a mensagem formatada

## 📱 WhatsApp:

O número configurado é: **61999836118**

A mensagem enviada terá o formato:
```
*Novo Pedido de [Nome]*

📧 Email: [email]
📱 Telefone: [telefone]
💬 Mensagem:
[mensagem do cliente]
```

## 🔐 Segurança:

⚠️ **IMPORTANTE:** Em produção, altere a chave secreta no `main.py`:
```python
app.config['SECRET_KEY'] = 'sua-chave-secreta-aqui-mude-em-producao'
```

Use uma chave forte e aleatória!

## 📊 Banco de Dados:

O banco de dados SQLite será criado automaticamente como `database.db` na pasta do projeto.

Você pode visualizar os pedidos salvos usando um gerenciador de banco de dados SQLite.

## 🛠️ Estrutura de Arquivos:

- `main.py` - Configuração principal do Flask e banco de dados
- `models.py` - Modelos de dados (User e Pedido)
- `views.py` - Rotas e lógica da aplicação
- `init_db.py` - Script para inicializar o banco
- `templates/` - Arquivos HTML
- `static/` - Arquivos CSS e JS
