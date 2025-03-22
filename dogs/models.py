from django.db import models

from users.models import NULLABLE_FOR_STRING

class Breed(models.Model):
    name = models.CharField(max_length=100, verbose_name='bread')
    description = models.CharField(max_length=1000, verbose_name='description', **NULLABLE_FOR_STRING)

    class Meta:
        verbose_name = 'bread'
        verbose_name_plural = 'breads'

    def __str__(self):
        return f'{self.name}'
