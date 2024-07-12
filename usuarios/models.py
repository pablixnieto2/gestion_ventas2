from django.contrib.auth.models import AbstractUser
from django.db import models
from simple_history.models import HistoricalRecords

class Usuario(AbstractUser):
    telefono = models.CharField(max_length=20, blank=True, null=True)
    history = HistoricalRecords()

    def __str__(self):
        return self.username
