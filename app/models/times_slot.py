from datetime import datetime, timedelta
from sqlalchemy import Column, Integer, Date, Boolean, ForeignKey, Time
from app.utils.db_helper import *

class TimeSlot(db.Model):
    __tablename__ = 'time_slot'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    barber_id = Column(Integer, ForeignKey('barbers.id'), nullable=False)
    date = Column(Date, nullable=False)
    start_time = Column(Time, nullable=False)
    end_time = Column(Time, nullable=False)
    is_available = Column(Boolean, nullable=False, default=True)

    def __init__(self, barber_id, date, start_time, time_default=30,is_available=True):
        self.barber_id = barber_id

        if isinstance(date, str):
            date = datetime.strptime(date, "%Y-%m-%d").date()

        if isinstance(start_time, str):
            start_time = datetime.strptime(start_time, "%H:%M").time()

        self.date = date
        self.start_time = start_time

        dt_start = datetime.combine(date,start_time)
        dt_end = dt_start + timedelta(minutes=time_default)

        self.end_time = dt_end.time()
        self.is_available = is_available

    @classmethod
    def create_slot(cls, barber_id, date, start_time,is_available=True):
        slot = cls(barber_id, date, start_time, is_available=is_available)
        commit_instance(slot)
        return slot

    @classmethod
    def get_all_slots(cls):
        return get_all_instances(cls)

    @classmethod
    def get_slot(cls, id_slot):
        return get_instance_by(cls,id=id_slot)

    @classmethod
    def delete_slot(cls, id_barber):
        return delete_instance_by(cls,id_barber)

    @classmethod
    def get_slot_of_barber(cls, id_barber):
        from app.models.users import User
        from app.models.barbers import Barbers
        try:
            user = db.session.query(User).join(Barbers, User.id == Barbers.id_users).filter(Barbers.id==id_barber).one()
            return user
        except Exception as e:
            print(f'Erro ao listar barbeiros pelo slot disponivel! Error: {e}')
            return None
        finally:
            db.session.close()
