# Generated by Django 4.0.8 on 2023-01-23 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0004_event_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='end_at',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_at',
            field=models.DateTimeField(),
        ),
    ]
