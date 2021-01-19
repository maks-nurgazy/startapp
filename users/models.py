from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    company_name = models.CharField(max_length=256, unique=True)
    phone = models.CharField(max_length=256)
    address = models.CharField(max_length=256)

    def __str__(self):
        return self.username
