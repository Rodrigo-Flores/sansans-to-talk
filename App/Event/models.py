from django.db import models
from django.contrib.auth.models import User

class Events(models.Model):
    event_id = models.AutoField(primary_key=True)
    event_name = models.CharField(max_length=100)
    event_description = models.TextField()
    event_date = models.DateField()
    event_time = models.TimeField()

    __str__ = lambda self: self.event_name

#! User profile model
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, default='')
    last_name = models.CharField(max_length=100, default='')
    email = models.EmailField(max_length=100, default='')

    __str__ = lambda self: self.user.username

class Attendance(models.Model):
    # event = models.ForeignKey(Events, on_delete=models.CASCADE)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.CharField(max_length=1000)
    user = models.CharField(max_length=1000)

    __str__ = lambda self: self.user.username