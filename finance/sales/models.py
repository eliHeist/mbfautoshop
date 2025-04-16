from django.db import models
from inventory.parts.models import Part
from inventory.stock.models import StockOut
from people.customers.models import Customer

class Sale(models.Model):
    # customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date = models.DateTimeField()
    comments = models.TextField(blank=True)

    def __str__(self):
        return f"Sale {self.id} - {self.date}"
    
    def getTotalAmount(self):
        total = 0
        for item in self.items.all():
            total += item.amount()
        return total

class SaleItem(models.Model):
    sale = models.ForeignKey(Sale, related_name="items", on_delete=models.CASCADE)
    part = models.ForeignKey(Part, on_delete=models.CASCADE)
    stock_out = models.OneToOneField(StockOut, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=0)

    def __str__(self):
        return f"{self.quantity} x {self.part.name} (Sale {self.sale.id})"
    
    def amount(self):
        return self.quantity * self.unit_price
