from django.db import models
from django.contrib.auth.models import AbstractUser

NULLABLE = {"null": True, "blank": True}
NULLABLE_FOR_STRING = {"null": False, "blank": True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="Эл. почта")
    phone = models.CharField(
        max_length=35,
        verbose_name="Номер телефона",
        **NULLABLE_FOR_STRING,
    )
    telegram = models.CharField(
        max_length=150,
        verbose_name="Телеграм",
        **NULLABLE_FOR_STRING,
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name="Активен",
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ["id"]

    def __str__(self):
        return f"{self.email}"
