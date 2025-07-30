from sqlalchemy import Column, Integer, String, ForeignKey
from app.models.users import User
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
    services_link = db.relationship('ServiceBarber', back_populates='barber')

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

    @classmethod
    def get_barber_name(cls, barber_name):
        barber = (db.session.query(User)
                   .join(Barbers, Barbers.id_users == User.id)
                   .filter(User.first_name == barber_name).first())
        return barber if barber else False


    @classmethod
    def get_barber_id(cls, user_id):
        barber = get_instance_by(cls,id_users=user_id)
        return barber.id if barber else False

