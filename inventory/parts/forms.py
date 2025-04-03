from django.forms import ModelForm
from .models import Part, PartType


class PartCreateModelForm(ModelForm):
    class Meta:
        model = Part
        fields = ["name", "_type", "part_number", "selling_price", "description"]


class PartTypeModelForm(ModelForm):
    class Meta:
        model = PartType
        fields = ["name"]