# Generated by Django 3.2.7 on 2021-11-16 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Event', '0008_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
