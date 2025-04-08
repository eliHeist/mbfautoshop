from django import forms

from .models import StockIn, StockOut, StockTransaction


class StockTransactionForm(forms.ModelForm):
    class Meta:
        model = StockTransaction
        fields = ["part", "transaction_type", "quantity", "date", "remarks"]


class StockInForm(forms.ModelForm):
    class Meta:
        model = StockIn
        fields = ['part', 'quantity', 'date', 'remarks']


class StockOutForm(forms.ModelForm):
    class Meta:
        model = StockOut
        fields = ['part', 'quantity', 'date', 'remarks']


StockInTransactionFormSet = forms.modelformset_factory(
    StockIn,
    fields=['part', 'quantity', 'date', 'remarks'], 
    extra=1,  # Add 1 empty form by default
    can_delete=True
)
