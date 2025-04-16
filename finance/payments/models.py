from django.db import models
from finance.sales.models import Sale

class PaymentMethod(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Payment(models.Model):
    PAYMENT_TYPES = [
        ('IN', 'Income'),
        ('EX', 'Expense'),
    ]
    
    type = models.CharField(max_length=3, choices=PAYMENT_TYPES)
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE, related_name="payments", null=True, blank=True)
    method = models.ForeignKey(PaymentMethod, on_delete=models.SET_NULL, null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_added = models.DateTimeField(auto_now_add=True)
    date = models.DateTimeField()

    def __str__(self):
        return f"Payment {self.id} - UGX {self.amount} for Sale {self.sale.id}"



class Income(Payment):
    # objects = StockInManager()

    def save(self, *args, **kwargs):
        self.type = 'IN'
        super().save(*args, **kwargs)

    class Meta:
        proxy = True
        verbose_name = "Income"
        verbose_name_plural = "Income"