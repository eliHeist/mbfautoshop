from ninja import ModelSchema

from finance.sales.schemas import SaleSchema
from .models import PaymentMethod, Income


class PaymentMethodSchema(ModelSchema):
    class Config:
        model = PaymentMethod
        model_fields = "__all__"
        

class IncomeSchema(ModelSchema):
    sale: SaleSchema | None = None
    class Config:
        model = Income
        model_fields = ["sale", "method", "amount", "date"]