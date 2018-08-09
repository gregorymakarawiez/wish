from django.conf.urls import url
from . import views

app_name='task'

urlpatterns = [
    url(r'^$', views.list, name='list'),
    url(r'^create/$', views.create, name='create'),
    #url(r'^(?P<pk>\d+)/validate/$', views.validate, name='validate'),
    url(r'^(?P<pk>\d+)/edit_wizard/(?P<page>\d+)/$', views.edit_wizard, name='edit_wizard'),
    #url(r'^(?P<pk>\d+)/edit/(?P<page>\d+)/$', views.edit, name='edit'),
    url(r'^(?P<pk>\d+)/delete/$', views.delete, name='delete'),
]
