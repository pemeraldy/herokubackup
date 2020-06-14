from django.db import models

# Create your models here.
class Product(models.Model):
    PRODUCT_TYPE = (
        ('Phone', 'Phone'),
        ('Laptop','Laptop'),
        ('Chargers', 'Chargers')
    )
    CATEGORY = (
        ('Incoming','Incoming'),
        ('Outgoing', 'Outgoing'),
        ('Available','Available')
    )
    name = models.CharField(max_length=200, null=True)
    product_type = models.CharField(max_length=200, null=True, choices=PRODUCT_TYPE)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    quantity = models.IntegerField(null=True)
    date = models.DateTimeField(auto_now_add=True, null=True)
    price = models.FloatField(null=True)
    reoder_level = models.IntegerField(null=True)
    def __str__(self):
        return self.name


