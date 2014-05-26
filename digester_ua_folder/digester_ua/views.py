# Create your views here.
import os, codecs, time
MODULE_ROOT = os.path.normpath(os.path.dirname(__file__))
from django.http import HttpResponse, HttpResponseNotFound
from mods.CheckanimeLastadded import extract_raw_data_to_template
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

def home(request):
    res = '<h1>Page was found</h1>'
    res += '<h2>This is my first page</h2>'
    return HttpResponse(res)

def test(request):
    res = '<h1>Page was found</h1>'
    res += '<h2>This is my test page - second view in views.py</h2>'
    return HttpResponse(res)

class Profile_data(View):

    # @render_to("profile_data.html")
    # def get(self, request):
        # form = EmailForm()
        # return {'form': form}
    # def __init__(self, request):
        # pass
    
    @render_to("profile_data.html")
    def get(self, request):
        # form = EmailForm(request.POST.copy())
        user = request.user
        if user.is_authenticated():
            # anime_file_name = os.path.join(MODULE_ROOT, 'mods', 'anime_url.txt')
            temp_file_name = os.path.join(MODULE_ROOT, 'mods', 'temp.tmp')
            # f = open(anime_file_name)
            links = []
            # links = f.readlines()
            # f.close()
            ud = User_data
            users_available = ud.objects.filter(username=user)
            if users_available:
                for obj in ud.objects.filter(username=user):
                    links.append(obj.url)
            else:
                return {'all_data': {'-':['user data is empty for now']}}
            # print links
            ##########################################################
            #contains data with previous latest extracted series
            last_out_string = ''
            with codecs.open(temp_file_name) as los:
                for item in los:
                    last_out_string+=item
            #start extracting
            res = extract_raw_data_to_template(links, last_out_string)
            # # t = get_template('index.html')
            # # html = t.render(Context({'content': '123'}))
            # # res = '<h2>test res</h2>'
            # ht = get_template('profile_data.html')#Template('{% extends "index.html" %}{% block content %}'+res+'{% endblock %}')
            # html = ht.render(Context({'data_content': res}))
            return {'all_data': res}#HttpResponse(html)
            # if form.is_valid():
                # data = request.user.email = request.POST['email']
                # request.user.save()
                # return {'form': form}
        else:
            return {'all_data': ''}
