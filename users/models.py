# This creates a custom user that starts out as identical to the default
# user
#
# The sequence is:
#
# (note, we can run the Django server before this process is complete, we 
# just mustn't create or run migrations)
#
# 1. Create the Django Project
# 2. Create a `users` app
# 3. Decide whether to subclass `AbstractUser` or `AbstractBaseUser`
#    (this project  uses the former, which is much, much easier)
# 4. Create initial custom user model:
#    4.1 update `settings.py`
#    4.2 create a replacement `User` model (see below)
#    4.3 create new user forms (`forms.py`)
#    4.4 customise Django admin (`admin.py`)
# 5. Run `makemigrations` for `users`
# 6. Run `migrate` for `users`
# 7. Create a superuser
# 8. Update `settings.py` for templates
# 9. Create the project-level templates (see the templates for details):
#    9.1 `base.html` (or `_layout.html`)
#    9.2 `registration/login.html`
#    9.3 `home.html`
#    9.4 `signup.html`
# 10. Create URL routing:
#    10.1 `<project_dir>/<project_dir>/urls.py`
#    10.2 `users/urls.py`
# 11. Create views:
#    11.1 `users/views.py`

from django.contrib.auth.models import AbstractUser
#from django.db import models


class KSUser(AbstractUser):
    pass
