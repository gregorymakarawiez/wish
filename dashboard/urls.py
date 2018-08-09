from django.conf.urls import url
from dashboard import views

app_name='dashboard'

urlpatterns = [
    # Matches any html file - to be used for dashboard
    # Avoid using your .html in your resources.
    # Or create a separate django app.
    url(r'^.*\.html', views.dashboard, name='dashboard'),
    # The home page
    url(r'^$', views.home, name='home'),
]
