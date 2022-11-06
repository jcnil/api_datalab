from datetime import datetime
from typing import Optional, Union

from pydantic import BaseModel, Field


class ResponseSerializer(BaseModel):
    data: Optional[Union[dict, list]] = Field(
        title="Response data",
    )
    message: Optional[str] = Field(
        title="Complementary message",
    )
    errors: Optional[Union[dict, list]] = Field(
        title="Retrieves a list of errors if an action fails",
    )


class CarInSerializer(BaseModel):
    plate_number: str = Field(
        ...,
        example="354-NYH",
        title="Plate Number"
    )
    type_vehicule: str = Field(
        ...,
        example="oficial",
        title="Type of Vehicule"
    )
    start_date: str = Field(
        ...,
        example="2022-02-06 23:42:59",
        title="Date Into Vehicule",
    )
    end_date: str = Field(
        example=datetime.now(),
        title="Date Out Vehicule",
    )
