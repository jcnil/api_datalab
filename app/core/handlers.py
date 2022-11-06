from app.core.process import (
    CarProcess
)


class CarHandler:
    @staticmethod
    def register(request):
        obj = CarProcess()
        return obj.register(request)

    @staticmethod
    def get_car(plate_number: str):
        obj = CarProcess()
        return obj.get_car(plate_number)

    @staticmethod
    def update(plate_number: str):
        return CarProcess().update_car(plate_number)
