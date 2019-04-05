# Details of 4.4 from Custom User Model Implementation
# (see users.models for full outline)
#
# We need to do this because Admin is highly coupled to the default User model
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import KSUserChangeForm, KSUserCreationForm
from .models import KSUser

# for many more examples of customising admin, see the project
# 'customise_admin' at:
# https://github.com/Crossroadsman/Treehouse/tree/master/Tracks/Django/django/customise_admin
class KSUserAdmin(UserAdmin):
    add_form = KSUserCreationForm
    form = KSUserChangeForm
    model = KSUser
    list_display = ['username', 'email', 'first_name', 'last_name',]


admin.site.register(KSUser, KSUserAdmin)