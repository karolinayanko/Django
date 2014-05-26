from django.contrib.auth.models import models
from django import forms as forms
from django.contrib.auth import authenticate, login, logout


class User_data(models.Model):
    username = models.TextField(max_length=30)
    url = models.TextField(max_length=150)
    text = models.TextField(max_length=50)