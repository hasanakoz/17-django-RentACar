from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator


class Car(models.Model):
    GEAR = (
        ('a', 'automatic'),
        ('m', 'manuel')
    )
    plate_number = models.CharField(max_length=15, unique=True)
    brand = models.CharField(max_length=15)
    model = models.CharField(max_length=20)
    year = models.SmallIntegerField()
    gear = models.CharField(max_length=1, choices=GEAR)
    rent_per_day = models.DecimalField(
        max_digits=7,
        decimal_places=2,
        validators=[MinValueValidator(1)]
    )
    availability = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.model} - {self.brand} - {self.plate_number}'
