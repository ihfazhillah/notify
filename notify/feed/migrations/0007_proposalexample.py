# Generated by Django 4.0.8 on 2022-12-21 15:14

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0006_upworkitemcategory_upworkskill_upworkitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProposalExample',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('text', models.TextField()),
                ('item', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='proposal_example', to='feed.item')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
