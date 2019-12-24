from django.db import models


class Customer(models.Model):
    user = models.ForeignKey('User', models.PROTECT, null=True)
