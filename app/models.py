from django.db import models


class Simple_Product(models.Model):
    Sku = models.CharField(max_length=50)
    Name = models.CharField(max_length=50)
    Short_Decs = models.CharField(max_length=255)
    Long_Desc = models.CharField(max_length=225)
    Price = models.IntegerField()
    Quantity = models.IntegerField()
    Image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.Name


class Variety_Product(models.Model):
    Sku = models.CharField(max_length=50)
    Name = models.CharField(max_length=50)
    Short_Decs = models.CharField(max_length=255)
    Long_Desc = models.CharField(max_length=255)
    Price = models.IntegerField()
    Quantity = models.IntegerField()
