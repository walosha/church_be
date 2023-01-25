# Generated by Django 4.0.8 on 2023-01-25 09:39

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('siteinfo', '0008_remove_siteinfo_audio1'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteinfo',
            name='audio1',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True),
        ),
    ]
