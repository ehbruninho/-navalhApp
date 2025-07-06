from sqlalchemy import Column, Integer, ForeignKey, Boolean, Float, Enum
from app import db
from app.utils.db_helper import commit_instance, get_instance_by, delete_instance_by


class Payment(db.Model):
    __tablename__ = 'payments'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    appointment_id = Column(Integer, ForeignKey('appointments.id'), nullable=False)
    amount = Column(Float, nullable=False)
    status = Column(Boolean, nullable=False, default=False)
    payment_method = Column(Enum("Cartão de Crédito","Pix","Cartão de Débito", "Dinheiro"), nullable=False)

    def __init__(self, appointment_id, amount, payment_method, status):
        self.appointment_id = appointment_id
        self.amount = amount
        self.payment_method = payment_method
        self.status = status

    @classmethod
    def create_payment(cls, appointment_id, amount, payment_method, status):
        payment = cls(appointment_id, amount, payment_method, status)
        commit_instance(payment)
        return payment

    @classmethod
    def get_payment(cls,id_payment):
        return get_instance_by(cls, id_payment=id_payment)

    @classmethod
    def delete_payment(cls, id_payment):
        return delete_instance_by(cls, id_payment)
