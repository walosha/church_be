# Generated by Django 4.0.8 on 2023-01-25 09:16

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('siteinfo', '0005_alter_siteinfo_audio1_alter_siteinfo_audio2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siteinfo',
            name='image1',
            field=cloudinary.models.CloudinaryField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='siteinfo',
            name='image2',
            field=cloudinary.models.CloudinaryField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='siteinfo',
            name='image3',
            field=cloudinary.models.CloudinaryField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='siteinfo',
            name='image4',
            field=cloudinary.models.CloudinaryField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='siteinfo',
            name='image5',
            field=cloudinary.models.CloudinaryField(blank=True, default=None, max_length=255, null=True),
        ),
    ]