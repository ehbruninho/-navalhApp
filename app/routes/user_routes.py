from flask import Blueprint, flash, render_template, redirect, url_for, session
from app.forms.user_forms import *
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
    return render_template('user_templates/register.html', form=form)

@user_bp.route('/login', methods=['GET', 'POST'])
def login_user():
    form = LoginForm()
    if form.validate_on_submit():
        user,message,category,next_route = UserController.login_user_and_redirect(form.email.data, form.password.data)
        if not user:
            flash(message,category)
            return render_template('user_templates/login.html', form=form)

        session['user_id'] = user.id  # <--- faltando isso?
        session.permanent = True
        flash(message,category)
        return redirect(url_for(f"{next_route}"))

    return render_template('user_templates/login.html', form=form)

@user_bp.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():

    return render_template('user_templates/dashboard.html')

@user_bp.route('/complete_register', methods=['GET', 'POST'])
@login_required
def complete_register():
    form = PerfilForms()
    if form.validate_on_submit():
        user_id = session.get('user_id')
        if not user_id:
            flash('Sessão expirada.', 'danger')
            return redirect(url_for('user.login_user'))

        perfil, message,category,routes = UserController.complete_user_profile(
            user_id = session.get('user_id'),
            first_name = form.first_name.data,
            last_name = form.last_name.data,
            doc_number=form.doc_number.data,
            foto = form.foto.data,
            mobile_number=form.mobile_number.data,
        )
        if perfil:
            flash(message,category)
            return redirect(url_for(routes))
        else:
            flash(message,category)
    return render_template('user_templates/complete_profile.html', form=form)

@user_bp.route('/verify_token', methods=['GET','POST'])
@login_required
def verify_token():
    form = VerifyToken()
    if form.validate_on_submit():
        user_id = session.get('user_id')
        if not user_id:
            flash('Sessão expirada.', 'danger')
            return redirect(url_for('user.login_user'))

        token_ok = UserController.verify_token(user_id, form.token.data)
        if token_ok:
            flash('Verificado com sucesso', 'success')
            return redirect(url_for('user.dashboard'))
        else:
            flash('Token inválido', 'danger')
    return render_template('user_templates/verify_token.html', form=form)

@user_bp.route('/logout')
@login_required
def logout_user():
    session.clear()
    return redirect(url_for('user.login_user'))

@user_bp.route('/profile', methods=['GET'])
@login_required
def view_profile():
    user,message,category,routes = UserController.view_profile(user_id = session.get('user_id'))
    if not user:
        return redirect(url_for(routes))

    form = UserPerfil(first_name=user.first_name,
                       last_name=user.last_name,
                       doc_number=user.doc_register,
                       mobile_number=user.mobile_number,
                       email=user.email,
                       cat_user= user.type_user)

    return render_template('user_templates/view_profile.html', form=form, user=user)

@user_bp.route('/update_password', methods=['GET', 'POST'])
@login_required
def update_password():
    user_id = session.get('user_id')
    form = UpdatePassword()
    if form.validate_on_submit():
        if not user_id:
            flash("Sessão expirada.", "danger")
            return redirect(url_for('user.login_user'))

        user, message, category, routes = UserController.update_password(user_id = session.get('user_id'),
                old_password = form.old_password.data,
                new_password = form.new_password.data)
        if user:
            flash(message,category)
            return redirect(url_for(routes))
    return render_template('user_templates/update_password.html', form=form)
