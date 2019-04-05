from django.shortcuts import render

from app.models import ThingWithImage


def guillotine(request):

    image = ThingWithImage.objects.get(pk=1)

    print(f"IMAGE URL: {image.image}")

    template = 'guillotine/guillotine.html'
    context = {'image': image}
    return render(request, template, context)


def process(request):
    if request.method != "POST":
        raise ValueError("Should only be a POST")

    json = request.json # confirm syntax
    # do stuff with the JSON
    print(json)

