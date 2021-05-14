from django.db import models


class Product(models.Model):
    """
    Model for Wishlist-Product.
    """
    title = models.CharField(max_length=50, null=False)
    description = models.TextField(null=False)
    image_url = models.URLField(null=True)
    product_url = models.URLField(null=True)
    price = models.FloatField(null=False)
    purchased = models.BooleanField(null=False, default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
