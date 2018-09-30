
from django.db import models

class Color(models.Model):
    field1 = models.CharField(max_length=264, unique=False,verbose_name="Plate 1")
    field2 = models.CharField(max_length=264,verbose_name="Plate 2")
    field3 = models.CharField(max_length=264,verbose_name="Plate 3")
    field4 = models.CharField(max_length=264,verbose_name="Plate 4")
    field5 = models.CharField(max_length=264,verbose_name="Plate 5")
    field6 = models.CharField(max_length=264,verbose_name="Plate 6")
    field7 = models.CharField(max_length=264,verbose_name="Plate 7")
    field8 = models.CharField(max_length=264,verbose_name="Plate 8")
    field9 = models.CharField(max_length=264,verbose_name="Plate 9")
    field10 = models.CharField(max_length=264,verbose_name="Plate 10")
    field11 = models.CharField(max_length=264,verbose_name="Plate 11")
    field12 = models.CharField(max_length=264,verbose_name="Plate 12")
    field13 = models.CharField(max_length=264,verbose_name="Plate 13")
    field14 = models.CharField(max_length=264,verbose_name="Plate 14")
    field15 = models.CharField(max_length=264,verbose_name="Plate 15")
    field16 = models.CharField(max_length=264,verbose_name="Plate 16")
    field17 = models.CharField(max_length=264,verbose_name="Plate 17")
    field18 = models.CharField(max_length=264,verbose_name="Plate 18")
    field19 = models.CharField(max_length=264,verbose_name="Plate 19")
    field20 = models.CharField(max_length=264,verbose_name="Plate 20")
    field21 = models.CharField(max_length=264,verbose_name="Plate 21")


    def __st__(self):
        return self.f_name
