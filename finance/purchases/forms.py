from django import forms
from .models import Purchase

class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ['amount', 'type', 'date', 'description']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Optional: Set initial date to today
        from django.utils.timezone import now
        self.fields['date'].initial = now()
