from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateField, TextAreaField
from wtforms.validators import DataRequired, Length, ValidationError
from ferramentas import login_manager
from ferramentas.models import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class RegisterForm(FlaskForm):

    def validate_name(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('Nome de Usuário Já registrado!')
    name = StringField('Nome', validators=[DataRequired(message="Campo Obrigatório"), Length(min=3, max=12,message="Máximo de 12 caráteres, mínimo  de 3")])
    password = PasswordField('Senha', validators=[DataRequired(message="Campo Obrigatório"), Length(min=8, max=32,message="Máximo de 32 caráteres, mínimo  de 8")])
    secretaria = StringField('Secretaria', validators=[DataRequired(message="Campo Obrigatório")])
    nivel = StringField('Nivel de Usuário', validators=[DataRequired()])
    submit = SubmitField(label='Enviar')

class LoginForm(FlaskForm):
    name = StringField('Nome', validators=[DataRequired(message="Campo Obrigatório"), Length(min=3, max=12,message="Máximo de 12 caráteres, mínimo  de 3")])
    password = PasswordField('Senha', validators=[DataRequired(message="Campo Obrigatório"), Length(min=8, max=32,message="Máximo de 32 caráteres, mínimo  de 8")])
    submit = SubmitField(label='Enviar')

class MemorandoIncluirForm(FlaskForm):
    data = DateField('Data(*)',validators=[DataRequired()],format="%Y-%m-%d")
    credor = StringField('Credor(*)',validators=[DataRequired()])
    historico = TextAreaField('Historico')
    valor = StringField('Valor')
    submit = SubmitField(label='Enviar')
class RemoverMemorando(FlaskForm):
    submit = SubmitField(label='Remover')