from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.urls import reverse_lazy
from .models import Events
from .form_event import EventForm

class EventList(ListView):
    model = Events
    template_name = 'index.html'

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