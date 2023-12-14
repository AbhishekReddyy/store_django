from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

# Create your models here.
class Tag(models.Model):
    lable = models.CharField(max_length=255)

class TaggedItem(models.Model):
    #what tag is assoiciated to what object
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    # To generically allocate a tag to any object/app
    # we need  type of object like type(product) and ID
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()
 