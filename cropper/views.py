from django.shortcuts import render


def cropper(request):
    template = 'cropper/cropper.html'
    context = {}
    return render(request, template, context)
