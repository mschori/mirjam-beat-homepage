from django.contrib import admin
from .models import Product, Contribution


@admin.register(Product)
@admin.register(Contribution)
class BabyWishlistAdmin(admin.ModelAdmin):
    """
    Admin-Registration for Product.
    """
    pass
