from sqlalchemy import Column, Integer, String
from app import db

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
        try:
            region = cls(city, postal_code, uf)
            db.session.add(region)
            db.session.commit()
        except Exception as e:
            print(f"Erro ao salvar região! Error: {e}")
            db.session.rollback()
        finally:
            db.session.close()

    @classmethod
    def get_region(cls, id_region):
        try:
            region = db.session.query(cls).filter_by(id=id_region).first()
            return region
        except Exception as e:
            print(f'Erro ao buscar região! Error: {e}')
        finally:
            db.session.close()

    @classmethod
    def delete_region(cls, id_region):
        try:
            region = cls.get_region(id_region)
            db.session.delete(region)
            db.session.commit()
        except Exception as e:
            print(f'Erro ao deletar região! Error: {e}')
        finally:
            db.session.close()
    @classmethod
    def get_all_regions(cls):
        try:
            regions = db.session.query(cls).all()
            return regions
        except Exception as e:
            print(f' Erro ao listar regiões! Error: {e}')
        finally:
            db.session.close()