from django.urls import re_path

from . import views


app_name = 'cropper'
urlpatterns = [
    re_path(r'^$', views.picture_list, name='picture_list'),
]