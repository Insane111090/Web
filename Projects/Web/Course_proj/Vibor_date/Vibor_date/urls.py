from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$','date.views.home'),
    url(r'^save_to_db$','date.views.result'),
    # Examples:
    # url(r'^$', 'Vibor_date.views.home', name='home'),
    # url(r'^Vibor_date/', include('Vibor_date.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
