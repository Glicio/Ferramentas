from flask import render_template, redirect, url_for, flash, request
from ferramentas import app, db
from flask_login import login_required, login_user, current_user, logout_user
from ferramentas.models import User, Memorando
from ferramentas.forms import RegisterForm, LoginForm, MemorandoIncluirForm, RemoverMemorando
import datetime


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/certidoes")
def certidoes():
    return render_template("certidoes.html")


@app.route("/folha")
def folha():
    return render_template("folha.html")


@app.route("/memorando", methods=("GET","POST"))
@login_required
def memorando():
    form = MemorandoIncluirForm()
    form2 = RegisterForm()
    table = Memorando.query.filter_by(secretaria_criador=current_user.secretaria).order_by(Memorando.data_memorando.desc()).all()
    table2 = Memorando.query.filter_by(secretaria_criador=current_user.secretaria).order_by(Memorando.n_memorando).all()
    if form.validate_on_submit():
        memorando_a_criar = Memorando(n_memo_to_set=[table2,form.data.data], data_memorando=form.data.data,
              credor=form.credor.data, historico=form.historico.data, valor=form.valor.data,
              id_criador=current_user.id, secretaria_criador=current_user.secretaria)
        db.session.add(memorando_a_criar)
        db.session.commit()
        return redirect(url_for('memorando'))
    if form.errors:
        flash(form.errors)
    if form2.is_submitted():
        memo = str(request.form.get("memo")).split("_")
        print(memo[0])
        Memorando.query.filter_by(data_memorando=datetime.datetime.strptime(memo[0], '%Y-%m-%d %H:%M:%S'),n_memorando=memo[1]).delete()
        db.session.commit()
        return redirect(url_for('memorando'))
    return render_template("memorandos.html", form=form, table=table,user=User,form2=form2)


@app.route("/register", methods=('GET', 'POST'))
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        usuario_a_criar = User(username=form.name.data, nivel=form.nivel.data, password=form.password.data,
                               secretaria=form.secretaria.data)
        db.session.add(usuario_a_criar)
        db.session.commit()
        login_user(usuario_a_criar)
        return redirect(url_for('memorando'))
    if form.errors:
        flash(form.errors)
        print(form.errors)
    if current_user.is_authenticated and current_user.nivel == 3:
        return render_template("register.html", form=form)
    else:
        return redirect(url_for('home'))


@app.route('/login', methods=('GET', 'POST'))
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        usuario_a_logar = User.query.filter_by(username=form.name.data).first()
        if usuario_a_logar and usuario_a_logar.check_password_correction(attempted_password=form.password.data):
            login_user(usuario_a_logar)
            return redirect('memorando')
        if form.errors:
            print(form.errors)
    return render_template("login.html", form=form)


@app.route('/logout', methods=('GET', 'POST'))
def logout_page():
    logout_user()
    return redirect(url_for('home'))


@app.route('/test')
def test_page():
    print(current_user.nivel)
    return redirect(url_for('home'))
