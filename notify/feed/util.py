import datetime
import html
import re

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


def parse_upwork_feed(raw):
    # change br to new lines
    result = {}

    raw = raw.replace("<br />", "\n").replace("\n\n", "\n")
    raw = html.unescape(raw)
    key_val_pattern = re.compile("((<b>(?P<key>.*?)</b>):(?P<value>.*?\n))")

    starts = []
    for match in re.finditer(key_val_pattern, raw):
        starts.append(match.start())

        group = match.groupdict()
        result[group['key'].lower().replace(" ", "_")] = group["value"].strip()

    min_start = min(starts)
    result["description"] = raw[:min_start].strip().replace("\n\n", "\n")

    return result
