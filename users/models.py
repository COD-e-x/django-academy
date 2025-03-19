
from django.db import models
from django.contrib.auth.models import AbstractUser

# NULLABLE = {'null': True, 'blank': True}
NULLABLE_FOR_STRING = {'null': False, 'blank': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='email')
    phone = models.CharField(max_length=35, verbose_name='phone number', **NULLABLE_FOR_STRING)
    telegram = models.CharField(max_length=150, verbose_name='telegram username', **NULLABLE_FOR_STRING)
    is_active = models.BooleanField(default=True, verbose_name='active')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['id']

    def __str__(self):
        return f'{self.email}'
