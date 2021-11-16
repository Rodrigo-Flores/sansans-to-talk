# Generated by Django 3.2.8 on 2021-11-12 02:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Event', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('profile_id', models.AutoField(primary_key=True, serialize=False)),
                ('profile_name', models.CharField(max_length=100)),
                ('profile_email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('attendance_id', models.AutoField(primary_key=True, serialize=False)),
                ('attendance_date', models.DateTimeField(auto_now_add=True)),
                ('attendance_status', models.BooleanField(default=True)),
                ('attendance_event_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Event.events')),
                ('attendance_profile_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Event.profile')),
            ],
        ),
    ]