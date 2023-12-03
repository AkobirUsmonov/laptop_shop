from django.db import models

# Create your models here.

class Laptop(models.Model):
    laptop_name_uz = models.CharField(max_length=100, verbose_name="Ko'chma_kopyuter")
    laptop_name_en = models.CharField(max_length=100, verbose_name='Laptop_name')
    laptop_name_ru = models.CharField(max_length=100, verbose_name='Имя ноутбука')

    class Meta:
        db_table = 'laptop_laptop'
        ordering = ['laptop_name_uz']


class PCs(models.Model):
    PCs_name_uz = models.CharField(max_length=100, verbose_name='PCs_name')
    PCs_name_en = models.CharField(max_length=100, verbose_name='Laptop_name')
    PCs_name_ru = models.CharField(max_length=100, verbose_name='Имя ноутбука')
    PCs_price = models.IntegerField(verbose_name="Narx/Price (so'm)")
    PCs_category = models.ForeignKey(Laptop, on_delete=models.CASCADE, null=True, default=None)

    class Meta:
        db_table = 'PCs_PCs'
        ordering = ['PCs_name_uz']