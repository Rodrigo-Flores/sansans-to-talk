# Generated by Django 3.2.8 on 2021-11-12 17:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Event', '0002_attendance_profile'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Profile',
            new_name='Profiles',
        ),
    ]