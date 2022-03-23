from django.db import models
from django.conf import settings
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    description = models.TextField(blank = True)
    nickname = models.CharField(max_length=40, blank =True)
    image = ProcessedImageField(
        blank = True,
        upload_to = 'profile/images',
        processors = [ResizeToFill(300,300)],
        format = 'JPEG',
        options = {'quality':90},
    )