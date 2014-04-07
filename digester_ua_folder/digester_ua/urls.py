from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'digester_ua.views.home', name='home'),
    url(r'^test/', 'digester_ua.views.test', name='test'),
    url(r'^test_2/', 'digester_ua.test2.test_two', name='test_two'),
    url(r'^show_data_test/', 'digester_ua.digester_show_data.showdata', name='showdata'),
    # url(r'^digester_ua/', include('digester_ua.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
