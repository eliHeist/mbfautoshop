from django import forms
from .models import Payment, Income


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = '__all__'
        
class IncomeForm(forms.ModelForm):
    payment_date = forms.DateField(label="Payment Date", widget=forms.DateInput(attrs={'type':'date'}))
    class Meta:
        model = Income
        fields = ['sale', 'method', 'amount', 'payment_date']
    
    def init(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.date:
            self.fields['payment_date'].initial = self.instance.date
    
    def save(self, commit = True):
        instance = super().save(commit=False)
        instance.date = self.cleaned_data['payment_date']

        if commit:
            instance.save()
        return instance
    