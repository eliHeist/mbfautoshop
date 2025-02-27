from django.db import models

class Supplier(models.Model):
    name = models.CharField(max_length=255)
    contact = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
