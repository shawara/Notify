from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.utils.translation import gettext as _

from ...models import Message, MESSAGE_FIELD_SCHEMA, Customer, Notification, Group, Device, Language


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

    def validate(self, attrs):
        if attrs.get('customer', None) is None and attrs.get('group', None) is None or \
                attrs.get('customer', None) and attrs.get('group', None):
            raise ValidationError(_('You must set either customer or group'))

        text: str = attrs['message'].text[Language.choices[0][0]]
        try:
            text.format(**attrs['kwargs'])
        except KeyError as err:
            raise ValidationError(
                {'kwargs': _('the passed args does not match message args {0}').format(str(err.args))})
        except Exception:
            raise ValidationError({'kwargs': _('this field must be object of key value')})
        return attrs
