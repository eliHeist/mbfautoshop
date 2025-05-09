from inventory.parts.schemas import PartSchema
from .models import StockIn, StockOut
from ninja import ModelSchema


class StockInSchema(ModelSchema):
    class Config:
        model = StockIn
        model_fields = ["id", "part", "quantity", "date", "remarks"]


class StockOutSchema(ModelSchema):
    part: PartSchema | None = None
    class Config:
        model = StockOut
        model_fields = ["id", "part", "quantity", "date", "remarks"]


