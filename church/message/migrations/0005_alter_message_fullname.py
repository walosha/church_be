# Generated by Django 4.0.8 on 2023-01-21 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0004_alter_message_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='fullname',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
