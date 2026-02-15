from main import app
from database import db
from flask import render_template, request, redirect, url_for, session, flash
from models import User, Pedido
from functools import wraps
from urllib.parse import quote

# Decorator para proteger rotas que exigem login
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

# Rota de login
@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        # Busca o usuário no banco de dados
        user = User.query.filter_by(email=email, password=password).first()
        
        if user:
            # Cria a sessão
            session['user_id'] = user.id
            session['username'] = user.username
            flash('Login realizado com sucesso!', 'success')
            return redirect(url_for('homepage'))
        else:
            flash('Email ou senha incorretos!', 'error')
    
    return render_template("login.html")

# Rota de logout
@app.route("/logout")
def logout():
    session.clear()
    flash('Logout realizado com sucesso!', 'success')
    return redirect(url_for('login'))

# Rota protegida - página de compras (index)
@app.route("/blog")
@login_required
def homepage():
    return render_template("index.html")

# Rota para processar o formulário de pedido
@app.route("/processar_pedido", methods=['POST'])
@login_required
def processar_pedido():
    nome = request.form.get('nome')
    email = request.form.get('email')
    telefone = request.form.get('telefone')
    mensagem = request.form.get('mensagem')
    
    if not nome or not email or not mensagem:
        flash('Por favor, preencha todos os campos obrigatórios!', 'error')
        return redirect(url_for('homepage'))
    
    # Salva o pedido no banco de dados
    novo_pedido = Pedido(
        nome=nome,
        email=email,
        telefone=telefone,
        mensagem=mensagem
    )
    
    db.session.add(novo_pedido)
    db.session.commit()
    
    # Formata a mensagem para o WhatsApp
    mensagem_whatsapp = f"*Novo Pedido de {nome}*\n\n"
    mensagem_whatsapp += f"📧 Email: {email}\n"
    if telefone:
        mensagem_whatsapp += f"📱 Telefone: {telefone}\n"
    mensagem_whatsapp += f"\n💬 Mensagem:\n{mensagem}"
    
    # Codifica a mensagem para URL
    mensagem_codificada = quote(mensagem_whatsapp)
    
    # Número do WhatsApp (61999836118)
    numero_whatsapp = "5561999836118"  # Formato: 55 (Brasil) + DDD + número
    
    # URL do WhatsApp Web
    url_whatsapp = f"https://wa.me/{numero_whatsapp}?text={mensagem_codificada}"
    
    flash('Pedido salvo com sucesso! Redirecionando para o WhatsApp...', 'success')
    
    # Redireciona para o WhatsApp
    return redirect(url_whatsapp)