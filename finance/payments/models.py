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
    
    date_added = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=3, choices=PAYMENT_TYPES, null=True)

    sale = models.ForeignKey(Sale, on_delete=models.CASCADE, related_name="payments", null=True, blank=True)
    method = models.ForeignKey(PaymentMethod, on_delete=models.SET_NULL, null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()

    def __str__(self):
        return f"Payment {self.pk} - UGX {self.amount}"
    


# model manager for Income
class IncomeManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(type='IN') 


class Income(Payment):
    objects = IncomeManager()

    def save(self, *args, **kwargs):
        self.type = 'IN'
        super().save(*args, **kwargs)

    class Meta:
        proxy = True
        verbose_name = "Income"
        verbose_name_plural = "Income"



# model manager for Expense
class ExpenseManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(type='EX')


class Expense(Payment):
    objects = ExpenseManager()

    def save(self, *args, **kwargs):
        self.type = 'EX'
        super().save(*args, **kwargs)

    class Meta:
        proxy = True
        verbose_name = "Expense"
        verbose_name_plural = "Expenses"