# Generated by Django 4.0.8 on 2023-01-01 05:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0009_myproposal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myproposal',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feed.item'),
        ),
    ]
