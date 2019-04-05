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


class ThingWithImage(models.Model):

    text = models.CharField(max_length=255, blank=True, default='')

    image = models.ImageField(
        upload_to=image_path,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.text
