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
        barbers = Local.get_barber_local(local_name)
        if not barbers:
            return None

        grouped = {}

        for barber in barbers:
            nome = f"{barber[1]} {barber[2]}"

            if nome not in grouped:
                grouped[nome] = {
                    "id": barber[0],
                    "servicos": []
                }
            grouped[nome]["servicos"].append({
                "servico": barber[3]
            })

        return grouped

    @staticmethod
    def get_local_from_city_name(id_region):
        return Local.get_local_from_city(id_region)