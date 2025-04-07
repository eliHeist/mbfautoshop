from django.db import models
from inventory.parts.models import Part


class StockTransactionManager(models.Manager):
    def all_transactions(self):
        return self.all()
    
    def get_in_transactions(self):
        return super().get_queryset().filter(transaction_type='IN')
    
    def get_out_transactions(self):
        return super().get_queryset().filter(transaction_type='OUT')


class StockInManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(transaction_type='IN')


class StockOutManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(transaction_type='OUT')


# MODELS
class StockTransaction(models.Model):
    TRANSACTION_TYPES = [
        ('IN', 'Stock In'),
        ('OUT', 'Stock Out'),
    ]
    
    part = models.ForeignKey(Part, on_delete=models.CASCADE, related_name='stock_transactions')
    transaction_type = models.CharField(max_length=3, choices=TRANSACTION_TYPES)
    quantity = models.PositiveIntegerField()
    date = models.DateTimeField()
    date_added = models.DateTimeField(auto_now_add=True)
    remarks = models.TextField(blank=True, null=True)
    
    objects = StockTransactionManager()

    def __str__(self):
        return f"{self.transaction_type} - {self.part.name} ({self.quantity})"


# === Proxy Models ===
class StockIn(StockTransaction):
    objects = StockInManager()

    def save(self, *args, **kwargs):
        self.transaction_type = 'IN'
        super().save(*args, **kwargs)

    class Meta:
        proxy = True
        verbose_name = "Stock In"
        verbose_name_plural = "Stock In Records"


class StockOut(StockTransaction):
    objects = StockOutManager()

    def save(self, *args, **kwargs):
        self.transaction_type = 'OUT'
        super().save(*args, **kwargs)

    class Meta:
        proxy = True
        verbose_name = "Stock Out"
        verbose_name_plural = "Stock Out Records"

