# -*- coding: utf-8 -8-
from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login, logout

from account import views as login_views



urlpatterns = patterns('',
                       (r'^login/$',  login_views.Login.as_view()),
                       (r'^logout/$', login_views.Logout.as_view()),
                       (r'^profile/', login_views.Profile.as_view()),
                       (r'^change_pass/', login_views.Passchange.as_view()),
                       (r'^recover_pass/', login_views.Recover.as_view()),
                       # (r'^list/', include('list.urls')),
                       )