import openai
from django.conf import settings

from notify.feed.models import Item
from notify.prompt.models import ProposalPrompt
from notify.users.models import User

default_prompt = f"write a job proposal for upwork, highlight curiosity and interest for that job, ask question to " \
                 f"imcrease engagement rate between us, highlight past experience and portofolio links, then the CTA " \
                 f"in the last. for this job post description:\n "


def generate_proposal(item_id: int, user_id: int) -> str:
    openai.api_key = settings.OPENAI_API_KEY

    item = Item.objects.get(pk=item_id)

    user = User.objects.get(pk=user_id)
    prompt = ProposalPrompt.objects.filter(
        user=user,
        selected=True
    ).first()
    if prompt:
        prompt = prompt.text
    else:
        prompt = default_prompt

    prompt += item.upwork.description

    max_tokens = 4097 - (len(prompt) + 3)

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=max_tokens,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    return response.choices[0].text
