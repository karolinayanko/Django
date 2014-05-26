# -*- coding: utf-8 -*-
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import View

from digester_ua.utils import render_to


class Register(View):

    @render_to("registration/registration_form.html")
    def get(self, request):
        form = UserCreationForm()
        return {'form': form}

    @render_to("registration/registration_form.html")
    def post(self, request):
        form = UserCreationForm(request.POST.copy())

        if form.is_valid():
            form.save()

            return {"redirect": "/account/login"}

        return {'form' : form}