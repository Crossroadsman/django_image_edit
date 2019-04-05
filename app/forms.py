from django import forms

from .models import ThingWithImage

class ImageForm(forms.ModelForm):

    class Meta:
        model = ThingWithImage
        fields = ("text", "image")

        labels = {
            "text": "caption",
        }
    