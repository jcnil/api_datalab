from decouple import config

from mongoengine import connect


def connect_db() -> None:
    """
    :return: connect mongodb
    """
    return connect(
        host=config("MONGO_URI")
    )
