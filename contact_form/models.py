from django.db import models


class Contact(models.Model):
    email = models.EmailField(max_length=150)
    message = models.TextField(max_length=1000)

    def __str__(self):
        # Будет отображаться следующее поле в панели адм.
        return self.email