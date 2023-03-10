# Generated by Django 4.0.8 on 2023-01-17 23:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_alter_event_options'),
        ('attendance', '0003_attendance_attendees'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='eventId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='event_attendance', to='event.event'),
        ),
    ]
