from django.contrib.auth.models import models
from django import forms as forms
from django.contrib.auth import authenticate, login, logout


class User(models.Model):
    email = models.TextField(max_length=50)
    username = models.TextField(max_length=30)
    password = models.TextField(max_length=50)
    date_joined = models.DateTimeField(auto_now_add=True)