from django.db import models
from users.models import User


class Product(models.Model):
    """
    Model for Wishlist-Product.
    """
    title = models.CharField(max_length=50, null=False)
    description = models.TextField(null=False)
    image_url = models.URLField(null=True)
    product_url = models.URLField(null=True)
    price_progress = models.FloatField(null=False, default=0)
    price_full = models.FloatField(null=False)
    purchased = models.BooleanField(null=False, default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Contribution(models.Model):
    """
    Model for Wishlist-Contributions.
    """
    amount = models.FloatField(null=False)
    comment = models.TextField(null=False)
    product = models.ForeignKey(Product, null=False, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=False, on_delete=models.RESTRICT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.product.title}: {self.amount} from {self.user}'
