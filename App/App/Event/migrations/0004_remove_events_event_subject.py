# Generated by Django 3.2.8 on 2021-11-12 18:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Event', '0003_rename_profile_profiles'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='events',
            name='event_subject',
        ),
    ]
