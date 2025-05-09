from ninja import ModelSchema, Schema

from inventory.stock.schemas import StockOutSchema

from .models import Sale, SaleItem


class SaleSchema(ModelSchema):
    class Config:
        model = Sale
        model_fields = ["id", "date", "comments"]


class SaleItemSchema(ModelSchema):
    stock_out: StockOutSchema | None = None
    sale: SaleSchema | None = None
    class Config:
        model = SaleItem
        model_fields = ["id", "sale", "stock_out"]


