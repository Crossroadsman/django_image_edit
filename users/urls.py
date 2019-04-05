# Details of 10.2 from Custom User Model Implementation
# (see users.models for full outline)
#
# - create path for signup

from django.urls import re_path

from . import views


urlpatterns = [
    re_path(r'signup/', views.SignUpView.as_view(), name='signup'),
]