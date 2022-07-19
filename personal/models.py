from django.db import models


# Create your models here.


class Persons(models.Model):
    image = models.ImageField(upload_to='static/media/', blank=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    instrument = models.CharField(max_length=100)
