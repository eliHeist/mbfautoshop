from django import forms
from .models import Part, PartType


class PartCreateModelForm(forms.ModelForm):
    class Meta:
        model = Part
        fields = ["name", "type", "part_number", "selling_price", "description"]


class PartTypeModelForm(forms.ModelForm):
    class Meta:
        model = PartType
        fields = ["name"]