from django.db import models


def image_path(instance, filename):
    """See django.db.models.FileField in the django docs
    
    `instance` is the object with the ImageField (in our case a ThingWithImage);
    `filename` is the file's original filename
    """
    if len(instance.text) > 0:
        prefix = instance.text[0]
    else:
        prefix = "no_text"

    return f'images/{prefix}/{filename}'


'''It's probably best to isolate the Image as its own model, which can be
1-to-1 linked with whatever model would be associated with the image. Thus
we'll call this model Picture and it will just have two fields: the 
ImageField and a text description field.
'''
class Picture(models.Model):

    text = models.CharField(max_length=255, blank=True, default='')

    image = models.ImageField(
        upload_to=image_path,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.text
