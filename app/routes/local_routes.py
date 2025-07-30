from flask import Blueprint, flash, render_template, redirect, url_for
from app.forms.local_forms import LocalForm, RegionForm, CityFilterForm
from app.controllers.local_controllers import *
from app.utils.auth_decorator import admin_required, login_required


local_bp = Blueprint('local', __name__)

@local_bp.route('/register_local', methods=['GET','POST'])
@admin_required
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
    return render_template('local_templates/register_local.html', form=forms)

@local_bp.route('/register_region', methods=['GET','POST'])
@admin_required
def register_region():
    forms = RegionForm()
    if forms.validate_on_submit():
            return redirect(url_for('user.dashboard'))
    return render_template('local_templates/register_region.html', form=forms)

@local_bp.route('/view_local', methods=['GET'])
@login_required
def view_local():
    locais = LocalController.get_all_local()
    if not locais:
        flash("Nenhuma barbearia registrada!","warning")
        return redirect(url_for('user.dashboard'))

    return render_template('local_templates/view_local.html', locais=locais)


@local_bp.route('/view_local/<local_name>')
@login_required
def view_local_detail(local_name):
    """endpoint = barbers?barbershop=id"""
    name = local_name.replace('-',' ').title()
    print(name)
    local = LocalController.get_local_name(name)
    if not local:
        flash("Nenhuma barbearia registrada!","warning")
        return redirect(url_for('user.dashboard'))

    barbers = LocalController.get_local_barber(name)

    return render_template('local_templates/view_local_detail.html', local=local, barbers=barbers)

@local_bp.route('/local_from_city', methods=['GET','POST'])
def view_local_from_city():
    form = CityFilterForm()
    locals = []

    if form.validate_on_submit():
        city_id = form.city.data
        locals = LocalController.get_local_from_city_name(city_id)
        if not locals:
            flash("Nenhuma barbearia registrada!","warning")
            print("Nenhuma barbearia registrada!")
            return redirect(url_for('user.dashboard'))
    return render_template('local_templates/filter.html', form=form, locals=locals)
