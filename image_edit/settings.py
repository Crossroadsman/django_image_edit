"""
Django settings for image_edit project.

Generated by 'django-admin startproject' using Django 2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

# Details of 4.1 from Custom User Model Implementation
# (see users.models for full outline)
#
# - add the `users` app (passing the config model instead of the whole app)
#   (for an explanation of this newer config model approach, see:
#    https://stackoverflow.com/questions/34377237/confused-a-bit-about-django-installed-apps-naming-convention
#   )
# - add the `AUTH_USER_MODEL` setting to tell Django to use our model instead 
#   of `User`
#
# Details of 8 from Custom User Model Implementation
#
# - configure `TEMPLATES` to have a project-level templates directory
# - set the redirect links for login and logout

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')
MEDIA_DIR = BASE_DIR  # change this later


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'yoyvnt&9pxyg7w&e+#y#!rmg%7ic+b9gxzpy^*c**4uc!&+kmy'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'users.apps.UsersConfig',
    'app.apps.AppConfig',
    #'guillotine.apps.GuillotineConfig',
    'cropper.apps.CropperConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'image_edit.urls'

'''ASK 20180228
Django looks for templates in the following order:
1. Whatever is specified by the `loaders` option of `OPTIONS` (if any)
   (if set, `APP_DIRS` must not be set);
2. `DIRS`;
3. `APP_DIRS` (in order of `INSTALLED_APPS`)
(see: https://stackoverflow.com/questions/18029547/django-templates-lookup-order)
'''
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            TEMPLATE_DIR,
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'image_edit.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

AUTH_USER_MODEL = 'users.KSUser'

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'


# Media files
MEDIA_ROOT = MEDIA_DIR
MEDIA_URL = '/media/'


# LOGIN_URL is where `login_required` will redirect users that are not logged in
# (it will also pass the current path as a query string `?next=/some/path`)
# This can be specified here. Alternatively, it can be substituted with a path
# as an arg to login_required() (e.g., `login_required(login_url='/accounts/login/`)
# it accepts view function names and named URL patterns
# if not specified, it defaults to `/accounts/login/`

# LOGIN_REDIRECT_URL
# https://docs.djangoproject.com/en/2.1/ref/settings/#login-redirect-url
# Default: '/accounts/profile/'
# The URL to redirect to after login when the login view gets no `next` parameter
# Also accepts named URL patterns (e.g., `'project:main_page'`)
LOGIN_REDIRECT_URL = 'home'

# LOGIN_REDIRECT_URL
# https://docs.djangoproject.com/en/2.1/ref/settings/#logout-redirect-url
# Default: None
# The URL to redirect to after logout (using LogoutView) when the view gets no 
# `next_page` parameter. If `None`, no redirect is performed and the Logout 
# view is rendered instead.
# Also accepts named URL patterns
LOGOUT_REDIRECT_URL = 'home'


# AJAX and CSRF
# See:
# https://docs.djangoproject.com/en/2.2/ref/csrf/#ajax
# Step 1 - Get CSRF token:
# - if CSRF_USE_SESSIONS is False (default) and CSRF_COOKIE_HTTPONLY is False
#   (default):
#   - get the csrftoken cookie in the JS
# Step 2 - Use the token in the AJAX request:
#   - If using jQuery, see the example code at https://docs.djangoproject.com/en/2.2/ref/csrf/#setting-the-token-on-the-ajax-request