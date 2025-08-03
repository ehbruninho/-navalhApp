from flask import Blueprint, flash, render_template, redirect, url_for
from app.controllers.barber_controllers import BarberController

from app.utils.auth_decorator import login_required

barber_bp = Blueprint('barber', __name__)

@barber_bp.route('/barber/<int:barber_id>')
@login_required
def view_barber_detail(barber_id):
    details = BarberController.get_barber_detail(barber_id)
    if not details:
        flash("Nenhum serviço cadastrado!","warning")
        return redirect(url_for('local.view_local'))

    return render_template("barbers_template/view_barber_details.html", details=details)