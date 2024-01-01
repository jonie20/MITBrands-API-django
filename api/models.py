from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=10)
    description = models.CharField(max_length=600)
    price = models.PositiveIntegerField(max_length=10)
    Image = models.ImageField(blank=False, null= False, upload_to = "uploads/ClothProducts")

    def __str__(self):
        return self.name
