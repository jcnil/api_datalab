from fastapi import APIRouter
from fastapi.responses import JSONResponse

from app.core.constants import SERVER_ERROR
from app.core.exceptions import (
    NotFoundException,
    ExistException
)
from app.core.handlers import (
    CarHandler,
)
from app.api.v1.serializers import (
    CarInSerializer,
    ResponseSerializer
)

router = APIRouter()


@router.post(
    "/cars/",
    tags=["Cars"],
    response_model=ResponseSerializer
)
async def post_car(car: CarInSerializer) -> dict:
    """Post new car"""
    try:
        request = car.dict()
        result = CarHandler.register(request)
        return JSONResponse(
            content={
                "status": result["status"],
                "data": result["data"],
                "message": str(result["message"])
            }
        )
    except ExistException as e:
        return JSONResponse(
            content={
                "status": e.status,
                "data": request,
                "message": str(e.message("Car")),
                "errors": SERVER_ERROR
            },
            status_code=e.status
        )


@router.get(
    "/cars/{plate_number}",
    tags=["Cars"],
    response_model=ResponseSerializer
)
async def get_car(
    plate_number: str
):
    """Get Car by specific plate number"""
    try:
        result = CarHandler.get_car(
            plate_number=plate_number
        )
        return JSONResponse(
            content={
                "status": result["status"],
                "data": result["data"],
                "message": str(result["message"])
            }
        )
    except NotFoundException as e:
        return JSONResponse(
            content={
                "status": e.status,
                "data": plate_number,
                "message": str(e.message("Car")),
                "errors": SERVER_ERROR
            },
            status_code=e.status
        )


@router.put(
    "/cars/",
    tags=["Cars"],
    response_model=ResponseSerializer
)
async def update(
    car: CarInSerializer
):
    """Get Car by specific plate number"""
    try:
        request = car.dict()
        result = CarHandler.update(request)
        return JSONResponse(
            content={
                "status": result["status"],
                "data": result["data"],
                "message": str(result["message"])
            }
        )
    except NotFoundException as e:
        return JSONResponse(
            content={
                "status": e.status,
                "data": car.plate_number,
                "message": str(e.message("Car")),
                "errors": SERVER_ERROR
            },
            status_code=e.status
        )
