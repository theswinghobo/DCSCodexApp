# Generated by Django 3.0.2 on 2020-02-23 07:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DCSCodexAdmin', '0007_auto_20200223_1507'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='group',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='DCSCodexAdmin.Group'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(related_name='users', to='DCSCodexAdmin.Group'),
        ),
    ]
