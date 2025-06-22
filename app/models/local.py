from sqlalchemy import Column, Integer, String, ForeignKey
from app.utils.db_helper import *

class Local(db.Model):
    __tablename__ = 'local'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(255), nullable=False)
    address = Column(String(255), nullable=False)
    number_address = Column(Integer, nullable=True)
    district = Column(String(255), nullable=True)
    id_region = Column(Integer, ForeignKey('region.id'))

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


