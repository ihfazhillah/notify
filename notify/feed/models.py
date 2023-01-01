from django.contrib.auth import get_user_model
from django.contrib.postgres.fields import RangeField, IntegerRangeField, DecimalRangeField
from django.db import models
from model_utils.models import TimeStampedModel


# Create your models here.

class Tag(TimeStampedModel):
    title = models.CharField(max_length=255)

    # we use text field here, because the upwork text need more than 255 length
    url = models.TextField()

    def __str__(self):
        return self.title


class Item(TimeStampedModel):
    tags = models.ManyToManyField(Tag, related_name="items")
    guid = models.TextField()
    content = models.TextField()
    title = models.CharField(max_length=255)
    published = models.DateTimeField(null=True)

    def __str__(self):
        return self.title


class ItemAccess(TimeStampedModel):
    """
    Used to track if user already open the item or not.
    """
    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE
    )
    item = models.ForeignKey(
        Item, on_delete=models.CASCADE
    )


class UpworkSkill(TimeStampedModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class UpworkItemCategory(TimeStampedModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class UpworkItem(TimeStampedModel):
    item = models.OneToOneField(Item, related_name="upwork", on_delete=models.CASCADE)
    description = models.TextField()
    budget = models.IntegerField(null=True, blank=True)
    hourly_range = DecimalRangeField(null=True, blank=True)
    posted_on = models.DateTimeField(blank=True, null=True)
    category = models.ForeignKey(UpworkItemCategory, on_delete=models.CASCADE, related_name="items")
    country = models.CharField(max_length=255, blank=True, null=True)
    skills = models.ManyToManyField(UpworkSkill)


class ProposalExample(TimeStampedModel):
    text = models.TextField()
    item = models.OneToOneField(Item, related_name="proposal_example", on_delete=models.CASCADE)


class MyProposal(TimeStampedModel):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    text = models.TextField()
