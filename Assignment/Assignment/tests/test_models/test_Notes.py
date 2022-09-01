from django.test import TestCase
from Assignment.tests.factories import NotesFactory

# todo:In Progress (Due to some errors)


class NotesModelsTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.Company = NotesFactory._meta.model

    def test_crud_company(self):
        company = NotesFactory(name="X Company")


# from django.test import TestCase, Client
# import json
# from rest_framework.authtoken.models import Token
# from rest_framework.test import APITestCase
# from .models import User
# import requests

# # Create your tests here.
# class TestViewSets(TestCase):
#     def setUp(self):
#         self.client = Client()
#         self._url = "http://127.0.0.1:8000/"
#         self.token = ""
#         return super().setUp()

#     def test_register_POST(self):
#         register = self._url + "register"
#         client = Client()
#         data = {
#             "email": "usman.beg@gmail.com",
#             "first_name": "usman",
#             "last_name": "beg",
#             "username": "usmanbeg",
#             "password": "usmanbeg123",
#         }
#         response = client.post(register, data=data, format="json")
#         self.assertEquals(response.status_code, 201)

#     def test_Login_POST(self):
#         self.test_register_POST()
#         login = self._url + "api/token/"
#         data = {"username": "usmanbeg", "password": "usmanbeg123"}
#         response = self.client.post(login, data=data, format="json")
#         data = response.json()
#         self.token = data["access"]
#         self.assertEquals(response.status_code, 200)

#     def test_create_note_POST(self):
#         self.test_Login_POST()
#         create_note = self._url + "Notes/"
#         hed = {"Authorization": "Bearer " + self.token}
#         data = {
#             "title": "Note 6",
#             "text": "sixth-Party",
#             "date_created": "2022-08-30",
#             "date_updated": "2022-08-30",
#             "archive": 0,
#         }
#         response = requests.post(create_note, data=data, headers=hed)
#         self.assertEquals(response.status_code, 201)

#     def test_notes_list_GET(self):
#         self.test_Login_POST()
#         create_note = self._url + "Notes/"
#         hed = {"Authorization": "Bearer " + self.token}
#         response = requests.get(create_note, headers=hed)
#         self.assertEquals(response.status_code, 200)

#     def test_notes_delete_DELETE(self):
#         self.test_Login_POST()
#         create_note = self._url + "Notes/1"
#         hed = {"Authorization": "Bearer " + self.token}
#         response = requests.delete(create_note, headers=hed)
#         self.assertEquals(response.status_code, 204)


# from rest_framework.test import APITestCase ,APIClient
# from notes.models import User
# class NotesViewsetTestCases(APITestCase):
#     def setUp(self):
#         self.user =User.objects.create_user(
#             email = "usman.beg@gmail.com",
#             first_name = "usman",
#             last_name = "beg",
#             username = "usmanbeg",
#             password = "usmanbeg123"
#         )
#         self._url = "http://127.0.0.1:8000/"

#         return super().setUp()

#     def test_register_user(self):
#         register = self._url + "register"
#         data = {
#             "email": "ali.beg@gmail.com",
#             "first_name": "ali",
#             "last_name": "beg",
#             "username": "alibeg",
#             "password": "alibeg123",
#         }
#         response = self.client.post(register, data=data, format="json")
#         self.assertEquals(response.status_code, 201)

# def test_login_user(self):
#     url = self._url + "api/token/"
#     data = {
#         "username":"usmanbeg",
#         "password":"usmanbeg123"

#     }

#     self.client.force_authenticate(user=self.user)
#     response = self.client.post(url, data)
#     self.assertEquals(response.status_code, 200)

# def test_add_note(self):
#     url = self._url + "Notes/"
#     data = {
#         "title":"Note 6",
#         "text":"sixth-Party",
#         "date_created":"2022-08-30",
#         "date_updated":"2022-08-30",
#         "archive":0
#         }
#     self.client.force_authenticate(user=self.user)
#     response = self.client.post(url, data)
#     self.assertEquals(response.status_code, 201)


# def test_list_notes(self):
#     url = self._url + "Notes/"
#     self.client.force_authenticate(user=self.user)
#     response = self.client.get(url)
#     self.assertEquals(response.status_code, 200)

# def test_delete_note(self):
#     url = self._url + "Notes/1"
#     self.client.force_authenticate(user=self.user)
#     response = self.client.delete(url)
#     self.assertEquals(response.status_code, 204)
