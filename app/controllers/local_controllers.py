from app.models.local import Local
class LocalController:
    @staticmethod
    def register_local(name,address,number_address,district,city_id):
        return Local.create_local(name,address,number_address,district,city_id)


