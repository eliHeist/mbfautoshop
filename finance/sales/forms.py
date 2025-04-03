from .models import Sale, SaleItem
from django.forms import ModelForm, inlineformset_factory


class SaleModelForm(ModelForm):
    class Meta:
        model = Sale
        fields = '__all__'


class SaleItemModelForm(ModelForm):
    class Meta:
        model = SaleItem
        fields = '__all__'


