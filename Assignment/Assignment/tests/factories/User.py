from notes.models import User
import factory
from faker import Factory
from rest_framework.test import APITestCase

# todo:In Progress (Due to some errors)

faker = Factory.create()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "User"

    first_name = faker.name
    # last_name = factory.faker('last_name')
    # email = factory.faker('email')
    # username = factory.faker('username')
    # password = factory.faker('password')
