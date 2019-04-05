"""image_edit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# Details of 10.1 from Custom User Model Implementation
# (see users.models for full outline)
#
# - include users.urls
# - include django.contrib.auth.urls
#
# Note, because the URL routing is based on finding the first match in the
# patterns list, we can override any builtins by putting our same-named
# routes before the builtins.

from django.contrib import admin
from django.urls import path, re_path, include

# from . import views

# Notes on namespacing
# --------------------
# A URL namespace comes in two parts, both of which are strings
# see:
# https://docs.djangoproject.com/en/2.1/topics/http/urls/
# - application namespace
#   - describes the name of the app
#   - every instance of the same app has the same app namespace
#   - e.g., Django's admin has the app namespace of 'admin'
#   - specified using either of the following methods:
#     - when a whole module is being `include`d:
#       add `app_name = '<app_name>'` to the line above the urlpatterns
#       declaration; or
#     - when `include`ing a list of `path`s/`re_path`s:
#       turn the list into a 2-tuple where the first element is the list and
#       the second element is the namespace
# - instance namespace
#   - describes a particular instance of an app
#   - can be the same as the app namespace
#   - used to specify a default instance of an application
#   - e.g., the default Django admin instance has an instance namespace of 'admin'
#   - specified by passing the `namespace` argument to `include`
#
# They can be nested. E.g., `sports:polls:index` would look for a pattern named
# `index` in `polls` that is itself defined in `sports`.
#
# Reversing Process:
# 1. Django looks for a matching app namespace (e.g., `polls`). This yields a
#    list of instances of that application;
# 2. If there is a current application defined, Django finds and returns the 
#    URL resolver for that instance:
#    - in code, this is specified by passing the `current_app` to the 
#      `reverse()` function;
#    - in a template, this defaults to the namespace of the currently resolved
#      view. This can be overridden by setting the desired application on the
#      `request.current_app` attribute;
# 3. If there is no current application, Django looks for a default application
#    instance (one where the instance namespace matches the application 
#    namespace);
# 4. If there is no default application instance, Django picks the last 
#    deployed instance of that application, whatever its instance name may be;
# 5. If a provided namespace doesn't match an application namespace in step 1,
#    Django will attempt a direct lookup of the namespace as an instance
#    namespace.

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'users/', include('users.urls')),
    re_path(r'users/', include('django.contrib.auth.urls')),
]
