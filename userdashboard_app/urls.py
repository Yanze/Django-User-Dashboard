from django.conf.urls import url, patterns
from . import views

urlpatterns = [
    url(r'^$', views.Index.as_view(), name='index'),
    url(r'^dashboard/$', views.dashboard, name="dashboard"),
    url(r'^signin/$', views.Signin.as_view(), name='signin'),
]
