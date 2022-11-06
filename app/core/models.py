from datetime import datetime

from mongoengine.fields import (
    StringField,
    DecimalField,
    DictField,
    DateTimeField,
    ListField,
    IntField
)
from mongoengine import Document

from app.core.enums import CarTypeEnum


class BaseDocument:
    """Document base to inherit all models

    Attributes:
        updated_at (datetime.datetime)
        created_at (datetime.datetime)
        deleted_at (datetime.datetime)
        deleted_by (DictField)
    """
    updated_at = DateTimeField(required=False)
    created_at = DateTimeField(default=lambda: datetime.now().isoformat())
    deleted_at = DateTimeField(required=False)
    deleted_by = DictField(required=False)


class CarModel(BaseDocument, Document):
    meta = {
        "collection": "cars",
        "indexes": ["plate_number"]
    }
    plate_number = StringField()
    type_vehicule = StringField(
        required=True,
        choices=CarTypeEnum.values()
    )
    start_date = DateTimeField()
    minutes = IntField(default=0)
    end_date = DateTimeField(required=False)
    payment = DecimalField(default=0.0)
    historical = ListField(default=[])

    def to_json(self):

        return {
            "plate_number": self.plate_number,
            "type_vehicule": self.type_vehicule,
            "start_date": self.start_date,
            "start_minute": self.start_minute,
            "end_date": self.end_date,
            "payment": self.payment,
            "historical": [i.to_json() for i in self.historical]
        }
