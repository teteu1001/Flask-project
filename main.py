from flask import Flask
from database import db

app = Flask(__name__)
# Configuração do banco de dados SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Chave secreta para sessões
app.config['SECRET_KEY'] = 'sua-chave-secreta-aqui-mude-em-producao'

# Inicializa o banco de dados com o app
db.init_app(app)

# Importa os modelos primeiro (após db estar definido)
from models import User, Pedido

# Cria as tabelas e usuário padrão (se não existir)
with app.app_context():
    db.create_all()
    # Só cria o usuário padrão se ainda não existir
    if not User.query.filter_by(email='admin@teste.com').first():
        usuario_padrao = User(username='admin', email='admin@teste.com', password='123456')
        db.session.add(usuario_padrao)
        db.session.commit()
        print("Banco de dados criado! Usuario: admin@teste.com / Senha: 123456")

# Importa as rotas DEPOIS de criar o banco (evita importação circular)
from views import *

if __name__ == "__main__":
    app.run(debug=True)