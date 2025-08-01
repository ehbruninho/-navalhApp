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
        barbers_local = []
        barbers = Local.get_barber_local(local_name)
        if not barbers:
            return None

        for barber in barbers:
            barbers_local.append(
                {
                    "nome": barber[0],
                    "sobrenome": barber[1],
                    "servico": barber[2],
                    "valor": barber[3],
                    "duracao": barber[4]
                }
            )
        return barbers_local

    @staticmethod
    def get_local_from_city_name(id_region):
        return Local.get_local_from_city(id_region)