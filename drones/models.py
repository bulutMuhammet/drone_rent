from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models

# Create your models here.
class Drone(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    CATEGORY_CHOICES = (
        ('kategori1', 'Kategori 1'),
        ('kategori2', 'Kategori 2'),
        ('kategori3', 'Kategori 3'),
    )
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)

    def __str__(self):
        return f"{self.brand} {self.model}"



class RentedDrone(models.Model):
    drone = models.ForeignKey(Drone, on_delete=models.CASCADE, null=False)
    start_date = models.DateTimeField(null=False)
    end_date = models.DateTimeField(null=False)
    renting_user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return f"Kiralanan İHA: {self.drone} - Kiralayan Kullanıcı: {self.renting_user}"

    # def clean(self):
