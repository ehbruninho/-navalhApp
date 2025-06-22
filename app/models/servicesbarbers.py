from sqlalchemy import Column, ForeignKey, Integer, Float
from app.utils.db_helper import  *

class ServiceBarber(db.Model):
    __tablename__ = 'barber_service'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    barber_id = Column(Integer, ForeignKey('barbers.id'), nullable=False)
    service_id = Column(Integer, ForeignKey('services.id'), nullable=False)
    price = Column(Float, nullable=False)
    duration = Column(Integer, nullable=False)

    def __init__(self, barber_id, service_id, price, duration):
        self.barber_id = barber_id
        self.service_id = service_id
        self.price = price
        self.duration = duration

    @classmethod
    def create_service_barber(cls, id_barber, id_service, price, duration):
        service_barber = cls(id_barber, id_service, price, duration)
        commit_instance(service_barber)
        return service_barber

    @classmethod
    def get_service_barber(cls, id_barber):
        return get_instance_by(cls,barber_id=id_barber)

    @classmethod
    def delete_service_barber(cls, id_service_barber):
        return delete_instance_by(cls,id_service_barber)

