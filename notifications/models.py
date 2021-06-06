from django.db import models
from django.utils.translation import gettext as _
from drf_yasg import openapi

from notifications.validators import JSONSchemaValidator


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Language(models.TextChoices):
    EN = 'en', _('English')
    AR = 'ar', _('Arabic')


MESSAGE_FIELD_SCHEMA = {
    "description": "Dynamic values should be described as `{name}`\nExample en:Your OTP code is {code}",
    'type': openapi.TYPE_OBJECT,
    'properties': {lang[0]: {'type': openapi.TYPE_STRING} for lang in Language.choices},
    'required': [lang[0] for lang in Language.choices]
}

CALCULATED_VALUES = ['$customer.full_name', '$customer.email', '$customer.phone', '$group.name']

KWARGS_FIELD_SCHEMA = {
    "description": """This object format "code":"1234"  for calculated values use `$` as prefix 
     ex: `"name" : "$customer.full_name"`
     currently supported calculated values are `{0}`""".format("`,`".join(CALCULATED_VALUES)),
    'type': openapi.TYPE_OBJECT,
    'additionalProperties': {'type': openapi.TYPE_STRING}
}


class Message(TimeStampedModel):
    text = models.JSONField()

    def clean(self):
        JSONSchemaValidator(MESSAGE_FIELD_SCHEMA)(self.text)

    def save(self, *args, **kwargs):
        self.clean()
        return super(Message, self).save(*args, **kwargs)


class Notification(TimeStampedModel):
    class Type(models.TextChoices):
        PUSH = 'push', _('Push')
        SMS = 'sms', _('SMS')

    type = models.CharField(max_length=4, choices=Type.choices)
    message = models.ForeignKey('Message', null=True, on_delete=models.CASCADE)
    kwargs = models.JSONField()
    customer = models.ForeignKey('Customer', null=True, blank=True, on_delete=models.CASCADE)
    group = models.ForeignKey('Group', null=True, blank=True, on_delete=models.CASCADE)

    def clean(self):
        JSONSchemaValidator(KWARGS_FIELD_SCHEMA)(self.kwargs)

    def save(self, *args, **kwargs):
        self.clean()
        return super(Notification, self).save(*args, **kwargs)


class Customer(TimeStampedModel):
    language = models.CharField(max_length=2, choices=Language.choices, default=Language.EN)
    full_name = models.CharField(max_length=70)
    phone = models.CharField(max_length=20)
    email = models.EmailField()


class Group(TimeStampedModel):
    name = models.CharField(max_length=127)
    customers = models.ManyToManyField('Customer', related_name='groups')


class Device(TimeStampedModel):
    class Type(models.TextChoices):
        IOS = 'ios', _('iOS')
        ANDROID = 'android', _('Android')
        WEB = 'web', _('Web')

    type = models.CharField(max_length=7, choices=Type.choices)
    push_id = models.CharField(max_length=255)
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE, related_name='devices')
    version = models.CharField(max_length=31, null=True, blank=True)
    app_version = models.CharField(max_length=31, null=True, blank=True)
