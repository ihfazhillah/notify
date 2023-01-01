from rest_framework import serializers

from notify.feed.models import Item, Tag, MyProposal
from notify.feed.util import parse_upwork_feed


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["title", "url", "pk"]


class ItemSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)
    budget = serializers.SerializerMethodField()
    hourly_range = serializers.SerializerMethodField()
    proposal_example_text = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    category = serializers.SerializerMethodField()
    country = serializers.SerializerMethodField()
    skills = serializers.SerializerMethodField()

    class Meta:
        model = Item
        fields = [
            "pk",
            "guid",
            "title",
            "published",
            "tags",
            "description",
            "budget",
            "hourly_range",
            "category",
            "country",
            "skills",
            "proposal_example_text"
        ]

    def get_budget(self, obj):
        return obj.budget

    def get_hourly_range(self, obj):
        if not obj.hourly_range:
            return
        return [obj.hourly_range.lower, obj.hourly_range.upper]

    def get_description(self, obj):
        return obj.description

    def get_category(self, obj):
        return obj.category

    def get_country(self, obj):
        return obj.country

    def get_skills(self, obj):
        return obj.skills

    def get_proposal_example_text(self, obj):
        return obj.proposal_example_text


class SimpleItemSerializer(serializers.ModelSerializer):
    budget = serializers.SerializerMethodField()
    hourly_range = serializers.SerializerMethodField()
    accessed = serializers.SerializerMethodField()

    class Meta:
        model = Item
        fields = (
            "pk",
            "title",
            "budget",
            "hourly_range",
            "accessed",
            "published"
        )

    def get_budget(self, obj):
        return obj.budget

    def get_hourly_range(self, obj):
        if not obj.hourly_range:
            return
        return [obj.hourly_range.lower, obj.hourly_range.upper]

    def get_accessed(self, obj):
        return obj.accessed


class MyProposalSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyProposal
        fields = (
            "pk",
            "text"
        )


class MyProposalBodySerializer(serializers.ModelSerializer):
    class Meta:
        model = MyProposal
        fields = ("text",)
