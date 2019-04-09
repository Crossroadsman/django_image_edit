from django.urls import re_path

from . import views


app_name = 'guillotine'
urlpatterns = [
    re_path(r'^(?P<id>\d+)$', views.guillotine, name='guillotine'),
    re_path(r'^(?P<id>\d+)/process$', views.process, name='process'),
]