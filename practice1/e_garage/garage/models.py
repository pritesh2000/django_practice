from django.db import models
from generic.models import BaseField
# Create your models here.

"""
class Category(BaseField):
    category_name = models.CharField(max_length=50)
    is_active = models.BooleanField(default= 1)

    class Meta():
        db_table = 'category'

class Subcategory(BaseField):
    subcategory_name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=1)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta():
        db_table = 'subcategory'

class Service(BaseField):
    service_name = models.CharField(max_length=30)
    description = models.CharField(max_length=500)
    price = models.IntegerField()
    is_available = models.BooleanField(default=1)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE)

    class Meta():
        db_table = 'service'
"""