# Generated by Django 4.0.8 on 2022-12-31 13:56

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('prompt', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GeneralPrompt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('prompt_type', models.CharField(max_length=255, unique=True)),
                ('text', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
