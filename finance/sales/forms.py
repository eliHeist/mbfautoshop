from inventory.stock.models import StockOut
from .models import Sale, SaleItem
from django import forms


class SaleModelForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = '__all__'


class SaleItemModelForm(forms.ModelForm):
    quantity = forms.IntegerField(min_value=1)  # Custom field for StockOut quantity

    class Meta:
        model = SaleItem
        fields = ['sale', 'part', 'quantity']
    
    def save(self, commit=True):
        sale_item = super().save(commit=False)

        quantity = self.cleaned_data.get('quantity')
        part = self.cleaned_data.get('part')
        sale = self.cleaned_data.get('sale')
        sale_date = sale.date  # Get the date from the related Sale

        # Create or update StockOut
        if sale_item.stock_out:
            stock_out = sale_item.stock_out
            stock_out.quantity = quantity
            stock_out.date = sale_date  # Use sale date
            stock_out.remarks = f"Updated via SaleItemForm for Part: {part}"
            stock_out.save()
        else:
            stock_out = StockOut.objects.create(
                part=part,
                quantity=quantity,
                date=sale_date,  # Use sale date here
                remarks=f"Created via SaleItemForm for Part: {part}"
            )
            sale_item.stock_out = stock_out

        if commit:
            sale_item.save()

        return sale_item


sale_item_formset = forms.inlineformset_factory(Sale, SaleItem, form=SaleItemModelForm, fields=['sale', 'part', 'quantity'], extra=1)
