from .models import Sale, SaleItem
from django import forms


class SaleModelForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = '__all__'


class SaleItemModelForm(forms.ModelForm):
    class Meta:
        model = SaleItem
        fields = '__all__'


sale_item_formset = forms.inlineformset_factory(Sale, SaleItem, fields='__all__')
