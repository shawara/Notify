from django.contrib.auth import get_user_model
from django.urls import reverse
from model_bakery import baker
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

User = get_user_model()


class CustomerTestCase(APITestCase):
    def setUp(self):
        self.user = baker.make(User, username="admin", password="123456", email="admin@test.com")

    def api_authenticate(self, user):
        token = TokenObtainPairSerializer.get_token(user).access_token
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + str(token))

    def test_is_not_authenticated(self):
        response = self.client.get(reverse('v1:notifications:list-create-customers'))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_list_customers(self):
        self.api_authenticate(self.user)
        response = self.client.get(reverse('v1:notifications:list-create-customers'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class MessageTestCase(APITestCase):
    def setUp(self):
        self.user = baker.make(User, username="admin", password="123456", email="admin@test.com")

    def api_authenticate(self, user):
        token = TokenObtainPairSerializer.get_token(user).access_token
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + str(token))

    def test_create_message(self):
        self.api_authenticate(self.user)
        response = self.client.post(reverse('v1:notifications:list-create-message'),
                                    {"text": {"en": "OTP code is {code}", "ar": "كود المرور هو {code}"}})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class NotificationTestCase(APITestCase):
    def setUp(self):
        self.user = baker.make(User, username="admin", password="123456", email="admin@test.com")
        self.customer = baker.make('notifications.Customer', email="a@gmail.com")
        self.message = baker.make('notifications.Message',
                                  text={"en": "OTP code is {code}", "ar": "كود المرور هو {code}"})

    def api_authenticate(self, user):
        token = TokenObtainPairSerializer.get_token(user).access_token
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + str(token))

    def test_create_notification_with_bad_kwargs(self):
        self.api_authenticate(self.user)
        response = self.client.post(reverse('v1:notifications:list-create-notification'),
                                    {"kwargs": {},
                                     "type": "push",
                                     "customer": self.customer.id,
                                     "message": self.message.id})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_notification(self):
        self.api_authenticate(self.user)
        response = self.client.post(reverse('v1:notifications:list-create-notification'),
                                    data={"kwargs": {"code": "1234"},
                                          "type": "push",
                                          "customer": self.customer.id,
                                          "message": self.message.id})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
