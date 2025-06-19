from sqlalchemy import Column, Integer, String, ForeignKey
from app import db

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
        try:
            local = Local(name=name, address=address,number_address=number_address, district=district, id_region=id_region)
            db.session.add(local)
            db.session.commit()
            return local
        except Exception as e:
            print(f'Erro ao salvar local! Error: {e}')
            db.session.rollback()
        finally:
            db.session.close()

    @classmethod
    def delete_local(cls,id_local):
        try:
            local = db.session.query(cls).filter_by(id=id_local).first()
            db.session.delete(local)
            db.session.commit()
        except Exception as e:
            print(f'Erro ao deletar local! Error: {e}')
            db.session.rollback()
        finally:
            db.session.close()

    @classmethod
    def update_local(cls,id_local, address, number_address, district, id_region):
        try:
            local = db.session.query(cls).filter_by(id=id_local).first()
            local.name = address
            local.number_address = number_address
            local.district = district
            local.id_region = id_region
            db.session.commit()
        except Exception as e:
            print(f'Erro ao atualizar local! Error: {e}')
            db.session.rollback()
        finally:
            db.session.close()

    @classmethod
    def get_all_local(cls):
        try:
            local = db.session.query(cls).all()
            return local
        except Exception as e:
            print(f'Erro ao listar local! Error: {e}')
        finally:
            db.session.close()


