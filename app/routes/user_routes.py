from flask import Blueprint, flash, render_template, redirect, url_for
from app.forms.login_form import LoginForm, RegistrationForm
from app.controllers import user_controllers
from app.utils.notifications.send_email import send_token

# Cria o blueprint
user_bp = Blueprint('user', __name__)

# Define rotas usando ele
@user_bp.route('/register_user', methods=['GET','POST'])
def register_users():
    form = RegistrationForm()
    if form.validate_on_submit():
        user,token = user_controllers.create_user(form.email.data, form.password.data)
        if user:
            flash('Usuario registrado com sucesso!','success')
            send_token(user.email, token)
            return redirect(url_for('user.login_user'))
        else:
            flash('Falha ao registrar Usuario','danger')
    return render_template('register.html', form=form)

@user_bp.route('/login', methods=['GET', 'POST'])
def login_user():
    form = LoginForm()
    if form.validate_on_submit():
        user = user_controllers.authenticate_user(form.email.data, form.password.data)
        if user:
            return redirect(url_for('user.dashboard', user_id=user.id))
        else:
            flash('Falha ao logar Usuario','danger')
    return render_template('login.html', form=form)

@user_bp.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    redirect(url_for('user.dashboard'))

