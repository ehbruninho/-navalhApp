from app.models.barbers import Barbers

class BarberController:

    @staticmethod
    def get_barber_detail(barber_id):


        details = Barbers.fetch_barber_detail(barber_id)
        if not details:
            return None

        grouped = {}

        for detail in details:
            nome = f"{detail[0]} {detail[1]}"
            if nome not in grouped:
                grouped[nome] = {
                    "ratting": detail[6],
                    "local": detail[2],
                    "servicos": []
                }
            grouped[nome]["servicos"].append({
                "servico": detail[3],
                "valor": detail[4],
                "duracao": detail[5]
            })

        return grouped


