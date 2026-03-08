from django.db import models

class Item(models.Model):
    item_name = models.CharField(max_length=30)
    item_desc = models.CharField(max_length=500)
    item_price = models.IntegerField()
    
    def __str__(self):
        return self.item_name
    