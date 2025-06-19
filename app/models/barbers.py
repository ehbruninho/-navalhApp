from sqlalchemy import Column, Integer, String, ForeignKey
from app import db

class Barbers(db.Model):
    __tablename__ = 'barbers'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    id_users = Column(Integer, ForeignKey('users.id'))
    id_local = Column(Integer, ForeignKey('local.id'))
    bio = Column(String(255), nullable=True)
    rating = Column(Integer, nullable=True)

    def __init__(self,id_users, id_local, bio):
        self.id_users = id_users
        self.id_local = id_local
        self.bio = bio

    @classmethod
    def create_barber(cls, id_users, id_local, bio):
        try:
            barber = cls(id_users, id_local, bio)
            db.session.add(barber)
            db.session.commit()
            return barber
        except Exception as e:
            print(f'Erro ao criar barbeiro(a)! Error: {e}')
            db.session.rollback()
        finally:
            db.session.close()

    @classmethod
    def create_rating(cls, id_barber, rating):
        try:
            barber = cls.query.filter_by(id=id_barber).first()
            barber.rating = rating
            db.session.add(barber)
            db.session.commit()
            return barber
        except Exception as e:
            print(f'Erro ao salvar classificação! Error: {e}')
            db.session.rollback()
        finally:
            db.session.close()

    @classmethod
    def get_all_barbers(cls):
        try:
            barbers = cls.query.all()
            return barbers
        except Exception as e:
            print(f'Erro ao listar barbeiros(as)! Error: {e}')
        finally:
            db.session.close()

    @classmethod
    def get_barber(cls, barber_id):
        try:
            barber = cls.query.filter_by(id=barber_id).first()
            return barber
        except Exception as e:
            print(f'Erro ao listar barbeiro(a)! Error: {e}')
        finally:
            db.session.close()




