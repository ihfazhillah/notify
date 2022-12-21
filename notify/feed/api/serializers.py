from rest_framework import serializers

from notify.feed.models import Item, Tag
from notify.feed.util import parse_upwork_feed


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["title", "url", "pk"]


class ItemSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)
    class Meta:
        model = Item
        fields = [
            "pk",
            "guid",
            "content",
            "title",
            "published",
            "tags",
            "accessed",
            "parsed_item"
        ]

    accessed = serializers.SerializerMethodField()
    def get_accessed(self, obj):
        return obj.accessed

    parsed_item = serializers.SerializerMethodField()
    def get_parsed_item(self, obj):
        return parse_upwork_feed(obj.content)
