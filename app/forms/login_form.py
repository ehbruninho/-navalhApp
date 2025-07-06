from flask_wtf import FlaskForm
from wtforms import PasswordField, EmailField, SubmitField, StringField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from app.models.users import User
from wtforms.fields import FileField

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
    cpf = StringField('CPF', validators=[DataRequired()])
    mobile_number = StringField('Telefone', validators=[DataRequired()])
    foto = FileField('Foto', validators=[DataRequired()])
    submit = SubmitField('Cadastrar')

