from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$','pages.views.home'),
    url(r'^home/(?P<direct>([-,.\w]*/)*)$','pages.views.listing'),
    url(r'^library/(books/)?$','pages.views.books_list'),
    url(r'^library/books/(?P<dr>([0-9])*/)$','pages.views.book_info'),
    url(r'^library/authors/(?P<dr>([0-9])*/)$','pages.views.author'),
    # Examples:
    # url(r'^$', 'control_panel.views.home', name='home'),
    # url(r'^control_panel/', include('control_panel.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
