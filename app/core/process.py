from app.core.exceptions import NotFoundException
from app.core.querysets import Queryset
from app.core.constants import (
    OK
)


class CarProcess:
    @staticmethod
    def register(request) -> dict:
        """
        this function register car
        :param request:
        :return: response dictionary
        """
        plate_number = request.get('plate_number')
        car = Queryset.get_car_by_plate_number(
            plate_number=plate_number
        )

        if not car:

            Queryset.create_car(request)

            return {
                "status": OK,
                "message": "Registered",
                "data": request
            }

        return {
            "status": OK,
            "message": "Exist Car",
            "data": car.plate_number
        }

    @staticmethod
    def get_car(
        plate_number
    ) -> dict:
        """
        this function get car exist in database
        :param request: plate_number
        :return: response dictionary
        """
        car = Queryset.get_car_by_plate_number(
            plate_number=plate_number
        )

        if car is not None:
            return {
                "status": OK,
                "message": "Exist Car in Database",
                "data": {
                    "plate_number": car.plate_number,
                    "type_vehicule": car.type_vehicule,
                    "start_date": str(car.start_date),
                    "end_date": str(car.end_date),
                    "minutes": str(car.minutes),
                    "pay": str(car.payment)
                }
            }
        raise NotFoundException

    @staticmethod
    def update_car(
        request
    ) -> dict:
        """
        this function update car in database
        :param request: plate_number
        :return: response dictionary
        """
        Queryset.create_car(request)

        return {
            "status": OK,
            "message": "Car Update",
            "data": request
        }
