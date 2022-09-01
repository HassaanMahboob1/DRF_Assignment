from http import client
from django.test import TestCase, Client
from Assignment.tests.factories.User import UserFactory

# todo:In Progress (Due to some errors)


class NotesModelsTestCase(TestCase):
    def setUp(self):
        self.obj1 = UserFactory(
            first_name="usman",
            last_name="beg",
            email="usmanbeg@gmail.com",
            username="usmanbeg",
            password="usmanbeg123",
        )
        client = Client()

    def test_register(self):
        url = "http://127.0.0.1:8000/register"
        resp = self.client.get(url)
        print(resp)
