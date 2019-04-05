from django.contrib.auth import get_user_model
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from .forms import ImageForm


def app_main(request):

    if request.method == "POST":
        image_form = ImageForm(request.POST, request.FILES)
        if image_form.is_valid():
            image_form.save()
            return redirect(reverse('app:main'))

    else:  # GET
        image_form = ImageForm()

    template = 'app/app.html'
    context = {'image_form': image_form}
    return render(request, template, context)
