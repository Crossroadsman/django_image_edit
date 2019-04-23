from PIL import Image

from django import forms
from django.core.files import File

from app.forms import PictureForm
from app.models import Picture


"""Note this could be in app.forms"""
class CropperForm(PictureForm):
    x = forms.FloatField(widget=forms.HiddenInput)
    y = forms.FloatField(widget=forms.HiddenInput)
    width = forms.FloatField(widget=forms.HiddenInput)
    height = forms.FloatField(widget=forms.HiddenInput)

    class Meta:
        model = Picture
        fields = ('image', 'x', 'y', 'width', 'height',)

    def save(self):
        picture = super.save()

        x = self.cleaned_data.get('x')
        x = self.cleaned_data.get('y')
        width = self.cleaned_data.get('width')
        height = self.cleaned_data.get('height')

        image = Image.open(picture.image)

        cropped_image = image.crop(
            (x, y, x + width, y + height)
        )

        # could resize here if we wanted to. E.g.:
        #resized_image = cropped_image.resize((400, 300), Image.ANTIALIAS)

        cropped_image.save(picture.image.path) # double check this vs name

        return picture
