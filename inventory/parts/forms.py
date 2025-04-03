from django import forms
from .models import Part, PartCategory


class PartCreateModelForm(forms.ModelForm):
    class Meta:
        model = Part
        fields = ["name", "type", "part_number", "selling_price", "description"]


class PartCategoryModelForm(forms.ModelForm):
    class Meta:
        model = PartCategory
        fields = ["name"]