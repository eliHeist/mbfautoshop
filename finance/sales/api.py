from ninja import Router

from .models import Sale
from .schemas import SaleSchema

sales_api = Router()

@sales_api.post("/", response=SaleSchema, url_name="create_sale")
@transaction.atomic
def create_sale(request):
    
    