from sqlalchemy import Column, String, Integer
from app.utils.db_helper import *

class Services(db.Model):
    __tablename__ = 'services'
    id = Column(Integer, primary_key=True, autoincrement=True,nullable=False)
    name = Column(String(100), nullable=False)
    description = Column(String(200), nullable=False)

    services_link = db.relationship('ServiceBarber', back_populates='service')

    def __init__(self, name, description):
        self.name = name
        self.description = description


    @classmethod
    def create_service(cls, name, description):
        service = cls(name, description)
        commit_instance(service)
        return service


    @classmethod
    def delete_service(cls,id_service):
        return delete_instance_by(cls, id_service)

    @classmethod
    def get_all_services(cls):
       return get_all_instances(cls)

    @classmethod
    def get_barber_for_service(cls,name_service):
        from app.models.servicesbarbers import ServiceBarber
        from app.models.barbers import Barbers
        from app.models.users import User

        barber = (db.session.query(User.first_name, User.last_name, User.mobile_number)
                      .join(Barbers, User.id == Barbers.id)
                      .join(ServiceBarber, Barbers.id == ServiceBarber.barber_id)
                      .join(cls,cls.id == ServiceBarber.service_id)
                      .filter(cls.name == name_service)
                      .all())
        return barber

    @classmethod
    def update_service(cls,id_service,name_service,description):
        updates = {
            'name': name_service,
            'description': description
        }
        service = update_instance_by(cls,id_service,updates)
        return bool(service)
