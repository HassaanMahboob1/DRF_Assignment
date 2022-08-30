from urllib import response
from django.test import TestCase, Client
import json
from django.urls import reverse
from .models import Notes, User

# Create your tests here.
class TestViewSets(TestCase):
    def test_list_GET(self):

        client = Client()
        print(client.post("/register"))
        response = client.get("/register")
        self.assertEquals(response.status_code, 200)
