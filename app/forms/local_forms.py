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


class RegionForm(FlaskForm):
    city = StringField('Nome',validators=[DataRequired()])
    postal_code = StringField('Postal',validators=[DataRequired()])
    state = SelectField('UF',validators=[DataRequired()],choices=[('RS','RS'),('SC','SC')])
    submit = SubmitField('Salvar')

class ViewRegionForm(FlaskForm):
    name = StringField('Estabelecimento',render_kw={"readonly":True})
    address = StringField('Endereço', render_kw={"readonly":True})
    number_address = StringField('Numero', render_kw={"readonly":True})
    district = StringField('Bairro', render_kw={"readonly":True})
    city = SelectField('Cidade', render_kw={"readonly":True})
    submit = SubmitField('Voltar')