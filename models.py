import uuid
from typing import Optional
from pydantic import BaseModel, Field

class Transakcje(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    data: str = Field(...)
    typ: str = Field(...)
    waluta: str = Field(...)
    kwota: float = Field(...)
    wydano: float = Field(...)

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "_id": "066de609-b04a-4b30-b46c-32537c7f1f6e",
                "data": "12-08-2023",
                "typ": "sprzedaz",
                "waluta": "EUR",
                "kwota": 120,
                "wydano": 27.67
            }
        }
