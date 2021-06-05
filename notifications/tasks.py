from celery import shared_task, Task

from notifications.models import Notification


class BaseTaskWithRetry(Task):
    autoretry_for = (Exception, KeyError)
    retry_kwargs = {'max_retries': 3, 'countdown': 5}
    retry_backoff = True


@shared_task(base=BaseTaskWithRetry)
def send_sms(notification_id):
    print('send sms')
    # optimized fetch from database
    notification = Notification.objects.select_related('customer', 'group', 'message').prefetch_related(
        'group__customers').get(pk=notification_id)

    return {'status': 'ok'}


@shared_task(base=BaseTaskWithRetry)
def send_push(notification_id):
    print('send push')
    # optimized fetch from database
    notification = Notification.objects.select_related('customer', 'group', 'message').prefetch_related(
        'group__customers', 'group__customers__devices', 'customer__devices').get(pk=notification_id)

    if notification.customer:
        customer_msg = notification.message.text[notification.customer.language].format(**notification.kwargs)
    return {'status': 'ok'}
