from django.db.models.signals import post_save
from django.dispatch import receiver
from notifications.tasks import send_push, send_sms

from notifications.models import Notification


@receiver(post_save, sender=Notification)
def process_notification_after_created(sender, instance: Notification, created, **kwargs):
    if created:
        if instance.type == Notification.Type.PUSH:
            send_push.delay(instance.id)
        else:
            send_sms.delay(instance.id)
