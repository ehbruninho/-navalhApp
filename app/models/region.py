from sqlalchemy import Column, Integer, String
from app.utils.db_helper import *

class Region(db.Model):
    __tablename__ = 'region'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    city = Column(String(50), nullable=False)
    postal_code = Column(String(10), nullable=False)
    uf = Column(String(2), nullable=False)

    def __init__(self, city, postal_code, uf):
        self.city = city
        self.postal_code = postal_code
        self.uf = uf

    @classmethod
    def create_region(cls, city, postal_code, uf):
        region = cls(city, postal_code, uf)
        commit_instance(region)
        return region

    @classmethod
    def get_region(cls, id_region):
        return get_instance_by(cls,id=id_region)

    @classmethod
    def delete_region(cls, id_region):
        return delete_instance_by(cls,id_region)
    @classmethod
    def get_all_regions(cls):
        return get_all_instances(cls)