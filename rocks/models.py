from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Rock(models.Model):
    """
    Post model, related to 'owner', i.e. a User instance.
    Default image set so that we can always reference image.url.
    """

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    extra_info = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    material = models.CharField(max_length=255, blank=True, null=True)
    size = models.CharField(max_length=50, blank=True, null=True)
    era = models.CharField(max_length=255, blank=True, null=True)
    tools_used = models.TextField(blank=True, null=True)
    date_found = models.DateTimeField(blank=True, null=True)
    prepped_self = models.BooleanField(blank=False, default=False)
    image = CloudinaryField(
        'image', default='placholder', blank=True, null=True)
    # finished_image = CloudinaryField(
    #     'image', blank=True, null=True
    # )

    class Meta:
        verbose_name_plural = 'Rocks'

    class Meta:
        ordering = ['-title']

    def __str__(self):
        return f'{self.id} {self.title}'