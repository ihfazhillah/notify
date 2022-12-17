from rest_framework import serializers

from notify.feed.models import Item, Tag


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
            "accessed"
        ]

    accessed = serializers.SerializerMethodField()
    def get_accessed(self, obj):
        return obj.accessed
