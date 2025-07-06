from flask import Blueprint, flash, render_template, redirect, url_for, session
from app.forms.login_form import LoginForm, RegistrationForm, PerfilForms
from app.controllers.user_controllers import UserController
from app.utils.auth_decorator import login_required
from app.utils.notifications.send_email import send_token

# Cria o blueprint
user_bp = Blueprint('user', __name__)

# Define rotas usando ele
@user_bp.route('/register_user', methods=['GET','POST'])
def register_users():
    form = RegistrationForm()
    if form.validate_on_submit():
        user,token = UserController.create_user(form.email.data, form.password.data)
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
        user = UserController.authenticate_user(form.email.data, form.password.data)
        if user:
            session['user_id'] = user.id
            session.permanent = True
            return redirect(url_for('user.dashboard'))
        else:
            flash('Falha ao logar Usuario','danger')
    return render_template('login.html', form=form)

@user_bp.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    print(f"ID da sessão atual: {session.get('user_id')}")
    form = PerfilForms()
    if form.validate_on_submit():
        perfil = UserController.complete_user_profile(
            user_id = session.get('user_id'),
            first_name = form.first_name.data,
            last_name = form.last_name.data,
            doc_number=form.doc_number.data,
            foto = form.foto.data,
            mobile_number=form.mobile_number.data,
        )
        if perfil['status'] == 'sucesso':
            flash(perfil['mensagem'], 'success')
        else:
            flash(perfil['mensagem'], 'danger')
    return render_template('complete_profile.html', form=form)

def logout_user():
    session.clear()
    return redirect(url_for('user.login_user'))