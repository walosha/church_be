# Generated by Django 4.0.8 on 2023-01-21 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteinfo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siteinfo',
            name='audio1',
            field=models.FileField(blank=True, null=True, upload_to='audio/'),
        ),
        migrations.AlterField(
            model_name='siteinfo',
            name='audio2',
            field=models.FileField(blank=True, null=True, upload_to='audio/'),
        ),
        migrations.AlterField(
            model_name='siteinfo',
            name='audio3',
            field=models.FileField(blank=True, null=True, upload_to='audio/'),
        ),
        migrations.AlterField(
            model_name='siteinfo',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='site/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='siteinfo',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to='site/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='siteinfo',
            name='image4',
            field=models.ImageField(blank=True, null=True, upload_to='site/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='siteinfo',
            name='image5',
            field=models.ImageField(blank=True, null=True, upload_to='site/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='siteinfo',
            name='video1',
            field=models.FileField(blank=True, null=True, upload_to='videos/'),
        ),
        migrations.AlterField(
            model_name='siteinfo',
            name='video2',
            field=models.FileField(blank=True, null=True, upload_to='videos/'),
        ),
        migrations.AlterField(
            model_name='siteinfo',
            name='video3',
            field=models.FileField(blank=True, null=True, upload_to='videos/'),
        ),
    ]
