from app.models.services import Services
from app.models.barbers import Barbers
from app.models.servicesbarbers import ServiceBarber

class ServiceController:
    @staticmethod
    def create_service(name,description):
        return Services.create_service(name,description)

    @staticmethod
    def edit_service(service_id,name,description):
        return Services.edit_service(service_id,name,description)

    @staticmethod
    def delete_service(service_id):
        return Services.delete_service(service_id)

    @staticmethod
    def get_service_by_barber(barber_name):
        barber = Barbers.get_barber_name(barber_name)
        if barber:
            service = ServiceBarber.get_service_by_barber(barber.id)
            return service
        return False, "Barbeiro sem serviço cadastrado!","warning","user.dashboard"

    @staticmethod
    def get_service_for_barber(barber_id):
        services = ServiceBarber.get_service_by_barber(barber_id)
        if not services:
            return False, "Nenhum serviço cadastrado para esse barber!", "warning", "user.dashboard"

        barber_service = []

        for service in services:
            barber_service.append({
                "nome": service[0],
                "sobrenome": service[1],
                "servico": service[2],
                "preco": service[3],
                "duracao": service[4]
            })
        return barber_service

    @staticmethod
    def get_service_name(name_service):
        service = Services.get_barber_for_service(name_service)
        barbers = []
        if not service:
            return False, "Nenhum barbeiro encontrado para esse serviço!", "warning", "user.dashboard"
        for services in service:
            barbers.append({
                "nome": services[0],
                "sobrenome": services[1],
                "telefone": services[2]
            })

        return barbers

    @staticmethod
    def add_service_barber(barber_id, service_id, price, duration):
        service_barber = ServiceBarber.create_service_barber(barber_id,service_id,price,duration)
        return service_barber

    @staticmethod
    def get_barber_id(user_id):
        service_barber = Barbers.get_barber_id(user_id)
        if not service_barber:
            return False, "Usuário não é barbeiro!","warning","user.dashboard"
        return service_barber,"Usuário encontrado","success","user.dashboard"
