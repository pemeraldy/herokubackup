from django.db import models

# Create your models here.
class Tag(models.Model):
	name = models.CharField(max_length=200, null=True)

	def __str__(self):
		return self.name
class Product(models.Model):
    # PRODUCT_TYPE = (
    #     ('Phone', 'Phone'),
    #     ('Laptop','Laptop'),
    #     ('Chargers', 'Chargers')
    # )
    CATEGORY = (
        ('Incoming','Incoming'),
        ('Outgoing', 'Outgoing'),
        ('Available','Available')
    )
    name = models.CharField(max_length=200, null=True)
    product_tag = models.ManyToManyField(Tag)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    quantity = models.IntegerField(null=True)
    date = models.DateTimeField(auto_now_add=True, null=True)
    price = models.FloatField(null=True)
    reoder_level = models.IntegerField(null=True)
    def __str__(self):
        return self.name

class Sales(models.Model):
    STATUS = (
        ('Pending','Pending'),
        ('Delivered', 'Delivered')
    )
    product = models.ForeignKey(Product,null=True, on_delete=models.SET_NULL)
    customer_name = models.CharField(max_length=200, null=True)
    customer_email = models.CharField(max_length=200, null=True)
    quantity = quantity = models.IntegerField(null=True)
    date = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    amount = models.FloatField(null=True)

    def __str__ (self):
        return self.customer_name + self.product


