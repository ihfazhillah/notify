from django.contrib.auth import get_user_model
from django.db import models
from model_utils.models import TimeStampedModel


# Create your models here.

class Tag(TimeStampedModel):
    title = models.CharField(max_length=255)

    # we use text field here, because the upwork text need more than 255 length
    url = models.TextField()


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
