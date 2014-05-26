#-*-coding:utf-8-*-
import os, codecs, time
MODULE_ROOT = os.path.normpath(os.path.dirname(__file__))
from django.http import HttpResponse, HttpResponseNotFound
from mods.CheckanimeLastadded import extract_data_to_html
from django.template.loader import get_template
from django.template import Template, Context
import datetime
from django.views.generic import View
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.forms import PasswordResetForm
from django.core.mail import send_mail
from django.contrib.auth.models import User
from account.models import User_data

from digester_ua.utils import render_to
from digester_ua.settings import DEFAULT_FROM_EMAIL
from account.forms import LoginForm
from account.forms import ChangePasswordForm
from account.forms import EmailForm

class Profile_data(View):

    @render_to("profile_data.html")
    def get(self, request):
        form = EmailForm()
        return {'form': form}

    @render_to("profile_data.html")
    def post(self, request):
        # form = EmailForm(request.POST.copy())
        user = request.user
        if user.is_authenticated():
            # anime_file_name = os.path.join(MODULE_ROOT, 'mods', 'anime_url.txt')
            temp_file_name = os.path.join(MODULE_ROOT, 'mods', 'temp.tmp')
            f = open(anime_file_name)
            links = []
            links = f.readlines()
            f.close()
            #contains data with previous latest extracted series
            last_out_string = ''
            with codecs.open(temp_file_name) as los:
                for item in los:
                    last_out_string+=item
            #start extracting
            res = extract_data_to_html(links, last_out_string)
            # t = get_template('index.html')
            # html = t.render(Context({'content': '123'}))
            # res = '<h2>test res</h2>'
            ht = Template('{% extends "index.html" %}{% block content %}'+res+'{% endblock %}')
            html = ht.render(Context({'content': res}))
            return HttpResponse(html)
            # if form.is_valid():
                # data = request.user.email = request.POST['email']
                # request.user.save()
                # return {'form': form}
        else:
            return {"redirect": "/account/login"}

# def test_two(request):
    # #res = '<h1>Page was found</h1>'
    # #res += '<h2>This is my test page - second view outside views.py</h2>'
    # #now = datetime.datetime.now()
    # #opening files -> reading -> clearing data
    # anime_file_name = os.path.join(MODULE_ROOT, 'mods', 'anime_url.txt')
    # temp_file_name = os.path.join(MODULE_ROOT, 'mods', 'temp.tmp')
    # f = open(anime_file_name)
    # links = []
    # links = f.readlines()
    # f.close()
    # #contains data with previous latest extracted series
    # last_out_string = ''
    # with codecs.open(temp_file_name) as los:
        # for item in los:
            # last_out_string+=item
    # #start extracting
    # res = extract_data_to_html(links, last_out_string)
    # # t = get_template('index.html')
    # # html = t.render(Context({'content': '123'}))
    # # res = '<h2>test res</h2>'
    # ht = Template('{% extends "index.html" %}{% block content %}'+res+'{% endblock %}')
    # html = ht.render(Context({'content': res}))
    # return HttpResponse(html)