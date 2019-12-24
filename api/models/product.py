from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=20)
    stock_pcs = models.IntegerField()
    price = models.IntegerField()
    shop = models.ForeignKey('Shop', models.PROTECT)
    vip = models.BooleanField(default=False)

    def __str__(self):
        return self.name
