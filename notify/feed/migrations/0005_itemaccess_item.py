# Generated by Django 4.0.8 on 2022-12-17 17:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0004_itemaccess'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemaccess',
            name='item',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='feed.item'),
            preserve_default=False,
        ),
    ]