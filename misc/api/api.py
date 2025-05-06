from ninja import NinjaAPI
from inventory.parts.api import part_api


api_router = NinjaAPI(urls_namespace="api")

api_router.add_router('/parts', part_api)