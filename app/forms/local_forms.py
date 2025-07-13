from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField, SelectField
from wtforms.validators import DataRequired, ValidationError
from app.models.local import Local
from app.models.region import Region

class LocalForm(FlaskForm):
    name = StringField('Estabelecimento',validators=[DataRequired()])
    address = StringField('Endereço',validators=[DataRequired()])
    number_address = StringField('Numero',validators=[DataRequired()])
    district = StringField('Bairro',validators=[DataRequired()])
    city = SelectField('Cidade:',validators=[DataRequired()])
    submit = SubmitField('Salvar')

    def __init__(self, *args, **kwargs):
        super(LocalForm, self).__init__(*args, **kwargs)
        self.city.choices = [(region.id, region.city) for region in Region.get_all_regions()]


