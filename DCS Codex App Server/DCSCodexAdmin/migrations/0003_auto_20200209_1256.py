# Generated by Django 3.0.2 on 2020-02-09 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DCSCodexAdmin', '0002_group_users'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='users',
        ),
        migrations.AlterField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(related_name='users', to='DCSCodexAdmin.Group'),
        ),
    ]