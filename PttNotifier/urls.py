from django.conf.urls import patterns, include, url
from django.contrib import admin
from PttNotifier.views import home, contact, comments, privacy, terms_and_condictions, register
from django.contrib.auth.views import login, logout

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url('', include('users.urls')),
    url('', include('subscriptions.urls')),
    # url(r'^accounts/', include('django.contrib.auth.urls')),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url('', include('django.contrib.auth.urls', namespace='auth')),
    url(r'^accounts/login/$', login, name='login'),
    url(r'^accounts/logout/$', logout, name='logout'),
    url(r'^accounts/register/$', register, name='register'),
    url(r'^$', home, name='home'),
    url(r'^contact/$', contact, name='contact'),
    url(r'^comments/$', comments, name='comments'),
    url(r'^privacy/$', privacy, name='privacy'),
    url(r'^terms_and_condictions/$', terms_and_condictions, name='terms_and_condictions'),


)
