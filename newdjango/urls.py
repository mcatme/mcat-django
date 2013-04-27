from django.conf.urls.defaults import *
import django.contrib.auth.views
import home.views
import community.views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'newdjango.views.home', name='home'),
    # url(r'^newdjango/', include('newdjango.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    
    (r'^login', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
)

urlpatterns += patterns('home.views',
    (r'^$', 'home'),
    (r'^bye', 'bye'),
    (r'^gone', 'gone'),
    (r'^tour', 'tour'),
    (r'^join', 'join'),
    (r'^hello', 'hello'),
    (r'^about', 'about'),
    (r'^faq', 'faq'),
    (r'^contact', 'contact'),
    (r'^privacy', 'privacy'),
    (r'^terms', 'terms'),
    (r'^help', 'help'),
)

urlpatterns += patterns('community.views',
    (r'^dashboard', 'dashboard'),
)