import datetime

from fcm_django.models import FCMDevice
from firebase_admin.messaging import Message, Notification

from config import celery_app
from notify.feed.models import Tag, UpworkItemCategory, UpworkSkill, UpworkItem
from notify.feed.util import parse, parse_upwork_feed


@celery_app.task()
def notify_firebase(new_items):
    messages = [
        Message(
            data={
                "title": item.title,
                "guid": item.guid,
                "tags": ", ".join([tag.title for tag in item.tags.all()]),
                "id": str(item.pk)
            }
        )
        for item in new_items
    ]

    for message in messages:
        FCMDevice.objects.all().send_message(message)


@celery_app.task()
def parse_items(new_items):
    for item in new_items:
        parsed = parse_upwork_feed(item.content)

        category, _ = UpworkItemCategory.objects.get_or_create(
            name=parsed.get("category", "Unknown")
        )

        skills = [item[0] for item in [
            UpworkSkill.objects.get_or_create(name=skill)
            for skill in parsed.get("skills", [])
        ]]

        budget = parsed.get("budget")
        if budget:
            budget = budget.replace("$", "").replace(",", "")
            budget = int(budget)

        hourly_range = parsed.get("hourly_range")
        if hourly_range:
            hourly_range = [
                float(item.replace("$", ""))
                for item in
                hourly_range.split("-")
            ]

        posted_on = parsed.get("posted_on")
        fmt = "%B %d, %Y %H:%M %Z"
        posted_on_parsed = datetime.datetime.strptime(posted_on, fmt)

        instance = UpworkItem.objects.create(
            item=item,
            description=parsed.get('description'),
            budget=budget,
            hourly_range=hourly_range,
            posted_on=posted_on_parsed,
            category=category,
            country=parsed.get("country")
        )

        instance.skills.add(*skills)


@celery_app.task()
def parse_tags():
    """For now, parse all feeds"""
    new_items = []
    for tag in Tag.objects.all():
        new_items += parse(tag)

    return new_items


@celery_app.task()
def parse_feeds():
    parsing = parse_tags.s()
    parsing.link(notify_firebase.s())
    parsing.link(parse_items.s())
    parsing.delay()

