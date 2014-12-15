from django.conf.urls import patterns, include, url
from django.contrib import admin
from subscriptions.views import home

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'PttNotifier.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', home, name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url('', include('django.contrib.auth.urls', namespace='auth')),

)
