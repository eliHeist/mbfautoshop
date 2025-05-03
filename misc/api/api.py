from ninja import NinjaAPI
from inventory.parts.api import part_api


api = NinjaAPI(urls_namespace="api")

api.add_router('/parts', part_api)