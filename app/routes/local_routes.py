from flask import Blueprint, flash, render_template, redirect, url_for, session
from app.forms.local_forms import *
from app.controllers.local_controllers import *
from app.routes.user_routes import user_bp

local_bp = Blueprint('local', __name__)
@local_bp.route('/register_local', methods=['GET','POST'])
def register_locals():
    forms = LocalForm()
    if forms.validate_on_submit():
        local = LocalController.register_local(name=forms.name.data,
        address=forms.address.data,
        number_address=forms.number_address.data,
        district=forms.district.data,
        city_id=forms.city.data)

        if local:
            flash("Local registrado com sucesso!","success")
            return redirect(url_for('user.dashboard'))
    return render_template('register_local.html',form=forms)

