import json

from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.csrf import ensure_csrf_cookie

from app.models import ThingWithImage
from .editor import apply_transformations


@ensure_csrf_cookie
def guillotine(request, id):

    image = ThingWithImage.objects.get(pk=id)

    print(f"IMAGE URL: {image.image}")

    template = 'guillotine/guillotine.html'
    context = {'image': image, 'id': image.id}
    return render(request, template, context)


def process(request, id):
    """Receives an AJAX POST containing a JSON-formatted description of
    the transformations to apply to the image"""
    if request.method != "POST":
        msg = f"Should only be POST, not {request.method}!"
        raise ValueError(msg)

    json_body = request.body
    python_dict = json.loads(json_body)

    # here are all the transformations provided by Guillotine
    scale = python_dict['scale']
    angle = python_dict['angle']
    x = python_dict['x']
    y = python_dict['y']
    w = python_dict['w']
    h = python_dict['h']
    
    print("Transformations:")
    print(f'scale: {scale}')
    print(f'angle: {angle}')
    print(f'coords: ({x}, {y})')
    print(f'size: ({w}, {h})')

    print(f'image id: {id}')

    # Now we want to use Pillow to apply these transformations
    apply_transformations(id, python_dict)

    return redirect(reverse('guillotine:guillotine', kwargs={'id':id}))

