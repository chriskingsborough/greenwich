from django import forms

class RegistrationForm(forms.Form):

    username = forms.CharField(label='username', max_length=100)
    first_name = forms.CharField(label='first_name', max_length=100)
    last_name = forms.CharField(label='last_name', max_length=100)
    phone_number = forms.CharField(label='phone_number', max_length=15)
    email = forms.CharField(label='email', max_length=100)
    password = forms.CharField(label='password', max_length=None)