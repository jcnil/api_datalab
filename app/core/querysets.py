from datetime import datetime

from .models import (
    CarModel
)


class Queryset:

    @staticmethod
    def get_car_by_plate_number(
        plate_number
    ) -> CarModel:
        """
        Return a car based in plate_number.
        :param plate_number: str
        :return: CarModel
        """
        return CarModel.objects(
            plate_number=plate_number
        ).first()

    @staticmethod
    def create_car(request) -> CarModel:
        """
        Create an car
        :param request
        :return: CarModel
        """
        plate_number = request.get('plate_number')
        doc = CarModel.objects(
                plate_number=plate_number
        ).first()

        if doc:
            doc.updated_at = datetime.now()
            doc.historical.append(request)
            doc.plate_number = request.get('plate_number')
            doc.type_vehicule = request.get('type_vehicule')
            doc.start_date = request.get('start_date')
            doc.end_date = request.get('end_date')

            minutes = datetime.fromisoformat(
                request.get('end_date')
            ) - datetime.fromisoformat(
                    request.get('start_date')
            )
            micro = minutes.microseconds / 60000000
            total = (minutes.days * 1440) + (minutes.seconds / 60) + micro

            doc.minutes = total

            if request.get('type_vehicule') == 'residente':
                doc.payment = total * 0.05
            elif request.get('type_vehicule') == 'no residente':
                doc.payment = total * 0.5
            else:
                doc.payment = 0.0

        if not doc:
            request['minutes'] = datetime.fromisoformat(
                request.get('start_date')
            ).minute

            doc = CarModel(**request)
            doc.historical.append(request)

        return doc.save()
