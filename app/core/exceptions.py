from http import HTTPStatus


class ExistException(Exception):
    status = HTTPStatus.CONFLICT

    def message(self, obj):
        return f"{obj} already exists"


class NotFoundException(Exception):
    status = HTTPStatus.NOT_FOUND

    def message(self, obj):
        return f"{obj} doesn't found"
