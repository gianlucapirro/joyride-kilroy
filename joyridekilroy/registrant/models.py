from django.db import models

# Create your models here.


class Registrant(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, unique=True)
    phone = models.CharField(
        max_length=255, blank=True, default="", unique=True)
    roadtrip = models.CharField(max_length=3500)
    email_friend1 = models.EmailField(max_length=254, null=True, blank=True)
    email_friend2 = models.EmailField(max_length=254, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} - {self.last_name}"
