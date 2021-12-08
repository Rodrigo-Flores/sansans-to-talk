from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import widgets
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
    #? is this really necessary?
    # first_name = forms.CharField(max_length=100, required=True)
    # last_name = forms.CharField(max_length=100, required=True)
    # email = forms.EmailField(required=True)
    # password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    # password2 = forms.CharField(label='Password Confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name','email', 'password1', 'password2']
        help_texts = {i : '' for i in fields}
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'AmadeusTheGreat'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Amadeus'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Mozart'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'amadeus.mozart@example.com'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password Confirmation'}),
        }
        error_messages = {
            'password_mismatch': "The two password fields didn't match.",
        }


class AttendanceForm(forms.Form):
    event_id = forms.IntegerField(widget=forms.HiddenInput())
    user_id = forms.IntegerField(widget=forms.HiddenInput())
    attendance = forms.BooleanField(required=False)
    attendance_time = forms.TimeField(widget=forms.HiddenInput())
    attendance_date = forms.DateField(widget=forms.HiddenInput())
    class Meta:
        fields = ['event_id', 'user_id', 'attendance', 'attendance_time', 'attendance_date']
        help_texts = {i : '' for i in fields}
        widgets = {
            'event_id': forms.HiddenInput(),
            'user_id': forms.HiddenInput(),
            'attendance': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'attendance_time': forms.HiddenInput(),
            'attendance_date': forms.HiddenInput(),
        } 