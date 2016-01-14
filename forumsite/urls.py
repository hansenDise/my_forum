from django.conf.urls import url
from django.contrib.auth import views as auth_views
import views

urlpatterns = [
    url(r'^$',views.index),
    url(r'^login/$',views.login),
    url(r'^logout/$',views.logout_view),
    url(r'^register/$',views.register),
    url(r'^threads/(?P<threadid>\w{7})$',views.thread),
    url(r'^login_require/$',views.login_require),
    url(r'^committhreads/$',views.committhreads),
]