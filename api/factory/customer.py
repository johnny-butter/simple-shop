import factory
from api import models
from api.factory import UserFactory


class CustomerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Customer


class RegisterCustomerFactory(CustomerFactory):
    user = factory.SubFactory(UserFactory)
