from fcm_django.models import FCMDevice
from firebase_admin.messaging import Message, Notification

from config import celery_app
from notify.feed.models import Tag
from notify.feed.util import parse




@celery_app.task()
def parse_feeds():
    """For now, parse all feeds"""
    for tag in Tag.objects.all():
        new_items = parse(tag)

        # just send message to all users
        messages = [
            Message(
                data={
                    "title": item.title,
                    "guid": item.guid,
                    "tags": ", ".join([tag.title for tag in item.tags.all()]),
                    "id": item.pk
                }
            )
            for item in new_items
        ]

        for message in messages:
            FCMDevice.objects.all().send_message(message)
