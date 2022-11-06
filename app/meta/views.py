from fastapi import APIRouter
from starlette import status
from starlette.responses import JSONResponse

from app.api.v1.serializers import ResponseSerializer

router = APIRouter()


@router.get("/", tags=["meta"], response_model=ResponseSerializer)
async def root():
    try:
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                'message': 'API for Cars DataLab',
                "author": "Jose Nicolielly",
                "documentation_path": [
                    "/api/v1/docs#/",
                    "/api/v1/redoc",
                ]
            }
        )
    except Exception as e:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                'error': f'Internal server error {e}',
            }
        )


@router.get("/health", tags=["meta"], response_model=ResponseSerializer)
async def health_check():
    response = {
        "message": "ok"
    }
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=response
    )
