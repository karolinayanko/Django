# -*- coding: utf-8 -*-
from django.views.generic import View
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.forms import PasswordResetForm
from django.core.mail import send_mail
from django.contrib.auth.models import User
import random
import string

from digester_ua.utils import render_to
from digester_ua.settings import DEFAULT_FROM_EMAIL
from account.forms import LoginForm
from account.forms import ChangePasswordForm
from account.forms import EmailForm


class Profile(View):

    @render_to("account/profile.jinja")
    def get(self, request):
        form = EmailForm()
        return {'form': form}

    @render_to("account/profile.jinja")
    def post(self, request):
        form = EmailForm(request.POST.copy())
        user = request.user
        if user.is_authenticated():
            if form.is_valid():
                data = request.user.email = request.POST['email']
                request.user.save()
                return {'form': form}
        else:
            return {"redirect": "/account/login"}


class Login(View):

    @render_to("account/login.jinja")
    def get(self, request):
        if request.user.is_authenticated():
            return {"redirect": "/account/profile/"}

        form = LoginForm()
        return {'form': form}

    @render_to("account/login.jinja")
    def post(self, request):
        form = LoginForm(request.POST.copy())

        if form.is_valid():
            data = form.cleaned_data

            user = authenticate(username=data['username'], password=data['password'])
            if user:
                auth_login(request, user)
                return {"redirect": "/account/profile/"}

        return {'form': form}


class Logout(View):

    @render_to(None)
    def get(self, request):
        auth_logout(request)
        return {"redirect": "/account/login/"}


class Passchange(View):

    @render_to("account/password_change.jinja")
    def get(self, request):
        if request.user.is_authenticated():
            form = ChangePasswordForm()
            return {'form': form}

    @render_to("account/password_change.jinja")
    def post(self, request):
        user = request.user
        form = ChangePasswordForm(user, request.POST)
        if form.is_valid():
            user.set_password(form.cleaned_data["password1"])
            user.save()

            return {"redirect": "/account/profile"}

        return {'form': form}


class Recover(View):

    @render_to("account/recover_pass.jinja")
    def get(self, request):
        form = PasswordResetForm()
        return {'form': form}

    def post(self, request):
        form = PasswordResetForm(request.POST.copy())
        subject = 'Password recovery'
        body = 'Hi %s,Your password is: %s. You can change it when loggined in.'
        user = request.user.username
        email = request.POST['email']
        user = User.objects.get(email=email)
        size = 6
        chars = string.ascii_uppercase + string.digits
        password = ''.join(random.choice(chars) for x in range(size))
        user.set_password(password)
        user.save()
        send_mail(subject, body % (user, password), DEFAULT_FROM_EMAIL,
                  [email], fail_silently=False)

        return {'redirect': "/"}
