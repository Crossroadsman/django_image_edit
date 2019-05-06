from PIL import Image

from django.shortcuts import render, redirect
from django.views.decorators.csrf import ensure_csrf_cookie


@ensure_csrf_cookie
def cropper(request):
    template = 'cropper/cropper.html'
    context = {}
    return render(request, template, context)


def upload_image(request):

    image_file = request.FILES.get('image')

    if image_file:
        # unedited image is passed in as a file attached to the form
        print("Image is in request.FILES")

        image_object = Image.open(image_file)
        image_object.show()

    else:
        print("no image file")
    
    
    return redirect('cropper:cropper')
