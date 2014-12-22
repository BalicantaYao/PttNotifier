from django.conf.urls import patterns, include, url
from django.contrib import admin
from subscriptions.views import home, subscription_list, subscription_create, subscription_detail

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'PttNotifier.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', home, name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^subscription/$', subscription_list, name='subscription_list'),
    url(r'^subscription/(?P<pk>\d+)/$', subscription_detail, name='subscription_detail'),
    url(r'^new/$', subscription_create, name='subscription_create'),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url('', include('django.contrib.auth.urls', namespace='auth')),


)
