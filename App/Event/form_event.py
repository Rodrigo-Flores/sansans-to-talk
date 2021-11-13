from django import forms
from .models import Events

class EventForm(forms.ModelForm):
    class Meta:
        model = Events

        widgets = {
            'event_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Event Name'}),
            'event_description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Event Description'}),
            'event_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'MM/DD/YYYY'}),
            'event_time': forms.TimeInput(attrs={'class': 'form-control', 'placeholder': 'HH/MM'},),
        }

        fields = '__all__'