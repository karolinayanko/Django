from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from registration import views as registration_views
from digester_ua import views as digester_ua_views

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'digester_ua.views.home', name='home'),
    url(r'^test/', 'digester_ua.views.test', name='test'),
    url(r'^test_2/', 'digester_ua.test2.test_two', name='test_two'),
    url(r'^show_data_test/', 'digester_ua.digester_show_data.showdata', name='showdata'),
    url(r'^Profile_data/', digester_ua_views.Profile_data.as_view()),
    url(r'^register/$', registration_views.Register.as_view()),
    (r'^account/', include('account.urls')),
    # url(r'^digester_ua/', include('digester_ua.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
