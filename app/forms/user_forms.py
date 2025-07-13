from flask_wtf import FlaskForm
from wtforms import PasswordField, EmailField, SubmitField, StringField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from app.models.users import User
from wtforms.fields import FileField
from flask import session

class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Entrar')

class RegistrationForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Senha', validators=[DataRequired()])
    password2 = PasswordField('Confirme sua senha', validators=[DataRequired(), EqualTo('password',message='As senhas devem ser iguais')])
    submit = SubmitField('Cadastrar')

    def validate_email(self,field):
        if User.check_exist_email(field.data):
            raise ValidationError('Email já cadastrado')

class PerfilForms(FlaskForm):
    first_name = StringField('Nome', validators=[DataRequired()])
    last_name = StringField('Sobrenome', validators=[DataRequired()])
    doc_number = StringField('CPF', validators=[DataRequired()])
    mobile_number = StringField('Telefone', validators=[DataRequired()])
    foto = FileField('Foto', validators=[DataRequired()])
    submit = SubmitField('Cadastrar')

    def validate_doc_number(self,field):
        if User.get_doc_register(field.data):
            raise ValidationError('CPF já registrado!')

class VerifyToken(FlaskForm):
    token = StringField('Token', validators=[DataRequired()])
    submit = SubmitField('Verificar')

class UserPerfil(FlaskForm):
    first_name = StringField('Nome', render_kw={"readonly": True})
    last_name = StringField('Sobrenome', render_kw={"readonly": True})
    doc_number = StringField('CPF', render_kw={"readonly": True})
    mobile_number = StringField('Telefone', render_kw={"readonly": True})
    email = EmailField('Email', render_kw={"readonly": True})
    cat_user = StringField('Tipo de usuário:', render_kw={"readonly": True})

class UpdatePassword(FlaskForm):
    old_password = PasswordField('Senha Anterior', validators=[DataRequired()])
    new_password = PasswordField('Nova Senha', validators=[DataRequired()])
    confirm_password = PasswordField('Nova Senha', validators=[DataRequired(), EqualTo('new_password',message='As senhas devem ser iguais')])
    submit = SubmitField('Salvar')

    def validate_old_password(self,field):
        user_id = session.get('user_id')
        if not User.check_password(user_id,field.data):
            raise ValidationError('Senha incorreta!')

