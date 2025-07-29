from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField, DecimalField, TimeField
from wtforms.validators import DataRequired
from app.models.services import Services
from flask import session
from app.models.barbers import Barbers

from app.models.servicesbarbers import ServiceBarber


class ServiceForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    submit = SubmitField('Salvar')

class ServiceBarberForm(FlaskForm):
    service_id = SelectField('Service', validators=[DataRequired()])
    price = DecimalField('Price', validators=[DataRequired()])
    duration = TimeField("Duração", format='%H:%M', validators=[DataRequired()])
    submit = SubmitField('Salvar')

    def __init__(self,*args,**kwargs):
        super(ServiceBarberForm,self).__init__(*args,**kwargs)
        self.service_id.choices = [(service.id, service.name) for service in Services.get_all_services()]


