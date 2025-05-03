from ninja import ModelSchema
from .models import Part, PartCategory


class PartSchema(ModelSchema):
    class Meta:
        model = Part
        fields = ['name', 'type', 'part_number', 'selling_price', 'stock_quantity', 'break_even_price', 'description']
