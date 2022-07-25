from django.db import models


# Create your models here.

class Images(models.Model):
    image = models.ImageField('Image', upload_to='static/media/', blank=True, null=True)


class Persons(models.Model):
    image = models.ManyToManyField(Images)
    first_name = models.CharField('First name', max_length=20)
    last_name = models.CharField('Last name', max_length=20)
    instrument = models.CharField('Instrument', max_length=100)

    class Meta:
        verbose_name = 'Persons'
        verbose_name_plural = 'Persons'



