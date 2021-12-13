from django.contrib import admin
from .models import Events, UserProfile, Attendance

admin.site.register(Events)
admin.site.register(UserProfile)
admin.site.register(Attendance)

