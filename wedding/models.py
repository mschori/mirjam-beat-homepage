from django.db import models


class WeddingImage(models.Model):
    """
    Model for Wedding-Images.
    """
    url = models.URLField(null=False, max_length=500)


class WeddingVideo(models.Model):
    """
    Model for Wedding-Videos.
    """
    name = models.CharField(max_length=50, null=False)
    url = models.URLField(null=False, max_length=500)
    image_url = models.URLField(null=False, max_length=500)
