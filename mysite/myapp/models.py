from django.db import models

class Item(models.Model):

        
    def __str__(self):
        return self.item_name
    
    item_name = models.CharField(max_length=30)
    item_desc = models.CharField(max_length=500)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=500,default = 'https://www.creativefabrica.com/wp-content/uploads/2021/04/06/Food-Icon-with-Pink-Cutlery-Plate-Graphics-10479612-1.jpg')
