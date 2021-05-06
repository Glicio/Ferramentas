from ferramentas import db
from flask_login import UserMixin
from ferramentas import bcrypt
import re

class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    nivel = db.Column(db.Integer(), nullable=False)
    username = db.Column(db.String(), unique=True, nullable=False)
    password_hash = db.Column(db.String(), nullable=False)
    secretaria = db.Column(db.String(), nullable=False)
    processos = db.relationship('Memorando', backref="criador",lazy=True)

    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')

    def check_password_correction(self, attempted_password):
        return bcrypt.check_password_hash(self.password_hash, attempted_password)

class Memorando(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    n_memorando = db.Column(db.String(), nullable=False)
    data_memorando = db.Column(db.DateTime(), nullable=False)
    credor = db.Column(db.String(), nullable=False)
    historico = db.Column(db.String())
    valor = db.Column(db.String())
    id_criador = db.Column(db.Integer(), db.ForeignKey('user.id'))
    secretaria_criador = db.Column(db.String())

    @property
    def n_memo_to_set(self):
        return self.n_memo_to_set
    @n_memo_to_set.setter
    def n_memo_to_set(self, info=None):
        if info is None:
            table = ["Data", "Tabela"]
        data = str(info[1]).split("-")
        table = info[0]
        print("Tamanho: "+str(len(table)))
        print(data)
        if len(table) > 0:
            ultimo = 0
            for i in table:
                if str(i.data_memorando).split()[0] == str(info[1]):
                    #valor = re.split("\.|/",i.n_memorando)[2]
                    valor = i.n_memorando
                    if int(valor) > ultimo and int(valor) == ultimo+1:
                        ultimo = int(valor)
            print(ultimo)

            self.n_memorando = ultimo+1
        else:
            self.n_memorando = 1
