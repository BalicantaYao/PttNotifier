from django.conf.urls import patterns, url


urlpatterns = patterns(
    '',
    url(r'^user/profile/$', 'users.views.profile', name='user_profile'),
    url(r'^user/profile/$', 'users.views.profile', name='user_profile'),
)
