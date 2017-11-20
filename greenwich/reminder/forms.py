from django.forms import ModelForm
from django import forms
from index.models import User
from reminder.models import Event

class DateInput(forms.DateInput):
    input_type = 'date'

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = [
            'event_name',
            'recurring',
            'message',
            'start_date',
            'end_date',
            'interval',
            'interval_type',
            'warning',
            'warning_interval',
            'warning_interval_type',
            'date_type'
        ]

        widgets = {
            'event_name': forms.TextInput(),
            'recurring': forms.NullBooleanSelect(),
            'message': forms.TextInput(),
            'start_date': DateInput(),
            'end_date': DateInput(),
            'interval': forms.NumberInput(),
            'warning': forms.NullBooleanSelect(),
            'warning_interval': forms.NumberInput(),
            'date_type': forms.TextInput()
        }

