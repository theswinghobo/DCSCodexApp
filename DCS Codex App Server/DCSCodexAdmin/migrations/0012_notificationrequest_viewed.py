# Generated by Django 3.0.2 on 2020-03-12 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DCSCodexAdmin', '0011_notificationrequest'),
    ]

    operations = [
        migrations.AddField(
            model_name='notificationrequest',
            name='viewed',
            field=models.BooleanField(default=False),
        ),
    ]
