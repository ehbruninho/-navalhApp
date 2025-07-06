from app import db

def commit_instance(instance):
    try:
        db.session.add(instance)
        db.session.commit()
        return instance
    except Exception as e:
        print(f'Erro ao salvar (instance.__class__.__name__): {e}')
        db.session.rollback()
        return None

#Nessa função executa busca com o filtro pre definido.
def get_instance_by(cls, **filters):
    try:
        instance = cls.query.filter_by(**filters).first()
        return instance
    except Exception as e:
        print(f'Erro ao salvar (cls.__name__): {e}')
    finally:
        db.session.close()

def update_instance_by(cls, id_value, updates: dict, field="id"):
    try:
        instance = cls.query.filter_by(**{field: id_value}).first()
        for key, value in updates.items():
            setattr(instance, key, value)
        db.session.commit()
        return instance
    except Exception as e:
        print(f'Erro ao atualizar (cls.__name__): {e}')
    finally:
        db.session.close()

def delete_instance_by(cls, id_value,field="id"):
    try:
        instance = cls.query.filter_by(**{field: id_value}).first()
        if instance:
            db.session.delete(instance)
            db.session.commit()
            return instance
        else:
            return False
    except Exception as e:
        print(f'Erro ao deletar (cls.__name__): {e}')
        db.session.rollback()
    finally:
        db.session.close()

def get_all_instances(cls):
    try:
        return db.session.query(cls).all()
    except Exception as e:
        print(f'Erro ao listar (cls.__name__): {e}')
    finally:
        db.session.close()



