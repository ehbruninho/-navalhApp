from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import joinedload, aliased
from app.models.users import User
from app.models.barbers import Barbers
from app.utils.db_helper import *
from app.models.region import Region
from app.models.services import Services
from app.models.servicesbarbers import ServiceBarber

class Local(db.Model):
    __tablename__ = 'local'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(255), nullable=False)
    address = Column(String(255), nullable=False)
    number_address = Column(Integer, nullable=True)
    district = Column(String(255), nullable=True)
    id_region = Column(Integer, ForeignKey('region.id'))

    #relações entre tabelas
    region = db.relationship('Region', backref='region')
    barbers = db.relationship('Barbers', back_populates='local')

    def __init__(self, name, address, number_address, district, id_region):
        self.name = name
        self.address = address
        self.number_address = number_address
        self.district = district
        self.id_region = id_region

    @classmethod
    def create_local(cls, name, address, number_address, district, id_region):
        local = cls(name, address, number_address, district, id_region)
        commit_instance(local)
        return local

    @classmethod
    def delete_local(cls,id_local):
       return delete_instance_by(cls,id_local)

    @classmethod
    def update_local(cls,id_local, address, number_address, district, id_region):
        updates = {
            "address": address,
            "number_address": number_address,
            "district": district,
            "id_region" : id_region
        }
        local = update_instance_by(cls,id_local,updates)
        return bool(local)

    @classmethod
    def get_all_local(cls):
        return get_all_instances(cls)


    @classmethod
    def get_local_name(cls, local_name):
        return get_instance_by(cls,name=local_name)

    @classmethod
    def get_local_test(cls):
        locais = Local.query.options(joinedload(Local.region)).all()
        if locais:
            return locais
        return False

    @classmethod
    def get_barber_local(cls,local_name):
        barber_alias = aliased(Barbers)
        service_barber_alias = aliased(ServiceBarber)

        barbers = (
            db.session.query(
                User.first_name,
                User.last_name,
                Services.name,
                service_barber_alias.price,
                service_barber_alias.duration
            )
            .select_from(service_barber_alias)
            .join(barber_alias, service_barber_alias.barber_id == barber_alias.id)
            .join(Services, Services.id == service_barber_alias.service_id)
            .join(User, User.id == barber_alias.id_users)
            .join(Local, barber_alias.id_local == Local.id)
            .filter(Local.name == local_name)
            .all()
        )

        return barbers if barbers else False


    @classmethod
    def get_local_from_city(cls, region_id):
        locals = (db.session.query(cls.name,cls.address,cls.number_address,cls.district)
                  .join(Region, Region.id == cls.id_region).filter(Region.id == region_id).all()
                  )
        return locals if locals else False