from django.conf.urls import patterns, url
from users.views import profile

urlpatterns = patterns(
    '',
    url(r'^user/profile/$', 'users.views.profile', name='user_profile'),
    url(r'^user/profile/$', 'users.views.profile', name='user_profile'),
)