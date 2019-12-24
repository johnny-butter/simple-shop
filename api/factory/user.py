import factory
from api import models


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.User

    username = 'test_user'


class VipUserFactory(UserFactory):
    username = 'test_vip_user'
    vip = True
