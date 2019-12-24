import factory
from api import models


class OrderFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Order
