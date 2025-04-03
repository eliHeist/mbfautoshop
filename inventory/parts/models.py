from django.db import models

class PartType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Part(models.Model):
    name = models.CharField(max_length=255)
    type = models.ForeignKey(PartType, on_delete=models.CASCADE, related_name='parts', null=True)
    part_number = models.CharField(max_length=100)
    selling_price = models.DecimalField(max_digits=20, decimal_places=0)
    break_even_price = models.DecimalField(max_digits=20, decimal_places=0)
    stock_quantity = models.PositiveIntegerField(default=0)

    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.category.name}"
    
    def get_type(self):
        return self._type
