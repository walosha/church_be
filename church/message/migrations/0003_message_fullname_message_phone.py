# Generated by Django 4.0.8 on 2023-01-21 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0002_alter_message_message_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='fullname',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='message',
            name='phone',
            field=models.CharField(blank=True, max_length=11, null=True),
        ),
    ]
