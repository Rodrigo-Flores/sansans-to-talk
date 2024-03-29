# Generated by Django 3.2.8 on 2021-11-16 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Event', '0011_remove_userprofile_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='email',
            field=models.EmailField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='first_name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='last_name',
            field=models.CharField(default='', max_length=100),
        ),
    ]
