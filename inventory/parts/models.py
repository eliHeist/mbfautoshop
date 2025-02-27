from django.db import models

class PartCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Part(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(PartCategory, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.PositiveIntegerField(default=0)
    reorder_level = models.PositiveIntegerField(default=5)

    def __str__(self):
        return f"{self.name} - {self.category.name}"
