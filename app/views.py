#from django.contrib.auth import get_user_model
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from .forms import PictureForm


def app_main(request):

    if request.method == "POST":
        picture_form = PictureForm(request.POST, request.FILES)
        if picture_form.is_valid():
            picture_form.save()
            return redirect(reverse('app:main'))

    else:  # GET
        picture_form = PictureForm()

    template = 'app/app.html'
    context = {'image_form': picture_form}
    return render(request, template, context)
