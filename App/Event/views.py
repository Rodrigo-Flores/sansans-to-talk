from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Events, Attendance
from .forms import EventForm, UserRegistrationForm, AttendanceForm

def Home(request):
    events = Events.objects.all()

    return render(request, 'index.html', {'events':events})

#! Events views
@login_required
def EventList(request):
    current_user = request.GET.get('user')
    events = Events.objects.all()
    context = {
        'events':events,
        'current_user':current_user
    }

    return render(request, 'objects/event_list.html', context)

@login_required
def EventCreate(request):
    if request.method == 'GET':
        form = EventForm()

    elif request.method == 'POST':
        form = EventForm(request.POST)

    if form.is_valid():
        form.save()

        return redirect('event_list')

    return render(request, 'objects/manage_event.html', {'form':form})

@login_required
def EventDelete(request, event_id=None):
    events = Events.objects.get(event_id=event_id)

    if request.method == 'GET':
        return render(request, 'objects/delete_confirmation.html', {'events':events})

    elif request.method == 'POST':
        events.delete()
        return redirect('event_list')
    
    # return render(request, 'objects/delete_confirmation.html')

@login_required
def EventUpdate(request, event_id):
    events = Events.objects.get(event_id=event_id)

    if request.method == 'GET':
        form = EventForm(instance=events)

    elif request.method == 'POST':
        form = EventForm(request.POST, instance=events)
        if form.is_valid():
            form.save()

            return redirect('event_list')

    return render(request, 'objects/manage_event.html', {'form':form})

def EventDetail(request, event_id):
    events = Events.objects.get(event_id=event_id)
    context = {
        'events':events
    }
    return render(request, 'objects/event_detail.html', context)

#! User profile views
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'User created successfully')
            return redirect('login')
            
    else:
        form = UserRegistrationForm()

    return render(request, 'social/register.html', {'form':form})

@login_required
def profile(request, username=None):
    events = Events.objects.all()
    current_user = request.user
    if username and username != current_user.username:
        user = User.objects.get(username=username)
    else:
        user = current_user
    return render(request, 'social/profile.html', {'user':user, 'events':events})

#! Attendance views
@login_required
def AttendEvent(request, event_id):
    # events = Events.objects.get(event_id=event_id)
    events = Events.objects.get(event_id=event_id)
    if request.method == 'POST':
        event = request.POST['event_id']
        user = request.user
        value = request.POST['value']

        if value == 'attend':
            attendance = Attendance(event=event, user=user) # Create a new attendance without data
            try:
                attendance.save()
            except:
                return redirect('event_list')

        return render(request, 'objects/event_detail.html', {'events':events})

    elif request.method == 'GET':
        return render(request, 'objects/attendance_confirmation.html', {'events':events})

    return render(request, 'objects/attendance_confirmation.html', {'events':events})
