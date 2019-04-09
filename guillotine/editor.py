import os
import tempfile

from PIL import Image

from django.core.files import File

from app.models import ThingWithImage


def update_model(image_id, pillow_image):
    
    model = ThingWithImage.objects.get(pk=image_id)

    filepath = model.image.name
    filename = os.path.split(filepath)[1]

    with tempfile.TemporaryDirectory() as td:

        # save the image
        # Note Pillow can save a regular file (in which case the format kwarg
        # is optional) or a Python file object, in which case the format kwarg
        # is required. The format of an existing Image object can be obtained
        # by accessing its format attribute
        #
        # note: if we had assigned the temporary directory to a variable,
        # e.g., `td = tempfile.TemporaryDirectory`, we'd access the string
        # representation of the directory as td.name
        savepath = os.path.join(td, filename)
        pillow_image.save(savepath)

        fp = open(savepath, 'r+b')
        django_file = File(fp)

        # when we access an imagefield (or a filefield) on a model, we get
        # a `fieldfile` object, which is a proxy for interacting with the file
        # see: https://docs.djangoproject.com/en/2.2/ref/models/fields/#filefield-and-fieldfile
        #
        # this object has a `save(name, content)` method for saving the file (and
        # by default updating the database). `name` and `content` are required
        # arguments. `name` is the filename (and path). Assuming we are accessing 
        # an already-existing file, it will already have a name property.
        # `content` is an object containing the file's contents, which should be
        # of type `django.core.files.File`
        # We can make a Django `File` object from a Python File object by pasing
        # the Python object into the Django constructor:
        # see: https://docs.djangoproject.com/en/2.2/ref/models/fields/#django.db.models.fields.files.FieldFile.save
        model.image.save(
            name=filename,
            content=django_file
        )


def apply_transformations(image_id, transforms):
    """Takes an id that is used to grab the corresponding image from the DB and
    a set of transformations as a dictionary:
    - scale: decimal multiplier for scale
    - angle: decimal degrees of clockwise rotation
    - x: int for starting x position
    - y: int for starting y position
    - w: int for width in px
    - h: int for height in px
    """
    print(f"Loading image #{image_id}")
    print('Applying transforms:')
    print(f"scale: {transforms['scale']}x")
    print(f"rotation: {transforms['angle']} degrees")
    print(f"crop from ({transforms['x']}, {transforms['y']})")
    print(f"to a size of {transforms['w']} px by {transforms['h']} px")


    # get the image
    image_object = ThingWithImage.objects.get(pk=image_id)
    image_data = Image.open(image_object.image)

    
    # apply the transformations
    original_width, original_height = image_data.size
    new_size = (
        int(original_width * transforms['scale']),
        int(original_height * transforms['scale'])
    )

    print("step 1: scale")
    scaled = image_data.resize(new_size)

    print("step 2: rotate")
    # (note Pillow treats +ve degrees as counter-clockwise, Guillotine as clockwise)
    rotated = scaled.rotate(transforms['angle'] * -1, expand=1)

    print("step3: crop")
    crop_box = (
        transforms['x'],
        transforms['y'],
        transforms['x'] + transforms['w'],
        transforms['y'] + transforms['h'],
    )
    cropped = rotated.crop(crop_box)
    
    update_model(image_id, cropped)
