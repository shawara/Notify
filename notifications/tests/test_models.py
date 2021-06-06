from model_bakery import baker

from django.test import TestCase
from rest_framework.exceptions import ValidationError

from notifications.models import Customer, Group, Message, Notification


class TestCustomers(TestCase):
    def setUp(self):
        self.email = "me@gmail.com"

    def test_customer_created(self):
        customer = baker.make('notifications.Customer', email=self.email)
        self.assertEqual(Customer.objects.count(), 1)
        self.assertEqual(customer.email, self.email)


class TestGroups(TestCase):
    def setUp(self):
        self.customerA = baker.make('notifications.Customer', email="a@gmail.com")
        self.customerB = baker.make('notifications.Customer', email="b@gmail.com")

    def test_group_created(self):
        group = baker.make('notifications.Group', customers=[self.customerA, self.customerB])
        self.assertEqual(Group.objects.count(), 1)
        self.assertEqual(group.customers.count(), 2)


class TestMessages(TestCase):
    def test_create_not_valid_message(self):
        self.assertRaises(ValidationError, Message.objects.create, text={"en": "OTP code is {code}"})

    def test_create_valid_message(self):
        Message.objects.create(text={"en": "OTP code is {code}", "ar": "كود المرور هو {code}"})
        self.assertEqual(Message.objects.count(), 1)


class TestNotifications(TestCase):
    def setUp(self) -> None:
        self.message = baker.make('notifications.Message',
                                  text={"en": "OTP code is {code}", "ar": "كود المرور هو {code}"})
        self.customer = baker.make('notifications.Customer', email="a@gmail.com")

    def test_create_not_valid_notification(self):
        self.assertRaises(ValidationError, Notification.objects.create, message=self.message, customer=self.customer,
                          kwargs=[])

    def test_create_valid_notification(self):
        Notification.objects.create(message=self.message, customer=self.customer, kwargs={"code": "1242"})
        self.assertEqual(Notification.objects.count(), 1)
