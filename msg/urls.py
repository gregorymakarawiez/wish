from django.conf.urls import url
from . import views

app_name='msg'

urlpatterns = [
    url(r'^$', views.list, name='list'),
    url(r'^create/$', views.create, name='create'),
    url(r'^(?P<pk>\d+)/edit/$', views.edit, name='edit'),
    url(r'^test$', views.test2, name='test'),
]
