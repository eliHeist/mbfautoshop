from django.forms import ModelForm
from .models import StockTransaction


class StockTransactionForm(ModelForm):
    class Meta:
        model = StockTransaction
        fields = ["part", "transaction_type", "quantity", "date", "remarks"]
