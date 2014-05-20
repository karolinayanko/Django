from django import forms as forms


class RegistrationForm(forms.Form):
    email = forms.CharField(label=(u'E-mail'), max_length = 50)
    username = forms.CharField(label=(u'Username'), max_length = 30)
    password = forms.CharField(label=(u'Password'), max_length = 50)
    fields = ["username", "password", "email"]