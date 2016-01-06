from django.conf.urls import url

import views

urlpatterns = [
    url(r'^$',views.index),
    url(r'^login/$',views.login),
    url(r'^register/$',views.register),
    url(r'^threads/(?P<threadid>\w{7})$',views.thread),
]