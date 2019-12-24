import factory
from api import models
from api.factory.shop import ShopFactory


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Product

    name = 'protein'
    stock_pcs = 100
    price = 100
    shop = factory.SubFactory(ShopFactory)


class VipProductFactory(ProductFactory):
    name = 'vip_protein'
    vip = True
