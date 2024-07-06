from django.db import models

# Create your models here.
class ProductoModel (models.Model):
   nombre = models.CharField(max_length=100)
   precio = models.IntegerField()
   image = models.ImageField(upload_to="productos/", blank=True, null=True)