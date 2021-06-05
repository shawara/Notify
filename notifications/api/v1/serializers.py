from rest_framework import serializers

from ...models import Message, MESSAGE_FIELD_SCHEMA, Customer, Notification, Group, Device


class MessageJSONField(serializers.JSONField):
    class Meta:
        swagger_schema_fields = MESSAGE_FIELD_SCHEMA


class MessageSerializer(serializers.ModelSerializer):
    text = MessageJSONField()

    class Meta:
        fields = '__all__'
        model = Message


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Customer


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Device


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Group


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Notification
