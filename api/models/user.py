from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    vip = models.BooleanField(default=False)
