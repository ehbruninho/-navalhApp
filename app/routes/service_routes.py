from flask import Blueprint, flash, render_template, redirect, url_for

from app.forms.services_forms import *
from app.utils.auth_decorator import login_required, admin_required
from app.controllers.service_controllers import ServiceController

services_bp = Blueprint('services_bp', __name__)

@services_bp.route('/add_services', methods=['GET','POST'])
@admin_required
def add_service():
    form = ServiceForm()
    if form.validate_on_submit():
        service = ServiceController.create_service(name=form.name.data,
                 description=form.description.data)

        if service:
            flash('Serviço registrado com sucesso!', 'success')
            return redirect(url_for('user.dashboard'))
    return render_template('service_templates/register_service.html', form=form)


@services_bp.route('/add_barber_service', methods=['GET','POST'])
@login_required
def add_barber_service():
    form = ServiceBarberForm()
    if form.validate_on_submit():
        user_id = session.get('user_id')

        barber_id,message,category,next_router = ServiceController.get_barber_id(user_id)

        if not barber_id:
            flash(message,category)
            return redirect(url_for('user.dashboard'))

        time_obj = form.duration.data
        total_minutes = time_obj.hour * 60 + time_obj.minute

        service_barber = ServiceController.add_service_barber(barber_id,
                                                              service_id=form.service_id.data,
                                                              price=form.price.data,
                                                              duration=total_minutes,)

        if service_barber:
            flash("Serviço cadastrado com sucesso", "success")
            return redirect(url_for('user.dashboard'))


    return render_template('service_templates/register_barber_service.html', form=form)
