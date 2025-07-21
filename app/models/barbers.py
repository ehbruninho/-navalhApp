from sqlalchemy import Column, Integer, String, ForeignKey
from app.utils.db_helper import *

class Barbers(db.Model):
    __tablename__ = 'barbers'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    id_users = Column(Integer, ForeignKey('users.id'))
    id_local = Column(Integer, ForeignKey('local.id'))
    bio = Column(String(255), nullable=True)
    rating = Column(Integer, nullable=True, default="0")

    user = db.relationship('User', back_populates='barbers')
    local = db.relationship('Local', back_populates='barbers')

    def __init__(self,id_users, id_local, bio):
        self.id_users = id_users
        self.id_local = id_local
        self.bio = bio
        self.rating = "0"

    @classmethod
    def create_barber(cls, id_users, id_local, bio):
        barber = cls(id_users, id_local, bio)
        commit_instance(barber)
        return barber

    @classmethod
    def create_rating(cls, id_barber, rating):
        updates = {
            "rating": rating,
        }
        update = update_instance_by(cls, id_barber, updates)
        return bool(update)

    @classmethod
    def get_all_barbers(cls):
        return get_all_instances(cls)

    @classmethod
    def get_barber(cls, barber_id):
        return get_instance_by(cls,id=barber_id)




