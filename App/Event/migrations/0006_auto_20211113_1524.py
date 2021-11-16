# Generated by Django 3.2.7 on 2021-11-13 18:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Event', '0005_profiles_profile_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profiles',
            name='profile_email',
        ),
        migrations.RemoveField(
            model_name='profiles',
            name='profile_name',
        ),
        migrations.RemoveField(
            model_name='profiles',
            name='profile_password',
        ),
        migrations.AddField(
            model_name='profiles',
            name='profile_github',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='profiles',
            name='user',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
