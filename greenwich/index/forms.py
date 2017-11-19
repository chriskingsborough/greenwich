from django.forms import ModelForm
from django import forms
from index.models import User

class DateInput(forms.DateInput):
    input_type = 'date'

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'first_name',
            'last_name',
            'email',
            'phonenumber',
            'datebirth',
            'gender'
        ]
        widgets = {
            'password': forms.PasswordInput(),
            'datebirth': DateInput(),
            'email': forms.EmailInput()
        }
