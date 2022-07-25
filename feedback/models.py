from django.db import models


class Feedback(models.Model):
    email = models.EmailField('E-mail', max_length=25, blank=True)
    message = models.TextField()

    class Meta:
        verbose_name = 'Feedback Form'
        verbose_name_plural = 'Feedback Form'
