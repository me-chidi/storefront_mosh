from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

# Create your models here.
class Tag(models.Model):
    label = models.CharField(max_length=255)

class TaggedItem(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    # for iding the type of obj that is liked
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    # when the user ID is something like a GUID this method 
    # wont work so work around it
    # for referencing the particular obj
    object_id = models.PositiveIntegerField()
    # for accessing the actual obj
    content_object = GenericForeignKey()