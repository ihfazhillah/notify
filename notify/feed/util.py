import datetime

from notify.feed.models import Tag, Item
import feedparser


def parse(tag: Tag):
    """
    :param tag: Tag object
    :return: new entries list. If nothing, just response an empty list
    """

    resp = feedparser.parse(tag.url)
    resp.entries.reverse()

    new_entries = []

    for entry in resp.entries:
        item, created = Item.objects.get_or_create(
            guid=entry.guid,
            defaults={
                "title": entry.title,
                "content": entry.summary,
                "published": datetime.datetime(*entry.published_parsed[:7])
            }
        )

        if not item.tags.filter(pk=tag.id).exists():
            item.tags.add(tag)

        if created:
            new_entries.append(item)

    return new_entries
