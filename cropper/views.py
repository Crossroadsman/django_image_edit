from django.shortcuts import render, redirect


from app.models import Picture
from .forms import CropperForm


def picture_list(request):
    """Shows all the pictures in the database and is the endpoint for
    POSTing new images using Cropper
    """
    pictures = Picture.objects.all()

    if request.method == 'POST':
        form = CropperForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('cropper:picture_list')

    else:
        form = CropperForm()

    template = 'cropper/cropper.html'
    context = {
        'form': form,
        'pictures': pictures,
    }
    return render(request, template, context)

