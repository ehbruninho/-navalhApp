from sqlalchemy import Column, ForeignKey, Integer, Float
from app.utils.db_helper import  *
from app.models.barbers import Barbers
from app.models.services import Services
from app.models.users import User

class ServiceBarber(db.Model):
    __tablename__ = 'barber_service'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    barber_id = Column(Integer, ForeignKey('barbers.id'), nullable=False)
    service_id = Column(Integer, ForeignKey('services.id'), nullable=False)
    price = Column(Float, nullable=False)
    duration = Column(Integer, nullable=False)

    service = db.relationship('Services', back_populates='services_link')
    barber = db.relationship('Barbers', back_populates='services_link')

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
    def delete_service_barber(cls, id_service_barber):
        return delete_instance_by(cls,id_service_barber)

    @classmethod
    def get_service_by_barber(cls, id_barber):
        services = (db.session.query(User.first_name,User.last_name,Services.name,cls.price,cls.duration)
                    .select_from(cls)
                    .join(User, User.id == Barbers.id_users)
                    .join(Services,Services.id == cls.service_id)
                    .join(Barbers, Barbers.id == cls.barber_id)
                    .filter(cls.barber_id == id_barber)
                    .all())
        return services if services else None




