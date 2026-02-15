"""
Script para inicializar o banco de dados.
Execute este arquivo uma vez para criar as tabelas e um usuário padrão.
"""
from main import app
from database import db
from models import User

with app.app_context():
    # Cria todas as tabelas
    db.create_all()
    
    # Verifica se já existe um usuário
    usuario_existente = User.query.filter_by(email='admin@teste.com').first()
    
    if not usuario_existente:
        # Cria usuário padrão para teste
        usuario_padrao = User(
            username='admin',
            email='admin@teste.com',
            password='123456'
        )
        db.session.add(usuario_padrao)
        db.session.commit()
        print("Banco de dados criado com sucesso!")
        print("Usuario padrao criado:")
        print("   Email: admin@teste.com")
        print("   Senha: 123456")
    else:
        print("Banco de dados ja existe!")
        print("Usuario padrao ja foi criado anteriormente.")
