# Generated by Django 3.2.8 on 2021-11-11 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('event_id', models.AutoField(primary_key=True, serialize=False)),
                ('event_name', models.CharField(max_length=100)),
                ('event_subject', models.CharField(max_length=100)),
                ('event_description', models.TextField()),
                ('event_date', models.DateField()),
                ('event_time', models.TimeField()),
            ],
        ),
    ]