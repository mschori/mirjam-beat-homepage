from django.db import models


class WeddingImage(models.Model):
    """
    Model for Wedding-Images.
    """
    url = models.URLField(null=False)


class WeddingVideo(models.Model):
    """
    Model for Wedding-Videos.
    """
    name = models.CharField(max_length=50, null=False)
    url = models.URLField(null=False)
    image_url = models.URLField(null=False)
