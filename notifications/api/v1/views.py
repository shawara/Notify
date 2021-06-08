from rest_framework import viewsets

from .serializers import MessageSerializer, CustomerSerializer, DeviceSerializer, GroupSerializer, \
    NotificationSerializer
from ...models import Message, Notification, Customer, Group, Device


class MessageViewSet(viewsets.ModelViewSet):
    serializer_class = MessageSerializer
    queryset = Message.objects.order_by('-pk')


class NotificationViewSet(viewsets.ModelViewSet):
    serializer_class = NotificationSerializer
    queryset = Notification.objects.order_by('-pk')


class CustomerViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.order_by('-pk')


class GroupViewSet(viewsets.ModelViewSet):
    serializer_class = GroupSerializer
    queryset = Group.objects.order_by('-pk')


class DeviceViewSet(viewsets.ModelViewSet):
    serializer_class = DeviceSerializer
    queryset = Device.objects.order_by('-pk')
