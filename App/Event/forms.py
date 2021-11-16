from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
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

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password Confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username','email', 'password1', 'password2']
        help_texts = {i : "" for i in fields}