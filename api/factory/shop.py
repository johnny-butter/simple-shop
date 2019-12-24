import factory
from api import models


class ShopFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Shop

    name = 'mart'
