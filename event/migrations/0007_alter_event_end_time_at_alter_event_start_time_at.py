# Generated by Django 4.0.8 on 2023-01-23 20:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0006_remove_event_end_at_remove_event_start_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='end_time_at',
            field=models.TimeField(default=datetime.time(0, 0)),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_time_at',
            field=models.TimeField(default=datetime.time(0, 0)),
        ),
    ]
