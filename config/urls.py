from fastapi import APIRouter
from app.meta import views as meta
from app.api.v1 import views as car

urls = APIRouter()

urls.include_router(
    meta.router,
    prefix=""
)

urls.include_router(
    car.router,
    prefix="/api/v1"
)
