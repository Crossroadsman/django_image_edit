from django.urls import re_path

from . import views


app_name = 'guillotine'
urlpatterns = [
    re_path(r'^$', views.guillotine, name='guillotine'),
    re_path(r'^process$', views.process, name='process'),
]