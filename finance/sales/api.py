from django.db import transaction

from ninja import Router, Schema
from ninja.errors import HttpError

from finance.payments.schemas import IncomeSchema
from inventory.parts.models import Part

from .models import Sale, SaleItem
from .schemas import SaleSchema, SaleItemSchema

sales_api = Router()

class SaleInSchema(Schema):
    sale: SaleSchema
    incomes: list[IncomeSchema]
    sale_items: list[SaleItemSchema]

@sales_api.post("/createsale", response=SaleSchema, url_name="create_sale")
@transaction.atomic
def create_sale(request, data: SaleInSchema):
    print(data)
    return HttpError(440, "Testing mode")
    
    