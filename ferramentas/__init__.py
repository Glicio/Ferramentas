from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from ferramentas.funcoes import formatData

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///ferramentas.db"
app.config['SECRET_KEY'] = "11fbf5e98d8aa591a4303751"
app.jinja_env.globals.update(formatData=formatData)
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = "login_page"
login_manager.login_message = "Para acessar essa página faça login!"
bcrypt = Bcrypt(app)
from ferramentas import routes
