# Generated by Django 3.2.6 on 2021-08-09 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form_resto', '0003_auto_20210809_0643'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='request',
            name='maximum_distance',
        ),
        migrations.AddField(
            model_name='request',
            name='distance',
            field=models.IntegerField(default=1, help_text='in Km'),
        ),
    ]
