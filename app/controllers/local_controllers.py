from app.models.local import Local
class LocalController:
    @staticmethod
    def register_local(name,address,number_address,district,city_id):
        return Local.create_local(name,address,number_address,district,city_id)

    @staticmethod
    def get_all_local():
        return Local.get_local_test()

    @staticmethod
    def get_local_name(local_name):
        return Local.get_local_name(local_name)

    @staticmethod
    def get_local_barber(local_name):
        return Local.get_barber_local(local_name)