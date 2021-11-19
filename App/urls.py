"""App URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from App.Event.views import EventList, EventCreate, EventUpdate, EventDelete, Home, register, profile

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home.as_view(), name='home'), #? Change deafult path to other more user friendly
    
    #! Events urls
    path('events/', EventList.as_view(), name='event_list'), #? work in this path
    path('event_create/', EventCreate.as_view(), name='event_create'),
    path('event_update/<int:pk>/', EventUpdate.as_view(), name='event_update'),
    path('event_delete/<int:pk>/', EventDelete.as_view(), name='event_delete'),

    #! User profile urls
    path('register/', register, name='register'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('/', LogoutView.as_view(template_name='index.html'), name='logout'),
    path('profile/<str:username>', profile, name='profile'),
]
