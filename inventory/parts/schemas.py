from ninja import ModelSchema
from .models import Part, PartCategory


class PartCategorySchema(ModelSchema):
    class Meta:
        model = PartCategory
        fields = ['id', 'name']

class PartSchema(ModelSchema):
    type: PartCategorySchema | None = None
    class Meta:
        model = Part
        fields = ['id', 'name', 'type', 'part_number', 'selling_price', 'stock_quantity', 'break_even_price', 'description']

