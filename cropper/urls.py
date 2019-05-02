from django.urls import re_path

from . import views


app_name = 'cropper'
urlpatterns = [
    re_path(r'^$', views.cropper, name='cropper'),
    #re_path(r'^(?P<id>\d+)$', views.cropper, name='cropper'),
    #re_path(r'^(?P<id>\d+)/process$', views.process, name='process'),
]