# Create your views here.
#-*-coding:utf-8-*-
import os, codecs, time
MODULE_ROOT = os.path.normpath(os.path.dirname(__file__))
from django.http import HttpResponse, HttpResponseNotFound
from mods.CheckanimeLastadded import extract_data_to_html
from django.template.loader import get_template
from django.template import Template, Context
from django.contrib.auth.models import User
import datetime
def test_two(request):
    #res = '<h1>Page was found</h1>'
    #res += '<h2>This is my test page - second view outside views.py</h2>'
    #now = datetime.datetime.now()
    #opening files -> reading -> clearing data
    anime_file_name = os.path.join(MODULE_ROOT, 'mods', 'anime_url.txt')
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