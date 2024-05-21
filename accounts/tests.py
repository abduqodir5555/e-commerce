from django.test import TestCase
from django.urls import reverse

from rest_framework.test import APITestCase


class TestUserCreateView(APITestCase):
    def setUp(self):
        pass

    def test_happy(self):
        url = reverse("register")
        data = {
            "first_name": "TestName",
            "last_name": "TestLastName",
            "email": "testemail@gmail.com",
            "password": "kiber4224"
        }

        response = self.client.post(url, data=data)
        self.assertEquals(response.status_code, 201)
        self.assertEquals(list(response.data.keys()), ["first_name", "last_name", "email", "password"])
        self.assertEquals(response.data['first_name'], "TestName")
        self.assertEquals(response.data['last_name'], "TestLastName")
        self.assertEquals(response.data['email'], "testemail@gmail.com")
        self.assertEquals(response.data['password'], "kiber4224")


class TestVerifyOtpView(APITestCase):
    def setUp(self):
        self.user = User.objects.create(first_name="TestName", last_name="TestLastName", email="testemail@gmail.com")
        self.user.set_password("kiber4224")
        self.user.save()

    def test_happy(self):
        pass



