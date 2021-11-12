from django.db import models

class Events(models.Model):
    event_id = models.AutoField(primary_key=True)
    event_name = models.CharField(max_length=100)
    event_subject = models.CharField(max_length=100)
    event_description = models.TextField()
    event_date = models.DateField()
    event_time = models.TimeField()

    __str__ = lambda self: self.event_name

class Profile(models.Model):
    profile_id = models.AutoField(primary_key=True)
    profile_name = models.CharField(max_length=100)
    profile_email = models.EmailField()

    __str__ = lambda self: self.profile_name

class Attendance(models.Model):
    attendance_id = models.AutoField(primary_key=True)
    attendance_event_id = models.ForeignKey(Events, null=False, blank=False, on_delete=models.CASCADE) # WARNING
    attendance_profile_id = models.ForeignKey(Profile, null=False, blank=False, on_delete=models.CASCADE) # WARNING
    attendance_date = models.DateTimeField(auto_now_add=True)
    attendance_status = models.BooleanField(default=True)

    __str__ = lambda self: self.attendance_profile_id