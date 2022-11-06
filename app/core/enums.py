from enum import Enum


class CarTypeEnum(str, Enum):
    """
    Enum for car type
    """
    OFICIAL = "oficial"
    RESIDENT = "residente"
    NO_RESIDENT = "no residente"

    @staticmethod
    def values() -> list:
        return list(map(lambda e: e.value, CarTypeEnum))
