from django.db import models

# Create your models here.


class PC(models.Model):
    name = models.CharField(max_length=100,verbose_name='name')
    processor = models.CharField(max_length=100,verbose_name='processor')
    memory = models.PositiveIntegerField()
    storage = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    
    
    class Meta:
        db_table='pcs'
        ordering=['name', 'processor']



class Laptop(models.Model):
    brand = models.CharField(max_length=100,verbose_name='brand')
    model_name = models.CharField(max_length=100,verbose_name='model')
    price = models.IntegerField(verbose_name='price')
    processor = models.CharField(max_length=100)
    ram = models.IntegerField(verbose_name='ram')
    storage = models.IntegerField(verbose_name='storage')
    graphics_card = models.CharField(max_length=100,verbose_name='graphics_card')
    screen_size = models.IntegerField(verbose_name='screen_size')
    weight = models.IntegerField(verbose_name='weight')
    battery_life = models.IntegerField(verbose_name='battery_life')
    
    class Meta:
        db_table = 'laptops'
        ordering=['brand', 'processor', 'ram']