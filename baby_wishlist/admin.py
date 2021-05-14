from django.contrib import admin
from .models import Product


@admin.register(Product)
class BabyWishlistAdmin(admin.ModelAdmin):
    """
    Admin-Registration for Product.
    """
    pass
