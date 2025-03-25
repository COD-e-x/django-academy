from django.db import models

from users.models import NULLABLE
from users.models import NULLABLE_FOR_STRING


class Breed(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Порода",
    )
    description = models.CharField(
        max_length=1000,
        verbose_name="Описание",
        **NULLABLE_FOR_STRING,
    )

    class Meta:
        verbose_name = "Порода собаки"
        verbose_name_plural = "Породы собак"

    def __str__(self):
        return f"{self.name}"


class Dog(models.Model):
    name = models.CharField(
        max_length=250,
        verbose_name="Имя",
    )
    breed = models.ForeignKey(
        Breed,
        on_delete=models.CASCADE,
        verbose_name="Порода",
    )
    photo = models.ImageField(
        upload_to="dogs/",
        **NULLABLE,
        verbose_name="Фото",
    )
    birth_date = models.DateTimeField(
        **NULLABLE,
        verbose_name="Дата рождения",
    )

    class Meta:
        verbose_name = "Собака"
        verbose_name_plural = "Собаки"
        # abstract = True
        # app_label = 'dogs'
        # ordering = ['-birth_date']
        # permissions = []
        # db_table = 'doggies'
        # get_latest_by = 'birth_date'

    def __str__(self):
        return f"{self.name} ({self.breed})"
