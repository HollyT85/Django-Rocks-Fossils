from django.db import models
from django.contrib.auth.models import User



class Rock(models.Model):

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
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_post_i7zqny', blank=True, null=True
    )
    # finished_image = models.ImageField(
    #     upload_to='images/', blank=True, null=True
    # )

    class Meta:
        verbose_name_plural = 'Rocks'

    class Meta:
        ordering = ['date_found']

    def __str__(self):
        return f'{self.id} {self.title}'