from django.db import models

# Create your models here.

class Place(models.Model):
    id_2gis = models.CharField(max_length=300, verbose_name='ID 2GIS')