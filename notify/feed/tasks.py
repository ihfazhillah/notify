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
                    "content": item.content,
                    "published": str(item.published),
                    "guid": item.guid,
                    "tags": [tag.title for tag in item.tags.all()]
                },
                topic="job alert",
                notification=Notification(
                    title=item.title, body=f"New job alert: {item.title}"
                )
            )
            for item in new_items
        ]

        for message in messages:
            FCMDevice.objects.all().send_message(message)
