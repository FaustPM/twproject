from django.db import models


class Feedback(models.Model):
    email = models.EmailField('E-mail', max_length=25, blank=True, null=True)
    message = models.CharField('Message', max_length=120)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Feedback Form'
        verbose_name_plural = 'Feedback Form'
