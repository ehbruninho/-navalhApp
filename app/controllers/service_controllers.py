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
    def get_service_name(name_service):
        service = Services.get_barber_for_service(name_service)
        if service:
            return service
        return False , "Nenhum barbeiro encontrado para esse serviço!","warning","user.dashboard"

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
