from django.db import models

class PartCategory(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name
    
    def save(self):
        self.name = self.name.upper()
        return super().save()
    
    def get_parts(self):
        return self.parts.all()

class Part(models.Model):
    name = models.CharField(max_length=255)
    type = models.ForeignKey(PartCategory, on_delete=models.CASCADE, related_name='parts', null=True)
    part_number = models.CharField(max_length=100)
    selling_price = models.DecimalField(max_digits=20, decimal_places=0, null=True, blank=True)
    break_even_price = models.DecimalField(max_digits=20, decimal_places=0, null=True)
    stock_quantity = models.PositiveIntegerField(default=0)

    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.type.name}"
    
    def get_type(self):
        return self.type
    
    def get_stock(self):
        return self.stock_quantity
