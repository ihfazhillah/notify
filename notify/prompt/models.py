from django.db import models
from model_utils.models import TimeStampedModel

from notify.users.models import User


class ProposalPrompt(TimeStampedModel):
    text = models.TextField()
    label = models.CharField(max_length=255)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    # Per user only one that active
    selected = models.BooleanField(default=False)

    def __str__(self):
        return self.label


class GeneralPrompt(TimeStampedModel):
    """
    Used for general prompt. the type should unique.
    """
    prompt_type = models.CharField(max_length=255, unique=True)
    text = models.TextField()

    def __str__(self):
        return self.prompt_type
