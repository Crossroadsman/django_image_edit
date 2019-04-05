# Details of 4.3 from Custom User Model Implementation
# (see users.models for full outline)
#
# We're mostly subclassing the existing forms
#
# For an explanation of the Meta inheritance, see:
# https://docs.djangoproject.com/en/2.1/topics/db/models/#meta-inheritance
# and
# https://docs.djangoproject.com/en/2.1/topics/db/models/#meta-and-multi-table-inheritance
#
# Basically:
# - The inner Meta class is for putting "anything [model-related] that's not a
#   field" (full list of metadata options at:
#    https://docs.djangoproject.com/en/2.1/ref/models/options/
#   )
# - When Django processes(how/when?) the classes (does it mean when it turns the 
#   class into a DB migration?), it replaces the inner class with attributes on
#   the outer class.
# - Then, for abstract classes only, it creates a Meta attribute which is a
#   reference to the old Meta inner class but with one adjustment: if 
#   `abstract=True` is set in the Meta class, Django turns that to False in the 
#   Meta attribute.
# - Then the same inheritance override/extension rules apply as to any other 
#   Python attribute.
# - When inheriting from an abstract class, it's likely that we'd want either:
#   - exactly the same Meta as the parent: in which case do nothing;
#   - an extension of the parent's Meta: in which case declare the child's Meta
#     inner class as `Meta(ParentClass.Meta)` and then override any metadata 
#     attributes that we want to customise
# - When inheriting from a concrete model class, The Meta class has already been
#   turned into attributes on the parent class (it can't do this for an abstract
#   class because the parent doesn't really exist).
# - It therefore doesn't make sense to inherit from Meta in a concrete class and
#   indeed, the parent's Meta is not available.
# - You can add a new Meta class and can reverse some of the parent's Meta 
#   settings. For example setting `ordering = []` in the child's Meta will
#   undo the ordering that was set in the parent's Meta.
#
# It therefore seems that the Meta inheritance from the original guide was a 
# bug, since Django explicitly states you cannot inherit Meta in a concrete 
# child class, and UserCreationForm is a concrete class.
# Thus, we have removed it here.
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import KSUser


class KSUserCreationForm(UserCreationForm):

    class Meta:  # this is where the weird inheritance was before
        model = KSUser
        fields = ('username', 'email')


class KSUserChangeForm(UserChangeForm):

    class Meta:
        model = KSUser
        fields = ('username', 'email')