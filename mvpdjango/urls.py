from django.conf.urls import patterns, include, url
import django.contrib.auth.views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mvpdjango.views.home', name='home'),
    # url(r'^mvpdjango/', include('mvpdjango.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('mvpdjango.views',
    #(r'^$', 'home'),
    (r'^$', 'signup_form'),
    (r'^seeyousoon', 'seeyousoon'),
    (r'^goodbye', 'goodbye'),
    (r'^tour', 'tour'),
    (r'^join', 'join'),
    (r'^hello', 'hello'),
    (r'^success', 'success'),
    (r'^login', 'login_user'),
    (r'^about', 'about'),
    (r'^faq', 'faq'),
    (r'^contact', 'contact'),
    (r'^privacy', 'privacy'),
    (r'^terms', 'terms'),
    (r'^help', 'help'),
)
