from django.db import models
from cloudinary.models import CloudinaryField
from config.constants import *


class Item(models.Model):
    class Meta(object):
        db_table = 'item'

    status = models.CharField(
        'Status', blank= False, default = 'draft', max_length= 50, db_index= True, choices=STATUS
    )
    name = models.CharField(
         'Name', blank= False, null= False, max_length= 150, db_index= True
    )
    category= models.CharField(
        'Category', blank= False, null= False, max_length= 20, db_index= True, default= 'others', choices= CATEGORIES
    )
    price = models.DecimalField(
         'price', blank= False, null= False, max_digits= 11, decimal_places= 2   
    )
    image = CloudinaryField(
        'image', blank= True, null= True, 
    )
    created_at = models.DateTimeField(
        'Created Datetime', blank=True, auto_now_add=True
    )
    updated_at = models.DateTimeField(
        'Updated Datetime', blank=True, auto_now=True
    )

# Create your models here.
