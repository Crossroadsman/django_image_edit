from django.urls import re_path

from . import views


app_name = 'app'
urlpatterns = [
    re_path(r'^$', views.app_main, name='main'),
]