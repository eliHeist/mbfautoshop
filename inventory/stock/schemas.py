from .models import StockIn, StockOut
from ninja import ModelSchema


class StockInSchema(ModelSchema):
    class Config:
        model = StockIn
        model_fields = ["part", "quantity", "date", "remarks"]


class StockOutSchema(ModelSchema):
    class Config:
        model = StockOut
        model_fields = ["part", "quantity", "date", "remarks"]


