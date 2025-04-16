from django.db import models
from inventory.stock.models import StockTransaction

# Create your models here.
class Purchase(models.Model):
    TYPES = (
        ('other', 'Other'),
        ('stock', 'Stock'),
    )
    
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=20, choices=TYPES)
    date_added = models.DateTimeField(auto_now_add=True)
    date = models.DateTimeField()
    description = models.TextField(blank=True, null=True)
    
    re_stocks = models.ManyToManyField(StockTransaction, blank=True)
    
    def __str__(self):
        return f"{self.amount} - {self.type}"