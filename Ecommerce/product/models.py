from django.db import models
from django.urls import reverse 
# Create your models here.


class Product(models.Model):
    id = models.BigIntegerField(primary_key=True, db_column='product_id')
    name = models.CharField(max_length = 100)
    detail = models.TextField()
    category = models.CharField(max_length = 50)
    price = models.IntegerField()

    def get_absolute_url(self):
        return reverse("product_detail", kwargs={'pk':self.pk})

    def __str__(self):
        return self.name 

class Tag(models.Model):
    id = models.BigIntegerField(primary_key=True)
    product  = models.ForeignKey(Product, models.DO_NOTHING)
    tag  = models.CharField(max_length = 50) 

    class Meta:
        unique_together = (('product', 'tag'),)