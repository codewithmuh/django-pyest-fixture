from django.db import models

class Retail(models.Model):
    name = models.CharField(max_length=128)
    
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    
    def __str__(self):
        return self.name
 
class Product(models.Model):
    sku = models.CharField(max_length=50, unique=True)  # unique model number
    name = models.CharField(max_length=50)
    description = models.TextField(default="", blank=True)
    mrp = models.DecimalField(max_digits=10, decimal_places=2)
    weight = models.DecimalField(max_digits=10, decimal_places=2)
    retails = models.ManyToManyField(
        Retail,
        related_name="products",
        verbose_name="Retail stores that carry the product",
    )
    category = models.ForeignKey(
        Category, 
				related_name="products", 
				on_delete=models.CASCADE,
				blank=True,
				null=True,
    )
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)