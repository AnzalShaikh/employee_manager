from django.db import models
from django.contrib.auth.models import AbstractUser


USER_CHOICES = [('admin', 'Admin'), ('employee', 'Employee')]


class CustomUser(AbstractUser):
    user_type = models.CharField(
        max_length=250, choices=USER_CHOICES, null=True, blank=True)
