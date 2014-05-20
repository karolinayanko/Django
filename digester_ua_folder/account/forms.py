# -*- coding: utf-8 -*-
from django import forms as forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50, label=(u'Password'), widget=forms.PasswordInput)

    def clean_username(self):
        try:
            user = User.objects.get(username=self.cleaned_data['username'])
        except User.DoesNotExist:
            raise forms.ValidationError("User does not exist")
        return user

    def clean_password(self):
        user = self.cleaned_data['username'] # User object
        password = self.cleaned_data['password'] # String

        if user.check_password(password):
            return password
        else:
            raise forms.ValidationError("Wrong password")


class ChangePasswordForm(forms.Form):

    def __init__(self, user=None, *args, **kwargs):
        self.user = user
        super(ChangePasswordForm, self).__init__(*args, **kwargs)

    oldpassword = forms.CharField(label=("Current Password"))
    password1 = forms.CharField(label=("New Password"))
    password2 = forms.CharField(label=("New Password (again)"))

    def get_user(self ,user):
        user = User.get_username()
        return user

    def clean_oldpassword(self):
        if not self.user.check_password(self.cleaned_data.get("oldpassword")):
            raise forms.ValidationError("Please type your current password.")

        return self.cleaned_data["oldpassword"]

    def clean_password2(self):
        if self.cleaned_data["password1"] != self.cleaned_data["password2"]:
            raise forms.ValidationError("You must type the same password each time.")

        return self.cleaned_data["password2"]


class EmailForm(forms.Form):
    email = forms.EmailField(label=(u'E-mail'), max_length = 50)


