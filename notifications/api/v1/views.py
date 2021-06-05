from rest_framework.generics import ListCreateAPIView
from rest_framework.viewsets import GenericViewSet

from .serializers import MessageSerializer, CustomerSerializer, DeviceSerializer, GroupSerializer, \
    NotificationSerializer
from ...models import Message, Notification


class MessageViewSet(GenericViewSet):
    serializer_class = MessageSerializer
    queryset = Message.objects.all()


class NotificationViewSet(GenericViewSet):
    serializer_class = NotificationSerializer
    queryset = Notification.objects.all()


class CustomerViewSet(GenericViewSet):
    serializer_class = CustomerSerializer
    queryset = Message.objects.all()


class GroupViewSet(GenericViewSet):
    serializer_class = GroupSerializer
    queryset = Message.objects.all()


class DeviceViewSet(GenericViewSet):
    serializer_class = DeviceSerializer
    queryset = Message.objects.all()
