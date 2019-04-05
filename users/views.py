# Details of 11.1 from Custom User Model Implementation
# (see users.models for full outline)
#
# - create SignUp view GCBV
 
from django.urls import reverse_lazy
from django.views import generic

from .forms import KSUserCreationForm


class SignUpView(generic.CreateView):
    form_class = KSUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
