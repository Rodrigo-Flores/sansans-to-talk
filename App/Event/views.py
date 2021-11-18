from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Events
from .forms import EventForm, UserRegistrationForm

class Home(ListView):
    model = Events
    template_name = 'index.html'

#! Events views
class EventList(ListView):
    model = Events
    template_name = 'event_list.html'

class EventCreate(CreateView):
    model = Events
    form_class = EventForm
    template_name = 'manage_event.html'
    success_url = reverse_lazy('event_list')

class EventDelete(DeleteView):
    model = Events
    template_name = 'delete_confirmation.html'
    success_url = reverse_lazy('event_list')

class EventUpdate(UpdateView):
    model = Events
    form_class = EventForm
    template_name = 'manage_event.html'
    success_url = reverse_lazy('event_list')

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

    return render(request, 'register.html', {'form':form})

def profile(request, username=None):
    current_user = request.user
    if username and username != current_user.username:
        user = User.objects.get(username=username)
    else:
        user = current_user
    return render(request, 'profile.html', {'user':user})