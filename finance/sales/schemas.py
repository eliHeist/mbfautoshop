from ninja import ModelSchema

from inventory.parts.schemas import PartSchema
from inventory.stock.schemas import StockOutSchema

from .models import Sale, SaleItem


class SaleSchema(ModelSchema):
    class Config:
        model = Sale
        model_fields = ["id", "date"]


class SaleItemSchema(ModelSchema):
    part: PartSchema | None = None
    stock_out: StockOutSchema | None = None
    class Config:
        model = SaleItem
        model_fields = ["id", "quantity", "part", "stock_out"]
