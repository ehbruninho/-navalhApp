from sqlalchemy import Column, ForeignKey, Integer, Enum, Date, Boolean
from app import db
from app.utils.db_helper import commit_instance, get_instance_by, delete_instance_by
from datetime import datetime


class Appointment(db.Model):
    __tablename__ = 'appointments'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    service_id = Column(Integer, ForeignKey('barber_service.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    barber_id = Column(Integer, ForeignKey('barbers.id'), nullable=False)
    date = Column(Date, nullable=False)
    time_slot_id = Column(Integer, ForeignKey('time_slot.id'), nullable=False)
    payment_status = Column(Boolean, nullable=False, default=False)
    status = Column(Enum("Confirmado","Cancelado","Reservado"),nullable=False,default="Reservado")

    def __init__(self,service_id,user_id,barber_id,date,time_slot):
        self.service_id = service_id
        self.user_id = user_id
        self.barber_id = barber_id
        if isinstance(date, str):
            date = datetime.strptime(date, "%Y-%m-%d").date()

        self.date = date
        self.time_slot_id = time_slot
        self.status = "Reservado"

    @classmethod
    def create_appointment(cls, service_id,user_id,barber_id,date,time_slot):
        appointment = cls(service_id,user_id,barber_id,date,time_slot)
        commit_instance(appointment)
        return appointment

    @classmethod
    def get_appointment(cls, appointment_id):
        return get_instance_by(cls,id=appointment_id)

    @classmethod
    def delete_appointment(cls, appointment_id):
        return delete_instance_by(cls, appointment_id)

