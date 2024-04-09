from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.auth.models import User

# Create your models here.
class Likes(models.Model):
    label = models.CharField(max_length=255)

class LikedItem(models.Model):
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
