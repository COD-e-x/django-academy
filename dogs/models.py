from django.db import models

from users.models import NULLABLE
from users.models import NULLABLE_FOR_STRING


class Breed(models.Model):
    name = models.CharField(max_length=100, verbose_name="bread")
    description = models.CharField(
        max_length=1000,
        verbose_name="description",
        **NULLABLE_FOR_STRING,
    )

    class Meta:
        verbose_name = "bread"
        verbose_name_plural = "breads"

    def __str__(self):
        return f"{self.name}"


class Dog(models.Model):
    name = models.CharField(max_length=250, verbose_name="dog name")
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="dogs/", **NULLABLE)
    birth_date = models.DateTimeField(**NULLABLE)

    class Meta:
        verbose_name = "dog"
        verbose_name_plural = "dogs"
        # abstract = True
        # app_label = 'dogs'
        # ordering = ['-birth_date']
        # permissions = []
        # db_table = 'doggies'
        # get_latest_by = 'birth_date'

    def __str__(self):
        return f"{self.name} ({self.breed})"
