from django.db import models

# Create your models here.
class Items(models.Model):
    id = models.IntegerField(primary_key=True)
    image = models.CharField(max_length=200)
    company = models.CharField(max_length=200) 
    item_name = models.CharField(max_length=200)
    original_price = models.IntegerField()
    current_price = models.IntegerField()
    discount_percentage = models.IntegerField()
    return_period = models.IntegerField()
    delivery_date = models.DateField()
    description = models.CharField(max_length=200)
    rating = models.IntegerField()
    
  
    def __str__(self):
      return self.item_name