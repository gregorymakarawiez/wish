from django.conf.urls import url
from django.contrib.auth import views as auth_views
from .forms import SigninForm
from . import views
from Wish.settings import LOGIN_URL



app_name='account'

urlpatterns = [
    #url(r'^signin/$', auth_views.login, {'template_name': 'signin.html', 'authentication_form': SigninForm},name='signin'),
    url(r'^signin/$', views.signin, name='signin'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^logout/$', auth_views.logout,{'template_name': 'signin.html', 'next_page': LOGIN_URL}, name='logout'),
]
