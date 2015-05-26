from django.conf.urls import patterns, include, url
from django.contrib import admin
from PttNotifier.views import home, login, contact, comments, privacy, terms_and_condictions


urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url('', include('users.urls')),
    url('', include('subscriptions.urls')),
    # url(r'^accounts/', include('django.contrib.auth.urls')),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url('', include('django.contrib.auth.urls', namespace='auth')),
    url(r'^accounts/login/$', login, name='login'),
    url(r'^$', home, name='home'),
    url(r'^contact/$', contact, name='contact'),
    url(r'^comments/$', comments, name='comments'),
    url(r'^privacy/$', privacy, name='privacy'),
    url(r'^terms_and_condictions/$', terms_and_condictions, name='terms_and_condictions'),


)
