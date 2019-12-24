from django.db import models


class Order(models.Model):
    product = models.ForeignKey('Product', models.PROTECT)
    qy = models.IntegerField()
    price = models.IntegerField()
    shop = models.ForeignKey('Shop', models.PROTECT)
    customer = models.ForeignKey('Customer', models.PROTECT)
